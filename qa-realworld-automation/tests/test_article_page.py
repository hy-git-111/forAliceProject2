아래는 요청하신 `test_article_page.py` 파일의 코드입니다. POM 구조를 따르며 5개의 테스트 케이스를 포함합니다.

```python
import os
import json
import pytest
from pages.base_page import BasePage
from locators.article_locators import ArticlePageLocators as Loc

def load_test_data():
    """테스트 데이터 파일을 로드하는 함수"""
    data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_data.json')
    with open(data_file_path, 'r') as file:
        return json.load(file)

class ArticlePage(BasePage):
    """기사 페이지 관련 기능을 담당하는 페이지 객체"""
    
    def sign_up(self, username, email, password):
        """회원가입 기능 수행"""
        self._send_keys(Loc.SIGNUP_USERNAME_INPUT, username)
        self._send_keys(Loc.SIGNUP_EMAIL_INPUT, email)
        self._send_keys(Loc.SIGNUP_PASSWORD_INPUT, password)
        self._click(Loc.SIGNUP_SUBMIT_BUTTON)
    
    def sign_up_without_username(self, email, password):
        """사용자명 없이 회원가입 시도"""
        self._send_keys(Loc.SIGNUP_EMAIL_INPUT, email)
        self._send_keys(Loc.SIGNUP_PASSWORD_INPUT, password)
        self._click(Loc.SIGNUP_SUBMIT_BUTTON)
    
    def sign_up_without_email(self, username, password):
        """이메일 없이 회원가입 시도"""
        self._send_keys(Loc.SIGNUP_USERNAME_INPUT, username)
        self._send_keys(Loc.SIGNUP_PASSWORD_INPUT, password)
        self._click(Loc.SIGNUP_SUBMIT_BUTTON)
    
    def sign_up_without_password(self, username, email):
        """비밀번호 없이 회원가입 시도"""
        self._send_keys(Loc.SIGNUP_USERNAME_INPUT, username)
        self._send_keys(Loc.SIGNUP_EMAIL_INPUT, email)
        self._click(Loc.SIGNUP_SUBMIT_BUTTON)
    
    def sign_up_with_invalid_email(self, username, invalid_email, password):
        """유효하지 않은 이메일로 회원가입 시도"""
        self._send_keys(Loc.SIGNUP_USERNAME_INPUT, username)
        self._send_keys(Loc.SIGNUP_EMAIL_INPUT, invalid_email)
        self._send_keys(Loc.SIGNUP_PASSWORD_INPUT, password)
        self._click(Loc.SIGNUP_SUBMIT_BUTTON)
    
    def verify_successful_signup(self, username):
        """회원가입 성공 여부 확인"""
        return self._is_displayed(Loc.NAV_USERNAME) and self._get_text(Loc.NAV_USERNAME) == username
    
    def verify_nav_links_after_signup(self):
        """회원가입 후 네비게이션 링크 확인"""
        return (
            self._is_displayed(Loc.NAV_NEW_POST) and
            self._is_displayed(Loc.NAV_SETTINGS) and
            self._is_displayed(Loc.NAV_USERNAME) and
            not self._is_displayed(Loc.NAV_SIGNIN) and
            not self._is_displayed(Loc.NAV_SIGNUP)
        )
    
    def verify_error_message(self, expected_error):
        """에러 메시지 확인"""
        errors = self._get_text(Loc.ERROR_MESSAGE_CONTAINER)
        return expected_error in errors


@pytest.mark.data_required
def test_signup_success(driver):
    """
    회원가입 성공 테스트
    
    사전 조건:
    1. 회원가입 페이지 (/register) 접속
    2. 테스트에 사용할 고유 이메일과 사용자명
    
    검증 항목:
    1. 홈 페이지로 리디렉션
    2. 네비게이션 바에 사용자명 표시
    3. 네비게이션 바에 적절한 링크 표시/숨김
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["signup_success"]
        
        # 페이지 객체 생성 및 회원가입 페이지 접속
        page = ArticlePage(driver)
        page.navigate_to("/register")
        
        # 회원가입 수행
        page.sign_up(
            test_data["username"],
            test_data["email"],
            test_data["password"]
        )
        
        # 검증: 홈페이지로 리디렉션
        assert page.get_current_url() == page.base_url + "/"
        
        # 검증: 네비게이션 바에 사용자명 표시
        assert page.verify_successful_signup(test_data["username"])
        
        # 검증: 네비게이션 바에 적절한 링크 표시/숨김
        assert page.verify_nav_links_after_signup()
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")


@pytest.mark.data_not_required
def test_signup_empty_username(driver):
    """
    사용자명 없이 회원가입 시도 테스트
    
    사전 조건:
    1. 회원가입 페이지 (/register) 접속
    
    검증 항목:
    1. 사용자명 누락 에러 메시지 표시
    2. 페이지 URL 변경 없음
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["signup_empty_username"]
        
        # 페이지 객체 생성 및 회원가입 페이지 접속
        page = ArticlePage(driver)
        page.navigate_to("/register")
        current_url = page.get_current_url()
        
        # 사용자명 없이 회원가입 시도
        page.sign_up_without_username(
            test_data["email"],
            test_data["password"]
        )
        
        # 검증: 에러 메시지 표시
        assert page.verify_error_message("username can't be blank")
        
        # 검증: URL 변경 없음
        assert page.get_current_url() == current_url
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")


@pytest.mark.data_not_required
def test_signup_empty_email(driver):
    """
    이메일 없이 회원가입 시도 테스트
    
    사전 조건:
    1. 회원가입 페이지 (/register) 접속
    
    검증 항목:
    1. 이메일 누락 에러 메시지 표시
    2. 페이지 URL 변경 없음
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["signup_empty_email"]
        
        # 페이지 객체 생성 및 회원가입 페이지 접속
        page = ArticlePage(driver)
        page.navigate_to("/register")
        current_url = page.get_current_url()
        
        # 이메일 없이 회원가입 시도
        page.sign_up_without_email(
            test_data["username"],
            test_data["password"]
        )
        
        # 검증: 에러 메시지 표시
        assert page.verify_error_message("email can't be blank")
        
        # 검증: URL 변경 없음
        assert page.get_current_url() == current_url
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")


@pytest.mark.data_not_required
def test_signup_empty_password(driver):
    """
    비밀번호 없이 회원가입 시도 테스트
    
    사전 조건:
    1. 회원가입 페이지 (/register) 접속
    
    검증 항목:
    1. 비밀번호 누락 에러 메시지 표시
    2. 페이지 URL 변경 없음
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["signup_empty_password"]
        
        # 페이지 객체 생성 및 회원가입 페이지 접속
        page = ArticlePage(driver)
        page.navigate_to("/register")
        current_url = page.get_current_url()
        
        # 비밀번호 없이 회원가입 시도
        page.sign_up_without_password(
            test_data["username"],
            test_data["email"]
        )
        
        # 검증: 에러 메시지 표시
        assert page.verify_error_message("password can't be blank")
        
        # 검증: URL 변경 없음
        assert page.get_current_url() == current_url
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")


@pytest.mark.data_not_required
def test_signup_invalid_email(driver):
    """
    유효하지 않은 이메일로 회원가입 시도 테스트
    
    사전 조건:
    1. 회원가입 페이지 (/register) 접속
    
    검증 항목:
    1. 유효하지 않은 이메일 에러 메시지 표시
    2. 페이지 URL 변경 없음
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["signup_invalid_email"]
        
        # 페이지 객체 생성 및 회원가입 페이지 접속
        page = ArticlePage(driver)
        page.navigate_to("/register")
        current_url = page.get_current_url()
        
        # 유효하지 않은 이메일로 회원가입 시도
        page.sign_up_with_invalid_email(
            test_data["username"],
            test_data["invalid_email"],
            test_data["password"]
        )
        
        # 검증: 에러 메시지 표시
        assert page.verify_error_message("email is invalid")
        
        # 검증: URL 변경 없음
        assert page.get_current_url() == current_url
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")
``````python
import os
import json
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.article_locators import ArticlePageLocators as Loc

# 테스트 데이터 로드 함수
def load_test_data():
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_data.json')
    with open(data_file, 'r') as f:
        return json.load(f)

class ArticlesPage(BasePage):
    def navigate_to_register_page(self):
        self.driver.get(f"{self.base_url}/register")
    
    def sign_up(self, username, email, password):
        self._send_keys(Loc.USERNAME_INPUT, username)
        self._send_keys(Loc.EMAIL_INPUT, email)
        self._send_keys(Loc.PASSWORD_INPUT, password)
        self._click(Loc.SIGN_UP_BUTTON)
    
    def double_click_sign_up(self, username, email, password):
        self._send_keys(Loc.USERNAME_INPUT, username)
        self._send_keys(Loc.EMAIL_INPUT, email)
        self._send_keys(Loc.PASSWORD_INPUT, password)
        
        # 더블 클릭 구현
        button = self.driver.find_element(*Loc.SIGN_UP_BUTTON)
        actions = ActionChains(self.driver)
        actions.double_click(button).perform()
    
    def get_error_messages(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(Loc.ERROR_MESSAGE_CONTAINER)
            )
            return self.driver.find_element(*Loc.ERROR_MESSAGE_CONTAINER).text
        except:
            return ""
    
    def is_button_disabled(self):
        button = self.driver.find_element(*Loc.SIGN_UP_BUTTON)
        return button.get_attribute("disabled") == "true" or "disabled" in button.get_attribute("class")
    
    def get_current_url(self):
        return self.driver.current_url
    
    def check_username_in_navbar(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(Loc.NAVBAR_USERNAME)
            )
            return self.driver.find_element(*Loc.NAVBAR_USERNAME).text
        except:
            return ""
    
    def check_html_content(self, element_locator):
        element = self.driver.find_element(*element_locator)
        return element.get_attribute("innerHTML")

@pytest.mark.data_required
def test_signup_with_existing_email(driver):
    """
    이미 가입된 이메일로 회원가입 시도 시 적절한 에러 메시지가 표시되는지 확인
    """
    try:
        test_data = load_test_data()["duplicate_email"]
        page = ArticlesPage(driver)
        
        # 회원가입 페이지로 이동
        page.navigate_to_register_page()
        
        # 이미 존재하는 이메일로 회원가입 시도
        page.sign_up(
            test_data["username"], 
            test_data["existing_email"], 
            test_data["password"]
        )
        
        # 에러 메시지 확인
        error_message = page.get_error_messages()
        assert "email has already been taken" in error_message
        
        # URL 변경 없음 확인
        assert "/register" in page.get_current_url()
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")

@pytest.mark.data_required
def test_signup_with_existing_username(driver):
    """
    이미 가입된 사용자명으로 회원가입 시도 시 적절한 에러 메시지가 표시되는지 확인
    """
    try:
        test_data = load_test_data()["duplicate_username"]
        page = ArticlesPage(driver)
        
        # 회원가입 페이지로 이동
        page.navigate_to_register_page()
        
        # 이미 존재하는 사용자명으로 회원가입 시도
        page.sign_up(
            test_data["existing_username"], 
            test_data["email"], 
            test_data["password"]
        )
        
        # 에러 메시지 확인
        error_message = page.get_error_messages()
        assert "username has already been taken" in error_message
        
        # URL 변경 없음 확인
        assert "/register" in page.get_current_url()
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")

@pytest.mark.data_not_required
def test_signup_with_short_password(driver):
    """
    짧은 비밀번호로 회원가입 시도 시 적절한 에러 메시지가 표시되는지 확인
    """
    try:
        test_data = load_test_data()["short_password"]
        page = ArticlesPage(driver)
        
        # 회원가입 페이지로 이동
        page.navigate_to_register_page()
        
        # 짧은 비밀번호로 회원가입 시도
        page.sign_up(
            test_data["username"], 
            test_data["email"], 
            test_data["short_password"]
        )
        
        # 에러 메시지 확인
        error_message = page.get_error_messages()
        assert "password is too short" in error_message
        
        # URL 변경 없음 확인
        assert "/register" in page.get_current_url()
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")

@pytest.mark.data_not_required
def test_signup_with_xss_username(driver):
    """
    XSS 공격 가능성이 있는 사용자명으로 회원가입 시 적절히 처리되는지 확인
    """
    try:
        test_data = load_test_data()["xss_test"]
        page = ArticlesPage(driver)
        
        # 회원가입 페이지로 이동
        page.navigate_to_register_page()
        
        # XSS 스크립트가 포함된 사용자명으로 회원가입 시도
        page.sign_up(
            test_data["xss_username"], 
            test_data["email"], 
            test_data["password"]
        )
        
        # 로그인 성공 후 네비게이션 바에서 사용자명 확인
        username_html = page.check_html_content(Loc.NAVBAR_USERNAME)
        
        # 스크립트가 실행되지 않고 텍스트로 표시되는지 확인
        assert "alert('XSS_Signup')" in username_html
        assert "<script>" not in username_html or "&lt;script&gt;" in username_html
        
        # 자바스크립트 경고창이 실행되지 않았는지는 직접 확인할 수 없으므로 생략
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")

@pytest.mark.data_not_required
def test_signup_with_double_click(driver):
    """
    회원가입 버튼을 빠르게 두 번 클릭했을 때 중복 가입이 방지되는지 확인
    """
    try:
        test_data = load_test_data()["double_click"]
        page = ArticlesPage(driver)
        
        # 회원가입 페이지로 이동
        page.navigate_to_register_page()
        
        # 회원가입 버튼 더블 클릭
        page.double_click_sign_up(
            test_data["username"], 
            test_data["email"], 
            test_data["password"]
        )
        
        # 버튼이 비활성화되었는지 확인
        assert page.is_button_disabled(), "회원가입 버튼이 더블클릭 후 비활성화되지 않았습니다"
        
        # 로그인 성공 시 홈페이지로 리다이렉트 되는지 확인
        WebDriverWait(driver, 10).until(
            lambda d: "/register" not in d.current_url
        )
        
        # 추가 검증: 네비게이션 바에 사용자명이 표시되는지 확인
        username_displayed = page.check_username_in_navbar()
        assert test_data["username"] in username_displayed
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")
```