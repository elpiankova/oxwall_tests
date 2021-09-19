from selenium.webdriver.common.by import By


SIGN_IN_MENU = (By.CLASS_NAME, "ow_signin_label")

USERNAME_FIELD = (By.NAME, "identity")
PASSWORD_FIELD = (By.NAME, "password")
SIGN_IN_BUTTON = (By.NAME, "submit")
MESSAGE = (By.CLASS_NAME, "ow_message_node")


DASHOBORD_MENU = (By.CSS_SELECTOR, ".base_dashboard a")
PAGES_TITLE_ELEMENT = (By.CSS_SELECTOR, ".ow_page_container h1")

NEW_POST_TEXTFILD = (By.NAME, "status")
SEND_BUTTON = (By.NAME, "save")
POSTS_BLOCK = (By.XPATH, "//li[contains(@id, 'action-feed')]")

