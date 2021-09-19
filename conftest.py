import pytest
from selenium import webdriver

from oxwall_helper import OxwallApp


@pytest.fixture()
def driver():
    dr = webdriver.Chrome()
    # dr.implicitly_wait(3)
    dr.get("https://demo.oxwall.com/")  # "http://localhost/oxwall"
    yield dr
    dr.quit()


@pytest.fixture()
def app(driver):
    app = OxwallApp(driver)
    return app


@pytest.fixture()
def user():
    d = {"username": "demo",   # "admin"
         "password": "demo"}   # "pass"
    return d


@pytest.fixture()
def sign_in_user(driver, user, app):
    app.sign_in(user)
    yield user
    app.sign_out()

