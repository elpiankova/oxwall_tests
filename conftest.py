import json

import pytest
from selenium import webdriver
import os.path

from db.oxwall_db import OxwallDB
from oxwall_helper import OxwallApp
from page_objects.main_page import MainPage
from value_objects import User

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json",
                     help="project config file name")
    # parser.addoption("--browser", action="store", default="Chrome",
    #                  help="driver")


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, filename)) as f:
        return json.load(f)


@pytest.fixture()
def driver(config, selenium, base_url):
    dr = selenium
    # dr.implicitly_wait(3)
    # dr.get(config["web"]["base_url"])  # "https://demo.oxwall.com/"
    dr.get(base_url)
    yield dr
    dr.quit()


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(**config["db"])
    yield db
    db.close()


@pytest.fixture()
def app(driver):
    app = OxwallApp(driver)
    return app


user_filename = os.path.join(PROJECT_DIR, "data", "user_data.json")
with open(user_filename) as f:
    user_list = json.load(f)


@pytest.fixture(params=user_list, ids=[str(d) for d in user_list])
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)


@pytest.fixture()
def default_user(config):
    user = User(**config["web"]["user"])
    return user


@pytest.fixture()
def sign_in_user(driver, default_user, app):
    main_page = MainPage(driver)
    main_page.sign_in(default_user)
    yield default_user
    main_page.sign_out()

