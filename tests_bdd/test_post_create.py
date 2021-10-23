from pytest_bdd import given, when, then, scenario

from page_objects.dashboard_page import DashboardPage
from page_objects.main_page import MainPage


@scenario("posts.feature", "Create text post (without photos)")
def test_create_post():
    pass


@given("I as a logged user", target_fixture="logged_user")
def logged_user(driver, default_user):
    main_page = MainPage(driver)
    main_page.sign_in(default_user)
    return default_user


@given("initial amount of post in Oxwall database", target_fixture="initial_amount_post")
def initial_amount_post(driver):
    dashboard_page = DashboardPage(driver)
    number_of_posts_before = dashboard_page.count_posts()
    return number_of_posts_before


@when("I add a new post with <text> in Dashboard page")
def create_post(driver, text):
    dashboard_page = DashboardPage(driver)
    dashboard_page.el_post_textfield.clear()
    dashboard_page.create_new_post(text)


@then("a new post block appears before old table of posts")
def wait_new_post(driver, initial_amount_post):
    dashboard_page = DashboardPage(driver)
    dashboard_page.wait_new_post_appear(initial_amount_post)


@then("this post block has this <text> and author as this user and time \"within 1 minute\"")
def verify_new_post(driver, text, logged_user):
    dashboard_page = DashboardPage(driver)
    new_post = dashboard_page.el_posts[0]
    # Verify text and user of new post
    assert new_post.el_text.text == text
    assert new_post.el_user.text == logged_user.real_name
    assert new_post.el_time.text == "within 1 minute"
