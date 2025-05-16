# 웹 요소 로케이터 목록

## Home

Home_LOCATORS = {
    "root": "#root",
    "navbar_brand": ".navbar-brand",
    "home_link": ".nav-item:nth-child(1) .nav-link",
    "signin_link": ".nav-item:nth-child(2) .nav-link",
    "signup_link": ".nav-item:nth-child(3) .nav-link",
    "page_title": ".text-xs-center",
    "need_account_link": ".text-xs-center > a",
    "email_input": ".form-group:nth-child(1) .form-control",
    "password_input": ".form-group:nth-child(2) .form-control",
    "signin_button": ".btn-primary"
}# 웹 요소 로케이터 목록

## [Login]

Login_LOCATORS = {
    "root": "#root",
    "navbar_brand": ".navbar-brand",
    "home_link": ".nav-link[href='/']",
    "signin_link": ".nav-link[href='/login']",
    "signup_link": ".nav-link[href='/register']",
    "signin_header": ".text-xs-center",
    "need_account_link": ".text-xs-center > a",
    "email_input": ".form-control[type='email']",
    "password_input": ".form-control[type='password']",
    "signin_button": ".btn-primary[type='submit']"
}

## [Home]

Home_LOCATORS = {
    "root": "#root",
    "navbar_brand": ".navbar-brand",
    "home_link": ".nav-link[href='/']",
    "new_post_link": ".nav-link[href='/editor']",
    "settings_link": ".nav-link[href='/settings']",
    "profile_link": ".nav-link[href='/@1']",
    "user_pic": ".user-pic",
    "your_feed_link": ".nav-link.active",
    "global_feed_link": ".nav-link:not(.active)",
    "article_preview": ".article-preview",
    "popular_tags": ".sidebar p",
    "tag_list": ".tag-list"
}