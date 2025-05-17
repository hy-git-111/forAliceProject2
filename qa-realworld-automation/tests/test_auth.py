import os
import json
import pytest
import inspect
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 페이지 객체 임포트
from pages.settings_page import SettingsPage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.home_page import HomePage

# 로케이터 임포트
from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.profile_locators import ProfilePageLocators as ProfileLoc
from locators.signup_locators import SignupPageLocators as SignupLoc
from locators.editor_locators import EditorPageLocators as EditorLoc
from locators.login_locators import LoginPageLocators as LoginLoc
from locators.home_locators import HomePageLocators as HomeLoc

# 유틸리티 임포트
from utils.logger import setup_logger
from config import config

logger = setup_logger(__name__)

def loadTestData():
    # 테스트 데이터 로드 함수
    dataFilePath = os.path.join(config.TEST_DATA_DIR, "test_data.json")
    with open(dataFilePath, 'r', encoding='utf-8') as file:
        return json.load(file)

class TestAuth:
# 인증 시나리오 테스트 클래스
    @pytest.mark.data_not_required
    def testSuccessfulSignup(self, driver):
        # AUTH-AUTO-001: 회원가입 성공 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successSignup"]

            # 회원가입 페이지 접속 및 회원가입 진행
            signupPage = SignupPage(driver)
            signupPage.navigate()
            signupPage.signup(testData["user_name"], testData["email"], testData["password"])
            
            # 홈페이지로 리디렉션 확인
            homePage = HomePage(driver)
            
            # 1. URL 확인
            assert homePage.wait_for_url_contains("/"), "홈페이지로 리디렉션되지 않았습니다."
            
            # 2. 네비게이션 바에 사용자명 표시 확인
            navUsername = homePage.getNavigateUserName()
            assert navUsername == testData["user_name"], f"네비게이션 바에 사용자명이 올바르게 표시되지 않았습니다. 예상: {testData["user_name"]}, 실제: {navUsername}"
            
            # 3. 네비게이션 바 링크 확인
            assert homePage.is_element_visible(HomeLoc.NEW_POST_LINK), "New Post 링크가 표시되지 않았습니다."
            assert homePage.is_element_visible(HomeLoc.SETTINGS_LINK), "Settings 링크가 표시되지 않았습니다."
            assert homePage.is_element_visible(HomeLoc.USER_LINK), "사용자 링크가 표시되지 않았습니다."
            
            # Sign in, Sign up 링크 숨김 확인
            assert not homePage.is_element_visible(HomeLoc.SIGNIN_LINK), "Sign in 링크가 여전히 표시되고 있습니다."
            assert not homePage.is_element_visible(HomeLoc.SIGNUP_LINK), "Sign up 링크가 여전히 표시되고 있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 회원가입 성공 테스트 완료")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"회원가입 성공 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def testEmptyUsernameSignup(self, driver):
        # AUTH-AUTO-002: 사용자명 누락 회원가입 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["noUserNameSignup"]
            
            # 회원가입 페이지 접속 및 회원가입 시도
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 사용자명 필드는 비워두고 이메일과 비밀번호만 입력
            signupPage.signup("", testData["email"], testData["password"])
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            assert "username can't be blank" in errorMessages, f"사용자명 누락 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = signupPage.get_current_url()
            assert "/register" in currentUrl, f"페이지 URL이 변경되었습니다. 현재 URL: {currentUrl}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 사용자명 누락 테스트 완료")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"사용자명 누락 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def testEmptyEmailSignup(self, driver):
        # AUTH-AUTO-003: 이메일 누락 회원가입 테스트
        try:
             # 테스트 데이터 로드
            testData = loadTestData()["noEmailSignup"]
            
            # 회원가입 페이지 접속 및 회원가입 시도
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 이메일 필드는 비워두고 사용자명과 비밀번호만 입력
            signupPage.signup(testData["userName"], "", testData["password"])
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            assert "email can't be blank" in errorMessages, f"이메일 누락 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = signupPage.get_current_url()
            assert "/register" in currentUrl, f"페이지 URL이 변경되었습니다. 현재 URL: {currentUrl}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 이메일 누락 테스트 완료")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"이메일 누락 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def testEmptyPsswordSignup(self, driver):
        # AUTH-AUTO-004: 비밀번호 누락 회원가입 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["noPasswordSignup"]
            
            # 회원가입 페이지 접속 및 회원가입 시도
            signupPage = SignupPage(driver)
            signupPage.navigate()

            # 비밀번호 필드는 비워두고 사용자명과 이메일만 입력
            signupPage.signup(testData["userName"], testData["email"], "")
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            assert "password can't be blank" in errorMessages, f"비밀번호 누락 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = signupPage.get_current_url()
            assert "/register" in currentUrl, f"페이지 URL이 변경되었습니다. 현재 URL: {currentUrl}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 비밀번호 누락 테스트 완료")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"비밀번호 누락 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def testInvalidEmailFormatSignup(self, driver):
        # AUTH-AUTO-005: 잘못된 이메일 형식 회원가입 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["invalidEmailSignup"]
            
            # 회원가입 페이지 접속 및 회원가입 시도
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 유효하지 않은 이메일 형식으로 회원가입 시도
            signupPage.signup(testData["userName"], testData["email"], testData["password"])
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            assert "email is invalid" in errorMessages, f"잘못된 이메일 형식 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = signupPage.get_current_url()
            assert "/register" in currentUrl, f"페이지 URL이 변경되었습니다. 현재 URL: {currentUrl}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 잘못된 이메일 형식 테스트 완료")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"잘못된 이메일 형식 테스트 실패: {str(e)}")

    @pytest.mark.data_not_required
    def testDuplicateEmailSignup(self, driver):
        # AUTH-AUTO-006: 이미 존재하는 이메일로 회원가입 시도 시 에러 메시지 표시 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["duplicateEmailSignup"]
            
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 회원가입 정보 입력
            signupPage.enterUsername(testData["username"])
            signupPage.enterEmail(testData["email"])
            signupPage.enterPassword(testData["password"])
            
            # 회원가입 버튼 클릭
            signupPage.clickSignUp()
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            
            # 검증
            assert "email has already been taken" in errorMessages, f"이메일 중복 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = signupPage.get_current_url()
            assert "/register" in currentUrl, f"페이지 URL이 변경되었습니다. 현재 URL: {currentUrl}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 이메일 중복 회원가입 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"이메일 중복 회원가입 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def testDuplicateUsernameSignup(self, driver):
        # AUTH-AUTO-007: 이미 존재하는 사용자명으로 회원가입 시도 시 에러 메시지 표시 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["existingUsernameSignup"]
            
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 회원가입 정보 입력
            signupPage.enterUsername(testData["username"])
            signupPage.enterEmail(testData["email"])
            signupPage.enterPassword(testData["password"])
            
            # 회원가입 버튼 클릭
            signupPage.clickSignUp()
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            
            # 검증
            assert "username has already been taken" in errorMessages, f"사용자명 중복 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = signupPage.get_current_url()
            assert "/register" in currentUrl, f"페이지 URL이 변경되었습니다. 현재 URL: {currentUrl}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 사용자명 중복 회원가입 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"사용자명 중복 회원가입 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def testShortPasswordSignup(self, driver):
        # AUTH-AUTO-008: 짧은 비밀번호로 회원가입 시도 시 에러 메시지 표시 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["shortPwSignup"]
            
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 회원가입 정보 입력
            signupPage.enterUsername(testData["username"])
            signupPage.enterEmail(testData["email"])
            signupPage.enterPassword(testData["password"])
            
            # 회원가입 버튼 클릭
            signupPage.clickSignUp()
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            
            # 검증 - 비밀번호 길이 관련 에러 메시지 확인
            assert "password is too short" in errorMessages or "minimum is 6 characters" in errorMessages, f"비밀번호 길이 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = signupPage.get_current_url()
            assert "/register" in currentUrl, f"페이지 URL이 변경되었습니다. 현재 URL: {currentUrl}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 짧은 비밀번호 회원가입 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"짧은 비밀번호 회원가입 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def testXssInUsernameSignup(self, driver):
        # AUTH-AUTO-009: XSS 공격 문자열을 사용자명으로 회원가입 시 보안 처리 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["xssSignup"]
            
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 회원가입 정보 입력
            signupPage.enterUsername(testData["username"])
            signupPage.enterEmail(testData["email"])
            signupPage.enterPassword(testData["password"])
            
            # 회원가입 버튼 클릭
            signupPage.clickSignUp()
            
            # 회원가입 성공 확인
            isSignupSuccessful = signupPage.isSignupSuccessful()
            assert isSignupSuccessful, "XSS 테스트용 회원가입이 실패했습니다."
            
            # 홈페이지로 리디렉션 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지로 리디렉션되지 않았습니다."
            
            # 네비게이션 바에서 사용자명 확인
            navUsername = homePage.getNavigateUserName()
            
            # XSS 스크립트가 실행되지 않고 텍스트로 표시되는지 확인
            assert "<script>" in navUsername or "&lt;script&gt;" in navUsername, f"XSS 스크립트가 이스케이프되지 않았습니다. 표시된 사용자명: {navUsername}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} XSS 사용자명 회원가입 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"XSS 사용자명 회원가입 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def testDoubleClickSignupPrevention(self, driver):
        # AUTH-AUTO-010: 회원가입 버튼 더블 클릭 시 중복 가입 방지 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["doubleClickSignin"]
            
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 회원가입 정보 입력
            signupPage.enterUsername(testData["username"])
            signupPage.enterEmail(testData["email"])
            signupPage.enterPassword(testData["password"])
            
            # 회원가입 버튼 더블 클릭
            signupButton = driver.find_element(*SignupLoc.SIGNUP_SUBMIT_BUTTON)
            actions = ActionChains(driver)
            actions.double_click(signupButton).perform()
            
            # 회원가입 성공 확인
            isSignupSuccessful = signupPage.isSignupSuccessful()
            assert isSignupSuccessful, "더블 클릭 테스트용 회원가입이 실패했습니다."
            
            # 홈페이지로 리디렉션 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지로 리디렉션되지 않았습니다."

            # 로그인 성공 확인
            loginPage = LoginPage(driver)
            assert loginPage.isLoggedIn(), "더블 클릭으로 생성된 계정으로 로그인할 수 없습니다. 계정이 생성되지 않았거나 중복 생성되었을 수 있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 회원가입 버튼 더블 클릭 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"회원가입 버튼 더블 클릭 테스트 실패: {str(e)}")
            raise

    @pytest.mark.data_required
    def testSuccessfulLogin(self, driver):
    # AUTH-AUTO-011: 올바른 자격 증명으로 로그인 성공 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            email = testData["email"]
            password = testData["password"]
            expected_username = testData["username"]
            
            # 로그인 페이지 접속 및 로그인 진행
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(email, password)
            
            # 홈페이지로 리디렉션 확인
            homePage = HomePage(driver)
            
            # 1. URL 확인
            assert homePage.wait_for_url_contains("/"), "홈페이지로 리디렉션되지 않았습니다."
            
            # 2. 네비게이션 바에 사용자명 표시 확인
            displayedUsername = homePage.getNavigateUserName()
            assert displayedUsername == expected_username, f"네비게이션 바에 표시된 사용자명이 일치하지 않습니다. 예상: {expected_username}, 실제: {displayedUsername}"
            
            # 3. localStorage에 jwt 토큰 존재 확인
            jwtToken = driver.execute_script("return localStorage.getItem('jwt');")
            assert jwtToken is not None and jwtToken != "", "JWT 토큰이 localStorage에 저장되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 로그인 성공 테스트 완료")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def testLoginWithInvalidPassword(self, driver):
        # AUTH-AUTO-012: 잘못된 비밀번호로 로그인 실패 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["wrongPwLogin"]
            email = testData["email"]
            wrongPassword = testData["password"]
            
            # 로그인 전 localStorage 상태 확인 (이전 토큰 있으면 제거)
            driver.execute_script("localStorage.removeItem('jwt');")
            
            # 로그인 페이지 접속
            loginPage = LoginPage(driver)
            loginPage.navigate()
            
            # 현재 URL 저장
            initialUrl = loginPage.get_current_url()
            
            # 잘못된 비밀번호로 로그인 시도
            loginPage.enterEmail(email)
            loginPage.enterPassword(wrongPassword)
            loginPage.clickSignIn()
            
            # 에러 메시지 확인
            errorMessages = loginPage.getErrorMessages()
            assert any("email or password is invalid" in msg.lower() for msg in errorMessages), f"예상된 에러 메시지가 표시되지 않았습니다. 표시된 메시지: {errorMessages}"
            
            # URL 변경 없음 확인
            currentUrl = loginPage.get_current_url()
            assert currentUrl == initialUrl, f"로그인 실패 후 URL이 변경되었습니다. 초기: {initialUrl}, 현재: {currentUrl}"
            
            # localStorage에 토큰이 저장되지 않음 확인
            jwtToken = driver.execute_script("return localStorage.getItem('jwt');")
            assert jwtToken is None or jwtToken == "", "잘못된 로그인 시도 후 JWT 토큰이 localStorage에 저장되었습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 잘못된 비밀번호 로그인 테스트 완료")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def testLoginStateAfterRefresh(self, driver):
        # AUTH-AUTO-013: 페이지 새로고침 후 로그인 상태 유지 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            email = testData["email"]
            password = testData["password"]
            expected_username = testData["username"]
            
            # 로그인 페이지 접속 및 로그인 진행
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(email, password)
            
            # 홈페이지 로드 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지가 로드되지 않았습니다."
            
            # 로그인 전 사용자명 확인
            beforeRefreshUsername = homePage.getNavigateUserName()
            
            # 로그인 전 JWT 토큰 확인
            beforeRefreshToken = driver.execute_script("return localStorage.getItem('jwt');")
            
            # 페이지 새로고침
            driver.refresh()
            
            # 새로고침 후 페이지 로드 대기
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "새로고침 후 홈페이지가 로드되지 않았습니다."
            
            # 새로고침 후 사용자명 확인
            after_refresh_username = homePage.getNavigateUserName()
            assert after_refresh_username == beforeRefreshUsername, f"새로고침 후 사용자명이 변경되었습니다. 이전: {beforeRefreshUsername}, 이후: {after_refresh_username}"
            
            # 새로고침 후 JWT 토큰 확인
            afterFefreshToken = driver.execute_script("return localStorage.getItem('jwt');")
            assert afterFefreshToken == beforeRefreshToken, "새로고침 후 JWT 토큰이 변경되었습니다."
            assert afterFefreshToken is not None and afterFefreshToken != "", "새로고침 후 JWT 토큰이 사라졌습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 새로고침 후 로그인 상태 유지 테스트 완료")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def testLoginStateAfterNavigation(self, driver):
        # AUTH-AUTO-014: 페이지 이동 후 로그인 상태 유지 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            email = testData["email"]
            password = testData["password"]
            expected_username = testData["username"]
            
            # 로그인 페이지 접속 및 로그인 진행
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(email, password)
            
            # 홈페이지 로드 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지가 로드되지 않았습니다."
            
            # 초기 사용자명 확인
            initialUsername = homePage.getNavigateUserName()
            
            # 초기 JWT 토큰 확인
            initialToken = driver.execute_script("return localStorage.getItem('jwt');")
            
            # Settings 페이지로 이동
            driver.find_element(By.XPATH, "//a[contains(text(), 'Settings')]").click()
            
            # Settings 페이지 로드 확인
            settingsPage = SettingsPage(driver)
            assert settingsPage.isSettingsPageLoaded(), "Settings 페이지가 로드되지 않았습니다."
            
            # Settings 페이지에서 사용자명 확인
            settingsUsername = driver.find_element(By.XPATH, "//a[contains(@class, 'nav-link') and contains(text(), '" + expected_username + "')]").text
            assert settingsUsername == initialUsername, f"Settings 페이지에서 사용자명이 변경되었습니다. 이전: {initialUsername}, 이후: {settingsUsername}"
            
            # Settings 페이지에서 JWT 토큰 확인
            settingsToken = driver.execute_script("return localStorage.getItem('jwt');")
            assert settingsToken == initialToken, "Settings 페이지에서 JWT 토큰이 변경되었습니다."
            
            # Home 페이지로 복귀
            driver.find_element(By.XPATH, "//a[contains(text(), 'Home')]").click()
            
            # 홈페이지 로드 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "Home 페이지로 복귀 후 페이지가 로드되지 않았습니다."
            
            # Home 페이지 복귀 후 사용자명 확인
            finalUsername = homePage.getNavigateUserName()
            assert finalUsername == initialUsername, f"Home 페이지 복귀 후 사용자명이 변경되었습니다. 이전: {initialUsername}, 이후: {finalUsername}"
            
            # Home 페이지 복귀 후 JWT 토큰 확인
            finalToken = driver.execute_script("return localStorage.getItem('jwt');")
            assert finalToken == initialToken, "Home 페이지 복귀 후 JWT 토큰이 변경되었습니다."
            assert finalToken is not None and finalToken != "", "Home 페이지 복귀 후 JWT 토큰이 사라졌습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 페이지 이동 후 로그인 상태 유지 테스트 완료")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def testRedirectToLoginWhenAccessingEditorPage(self, driver):
        # AUTH-AUTO-015: 로그아웃 상태에서 에디터 페이지 접근 시 로그인 페이지로 리디렉션 테스트
        try:
            # localStorage에서 토큰 제거 (로그아웃 상태 확보)
            driver.get(config.BASE_URL)
            driver.execute_script("localStorage.removeItem('jwt');")
            
            # 보호된 페이지(editor)로 직접 이동 시도
            driver.get(f"{config.BASE_URL}/editor")
            
            # 로그인 페이지로 리디렉션 확인
            loginPage = LoginPage(driver)
            
            # URL에 /login이 포함되어 있는지 확인
            currentUrl = loginPage.get_current_url()
            assert "/login" in currentUrl, f"보호된 페이지 접근 시 로그인 페이지로 리디렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
            # 에디터 페이지 요소가 표시되지 않는지 확인
            editor_elements_present = loginPage.is_element_present(*EditorLoc.EDITOR_PUBLISH_BUTTON)
            assert not editor_elements_present, "로그인 페이지로 리디렉션되었지만 에디터 페이지 요소가 여전히 표시됩니다."

            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 보호된 페이지 접근 시 리디렉션 테스트 완료")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise

    @pytest.mark.data_not_required
    def testUnauthorizedSettingsAccess(self, driver):
        # AUTH-AUTO-016: 로그아웃 상태에서 설정 페이지 접근 시 로그인 페이지로 리디렉션 테스트
        try:
            # 로그아웃 상태 확인 (localStorage 토큰 제거)
            driver.execute_script("localStorage.removeItem('jwt');")
            
            # 설정 페이지로 직접 이동 시도
            settingsPage = SettingsPage(driver)
            driver.get(f"{driver.current_url.split('#')[0]}#/settings")
            
            # 로그인 페이지로 리디렉션 확인
            loginPage = LoginPage(driver)
            loginPage.wait_for_url_contains("login")
            
            # 현재 URL이 로그인 페이지인지 확인
            currentUrl = loginPage.get_current_url()
            assert "login" in currentUrl, f"로그인 페이지로 리디렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
            # 설정 페이지 내용이 표시되지 않는지 확인
            assert not settingsPage.is_element_present(ProfileLoc.PROFILE_EDIT_SETTINGS_BTN), "설정 페이지 내용이 표시되고 있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def testLogoutFunctionality(self, driver):
        # AUTH-AUTO-017: 로그아웃 기능 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            
            # 로그인 상태 설정
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 로그인 성공 확인
            homePage = HomePage(driver)
            assert homePage.is_element_visible(HomeLoc.USER_MENU), "로그인 상태가 아닙니다."
            
            # 로그아웃 버튼 클릭
            logoutButton = driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
            logoutButton.click()
            
            # 홈페이지로 리디렉션 확인
            homePage.wait_for_url_contains("")
            currentUrl = homePage.get_current_url()
            assert currentUrl.endswith('/') or currentUrl.endswith('#/'), f"홈페이지로 리디렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
            # 네비게이션 바에 "Sign in", "Sign up" 링크 표시 확인
            assert homePage.is_element_visible(HomeLoc.SIGNIN_LINK), "Sign in 링크가 표시되지 않습니다."
            assert homePage.is_element_visible(HomeLoc.SIGNUP_LINK), "Sign up 링크가 표시되지 않습니다."
            
            # 사용자명 관련 링크 숨김 확인
            assert not homePage.is_element_present(HomeLoc.USER_MENU), "사용자 메뉴가 여전히 표시되고 있습니다."
            
            # localStorage에서 jwt 토큰이 삭제되었는지 확인
            jwtToken = driver.execute_script("return localStorage.getItem('jwt');")
            assert jwtToken is None or jwtToken == "null" or jwtToken == "", "JWT 토큰이 삭제되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def tesBrowserBackAfterLogout(self, driver):
        # AUTH-AUTO-018: 로그아웃 후 브라우저 뒤로가기 시 로그인 페이지로 리디렉션 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            
            # 로그인 상태 설정
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 설정 페이지로 이동
            settingsPage = SettingsPage(driver)
            driver.get(f"{driver.current_url.split('#')[0]}#/settings")
            
            # 설정 페이지 로드 확인
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            """
            # 로그아웃 (네비게이션 바의 로그아웃 버튼 클릭)
            logoutButton = driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]")
            logoutButton.click()
            """

            # 홈페이지로 리디렉션 확인
            homePage = HomePage(driver)
            homePage.wait_for_url_contains("")
            
            # 브라우저 뒤로가기 (또는 설정 페이지로 직접 이동)
            driver.get(f"{driver.current_url.split('#')[0]}#/settings")
            
            # 로그인 페이지로 리디렉션 확인
            loginPage.wait_for_url_contains("login")
            currentUrl = loginPage.get_current_url()
            assert "login" in currentUrl, f"로그인 페이지로 리디렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
            # 설정 페이지 내용이 표시되지 않는지 확인
            assert not settingsPage.is_element_present(SettingsLoc.UPDATE_BUTTON), "설정 페이지 내용이 표시되고 있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    # @pytest.mark.data_required
    # def testExpiredTokenRedirection(self, driver):
    #     # AUTH-AUTO-019: 만료된 JWT 토큰으로 인증 필요 페이지 접근 시 로그인 페이지로 리디렉션 테스트
    #     try:
    #         # 테스트 데이터 로드
    #         testData = loadTestData()["successlLogin"]
            
    #         # 로그인 상태 설정
    #         loginPage = LoginPage(driver)
    #         loginPage.navigate()
    #         loginPage.login(testData["email"], testData["password"])
            
    #         # 로그인 성공 확인
    #         homePage = HomePage(driver)
    #         assert homePage.is_element_visible(HomeLoc.USER_MENU), "로그인 상태가 아닙니다."
            
    #         # JWT 토큰 만료 시뮬레이션 (잘못된/만료된 토큰으로 교체)
    #         driver.execute_script("localStorage.setItem('jwt', 'expired_or_invalid_token');")
            
    #         # 인증이 필요한 페이지(설정 페이지)로 이동 시도
    #         driver.get(f"{driver.current_url.split('#')[0]}#/settings")
            
    #         # 로그인 페이지로 리디렉션 확인
    #         loginPage.wait_for_url_contains("login")
    #         currentUrl = loginPage.get_current_url()
    #         assert "login" in currentUrl, f"로그인 페이지로 리디렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
    #         # localStorage에서 토큰 상태 확인 (제거되었거나 변경되었는지)
    #         jwtToken = driver.execute_script("return localStorage.getItem('jwt');")
    #         # 토큰이 제거되었거나 변경되었는지 확인 (구현에 따라 다를 수 있음)
    #         assert jwtToken is None or jwtToken != "expired_or_invalid_token", "만료된 토큰이 적절히 처리되지 않았습니다."
            
    #         logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
    #     except Exception as e:
    #         logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
    #         raise
    
    @pytest.mark.data_not_required
    def testSignupPagePlaceholders(self, driver):
        # AUTH-AUTO-020: 회원가입 페이지 placeholder 텍스트 확인 테스트
        try:
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 사용자명 입력 필드의 placeholder 텍스트 확인
            usernamePlaceholder = driver.find_element(*SignupLoc.SIGNUP_USERNAME_INPUT).get_attribute("placeholder")
            assert usernamePlaceholder == "Username", f"사용자명 필드의 placeholder가 예상과 다릅니다. 실제: {usernamePlaceholder}, 예상: Username"
            
            # 이메일 입력 필드의 placeholder 텍스트 확인
            emailPlaceholder = driver.find_element(*SignupLoc.SIGNUP_EMAIL_INPUT).get_attribute("placeholder")
            assert emailPlaceholder == "Email", f"이메일 필드의 placeholder가 예상과 다릅니다. 실제: {emailPlaceholder}, 예상: Email"
            
            # 비밀번호 입력 필드의 placeholder 텍스트 확인
            passwordPlaceholder = driver.find_element(*SignupLoc.SIGNUP_PASSWORD_INPUT).get_attribute("placeholder")
            assert passwordPlaceholder == "Password", f"비밀번호 필드의 placeholder가 예상과 다릅니다. 실제: {passwordPlaceholder}, 예상: Password"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise

    @pytest.mark.data_not_required
    def testSignupPageLabels(self, driver):
        # AUTH-AUTO-021:회원가입 페이지의 라벨 텍스트 확인 테스트
        try:
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 사용자명 필드 라벨 확인
            if signupPage.is_element_present(SignupLoc.SIGNUP_USERNAME_INPUT):
                usernameLabel = driver.find_element(*SignupLoc.SIGNUP_USERNAME_INPUT).text
                logger.info(f"사용자명 필드 라벨: {usernameLabel}")
                assert usernameLabel, "사용자명 필드 라벨이 비어있습니다."
            else:
                logger.info("사용자명 필드 라벨 요소가 존재하지 않습니다.")
            
            # 이메일 필드 라벨 확인
            if signupPage.is_element_present(SignupLoc.SIGNUP_EMAIL_INPUT):
                emailLabel = driver.find_element(*SignupLoc.SIGNUP_EMAIL_INPUT).text
                logger.info(f"이메일 필드 라벨: {emailLabel}")
                assert emailLabel, "이메일 필드 라벨이 비어있습니다."
            else:
                logger.info("이메일 필드 라벨 요소가 존재하지 않습니다.")
            
            # 비밀번호 필드 라벨 확인
            if signupPage.is_element_present(SignupLoc.SIGNUP_PASSWORD_INPUT):
                passwordLabel = driver.find_element(*SignupLoc.SIGNUP_PASSWORD_INPUT).text
                logger.info(f"비밀번호 필드 라벨: {passwordLabel}")
                assert passwordLabel, "비밀번호 필드 라벨이 비어있습니다."
            else:
                logger.info("비밀번호 필드 라벨 요소가 존재하지 않습니다.")
                
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 회원가입 페이지 라벨 확인 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"회원가입 페이지 라벨 확인 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def testSignupUsernameTooLong(self, driver):
        # AUTH-AUTO-022: 회원가입 시 사용자명 최대 길이 초과 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["longUsernameSignup"]
            
            # 회원가입 페이지 접속
            signupPage = SignupPage(driver)
            signupPage.navigate()
            
            # 현재 URL 저장
            currentUrl = signupPage.get_current_url()
            
            # 사용자명 필드에 최대 길이 초과 문자열 입력
            signupPage.enterUsername(testData["userName"])
            
            # 유효한 이메일, 비밀번호 입력
            signupPage.enterEmail(testData["email"])
            signupPage.enterPassword(testData["password"])
            
            # 'Sign up' 버튼 클릭
            signupPage.clickSignUp()
            
            # 에러 메시지 확인
            errorMessages = signupPage.getErrorMessages()
            
            # 에러 메시지에 "username is too long" 포함 여부 확인
            usernameTooLong_error = False
            for error in errorMessages:
                if "username is too long" in error.lower() or "maximum" in error.lower():
                    usernameTooLong_error = True
                    logger.info(f"에러 메시지 확인: {error}")
                    break
            
            assert usernameTooLong_error, "사용자명 최대 길이 초과 에러 메시지가 표시되지 않았습니다."
            
            # URL 변경 없음 확인
            assert signupPage.get_current_url() == currentUrl, "페이지 URL이 변경되었습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 사용자명 최대 길이 초과 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"사용자명 최대 길이 초과 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def testLoginPagePlaceholders(self, driver):
        # AUTH-AUTO-023: 로그인 페이지의 placeholder 텍스트 확인 테스트
        try:
            # 로그인 페이지 접속
            loginPage = LoginPage(driver)
            loginPage.navigate()
            
            # 이메일 필드 placeholder 확인
            emailPlaceholder = driver.find_element(*LoginLoc.LOGIN_EMAIL_INPUT).get_attribute("placeholder")
            logger.info(f"이메일 필드 placeholder: {emailPlaceholder}")
            assert emailPlaceholder, "이메일 필드 placeholder가 비어있습니다."
            
            # 비밀번호 필드 placeholder 확인
            passwordPlaceholder = driver.find_element(*LoginLoc.LOGIN_PASSWORD_INPUT).get_attribute("placeholder")
            logger.info(f"비밀번호 필드 placeholder: {passwordPlaceholder}")
            assert passwordPlaceholder, "비밀번호 필드 placeholder가 비어있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 로그인 페이지 placeholder 확인 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"로그인 페이지 placeholder 확인 테스트 실패: {str(e)}")
    
    @pytest.mark.data_required
    def testSettingsPagePlaceholders(self, driver):
        # AUTH-AUTO-024: 설정 페이지의 placeholder 및 label 텍스트 확인 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            
            # 로그인 후 설정 페이지 접속
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 설정 페이지로 이동
            settingsPage = SettingsPage(driver)
            driver.get(f"{driver.current_url.split('#')[0]}#/settings")
            
            # 페이지 로드 확인
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # Bio 필드 placeholder 확인
            bioPlaceholder = driver.find_element(*SettingsLoc.SETTINGS_BIO_TEXTAREA).get_attribute("placeholder")
            logger.info(f"Bio 필드 placeholder: {bioPlaceholder}")
            assert bioPlaceholder, "Bio 필드 placeholder가 비어있습니다."
            
            # Image URL 필드 placeholder 확인
            imageUrlPlaceholder = driver.find_element(*SettingsLoc.SETTINGS_PROFILE_PICTURE_INPUT).get_attribute("placeholder")
            logger.info(f"Image URL 필드 placeholder: {imageUrlPlaceholder}")
            assert imageUrlPlaceholder, "Image URL 필드 placeholder가 비어있습니다."
            
            # Username 필드 placeholder 확인
            usernamePlaceholder = driver.find_element(*SettingsLoc.SETTINGS_USERNAME_INPUT).get_attribute("placeholder")
            logger.info(f"Username 필드 placeholder: {usernamePlaceholder}")
            assert usernamePlaceholder, "Username 필드 placeholder가 비어있습니다."
            
            # Email 필드 placeholder 확인
            emailPlaceholder = driver.find_element(*SettingsLoc.SETTINGS_EMAIL_INPUT).get_attribute("placeholder")
            logger.info(f"Email 필드 placeholder: {emailPlaceholder}")
            assert emailPlaceholder, "Email 필드 placeholder가 비어있습니다."
            
            # Password 필드 placeholder 확인
            passwordPlaceholder = driver.find_element(*SettingsLoc.PASSWORD_INPUT).get_attribute("placeholder")
            logger.info(f"Password 필드 placeholder: {passwordPlaceholder}")
            assert passwordPlaceholder, "Password 필드 placeholder가 비어있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 설정 페이지 placeholder 확인 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"설정 페이지 placeholder 확인 테스트 실패: {str(e)}")
    
    @pytest.mark.data_required
    def testSettingsBioTooLong(self, driver):
        # AUTH-AUTO-025: 설정 페이지에서 Bio 최대 길이 초과 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["bioLongText"]
            login_data = loadTestData()["successlLogin"]
            
            # 로그인 후 설정 페이지 접속
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(login_data["email"], login_data["password"])
            
            # 설정 페이지로 이동
            settingsPage = SettingsPage(driver)
            driver.get(f"{driver.current_url.split('#')[0]}#/settings")
            
            # 페이지 로드 확인
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 기존 Bio 값 저장
            originalBio = driver.find_element(*SettingsLoc.SETTINGS_BIO_TEXTAREA).get_attribute("value")
            
            # Bio 필드 초기화
            settingsPage.clearField(SettingsLoc.SETTINGS_BIO_TEXTAREA)
            
            # Bio 필드에 최대 길이 초과 문자열 입력
            settingsPage.enterBio(testData["long_bio"])
            
            # 'Update Settings' 버튼 클릭
            settingsPage.clickUpdateButton()
            
            # 에러 메시지 확인
            if settingsPage.is_element_present(SettingsLoc.SETTINGS_BIO_TEXTAREA):
                errorMessages = driver.find_elements(*SettingsLoc.SETTINGS_BIO_TEXTAREA)
                errorTexts = [error.text for error in errorMessages]
                
                # 에러 메시지에 "bio is too long" 포함 여부 확인
                bioTooLongError = False
                for error in errorTexts:
                    if "bio is too long" in error.lower() or "maximum" in error.lower():
                        bioTooLongError = True
                        logger.info(f"에러 메시지 확인: {error}")
                        break
                
                assert bioTooLongError, "Bio 최대 길이 초과 에러 메시지가 표시되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} Bio 최대 길이 초과 테스트 성공")
        except Exception as e:
            logger.error(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            pytest.fail(f"Bio 최대 길이 초과 테스트 실패: {str(e)}")



    @pytest.mark.data_required
    def testMultiSessionLoginSync(self, driver):
        # AUTH-AUTO-026: 동일 브라우저의 다른 탭에서 로그인 상태 동기화 확인
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            
            # 로그인 페이지 객체 생성 및 로그인
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 로그인 성공 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지가 로드되지 않았습니다."
            
            # 현재 창의 핸들 저장
            originalWindow = driver.current_window_handle
            
            # 새 탭 열기
            driver.execute_script("window.open('about:blank', '_blank');")
            
            # 새 탭으로 전환
            newWindow = [window for window in driver.window_handles if window != originalWindow][0]
            driver.switch_to.window(newWindow)
            
            # 새 탭에서 홈페이지 접속
            driver.get(loginPage.url)
            
            # 새 탭에서 네비게이션 바의 사용자명 확인
            homePage = HomePage(driver)
            username = homePage.getNavigateUserName()
            
            # 사용자명이 올바르게 표시되는지 확인
            assert username == testData["username"], f"새 탭에서 사용자명이 올바르게 표시되지 않습니다. 예상: {testData['username']}, 실제: {username}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"멀티 세션 로그인 동기화 테스트 실패: {str(e)}")
            raise

    @pytest.mark.data_required
    def testMultiSessionLogoutSync(self, driver):
        # AUTH-AUTO-027: 동일 브라우저의 다른 탭에서 로그아웃 상태 동기화 확인
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            
            # 로그인 페이지 객체 생성 및 로그인
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 로그인 성공 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지가 로드되지 않았습니다."
            
            # 현재 창의 핸들 저장
            originalWindow = driver.current_window_handle
            
            # 새 탭 열기
            driver.execute_script("window.open('about:blank', '_blank');")
            
            # 새 탭으로 전환
            newWindow = [window for window in driver.window_handles if window != originalWindow][0]
            driver.switch_to.window(newWindow)
            
            # 새 탭에서 홈페이지 접속
            driver.get(loginPage.url)
            
            # 새 탭에서 로그인 상태 확인
            homePageTabB = HomePage(driver)
            assert homePageTabB.getNavigateUserName() == testData["username"], "새 탭에서 로그인 상태가 아닙니다."
            
            # 원래 탭으로 돌아가기
            driver.switch_to.window(originalWindow)
            
            # 로그아웃 버튼 클릭
            logoutButton = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(HomeLoc.LOGOUTBUTTON)
            )
            logoutButton.click()
            
            # 새 탭으로 다시 전환
            driver.switch_to.window(newWindow)
            
            # 잠시 대기 (localStorage 변경 감지 시간 고려)
            time.sleep(2)
            
            # 로그아웃 상태 확인 (Sign in, Sign up 링크 표시 여부)
            signinLink = driver.find_elements(*HomeLoc.SIGN_IN_LINK)
            signupLink = driver.find_elements(*HomeLoc.SIGN_UP_LINK)
            
            assert len(signinLink) > 0, "Sign in 링크가 표시되지 않습니다."
            assert len(signupLink) > 0, "Sign up 링크가 표시되지 않습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"멀티 세션 로그아웃 동기화 테스트 실패: {str(e)}")
            raise

    @pytest.mark.data_not_required
    def test_form_submission_loading_state(self, driver):
        # AUTH-AUTO-029: 폼 제출 시 로딩 상태 표시 확인
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["successlLogin"]
            
            # 로그인 페이지 접속
            loginPage = LoginPage(driver)
            loginPage.navigate()
            
            # 이메일과 비밀번호 입력
            loginPage.enterEmail(testData["email"])
            loginPage.enterPassword(testData["password"])
            
            # 버튼 요소 가져오기
            sign_in_button = driver.find_element(*LoginLoc.LOGIN_SIGN_IN_LINK)
            
            # 버튼 클릭 전 상태 확인
            is_disabled_before = sign_in_button.get_attribute("disabled")
            
            # 버튼 클릭
            sign_in_button.click()
            
            # 버튼 클릭 직후 상태 확인 (비활성화 또는 로딩 인디케이터)
            try:
                # 버튼 비활성화 확인
                WebDriverWait(driver, 3).until(
                    lambda d: d.find_element(*LoginLoc.SIGNIN_BUTTON).get_attribute("disabled") == "true"
                )
                buttonDisabled = True
            except:
                buttonDisabled = False
            
            # 버튼 비활성화 또는 로딩 인디케이터 중 하나는 반드시 있어야 함
            assert buttonDisabled, "폼 제출 시 버튼 비활성화 또는 로딩 인디케이터가 표시되지 않습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"폼 제출 로딩 상태 테스트 실패: {str(e)}")
            raise
