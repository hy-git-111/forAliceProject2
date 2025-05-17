from selenium.webdriver.common.by import By

class ProfilePageLocators:
<<<<<<< Updated upstream
    # ───── 네비게이션 바 ─────
=======
>>>>>>> Stashed changes
    PROFILE_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    PROFILE_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    PROFILE_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    PROFILE_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    PROFILE_USER_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    PROFILE_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
<<<<<<< Updated upstream

    # ───── 사용자 정보 영역 ─────
    PROFILE_USER_IMG = (By.CSS_SELECTOR, "img.user-img")
    PROFILE_USERNAME = (By.CSS_SELECTOR, "div.user-info h4")
    PROFILE_EDIT_SETTINGS_BTN = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-outline-secondary.action-btn")

    # ───── 탭 링크 ─────
    PROFILE_MY_ARTICLES_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    PROFILE_MY_ARTICLES_TAB = (By.CSS_SELECTOR, "a.nav-link.active")
    PROFILE_FAVORITED_ARTICLES_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1/favorites']")

    # ───── 아티클 카드 ─────
    PROFILE_ARTICLE_PREVIEW = (By.CSS_SELECTOR, "div.article-preview")
    PROFILE_NO_ARTICLES_TEXT = (By.CSS_SELECTOR, "div.article-preview")
    PROFILE_ARTICLE_META = (By.CSS_SELECTOR, "div.article-meta")
    PROFILE_AUTHOR_LINK = (By.CSS_SELECTOR, "a.author")
    PROFILE_ARTICLE_AUTHOR = (By.CSS_SELECTOR, "a.author")
    PROFILE_ARTICLE_DATE = (By.CSS_SELECTOR, "span.date")
    PROFILE_FAVORITE_BTN = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary")
    PROFILE_FAVORITE_COUNT = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary")
    PROFILE_ARTICLE_LIKE_BTN = (By.CSS_SELECTOR, "button.btn-outline-primary")
    PROFILE_ARTICLE_LIKE_COUNT = (By.CSS_SELECTOR, "button.btn-outline-primary")
    PROFILE_ARTICLE_LINK = (By.CSS_SELECTOR, "a.preview-link")
    PROFILE_ARTICLE_TITLE = (By.CSS_SELECTOR, "a.preview-link h1")
    PROFILE_ARTICLE_DESCRIPTION = (By.CSS_SELECTOR, "a.preview-link p")
    PROFILE_READ_MORE_LINK = (By.CSS_SELECTOR, "a.preview-link span")
    PROFILE_ARTICLE_READ_MORE = (By.CSS_SELECTOR, "a.preview-link span")
    PROFILE_TAG_LIST = (By.CSS_SELECTOR, "ul.tag-list")
=======
    PROFILE_USER_IMG = (By.CSS_SELECTOR, "img.user-img")
    PROFILE_USERNAME = (By.CSS_SELECTOR, "div.user-info h4")
    PROFILE_USER_BIO = (By.CSS_SELECTOR, "div.user-info p")
    PROFILE_EDIT_SETTINGS_BTN = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-outline-secondary.action-btn")
    PROFILE_MY_ARTICLES_TAB = (By.CSS_SELECTOR, "a.nav-link.active")
    PROFILE_FAVORITED_ARTICLES_TAB = (By.CSS_SELECTOR, "a.nav-link[href='/@1/favorites']")
    PROFILE_ARTICLE_PREVIEWS = (By.CSS_SELECTOR, "div.article-preview")
    PROFILE_ARTICLE_AUTHORS = (By.CSS_SELECTOR, "a.author")
    PROFILE_ARTICLE_DATES = (By.CSS_SELECTOR, "span.date")
    PROFILE_FAVORITE_BUTTONS = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary")
    PROFILE_ARTICLE_TITLES = (By.CSS_SELECTOR, "a.preview-link h1")
    PROFILE_ARTICLE_DESCRIPTIONS = (By.CSS_SELECTOR, "a.preview-link p")
    PROFILE_READ_MORE_LINKS = (By.CSS_SELECTOR, "a.preview-link span")
    PROFILE_PAGINATION = (By.CSS_SELECTOR, "ul.pagination")
    PROFILE_PAGE_ITEMS = (By.CSS_SELECTOR, "li.page-item")
    PROFILE_PAGE_LINKS = (By.CSS_SELECTOR, "a.page-link")from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    PROFILE_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    PROFILE_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    PROFILE_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    PROFILE_USER_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    PROFILE_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
    PROFILE_USER_IMG = (By.CSS_SELECTOR, "img.user-img")
    PROFILE_USERNAME = (By.CSS_SELECTOR, "div.user-info h4")
    PROFILE_USER_BIO = (By.CSS_SELECTOR, "div.user-info p")
    PROFILE_EDIT_SETTINGS_BTN = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-outline-secondary.action-btn")
    PROFILE_MY_ARTICLES_TAB = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    PROFILE_FAVORITED_ARTICLES_TAB = (By.CSS_SELECTOR, "a.nav-link[href='/@1/favorites']")
    PROFILE_ARTICLE_PREVIEWS = (By.CSS_SELECTOR, "div.article-preview")
    PROFILE_ARTICLE_AUTHORS = (By.CSS_SELECTOR, "a.author")
    PROFILE_ARTICLE_DATES = (By.CSS_SELECTOR, "span.date")
    PROFILE_FAVORITE_BUTTONS = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary")
    PROFILE_FAVORITE_COUNT = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary i.ion-heart")
    PROFILE_ARTICLE_TITLES = (By.CSS_SELECTOR, "a.preview-link h1")
    PROFILE_ARTICLE_DESCRIPTIONS = (By.CSS_SELECTOR, "a.preview-link p")
    PROFILE_READ_MORE_LINKS = (By.CSS_SELECTOR, "a.preview-link span")
    PROFILE_TAG_LIST = (By.CSS_SELECTOR, "ul.tag-list")
    PROFILE_TAGS = (By.CSS_SELECTOR, "li.tag-default.tag-pill.tag-outline")
    PROFILE_PAGINATION = (By.CSS_SELECTOR, "ul.pagination")
    PROFILE_PAGE_ITEMS = (By.CSS_SELECTOR, "li.page-item")
    PROFILE_PAGE_LINKS = (By.CSS_SELECTOR, "a.page-link")
    PROFILE_FAVORITED_ARTICLE_BUTTONS = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary")
>>>>>>> Stashed changes
