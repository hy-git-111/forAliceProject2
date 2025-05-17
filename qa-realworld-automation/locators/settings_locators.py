from selenium.webdriver.common.by import By

class SettingsPageLocators:
<<<<<<< Updated upstream
    # ───── 네비게이션 바 ─────
=======
>>>>>>> Stashed changes
    SETTINGS_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    SETTINGS_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    SETTINGS_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    SETTINGS_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    SETTINGS_PROFILE_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    SETTINGS_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
<<<<<<< Updated upstream

    # ───── 설정 폼 타이틀 ─────
    SETTINGS_TITLE = (By.CSS_SELECTOR, "h1.text-xs-center")

    # ───── 입력 필드 영역 ─────
=======
    SETTINGS_TITLE = (By.CSS_SELECTOR, "h1.text-xs-center")
    SETTINGS_PROFILE_PICTURE_INPUT = (By.CSS_SELECTOR, "input[placeholder='URL of profile picture']")
    SETTINGS_USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
    SETTINGS_BIO_TEXTAREA = (By.CSS_SELECTOR, "textarea[placeholder='Short bio about you']")
    SETTINGS_EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    SETTINGS_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][placeholder='New Password']")
    SETTINGS_UPDATE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    SETTINGS_LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btn-outline-danger")from selenium.webdriver.common.by import By

class SettingsPageLocators:
    SETTINGS_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    SETTINGS_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    SETTINGS_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    SETTINGS_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    SETTINGS_PROFILE_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    SETTINGS_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
    SETTINGS_TITLE = (By.CSS_SELECTOR, "h1.text-xs-center")
>>>>>>> Stashed changes
    SETTINGS_PROFILE_PICTURE_INPUT = (By.CSS_SELECTOR, "input[placeholder='URL of profile picture']")
    SETTINGS_USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
    SETTINGS_BIO_TEXTAREA = (By.CSS_SELECTOR, "textarea[placeholder='Short bio about you']")
    SETTINGS_EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    SETTINGS_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][placeholder='New Password']")
<<<<<<< Updated upstream

    # ───── 버튼 영역 ─────
    SETTINGS_UPDATE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    SETTINGS_LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btn-outline-danger")
=======
    SETTINGS_UPDATE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    SETTINGS_LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btn-outline-danger")
>>>>>>> Stashed changes
