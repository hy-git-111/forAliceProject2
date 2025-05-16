## ArticlePage

from selenium.webdriver.common.by import By

class ArticlePage:
    articleNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    articleHomeLink = (By.CSS_SELECTOR, "li.nav-item a.nav-link[href='/']")
    articleNewPostLink = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    articleSettingsLink = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    articleUserProfileLink = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    articleUserPic = (By.CSS_SELECTOR, "img.user-pic")
    articleYourFeedLink = (By.CSS_SELECTOR, "a.nav-link.active")
    articleGlobalFeedLink = (By.CSS_SELECTOR, "li.nav-item a.nav-link:not(.active)")
    articlePreview = (By.CSS_SELECTOR, "div.article-preview")
    articlePopularTagsText = (By.CSS_SELECTOR, "div.sidebar p")
    articleTagList = (By.CSS_SELECTOR, "div.tag-list")## ArticlePage

from selenium.webdriver.common.by import By

class ArticlePage:
    articleNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    articleHomeLink = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    articleNewPostLink = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    articleSettingsLink = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    articleProfileLink = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    articleUserPic = (By.CSS_SELECTOR, "img.user-pic")
    articleYourFeedLink = (By.CSS_SELECTOR, "a.nav-link.active")
    articleGlobalFeedLink = (By.CSS_SELECTOR, "a.nav-link:not(.active)")
    articlePreviewText = (By.CSS_SELECTOR, "div.article-preview")
    articlePopularTagsText = (By.CSS_SELECTOR, "div.sidebar p")
    articleTagList = (By.CSS_SELECTOR, "div.tag-list")
    articleRootContainer = (By.ID, "root")
    articleHomePage = (By.CSS_SELECTOR, "div.home-page")
    articleContainer = (By.CSS_SELECTOR, "div.container.page")## ArticlePage

from selenium.webdriver.common.by import By

class ArticlePage:
    # Navigation elements
    articleNavbarBrand = (By.CSS_SELECTOR, "a.navbar-brand")
    articleHomeLink = (By.CSS_SELECTOR, "a.nav-link[href='/']")
    articleNewPostLink = (By.CSS_SELECTOR, "a.nav-link[href='/editor']")
    articleSettingsLink = (By.CSS_SELECTOR, "a.nav-link[href='/settings']")
    articleProfileLink = (By.CSS_SELECTOR, "a.nav-link[href='/@1']")
    articleUserPic = (By.CSS_SELECTOR, "img.user-pic")
    
    # Home page elements
    articleYourFeedLink = (By.CSS_SELECTOR, "a.nav-link.active")
    articleGlobalFeedLink = (By.CSS_SELECTOR, "li.nav-item:nth-child(2) a.nav-link")
    articlePreviewText = (By.CSS_SELECTOR, "div.article-preview")
    articlePopularTagsText = (By.CSS_SELECTOR, "div.sidebar p")
    articleTagList = (By.CSS_SELECTOR, "div.tag-list")
    
    # Profile page elements
    articleUserImg = (By.CSS_SELECTOR, "img.user-img")
    articleUserName = (By.CSS_SELECTOR, "div.user-info h4")
    articleEditProfileBtn = (By.CSS_SELECTOR, "a.btn.btn-sm.btn-outline-secondary")
    articleMyArticlesLink = (By.CSS_SELECTOR, "a.nav-link.active[href='/@1']")
    articleFavoritedArticlesLink = (By.CSS_SELECTOR, "a.nav-link[href='/@1/favorites']")
    
    # Article elements
    articleAuthorLink = (By.CSS_SELECTOR, "a.author")
    articleDate = (By.CSS_SELECTOR, "span.date")
    articleLikeButton = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary")
    articleLikeCount = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-outline-primary")
    articleTitle = (By.CSS_SELECTOR, "a.preview-link h1")
    articleDescription = (By.CSS_SELECTOR, "a.preview-link p")
    articleReadMore = (By.CSS_SELECTOR, "a.preview-link span")
    articlePreviewTagList = (By.CSS_SELECTOR, "a.preview-link ul.tag-list")
    articlePreviewLink = (By.CSS_SELECTOR, "a.preview-link")