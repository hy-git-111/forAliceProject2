from selenium.webdriver.common.by import By

class ArticlePageLocators:
    # ───── 네비게이션 바 ─────
    ARTICLE_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    ARTICLE_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    ARTICLE_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    ARTICLE_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    ARTICLE_PROFILE_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    ARTICLE_USER_PROFILE_LINK = (By.CSS_SELECTOR, "li.nav-item a.nav-link[href='/@1']")
    ARTICLE_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
    ARTICLE_USER_IMG = (By.CSS_SELECTOR, "img.user-img")

    # ───── 피드 탭 ─────
    ARTICLE_YOUR_FEED_LINK = (By.CSS_SELECTOR, "a.nav-link.active")
    ARTICLE_GLOBAL_FEED_LINK = (By.CSS_SELECTOR, "a.nav-link:not(.active)")
    ARTICLE_GLOBAL_FEED_ALT = (By.CSS_SELECTOR, "li.nav-item:nth-child(2) a.nav-link")

    # ───── 태그 및 사이드바 ─────
    ARTICLE_POPULAR_TAGS_TEXT = (By.CSS_SELECTOR, "div.sidebar p")
    ARTICLE_TAG_LIST = (By.CSS_SELECTOR, "div.tag-list")
    ARTICLE_PREVIEW_TAG_LIST = (By.CSS_SELECTOR, "a.preview-link ul.tag-list")

    # ───── 아이콘 (우상단) ─────
    ARTICLE_COMPOSE_ICON = (By.CSS_SELECTOR, "i.ion-compose")
    ARTICLE_GEAR_ICON = (By.CSS_SELECTOR, "i.ion-gear-a")

    # ───── 유저 프로필 관련 ─────
    ARTICLE_USERNAME = (By.CSS_SELECTOR, "div.user-info h4")
    ARTICLE_EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-outline-secondary")
    ARTICLE_MY_ARTICLES_LINK = (By.CSS_SELECTOR, "a.nav-link.active[href='/@1']")
    ARTICLE_FAVORITED_ARTICLES_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1/favorites']")

    # ───── 기사 목록 프리뷰 ─────
    ARTICLE_PREVIEW = (By.CSS_SELECTOR, "div.article-preview")
    ARTICLE_PREVIEW_MESSAGE = (By.CSS_SELECTOR, "div.article-preview")
    ARTICLE_TITLE = (By.CSS_SELECTOR, "a.preview-link h1")
    ARTICLE_DESCRIPTION = (By.CSS_SELECTOR, "a.preview-link p")
    ARTICLE_READ_MORE = (By.CSS_SELECTOR, "a.preview-link span")
    ARTICLE_AUTHOR_LINK = (By.CSS_SELECTOR, "a.author")
    ARTICLE_DATE = (By.CSS_SELECTOR, "span.date")
    ARTICLE_FAVORITE_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary")

    # ───── 페이지 루트 ─────
    ARTICLE_ROOT_ELEMENT = (By.ID, "root")

####찾아야함
ARTICLE_COMMENT_INPUT = (By.CSS_SELECTOR, "TODO")
ARTICLE_POST_COMMENT_BUTTON = (By.CSS_SELECTOR, "TODO")
ARTICLE_COMMENT_LIST = (By.CSS_SELECTOR, "TODO")
ARTICLE_DELETE_COMMENT_BUTTONS = (By.CSS_SELECTOR, "TODO")