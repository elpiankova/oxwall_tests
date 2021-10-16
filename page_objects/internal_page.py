from .locators import InternalPagesLocators
from page_objects.base_page import Page
from .sign_in_page import SignInPage


class InternalPage(Page):
    @property
    def el_page_title(self):
        return self.find_element(InternalPagesLocators.PAGES_TITLE_ELEMENT)

    @property
    def el_sign_in(self):
        return self.find_element(InternalPagesLocators.SIGN_IN_MENU)

    def click_sign_in(self):
        self.el_sign_in.click()
        # return SignInPage(self.driver)

    def sign_out(self):
        pass

    def sign_in(self, user):
        self.click_sign_in()
        sign_in_page = SignInPage(self.driver)
        sign_in_page.input_username(user.username)
        sign_in_page.input_password(user.password)
        sign_in_page.click_sign_in_button()

    def photo_menu_click(self):
        pass

    def main_menu_click(self):
        pass
