from locators import SIGN_IN_MENU
from page_objects.base_page import Page


class InternalPage(Page):
    def click_sign_in(self):
        el = self.find_element(SIGN_IN_MENU)
        el.click()
        # return SignInPage(self.driver)

    def sign_out(self):
        pass

    def sign_in(self):
        pass

    def photo_menu_click(self):
        pass

    def main_menu_click(self):
        pass
