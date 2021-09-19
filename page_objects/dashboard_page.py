from selenium.webdriver.common.by import By

from custom_wait_conditions import presence_of_N_elements_located
from locators import NEW_POST_TEXTFILD, SEND_BUTTON, POSTS_BLOCK, PAGES_TITLE_ELEMENT
from page_objects.base_page import Page
from page_objects.internal_page import InternalPage


class DashboardPage(InternalPage):
    # TODO: extract locators
    def wait_new_post_appear(self, number_of_posts_before):
        # Wait new post appears
        expected_amount = number_of_posts_before + 1
        el_posts_new = self.wait.until(
            presence_of_N_elements_located(POSTS_BLOCK, expected_amount),
            message=f"Amount of posts is not {expected_amount}")
        el_post_text = el_posts_new[0].find_element(By.CLASS_NAME, "ow_newsfeed_content")
        return el_post_text

    def create_new_post(self, input_text):
        # Create new post
        el_post = self.find_element(NEW_POST_TEXTFILD)
        el_post.send_keys(input_text)
        el_send = self.find_clickable_element(SEND_BUTTON)
        el_send.click()

    def count_posts(self):
        # Amount of posts
        el_posts = self.find_elements(POSTS_BLOCK)
        number_of_posts_before = len(el_posts)
        return number_of_posts_before

    def is_this_page(self):
        return self.find_element(PAGES_TITLE_ELEMENT).text == "MY DASHBOARD"

