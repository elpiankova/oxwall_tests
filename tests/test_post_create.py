import time

from page_objects.dashboard_page import DashboardPage


def test_create_post(driver, sign_in_user):
    input_text = "new post typing"

    dashboard_page = DashboardPage(driver)
    number_of_posts_before = dashboard_page.count_posts()
    dashboard_page.create_new_post(input_text)
    el_post_text = dashboard_page.wait_new_post_appear(number_of_posts_before)
    # Verify text and user of new post
    assert el_post_text.text == input_text
    # TODO el_post_user == sign_in_user["username"]


# def test_create_post2(driver, sign_in_user, app):
#     input_text = "new post typing"
#
#     number_of_posts_before = app.count_posts()
#     app.create_new_post(input_text)
#     el_post_text = app.wait_new_post_appear(number_of_posts_before)
#     # Verify text and user of new post
#     assert el_post_text.text == input_text
#     # TODO el_post_user == sign_in_user["username"]

