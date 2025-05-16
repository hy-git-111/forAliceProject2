from selenium.webdriver.common.by import By

class HomePage:
    homeNavbarBrand = (By.CSS_SELECTOR, ".navbar-brand")
    homeNavLink = (By.CSS_SELECTOR, ".nav-link[href='/']")
    homeNewPostLink = (By.CSS_SELECTOR, ".nav-link[href='/editor']")
    homeSettingsLink = (By.CSS_SELECTOR, ".nav-link[href='/settings']")
    homeProfileLink = (By.CSS_SELECTOR, ".nav-link[href='/@1']")
    homeUserPic = (By.CSS_SELECTOR, ".user-pic")
    homeYourFeedLink = (By.CSS_SELECTOR, ".nav-link.active")
    homeGlobalFeedLink = (By.CSS_SELECTOR, ".nav-link:not(.active)")
    homeArticlePreview = (By.CSS_SELECTOR, ".article-preview")
    homePopularTagsText = (By.CSS_SELECTOR, ".sidebar p")
    homeTagList = (By.CSS_SELECTOR, ".tag-list")## HomePage

from selenium.webdriver.common.by import By

class HomePage:
    homeNavbarBrand = (By.CSS_SELECTOR, ".navbar-brand")
    homeNavbarNav = (By.CSS_SELECTOR, ".navbar-nav")
    homeNavHomeLink = (By.CSS_SELECTOR, ".nav-item:nth-child(1) .nav-link")
    homeNavNewPostLink = (By.CSS_SELECTOR, ".nav-item:nth-child(2) .nav-link")
    homeNavSettingsLink = (By.CSS_SELECTOR, ".nav-item:nth-child(3) .nav-link")
    homeNavUserLink = (By.CSS_SELECTOR, ".nav-item:nth-child(4) .nav-link")
    homeNavUserPic = (By.CSS_SELECTOR, ".user-pic")
    homeYourFeedLink = (By.CSS_SELECTOR, ".nav-link.active")
    homeGlobalFeedLink = (By.CSS_SELECTOR, ".nav-item:nth-child(2) .nav-link:not(.active)")
    homeArticlePreview = (By.CSS_SELECTOR, ".article-preview")
    homeSidebar = (By.CSS_SELECTOR, ".sidebar")
    homePopularTagsText = (By.CSS_SELECTOR, ".sidebar p")
    homeTagList = (By.CSS_SELECTOR, ".tag-list")
    homeRoot = (By.ID, "root")
    homeContainer = (By.CSS_SELECTOR, ".container.page")