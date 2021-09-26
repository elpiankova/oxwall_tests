from selenium.webdriver.common.by import By

from custom_wait_conditions import presence_of_N_elements_located
from page_objects.locators import DashboardPageLocators
from page_objects.blocks_elements.post_block import PostBlock
from page_objects.internal_page import InternalPage


class DashboardPage(InternalPage):
    @property
    def el_post_textfield(self):
        return self.find_element(DashboardPageLocators.NEW_POST_TEXTFILD)

    @property
    def el_send_button(self):
        return self.find_clickable_element(DashboardPageLocators.SEND_BUTTON)

    @property
    def el_posts(self):
        el_posts = self.find_elements(DashboardPageLocators.POSTS_BLOCK)

        # new_list = []
        # for el in el_posts:
        #     new_list.append(PostBlock(el))

        # new_list = map(PostBlock, el_posts)
        new_list = [PostBlock(e) for e in el_posts]
        return new_list

    def wait_new_post_appear(self, number_of_posts_before):
        # TODO: extract locators
        # Wait new post appears
        expected_amount = number_of_posts_before + 1
        el_posts_new = self.wait.until(
            presence_of_N_elements_located(DashboardPageLocators.POSTS_BLOCK, expected_amount),
            message=f"Amount of posts is not {expected_amount}")
        el_post_text = el_posts_new[0].find_element(By.CLASS_NAME, "ow_newsfeed_content")
        return el_post_text

    def create_new_post(self, input_text):
        # Create new post
        self.el_post_textfield.send_keys(input_text)
        self.el_send_button.click()

    def count_posts(self):
        # Amount of posts
        number_of_posts_before = len(self.el_posts)
        return number_of_posts_before

    def is_this_page(self):
        return self.el_page_title.text == "MY DASHBOAR"

