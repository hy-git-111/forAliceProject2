from selenium.webdriver.common.by import By

class EditorPage:
    editorNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    editorHomeLink = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    editorNewPostLink = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    editorSettingsLink = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    editorProfileLink = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    editorUserPic = (By.CSS_SELECTOR, "img.user-pic")
    editorTitleInput = (By.CSS_SELECTOR, "input.form-control.form-control-lg[placeholder='Article Title']")
    editorAboutInput = (By.CSS_SELECTOR, "input.form-control[placeholder='What\'s this article about?']")
    editorContentTextarea = (By.CSS_SELECTOR, "textarea.form-control")
    editorTagsInput = (By.CSS_SELECTOR, "input.form-control[placeholder='Enter tags']")
    editorTagList = (By.CSS_SELECTOR, "div.tag-list")
    editorPublishButton = (By.CSS_SELECTOR, "button.btn.btn-lg.pull-xs-right.btn-primary")