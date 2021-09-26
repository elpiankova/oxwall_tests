from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from custom_wait_conditions import presence_of_N_elements_located
from page_objects.locators import InternalPagesLocators, SignInPageLocators


class OxwallApp:
    """ Class that aggregate actions on Oxwall site """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.actions = ActionChains(self.driver)

    def sign_in(self, user):
        """
        Sign in with user
        parameters: user as a dictionary object
        """
        el = self.driver.find_element(*InternalPagesLocators.SIGN_IN_MENU)
        el.click()
        # el_submit = dr.find_element_by_id("input_iqaqewaj")
        el_name = self.driver.find_element(*SignInPageLocators.USERNAME_FIELD)
        el_name.clear()
        el_name.send_keys(user["username"])
        el_pass = self.driver.find_element(*SignInPageLocators.PASSWORD_FIELD)
        el_pass.clear()
        el_pass.send_keys(user["password"])
        el_confirm = self.driver.find_element(*SignInPageLocators.SIGN_IN_BUTTON)
        el_confirm.click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(ec.presence_of_element_located(InternalPagesLocators.DASHBOARD_MENU))

    def sign_out(self):
        # sign out
        el_profile = self.driver.find_element_by_css_selector(".ow_console_item.ow_console_dropdown.ow_console_dropdown_hover")
        self.actions.move_to_element(el_profile)
        self.actions.perform()
        el_sign_out = self.driver.find_elements_by_css_selector("li.ow_dropdown_menu_item.ow_cursor_pointer")
        self.actions.move_to_element(el_sign_out[5])
        self.actions.click(el_sign_out[5])
        self.actions.perform()

    def wait_new_post_appear(self, number_of_posts_before):
        # Wait new post appears
        expected_amount = number_of_posts_before + 1
        el_posts_new = self.wait.until(
            presence_of_N_elements_located((By.XPATH, "//li[contains(@id, 'action-feed')]"), expected_amount),
            message=f"Amount of posts is not {expected_amount}")
        el_post_text = el_posts_new[0].find_element(By.CLASS_NAME, "ow_newsfeed_content")
        return el_post_text

    def create_new_post(self, input_text):
        # Create new post
        el_post = self.driver.find_element_by_name("status")
        el_post.send_keys(input_text)
        el_send = self.wait.until(ec.element_to_be_clickable((By.NAME, "save")),
                             message="Clickable SEND button is not found")
        el_send.click()

    def count_posts(self):
        # Amount of posts
        el_posts = self.driver.find_elements_by_xpath("//li[contains(@id, 'action-feed')]")
        number_of_posts_before = len(el_posts)
        return number_of_posts_before

