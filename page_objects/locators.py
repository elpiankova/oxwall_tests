from selenium.webdriver.common.by import By


class CommonPageLocators:
    MESSAGE = (By.CLASS_NAME, "ow_message_node")


class InternalPagesLocators:
    SIGN_IN_MENU = (By.CLASS_NAME, "ow_signin_label")
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_responsive_menu .ow_main_menu .active")
    MAIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_main_menu_index a")
    DASHBOARD_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_dashboard a")
    JOIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_base_join_menu_item a")
    MEMBERS_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_users_main_menu_item a")
    PHOTO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .photo_photo a")
    VIDEO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .video_video ")
    PAGES_TITLE_ELEMENT = (By.CSS_SELECTOR, ".ow_page_container h1")


class SignInPageLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.NAME, "submit")


class DashboardPageLocators:
    NEW_POST_TEXTFILD = (By.NAME, "status")
    SEND_BUTTON = (By.NAME, "save")
    POSTS_BLOCK = (By.XPATH, "//li[contains(@id, 'action-feed')]")


class PostBlockLocators:
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    LIKES_BUTTON = (By.CSS_SELECTOR, ".ow_miniic_like.newsfeed_like_btn")
    LIKES_COUNTER = (By.CSS_SELECTOR, ".newsfeed_counter_likes")
