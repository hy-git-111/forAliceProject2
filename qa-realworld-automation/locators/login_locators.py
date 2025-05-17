from selenium.webdriver.common.by import By

class LoginPageLocators:
<<<<<<< Updated upstream
    # ───── 네비게이션 바 ─────
    LOGIN_NAVBAR_BRAND = (By.CSS_SELECTOR, ".navbar-brand")
    LOGIN_HOME_LINK = (By.CSS_SELECTOR, ".nav-link[href='/']")
    LOGIN_SIGN_IN_LINK = (By.CSS_SELECTOR, ".nav-link[href='/login']")
    LOGIN_SIGN_UP_LINK = (By.CSS_SELECTOR, ".nav-link[href='/register']")

    # ───── 로그인 폼 ─────
    LOGIN_HEADER = (By.CSS_SELECTOR, ".text-xs-center")
    LOGIN_NEED_ACCOUNT_LINK = (By.CSS_SELECTOR, ".text-xs-center a")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][placeholder='Password']")
    LOGIN_SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
=======
    LOGIN_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    LOGIN_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    LOGIN_SIGN_IN_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/login']")
    LOGIN_SIGN_UP_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/register']")
    LOGIN_HEADER = (By.CSS_SELECTOR, "h1.text-xs-center")
    LOGIN_NEED_ACCOUNT_LINK = (By.CSS_SELECTOR, "p.text-xs-center a")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][placeholder='Password']")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn-primary[type='submit']")
>>>>>>> Stashed changes
