from selenium.webdriver.common.by import By

class SignupPage:
    signupNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    signupHomeLink = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    signupSignInLink = (By.CSS_SELECTOR, "a.nav-link[href='/login']")
    signupSignUpLink = (By.CSS_SELECTOR, "a.nav-link[href='/register']")
    signupTitle = (By.CSS_SELECTOR, "h1.text-xs-center")
    signupHaveAccountLink = (By.CSS_SELECTOR, "p.text-xs-center a")
    signupUsernameInput = (By.CSS_SELECTOR, "input[type='text'][placeholder='Username']")
    signupEmailInput = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    signupPasswordInput = (By.CSS_SELECTOR, "input[type='password'][placeholder='Password']")
    signupSubmitButton = (By.CSS_SELECTOR, "button.btn-primary")