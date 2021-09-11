import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    dr = webdriver.Chrome()
    dr.implicitly_wait(3)
    dr.get("https://demo.oxwall.com/")  # "http://localhost/oxwall"
    yield dr
    dr.quit()


def user():
    d = {"username": "demo",   # "admin"
         "password": "demo"}   # "pass"
    return


@pytest.fixture()
def sign_in_user(driver, user):
    # Sign in
    el = driver.find_element_by_class_name("ow_signin_label")
    el.click()
    # el_submit = dr.find_element_by_id("input_iqaqewaj")
    el_name = driver.find_element_by_name("identity")
    el_name.clear()
    el_name.send_keys(user["username"])
    el_pass = driver.find_element_by_name("password")
    el_pass.clear()
    el_pass.send_keys(user["password"])
    el_confirm = driver.find_element_by_name("submit")
    el_confirm.click()
    yield user
    # TODO: Sing out

