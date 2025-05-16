# 웹 요소 로케이터 목록

## [ProfilePage]

ProfilePage_LOCATORS = {
    "root": "#root",
    "navbar_brand": ".navbar-brand",
    "home_link": ".nav-item:nth-child(1) .nav-link",
    "new_post_link": ".nav-item:nth-child(2) .nav-link",
    "settings_link": ".nav-item:nth-child(3) .nav-link",
    "profile_link": ".nav-item:nth-child(4) .nav-link",
    "user_pic_nav": ".user-pic",
    "user_img": ".user-img",
    "username_header": ".user-info h4",
    "user_bio": ".user-info p",
    "edit_profile_settings_btn": ".action-btn",
    "my_articles_tab": ".nav-pills .nav-link.active",
    "favorited_articles_tab": ".nav-pills .nav-link:not(.active)",
    "article_preview": ".article-preview",
    "article_author_img": ".article-meta img",
    "article_author_link": ".article-meta .author",
    "article_date": ".article-meta .date",
    "favorite_button": ".btn-outline-primary",
    "favorite_count": ".ion-heart",
    "article_title": ".preview-link h1",
    "article_description": ".preview-link p",
    "read_more_link": ".preview-link span",
    "tag_list": ".tag-list"
}# 웹 요소 로케이터 목록

## [Profile]

Profile_LOCATORS = {
    "root": "#root",
    "navbar": ".navbar",
    "navbar_brand": ".navbar-brand",
    "home_link": ".nav-item:nth-child(1) .nav-link",
    "new_post_link": ".nav-item:nth-child(2) .nav-link",
    "settings_link": ".nav-item:nth-child(3) .nav-link",
    "profile_link": ".nav-item:nth-child(4) .nav-link",
    "user_pic": ".user-pic",
    "profile_page": ".profile-page",
    "user_info": ".user-info",
    "user_img": ".user-img",
    "username": ".col-xs-12.col-md-10.offset-md-1 h4",
    "edit_profile_settings_btn": ".btn.btn-sm.btn-outline-secondary.action-btn",
    "articles_toggle": ".articles-toggle",
    "my_articles_tab": ".nav-pills .nav-item:nth-child(1) .nav-link",
    "favorited_articles_tab": ".nav-pills .nav-item:nth-child(2) .nav-link",
    "article_preview": ".article-preview",
    "article_meta": ".article-meta",
    "author_link": ".author",
    "date": ".date",
    "favorite_button": ".btn.btn-sm.btn-outline-primary",
    "favorite_count": ".ion-heart",
    "preview_link": ".preview-link",
    "article_title": ".preview-link h1",
    "article_description": ".preview-link p",
    "read_more": ".preview-link span",
    "tag_list": ".tag-list",
    "no_articles_message": ".article-preview:contains('No articles are here... yet.')"
}# 웹 요소 로케이터 목록

## Profile

Profile_LOCATORS = {
    "root": "#root",
    "navbar_brand": ".navbar-brand",
    "home_link": ".nav-item:nth-child(1) .nav-link",
    "new_post_link": ".nav-item:nth-child(2) .nav-link",
    "settings_link": ".nav-item:nth-child(3) .nav-link",
    "profile_link": ".nav-item:nth-child(4) .nav-link",
    "user_pic": ".user-pic",
    "profile_user_img": ".user-img",
    "profile_username": ".col-xs-12.col-md-10.offset-md-1 h4",
    "edit_profile_settings_btn": ".btn.btn-sm.btn-outline-secondary.action-btn",
    "my_articles_tab": ".nav-pills .nav-item:nth-child(1) .nav-link",
    "favorited_articles_tab": ".nav-pills .nav-item:nth-child(2) .nav-link",
    "article_preview": ".article-preview",
    "article_meta": ".article-meta",
    "article_author": ".article-meta .author",
    "article_date": ".article-meta .date",
    "favorite_button": ".btn.btn-sm.btn-outline-primary",
    "favorite_count": ".ion-heart",
    "article_preview_link": ".preview-link",
    "article_title": ".preview-link h1",
    "article_description": ".preview-link p",
    "read_more": ".preview-link span",
    "tag_list": ".tag-list",
    "no_articles_message": ".article-preview"
}

## Settings

Settings_LOCATORS = {
    "settings_page": ".settings-page",
    "settings_title": ".text-xs-center",
    "profile_picture_input": ".form-group:nth-child(1) .form-control",
    "username_input": ".form-group:nth-child(2) .form-control",
    "bio_textarea": ".form-group:nth-child(3) .form-control",
    "email_input": ".form-group:nth-child(4) .form-control",
    "password_input": ".form-group:nth-child(5) .form-control",
    "update_settings_button": ".btn.btn-lg.btn-primary",
    "logout_button": ".btn.btn-outline-danger"
}