## SettingsPage

from selenium.webdriver.common.by import By

class SettingsPage:
    settingsNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    settingsHomeLink = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    settingsNewPostLink = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    settingsSettingsLink = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    settingsProfileLink = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    settingsUserPic = (By.CSS_SELECTOR, "img.user-pic")
    settingsTitle = (By.CSS_SELECTOR, "h1.text-xs-center")
    settingsProfilePictureInput = (By.CSS_SELECTOR, "input[placeholder='URL of profile picture']")
    settingsUsernameInput = (By.CSS_SELECTOR, "input[placeholder='Username']")
    settingsBioTextarea = (By.CSS_SELECTOR, "textarea[placeholder='Short bio about you']")
    settingsEmailInput = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    settingsPasswordInput = (By.CSS_SELECTOR, "input[type='password'][placeholder='New Password']")
    settingsUpdateButton = (By.CSS_SELECTOR, "button.btn-primary")
    settingsLogoutButton = (By.CSS_SELECTOR, "button.btn-outline-danger")## SettingsPage

from selenium.webdriver.common.by import By

class SettingsPage:
    settingsNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    settingsHomeLink = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    settingsNewPostLink = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    settingsSettingsLink = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    settingsProfileLink = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    settingsUserPic = (By.CSS_SELECTOR, "img.user-pic")
    settingsTitle = (By.CSS_SELECTOR, "h1.text-xs-center")
    settingsProfilePictureInput = (By.CSS_SELECTOR, "input[placeholder='URL of profile picture']")
    settingsUsernameInput = (By.CSS_SELECTOR, "input[placeholder='Username']")
    settingsBioTextarea = (By.CSS_SELECTOR, "textarea[placeholder='Short bio about you']")
    settingsEmailInput = (By.CSS_SELECTOR, "input[type='email'][placeholder='Email']")
    settingsPasswordInput = (By.CSS_SELECTOR, "input[type='password'][placeholder='New Password']")
    settingsUpdateButton = (By.CSS_SELECTOR, "button.btn-primary")
    settingsLogoutButton = (By.CSS_SELECTOR, "button.btn-outline-danger")