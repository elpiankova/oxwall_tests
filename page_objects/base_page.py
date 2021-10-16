from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.locators import CommonPageLocators


class Page:
    """ Base Page Class that aggregate common actions on Oxwall pages """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.actions = ActionChains(self.driver)

    @property
    def message(self):
        return self.find_element(CommonPageLocators.MESSAGE)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator):
        el = self.wait.until(ec.presence_of_element_located(locator),
                             message=f"No element with locator='{locator}'")
        return el

    def find_elements(self, locator):
        el = self.wait.until(ec.presence_of_all_elements_located(locator),
                             message=f"No any elements with locator='{locator}'")
        return el

    def find_visible_element(self, locator):
        el = self.wait.until(ec.visibility_of_element_located(locator),
                             message=f"No visible element with locator='{locator}'")
        return el

    def find_one_visible_element_of_any_located(self, locator):
        els = self.wait.until(ec.visibility_of_any_elements_located(locator),
                              message=f"No elements visible with locators {locator}")
        return els[0]

    def find_clickable_element(self, locator):
        el = self.wait.until(ec.element_to_be_clickable(locator),
                             message=f"No clickable element with locator='{locator}'")
        return el
