import time

import allure
import pytest
import json
from conftest import PROJECT_DIR
import os.path
from data.random_string import random_string
from page_objects.dashboard_page import DashboardPage

filename = os.path.join(PROJECT_DIR, "data", "post_text_data.json")

with open(filename, encoding="utf-8") as f:
    post_data_list = json.load(f)

post_data_list.append(random_string(enter=True))


@allure.feature("Post feature")
@allure.title("Post create test")
@allure.story("Create text post (without photos)")
@pytest.mark.smoke
@pytest.mark.nondestructive
@pytest.mark.parametrize("input_text", post_data_list)
def test_create_post(driver, sign_in_user, input_text, db):
    # input_text = "new post typing"
    dashboard_page = DashboardPage(driver)
    number_of_posts_before = dashboard_page.count_posts()
    dashboard_page.el_post_textfield.clear()
    dashboard_page.create_new_post(input_text)
    dashboard_page.wait_new_post_appear(number_of_posts_before)

    text_in_db = db.get_last_text_post()
    assert text_in_db.replace("\r\n", "\n") == input_text

    dashboard_page.verify_post(input_text, sign_in_user)
    # new_post = dashboard_page.el_posts[0]
    # # Verify text and user of new post
    # assert new_post.el_text.text == input_text
    # assert new_post.el_user.text == sign_in_user.real_name
    # assert new_post.el_time.text == "within 1 minute"



filename = os.path.join(PROJECT_DIR, "data", "input_output.json")

with open(filename, encoding="utf-8") as f:
    post_data_list = json.load(f)


@allure.feature("Post feature")
@allure.title("Post create test 2")
@allure.story("Create text post (without photos) 2")
@pytest.mark.parametrize("input_text,output_text", post_data_list)
def test_create_post_2(driver, sign_in_user, input_text, output_text):
    # input_text = "new post typing"
    dashboard_page = DashboardPage(driver)
    dashboard_page.el_post_textfield.clear()
    number_of_posts_before = dashboard_page.count_posts()
    dashboard_page.create_new_post(input_text)
    dashboard_page.wait_new_post_appear(number_of_posts_before)
    new_post = dashboard_page.el_posts[0]
    # Verify text and user of new post
    assert new_post.el_text.text == output_text
    assert new_post.el_user.text == sign_in_user.real_name
    assert new_post.el_time.text == "within 1 minute"
    # TODO el_post_user == sign_in_user["username"]


@allure.feature("Post feature")
@allure.title("First post create")
@allure.story("Create first post ")
def test_add_like_to_first_post(driver, sign_in_user):
    dashboard_page = DashboardPage(driver)
    first_post = dashboard_page.el_posts[0]
    old_like_number = int(first_post.el_like_counter.text)
    first_post.add_like()
    assert first_post.el_like_counter.text == str(old_like_number + 1)


# def test_create_post2(driver, sign_in_user, app):
#     input_text = "new post typing"
#
#     number_of_posts_before = app.count_posts()
#     app.create_new_post(input_text)
#     el_post_text = app.wait_new_post_appear(number_of_posts_before)
#     # Verify text and user of new post
#     assert el_post_text.text == input_text
#     # TODO el_post_user == sign_in_user["username"]

