from selenium.webdriver.common.by import By

class LoginPage:
    loginNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    loginHomeLink = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    loginSignInLink = (By.CSS_SELECTOR, "a.nav-link[href='/login']")
    loginSignUpLink = (By.CSS_SELECTOR, "a.nav-link[href='/register']")
    loginHeader = (By.CSS_SELECTOR, "h1.text-xs-center")
    loginNeedAccountLink = (By.CSS_SELECTOR, "p.text-xs-center a")
    loginEmailInput = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    loginPasswordInput = (By.CSS_SELECTOR, "input[type='password'][placeholder='Password']")
    loginSignInButton = (By.CSS_SELECTOR, "button.btn-primary")