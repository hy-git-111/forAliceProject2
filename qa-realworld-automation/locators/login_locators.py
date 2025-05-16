from selenium.webdriver.common.by import By

class LoginPage:
    loginNavbarBrand = (By.CSS_SELECTOR, ".navbar-brand")
    loginHomeLink = (By.CSS_SELECTOR, ".nav-link[href='/']")
    loginSignInLink = (By.CSS_SELECTOR, ".nav-link[href='/login']")
    loginSignUpLink = (By.CSS_SELECTOR, ".nav-link[href='/register']")
    loginHeader = (By.CSS_SELECTOR, ".text-xs-center")
    loginNeedAccountLink = (By.CSS_SELECTOR, ".text-xs-center a")
    loginEmailInput = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    loginPasswordInput = (By.CSS_SELECTOR, "input[type='password'][placeholder='Password']")
    loginSignInButton = (By.CSS_SELECTOR, ".btn-primary")