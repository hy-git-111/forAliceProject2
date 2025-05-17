from selenium.webdriver.common.by import By

class ArticlePageLocators:
<<<<<<< Updated upstream
    # ───── 네비게이션 바 ─────
=======
>>>>>>> Stashed changes
    ARTICLE_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    ARTICLE_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    ARTICLE_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    ARTICLE_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
<<<<<<< Updated upstream
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
=======
    ARTICLE_USER_PROFILE_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    ARTICLE_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
    ARTICLE_YOUR_FEED_LINK = (By.CSS_SELECTOR, "a.nav-link.active")
    ARTICLE_GLOBAL_FEED_LINK = (By.CSS_SELECTOR, "a.nav-link:not(.active)")
    ARTICLE_PREVIEW_CONTAINER = (By.CSS_SELECTOR, "div.article-preview")
    ARTICLE_AUTHOR_IMAGES = (By.CSS_SELECTOR, "div.article-meta img")
    ARTICLE_AUTHOR_LINKS = (By.CSS_SELECTOR, "a.author")
    ARTICLE_DATES = (By.CSS_SELECTOR, "span.date")
    ARTICLE_FAVORITE_BUTTONS = (By.CSS_SELECTOR, "button.btn-sm")
    ARTICLE_HEART_ICONS = (By.CSS_SELECTOR, "i.ion-heart")
    ARTICLE_PREVIEW_LINKS = (By.CSS_SELECTOR, "a.preview-link")
    ARTICLE_TITLES = (By.CSS_SELECTOR, "a.preview-link h1")
    ARTICLE_DESCRIPTIONS = (By.CSS_SELECTOR, "a.preview-link p")
    ARTICLE_READ_MORE = (By.CSS_SELECTOR, "a.preview-link span")
    ARTICLE_TAG_LISTS = (By.CSS_SELECTOR, "ul.tag-list")
    ARTICLE_TAGS = (By.CSS_SELECTOR, "li.tag-default")
    ARTICLE_POPULAR_TAGS_SECTION = (By.CSS_SELECTOR, "div.sidebar")
    ARTICLE_POPULAR_TAGS_TITLE = (By.CSS_SELECTOR, "div.sidebar p")
    ARTICLE_POPULAR_TAG_LINKS = (By.CSS_SELECTOR, "div.sidebar a.tag-default")from selenium.webdriver.common.by import By

class ArticlePageLocators:
    # 네비게이션 바 요소
    ARTICLE_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    ARTICLE_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    ARTICLE_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    ARTICLE_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    ARTICLE_USER_PROFILE_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    ARTICLE_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
    
    # 홈페이지 요소
    ARTICLE_HOME_PAGE = (By.CSS_SELECTOR, "div.home-page")
    ARTICLE_YOUR_FEED_LINK = (By.CSS_SELECTOR, "a.nav-link.active")
    ARTICLE_GLOBAL_FEED_LINK = (By.CSS_SELECTOR, "ul.nav-pills a.nav-link:not(.active)")
    ARTICLE_ARTICLE_PREVIEW = (By.CSS_SELECTOR, "div.article-preview")
    ARTICLE_ARTICLE_META = (By.CSS_SELECTOR, "div.article-meta")
    ARTICLE_AUTHOR_LINK = (By.CSS_SELECTOR, "a.author")
    ARTICLE_DATE = (By.CSS_SELECTOR, "span.date")
    ARTICLE_FAVORITE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    ARTICLE_PREVIEW_LINK = (By.CSS_SELECTOR, "a.preview-link")
    ARTICLE_ARTICLE_TITLE = (By.CSS_SELECTOR, "a.preview-link h1")
    ARTICLE_ARTICLE_DESCRIPTION = (By.CSS_SELECTOR, "a.preview-link p")
    ARTICLE_READ_MORE = (By.CSS_SELECTOR, "a.preview-link span")
    ARTICLE_TAG_LIST = (By.CSS_SELECTOR, "ul.tag-list")
    ARTICLE_TAG_PILL = (By.CSS_SELECTOR, "li.tag-default.tag-pill.tag-outline")
    
    # 사이드바 요소
    ARTICLE_SIDEBAR = (By.CSS_SELECTOR, "div.sidebar")
    ARTICLE_POPULAR_TAGS = (By.CSS_SELECTOR, "div.sidebar p")
    ARTICLE_TAG_PILL_LINK = (By.CSS_SELECTOR, "a.tag-default.tag-pill")
    
    # 아티클 페이지 요소
    ARTICLE_ARTICLE_PAGE = (By.CSS_SELECTOR, "div.article-page")
    ARTICLE_BANNER = (By.CSS_SELECTOR, "div.banner")
    ARTICLE_ARTICLE_TITLE_BANNER = (By.CSS_SELECTOR, "div.banner h1")
    ARTICLE_ARTICLE_CONTENT = (By.CSS_SELECTOR, "div.article-content")
    ARTICLE_ARTICLE_TEXT = (By.CSS_SELECTOR, "div.article-content p")
    
    # 댓글 관련 요소
    ARTICLE_COMMENT_FORM = (By.CSS_SELECTOR, "form.comment-form")
    ARTICLE_COMMENT_TEXTAREA = (By.CSS_SELECTOR, "textarea.form-control")
    ARTICLE_POST_COMMENT_BUTTON = (By.CSS_SELECTOR, "button.btn-primary[type='submit']")
    ARTICLE_COMMENT_CARD = (By.CSS_SELECTOR, "div.card")
    ARTICLE_COMMENT_TEXT = (By.CSS_SELECTOR, "p.card-text")
    ARTICLE_COMMENT_AUTHOR = (By.CSS_SELECTOR, "a.comment-author")
    ARTICLE_COMMENT_DATE = (By.CSS_SELECTOR, "span.date-posted")
    ARTICLE_DELETE_COMMENT_BUTTON = (By.CSS_SELECTOR, "span.mod-options i.ion-trash-a")from selenium.webdriver.common.by import By

