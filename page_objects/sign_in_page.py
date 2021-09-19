from locators import USERNAME_FIELD, PASSWORD_FIELD, SIGN_IN_BUTTON, MESSAGE
from page_objects.base_page import Page


class SignInPage(Page):
    def input_username(self, username):
        el_name = self.find_element(USERNAME_FIELD)
        el_name.clear()
        el_name.send_keys(username)

    def input_password(self, password):
        el_pass = self.find_element(PASSWORD_FIELD)
        el_pass.clear()
        el_pass.send_keys(password)

    # def input_password(self, password):
    #     el_pass = self.find_element(PASSWORD_FIELD)
    #     el_pass.clear()

    def submit(self):
        # TODO press Enter
        pass

    def click_sign_in_button(self):
        el_confirm = self.find_element(SIGN_IN_BUTTON)
        el_confirm.click()

    def message(self):
        return self.find_element(MESSAGE)


