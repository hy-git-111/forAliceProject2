from selenium.webdriver.common.by import By

CRAWLING_LOCATORS = [
    ("Home", None),
    ("HOME_YourFeed_Article", (By.CLASS_NAME, "article-preview")),
    ("HOME_Global_Feed", (By.CSS_SELECTOR, "div.feed-toggle > ul > li:nth-child(2) > a")),
    ("HOME_New_Post", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(2) > a")),
    ("HOME_Settings", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(3) > a")),
    ("HOME_MyPage", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a")),
    ("HOME_MyPage_Edit_Profile", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a"), (By.CLASS_NAME, "btn-outline-secondary")),
    ("HOME_MyPage_Article", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a"), (By.CLASS_NAME, "article-preview")),
    ("HOME_MyPage_Favorited_Articles", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a"), (By.CSS_SELECTOR, "div.articles-toggle > ul > li:nth-child(2) > a")),
    ("HOME_NewPost_Publish", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(2) > a"))    # 5번 데이터 팔로우하는 계정 없음
]