class ArticlePageLocators:
    # Navbar elements
    ARTICLE_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    ARTICLE_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    ARTICLE_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    ARTICLE_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    ARTICLE_USER_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    ARTICLE_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
    
    # Home page elements
    ARTICLE_YOUR_FEED_LINK = (By.CSS_SELECTOR, "a.nav-link.active")
    ARTICLE_GLOBAL_FEED_LINK = (By.CSS_SELECTOR, "ul.nav.nav-pills.outline-active li:nth-child(2) a.nav-link")
    ARTICLE_PREVIEW_ITEMS = (By.CSS_SELECTOR, "div.article-preview")
    ARTICLE_FAVORITE_BUTTONS = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary, button.btn.btn-sm.btn-outline-primary")
    ARTICLE_PREVIEW_LINKS = (By.CSS_SELECTOR, "a.preview-link")
    ARTICLE_PREVIEW_TITLES = (By.CSS_SELECTOR, "a.preview-link h1")
    ARTICLE_PREVIEW_DESCRIPTIONS = (By.CSS_SELECTOR, "a.preview-link p")
    ARTICLE_READ_MORE_LINKS = (By.CSS_SELECTOR, "a.preview-link span")
    ARTICLE_TAG_LIST = (By.CSS_SELECTOR, "ul.tag-list")
    ARTICLE_TAG_ITEMS = (By.CSS_SELECTOR, "li.tag-default.tag-pill.tag-outline")
    ARTICLE_POPULAR_TAGS = (By.CSS_SELECTOR, "div.sidebar p")
    ARTICLE_TAG_PILLS = (By.CSS_SELECTOR, "a.tag-default.tag-pill")
    
    # Article detail page elements
    ARTICLE_BANNER = (By.CSS_SELECTOR, "div.banner")
    ARTICLE_TITLE = (By.CSS_SELECTOR, "div.banner h1")
    ARTICLE_AUTHOR_LINK = (By.CSS_SELECTOR, "a.author")
    ARTICLE_DATE = (By.CSS_SELECTOR, "span.date")
    ARTICLE_CONTENT = (By.CSS_SELECTOR, "div.article-content p")
    ARTICLE_COMMENT_FORM = (By.CSS_SELECTOR, "form.card.comment-form")
    ARTICLE_COMMENT_TEXTAREA = (By.CSS_SELECTOR, "textarea.form-control")
    ARTICLE_POST_COMMENT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary[type='submit']")
    ARTICLE_COMMENT_CARDS = (By.CSS_SELECTOR, "div.card")
    ARTICLE_COMMENT_TEXT = (By.CSS_SELECTOR, "p.card-text")
    ARTICLE_COMMENT_AUTHOR = (By.CSS_SELECTOR, "a.comment-author")
    ARTICLE_COMMENT_DATE = (By.CSS_SELECTOR, "span.date-posted")
    ARTICLE_DELETE_COMMENT_BUTTON = (By.CSS_SELECTOR, "span.mod-options i.ion-trash-a")
    
    # Profile page elements
    ARTICLE_PROFILE_USER_IMG = (By.CSS_SELECTOR, "img.user-img")
    ARTICLE_PROFILE_USERNAME = (By.CSS_SELECTOR, "div.user-info h4")
    ARTICLE_PROFILE_BIO = (By.CSS_SELECTOR, "div.user-info p")
    ARTICLE_EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-outline-secondary.action-btn")
    ARTICLE_MY_ARTICLES_TAB = (By.CSS_SELECTOR, "a.nav-link.active[href='/@1']")
    ARTICLE_FAVORITED_ARTICLES_TAB = (By.CSS_SELECTOR, "a.nav-link[href='/@1/favorites']")
    ARTICLE_PAGINATION = (By.CSS_SELECTOR, "ul.pagination")
    ARTICLE_PAGINATION_ITEMS = (By.CSS_SELECTOR, "li.page-item")
    ARTICLE_PAGINATION_LINKS = (By.CSS_SELECTOR, "a.page-link")
>>>>>>> Stashed changes
