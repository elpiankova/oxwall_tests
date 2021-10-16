from page_objects.internal_page import InternalPage
from selenium.webdriver.support import expected_conditions as ec

from page_objects.locators import JoinPageLocators


class JoinPage(InternalPage):
    @property
    def username_field(self):
        return self.find_one_visible_element_of_any_located(JoinPageLocators.USERNAME)

    @property
    def password_field(self):
        return self.find_one_visible_element_of_any_located(JoinPageLocators.PASSWORD)
