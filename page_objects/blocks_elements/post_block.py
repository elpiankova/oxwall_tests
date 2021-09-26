from page_objects.locators import PostBlockLocators


class PostBlock:
    def __init__(self, element):
        self.element = element

    @property
    def el_user(self):
        return self.element.find_element(*PostBlockLocators.POST_USER)

    @property
    def el_text(self):
        return self.element.find_element(*PostBlockLocators.POST_TEXT)

    @property
    def el_time(self):
        return self.element.find_element(*PostBlockLocators.POST_TIME)

    @property
    def el_like_bt(self):
        return self.element.find_element(*PostBlockLocators.LIKES_BUTTON)

    @property
    def el_like_counter(self):
        return self.element.find_element(*PostBlockLocators.LIKES_COUNTER)

    def add_like(self):
        self.el_like_bt.click()

    def delete(self):
        # TODO
        pass
