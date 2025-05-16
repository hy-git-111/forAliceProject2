from selenium.webdriver.common.by import By

CRAWLING_LOCATORS = [
    ("Home", None),
    ("Home_YourFeed_Article", (By.CLASS_NAME, "article-preview")),
    ("Home_Global_Feed", (By.CSS_SELECTOR, "div.feed-toggle > ul > li:nth-child(2) > a")),
    ("Home_New_Post", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(2) > a")),
    ("Home_Settings", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(3) > a")),
    ("Home_MyPage", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a")),
    ("Home_MyPage_Edit_Profile", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a"), (By.CLASS_NAME, "btn-outline-secondary")),
    ("Home_MyPage_Article", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a"), (By.CLASS_NAME, "article-preview")),
    ("Home_MyPage_Favorited_Articles", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(4) > a"), (By.CSS_SELECTOR, "div.articles-toggle > ul > li:nth-child(2) > a")),
    ("Home_NewPost_Publish", (By.CSS_SELECTOR, "nav > div > ul > li:nth-child(2) > a"))    # 5번 데이터 팔로우하는 계정 없음
]