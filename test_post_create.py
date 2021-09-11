import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from custom_wait_conditions import presence_of_N_elements_located


def test_create_post(driver, sign_in_user):
    # Amount of posts
    el_posts = driver.find_elements_by_xpath("//li[contains(@id, 'action-feed')]")
    number_of_posts_before = len(el_posts)

    # Create new post
    el_post = driver.find_element_by_name("status")
    input_text = "new post typing"
    el_post.send_keys(input_text)
    # el_post_submit = dr.find_element_by_name("submit")
    wait = WebDriverWait(driver, 3)
    el_send = wait.until(ec.element_to_be_clickable((By.NAME, "save")),
                         message="Clickable SEND button is not found")
    el_send.click()
    expected_amount = number_of_posts_before + 1
    # expected_amount = 12
    el_posts_new = wait.until(presence_of_N_elements_located((By.XPATH, "//li[contains(@id, 'action-feed')]"), expected_amount),
                              message=f"Amount of posts is not {expected_amount}")
    el_post_text = el_posts_new[0].find_element(By.CLASS_NAME, "ow_newsfeed_content")
    # TODO: el_post_user
    assert el_post_text.text == input_text
    # TODO el_post_user == sign_in_user["username"]
    # el_posts = dr.find_elements_by_xpath("//li[contains(@id, 'action-feed')]")

