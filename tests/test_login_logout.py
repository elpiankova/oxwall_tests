from page_objects.dashboard_page import DashboardPage
from page_objects.main_page import MainPage
from page_objects.sign_in_page import SignInPage


def test_sign_in_using_sign_in_button(driver, user):
    main_page = MainPage(driver)
    # assert main_page.el_page_title.text == "fdgd"
    main_page.click_sign_in()
    sign_in_page = SignInPage(driver)
    sign_in_page.input_username(user["username"])
    sign_in_page.input_password(user["password"])
    sign_in_page.click_sign_in_button()
    assert "info" in sign_in_page.message.get_attribute("class").split()
    assert sign_in_page.message.text == "AUTHENTICATION SUCCESS, PLEASE WAIT..."
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.el_page_title.text == "MY DASHBOARD"


def test_sign_in_using_submit(driver, user):
    main_page = MainPage(driver)
    main_page.click_sign_in()
    sign_in_page = SignInPage(driver)
    sign_in_page.input_username(user["username"])
    sign_in_page.input_password(user["password"])
    sign_in_page.submit()
    assert "info" in sign_in_page.message.get_attribute("class").split()
    assert sign_in_page.message.text == "Authentication success, please wait..."


def test_sign_in_without_password(driver, user):
    main_page = MainPage(driver)
    main_page.click_sign_in()
    sign_in_page = SignInPage(driver)
    sign_in_page.input_username(user["username"])
    sign_in_page.input_password('')
    sign_in_page.click_sign_in_button()
    assert "error" in sign_in_page.message().get_attribute("class").split()
    assert sign_in_page.message().text == "PLEASE FILL THE FORM PROPERLY"
    # assert sign_in_page.el_title.text == "Please sign in"
