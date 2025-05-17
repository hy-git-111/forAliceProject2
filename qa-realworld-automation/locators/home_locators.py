from selenium.webdriver.common.by import By

class HomePageLocators:
    # ───── 네비게이션 바 ─────
    NAVBAR_BRAND = (By.CSS_SELECTOR, ".navbar-brand")
    NAVBAR_NAV = (By.CSS_SELECTOR, ".navbar-nav")
    NAV_HOME_LINK = (By.CSS_SELECTOR, ".nav-item:nth-child(1) .nav-link")
    NAV_NEW_POST_LINK = (By.CSS_SELECTOR, ".nav-item:nth-child(2) .nav-link")
    NAV_SETTINGS_LINK = (By.CSS_SELECTOR, ".nav-item:nth-child(3) .nav-link")
    NAV_USER_LINK = (By.CSS_SELECTOR, ".nav-item:nth-child(4) .nav-link")
    NAV_USER_PIC = (By.CSS_SELECTOR, ".user-pic")

    # ───── 피드 탭 영역 ─────
    TAB_YOUR_FEED = (By.CSS_SELECTOR, ".nav-link.active")
    TAB_GLOBAL_FEED = (By.CSS_SELECTOR, ".nav-item:nth-child(2) .nav-link:not(.active)")

    # ───── 기사 목록 / 프리뷰 ─────
    ARTICLE_PREVIEW = (By.CSS_SELECTOR, ".article-preview")

    # ───── 사이드바 태그 ─────
    SIDEBAR = (By.CSS_SELECTOR, ".sidebar")
    POPULAR_TAGS_TEXT = (By.CSS_SELECTOR, ".sidebar p")
    TAG_LIST = (By.CSS_SELECTOR, ".tag-list")

    # ───── 페이지 전체 레이아웃 ─────
    ROOT = (By.ID, "root")
    CONTAINER = (By.CSS_SELECTOR, ".container.page")
