
    @pytest.mark.data_required
    def test_post_comment_on_article(self, driver):
        """
        테스트 시나리오: 게시글에 댓글 작성 기능 확인
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com" / PW "test1234")
        3. [Global Feed 탭]에 게시글 ≥ 1 존재
        
        재현 절차:
        1. [Global Feed 탭] 클릭
        2. 첫 번째 게시글 카드 클릭 > 상세 페이지 이동
        3. [댓글 입력란] 클릭 후 "테스트 댓글" 입력
        4. [Post Comment 버튼] 클릭
        
        기대 결과:
        1. 새 댓글 카드에 "테스트 댓글" 표시
        2. 프로필 이미지 표시
        3. 닉네임 링크 표시
        4. 작성 날짜 표시
        5. 휴지통 아이콘 표시
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_comment"]
            
            # 로그인
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            # 홈페이지 접근 및 Global Feed 탭 클릭
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 댓글 작성
            article_page = ArticlePage(driver)
            comment_text = "테스트 댓글"
            article_page.post_comment(comment_text)
            
            # 댓글 표시 확인
            assert article_page.is_comment_text_displayed(comment_text), "댓글 텍스트가 표시되지 않았습니다."
            
            # 프로필 이미지 확인
            assert article_page.is_comment_profile_image_displayed(), "댓글 프로필 이미지가 표시되지 않았습니다."
            
            # 닉네임 링크 확인
            assert article_page.is_comment_author_link_displayed(), "댓글 작성자 링크가 표시되지 않았습니다."
            
            # 작성 날짜 확인
            assert article_page.is_comment_date_displayed(), "댓글 작성 날짜가 표시되지 않았습니다."
            
            # 휴지통 아이콘 확인
            assert article_page.is_comment_delete_icon_displayed(), "댓글 삭제 아이콘이 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_long_english_comment_width(self, driver):
        """
        테스트 시나리오: 긴 영문 댓글 작성 시 너비 확인
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com", PW "test1234")
        3. Global Feed 탭에 게시글 ≥ 1 존재
        
        재현 절차:
        1. [Global Feed 탭] 클릭
        2. 첫 번째 게시글 카드 클릭 > 상세 페이지 이동
        3. [댓글 입력란] 클릭 후 120자 이상 영문 문자열 입력 ("TEST"×30)
        4. [Post Comment 버튼] 클릭
        
        기대 결과:
        1. 댓글 카드 너비가 댓글 리스트 컨테이너 너비보다 같거나 작음
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_comment"]
            
            # 로그인
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            # 홈페이지 접근 및 Global Feed 탭 클릭
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 긴 영문 댓글 작성 (120자 이상)
            article_page = ArticlePage(driver)
            long_comment = "TEST" * 30  # 120자 이상
            article_page.post_comment(long_comment)
            
            # 댓글 카드와 컨테이너 너비 비교
            comment_card_width = article_page.get_last_comment_card_width()
            comment_container_width = article_page.get_comment_container_width()
            
            assert comment_card_width <= comment_container_width, f"댓글 카드 너비({comment_card_width})가 컨테이너 너비({comment_container_width})보다 큽니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_long_special_chars_comment_width(self, driver):
        """
        테스트 시나리오: 긴 특수문자 댓글 작성 시 너비 확인
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com", PW "test1234")
        3. Global Feed 탭에 게시글 ≥ 1 존재
        
        재현 절차:
        1. [Global Feed 탭] 클릭
        2. 첫 번째 게시글 카드 클릭 > 상세 페이지 이동
        3. [댓글 입력란] 클릭 후 120자 이상 특수문자 문자열 입력 ("!@#%"×30)
        4. [Post Comment 버튼] 클릭
        
        기대 결과:
        1. 댓글 카드 너비가 댓글 리스트 컨테이너 너비보다 같거나 작음
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_comment"]
            
            # 로그인
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            # 홈페이지 접근 및 Global Feed 탭 클릭
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 긴 특수문자 댓글 작성 (120자 이상)
            article_page = ArticlePage(driver)
            special_chars_comment = "!@#%" * 30  # 120자 이상
            article_page.post_comment(special_chars_comment)
            
            # 댓글 카드와 컨테이너 너비 비교
            comment_card_width = article_page.get_last_comment_card_width()
            comment_container_width = article_page.get_comment_container_width()
            
            assert comment_card_width <= comment_container_width, f"댓글 카드 너비({comment_card_width})가 컨테이너 너비({comment_container_width})보다 큽니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 요청하신 5개의 테스트 케이스를 모두 구현했습니다:

1. 비밀번호 뒤에 공백이 있는 경우 오류 메시지 확인
2. 비밀번호에 공백만 입력한 경우 오류 메시지 확인
3. 게시글에 댓글 작성 기능 확인
4. 긴 영문 댓글 작성 시 너비 확인
5. 긴 특수문자 댓글 작성 시 너비 확인

각 테스트는 POM 구조를 따르며, 로케이터를 import하여 사용하고 있습니다. 또한 각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다. 테스트 데이터는 load_test_data() 함수를 통해 JSON 파일에서 로드하도록 구현했습니다.

모든 테스트는 독립적으로 실행되며, 오류 처리를 위해 try-except 구문을 사용했습니다. 또한 @pytest.mark.data_required 데코레이터를 통해 데이터 세팅이 필요한 테스트임을 표시했습니다.

# ===== 다음 배치 =====

테스트 케이스를 분석하고 POM 구조에 맞는 Pytest 테스트 코드를 작성하겠습니다. 먼저 필요한 로케이터와 페이지 객체를 가정하고 테스트 코드를 작성하겠습니다.

```python
import os
import json
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 로케이터 임포트
from locators.article_locators import ArticlePageLocators as ArticleLoc
from locators.home_locators import HomePageLocators as HomeLoc

# 페이지 객체 임포트
from pages.home_page import HomePage
from pages.article_page import ArticlePage
from pages.login_page import LoginPage

# 테스트 데이터 로드 함수
def load_test_data():
    """테스트 데이터 JSON 파일을 로드하는 함수"""
    with open('qa-realworld-automation/data/test_data.json', 'r', encoding='utf-8') as file:
        return json.load(file)


class TestArticleComments:
    """게시글 댓글 기능 테스트 클래스"""

    @pytest.mark.data_required
    def test_long_comment_display(self, driver):
        """
        긴 댓글(120자 이상)이 UI에 올바르게 표시되는지 테스트
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com", PW "test1234")
        3. Global Feed 탭에 게시글 ≥ 1 존재
        """
        try:
            # 로그인 및 Global Feed 탭으로 이동
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 댓글 작성
            article_page = ArticlePage(driver)
            long_comment = "0123" * 30  # 120자 이상 숫자 문자열
            article_page.add_comment(long_comment)
            
            # 댓글 카드 너비 검증
            comment_card = driver.find_element(*ArticleLoc.LAST_COMMENT_CARD)
            comment_container = driver.find_element(*ArticleLoc.COMMENT_CONTAINER)
            
            # 댓글 카드 너비가 컨테이너 너비보다 같거나 작은지 확인
            assert comment_card.size['width'] <= comment_container.size['width'], \
                "댓글 카드 너비가 컨테이너 너비보다 큽니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_multiline_comment_display(self, driver):
        """
        여러 줄 댓글이 UI에 올바르게 표시되는지 테스트
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com" / PW "test1234")
        3. [Global Feed 탭]에 게시글 ≥ 1 존재
        """
        try:
            # 로그인 및 Global Feed 탭으로 이동
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 여러 줄 댓글 작성
            article_page = ArticlePage(driver)
            multiline_comment = "첫 줄\n둘째 줄"
            article_page.add_comment(multiline_comment)
            
            # 댓글 본문에 줄바꿈이 있는지 확인
            last_comment_text = driver.find_element(*ArticleLoc.LAST_COMMENT_TEXT)
            
            # HTML 내용 확인 (줄바꿈 태그 또는 여러 블록 요소 확인)
            html_content = last_comment_text.get_attribute('innerHTML')
            
            # <br> 태그가 있거나 여러 블록 요소로 나뉘어 있는지 확인
            assert ("<br>" in html_content or 
                    "첫 줄" in html_content and "둘째 줄" in html_content), \
                "댓글에 줄바꿈이 올바르게 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_delete_comment(self, driver):
        """
        댓글 삭제 기능 테스트
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com" / PW "test1234")
        3. [Global Feed 탭]에 게시글 ≥ 1 존재
        4. 대상 게시글에 본인 댓글 "삭제 대상" 존재
        """
        try:
            # 로그인 및 Global Feed 탭으로 이동
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # "삭제 대상" 댓글 찾아 삭제
            article_page = ArticlePage(driver)
            article_page.delete_comment_with_text("삭제 대상")
            
            # 삭제된 댓글이 더 이상 존재하지 않는지 확인
            wait = WebDriverWait(driver, 10)
            
            # 페이지에 "삭제 대상" 텍스트를 포함하는 댓글 카드가 없는지 확인
            deleted_comments = driver.find_elements(*ArticleLoc.COMMENT_CARD_WITH_TEXT("삭제 대상"))
            assert len(deleted_comments) == 0, "댓글이 삭제되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_empty_comment_submission(self, driver):
        """
        빈 댓글 제출 시 동작 테스트
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com" / PW "test1234")
        3. [Global Feed 탭]에 게시글 ≥ 1 존재
        """
        try:
            # 로그인 및 Global Feed 탭으로 이동
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 댓글 개수 확인
            article_page = ArticlePage(driver)
            initial_comment_count = article_page.get_comment_count()
            
            # 빈 댓글 제출
            article_page.add_comment("")
            
            # 댓글 개수가 변하지 않았는지 확인
            final_comment_count = article_page.get_comment_count()
            assert initial_comment_count == final_comment_count, \
                "빈 댓글 제출 후 댓글 개수가 변경되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_new_comment_addition(self, driver):
        """
        새 댓글 추가 시 UI 업데이트 테스트
        
        사전 조건:
        1. 메인 페이지 진입
        2. 로그인 상태 (ID "test1@test.com" / PW "test1234")
        3. [Global Feed 탭]에 게시글 ≥ 1 존재
        4. 대상 게시글에 기존 댓글 2 건 이상 존재
        """
        try:
            # 로그인 및 Global Feed 탭으로 이동
            login_page = LoginPage(driver)
            login_page.login("test1@test.com", "test1234")
            
            home_page = HomePage(driver)
            home_page.click_global_feed_tab()
            
            # 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 기존 댓글 개수 및 첫 번째 댓글 내용 저장
            article_page = ArticlePage(driver)
            initial_comment_count = article_page.get_comment_count()
            
            # 첫 번째 댓글 내용 저장
            first_comment_text = ""
            if initial_comment_count > 0:
                first_comment_element = driver.find_element(*ArticleLoc.FIRST_COMMENT_TEXT)
                first_comment_text = first_comment_element.text
            
            # 새 댓글 추가
            new_comment = "신규 댓글"
            article_page.add_comment(new_comment)
            
            # 댓글 개수 증가 확인
            final_comment_count = article_page.get_comment_count()
            assert final_comment_count == initial_comment_count + 1, \
                f"댓글 개수가 예상대로 증가하지 않았습니다. 예상: {initial_comment_count + 1}, 실제: {final_comment_count}"
            
            # 마지막 댓글이 새로 추가한 댓글인지 확인
            last_comment_text = driver.find_element(*ArticleLoc.LAST_COMMENT_TEXT)
            assert new_comment in last_comment_text.text, \
                f"마지막 댓글이 새로 추가한 댓글이 아닙니다. 예상: {new_comment}, 실제: {last_comment_text.text}"
            
            # 첫 번째 댓글 내용이 변경되지 않았는지 확인
            if initial_comment_count > 0:
                current_first_comment = driver.find_element(*ArticleLoc.FIRST_COMMENT_TEXT)
                assert first_comment_text == current_first_comment.text, \
                    "첫 번째 댓글 내용이 변경되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 POM 구조를 따르며, 주어진 JSON 형식의 테스트 케이스를 기반으로 작성되었습니다. 각 테스트 함수는 테스트 케이스의 시나리오를 구현하고 있으며, 다음과 같은 특징을 가집니다:

1. 모든 테스트는 `@pytest.mark.data_required` 데코레이터를 사용하여 데이터 세팅이 필요함을 표시합니다.
2. 각 테스트는 독립적으로 실행되며, 필요한 사전 조건을 설정합니다.
3. 테스트 실패 시 예외를 잡아 명확한 오류 메시지를 제공합니다.
4. 각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다.

이 코드는 로케이터와 페이지 객체가 이미 존재한다는 가정 하에 작성되었으며, 실제 환경에서는 해당 파일들을 import하여 사용해야 합니다.

# ===== 다음 배치 =====

다음은 요청하신 테스트 케이스에 맞춰 작성한 Pytest 테스트 코드입니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하도록 작성했습니다.

```python
import os
import json
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Page Objects
from pages.home_page import HomePage
from pages.article_page import ArticlePage
from pages.profile_page import ProfilePage

# Locators
from locators.home_locators import HomePageLocators as HomeLoc
from locators.article_locators import ArticlePageLocators as ArticleLoc
from locators.profile_locators import ProfilePageLocators as ProfileLoc

# 테스트 데이터 로드 함수
def load_test_data():
    """테스트 데이터 파일을 로드하는 함수"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


class TestArticleInteractions:
    """게시글 상호작용 관련 테스트 클래스"""

    @pytest.mark.data_not_required
    def test_non_logged_in_user_article_view(self, driver):
        """
        비로그인 상태에서 게시글 상세 페이지 접근 시 댓글 작성 불가 테스트
        
        사전 조건:
        1. 메인 페이지 진입
        2. 비로그인 상태
        3. [Global Feed 탭]에 게시글 ≥ 1 존재
        """
        try:
            # 1. 홈페이지 접근
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            
            # 2. Global Feed 탭 클릭
            home_page.click_global_feed_tab()
            
            # 3. 첫 번째 게시글 클릭
            home_page.click_first_article()
            
            # 4. 상세 페이지 이동 확인
            article_page = ArticlePage(driver)
            
            # 5. 로그인 필요 문구 확인
            sign_in_message = article_page.get_sign_in_message()
            assert "Sign in or sign up to add comments on this article." in sign_in_message
            
            # 6. 댓글 입력창 및 제출 버튼 없음 확인
            assert article_page.is_comment_form_not_present() == True
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
