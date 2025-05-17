from selenium.webdriver.common.by import By

class EditorPageLocators:
<<<<<<< Updated upstream
    # ───── 네비게이션 바 ─────
=======
>>>>>>> Stashed changes
    EDITOR_NAVBAR_BRAND = (By.CSS_SELECTOR, "a.navbar-brand")
    EDITOR_HOME_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    EDITOR_NEW_POST_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    EDITOR_SETTINGS_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    EDITOR_PROFILE_LINK = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    EDITOR_USER_PIC = (By.CSS_SELECTOR, "img.user-pic")
<<<<<<< Updated upstream

    # ───── 게시글 작성 폼 ─────
    EDITOR_TITLE_INPUT = (By.CSS_SELECTOR, "input.form-control.form-control-lg[placeholder='Article Title']")
    EDITOR_ABOUT_INPUT = (By.CSS_SELECTOR, "input.form-control[placeholder='What\'s this article about?']")
    EDITOR_CONTENT_TEXTAREA = (By.CSS_SELECTOR, "textarea.form-control")
    EDITOR_TAGS_INPUT = (By.CSS_SELECTOR, "input.form-control[placeholder='Enter tags']")
    EDITOR_TAG_LIST = (By.CSS_SELECTOR, "div.tag-list")

    # ───── 버튼 영역 ─────
    EDITOR_PUBLISH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.pull-xs-right.btn-primary")
=======
    EDITOR_TITLE_INPUT = (By.CSS_SELECTOR, "input.form-control.form-control-lg[placeholder='Article Title']")
    EDITOR_ABOUT_INPUT = (By.CSS_SELECTOR, "input.form-control[placeholder='What\'s this article about?']")
    EDITOR_CONTENT_TEXTAREA = (By.CSS_SELECTOR, "textarea.form-control[placeholder='Write your article (in markdown)']")
    EDITOR_TAGS_INPUT = (By.CSS_SELECTOR, "input.form-control[placeholder='Enter tags']")
    EDITOR_TAG_LIST = (By.CSS_SELECTOR, "div.tag-list")
    EDITOR_PUBLISH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.pull-xs-right.btn-primary")
>>>>>>> Stashed changes
