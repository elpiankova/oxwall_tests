import json

import pytest
from selenium import webdriver
import os.path

from db.oxwall_db import OxwallDB
from oxwall_helper import OxwallApp
from page_objects.main_page import MainPage
from value_objects import User

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture()
def driver():
    dr = webdriver.Chrome()
    # dr.implicitly_wait(3)
    dr.get("http://localhost/oxwall")  # "https://demo.oxwall.com/"
    yield dr
    dr.quit()


@pytest.fixture(scope="session")
def db():
    db = OxwallDB()
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
def default_user():
    d = {"username": "admin",
         "password": "pass",
         "real_name": "Admin"}
    user = User(**d)
    return user


@pytest.fixture()
def sign_in_user(driver, default_user, app):
    main_page = MainPage(driver)
    main_page.sign_in(default_user)
    yield default_user
    main_page.sign_out()

