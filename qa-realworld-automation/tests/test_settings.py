
    @pytest.mark.data_required
    def test_access_settings_page(self, driver):
        """
        테스트 시나리오: 설정 페이지 접근
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 홈페이지에 접속.
        
        재현 절차:
        1. 네비게이션바에서 'settings'를 클릭한다.
        
        기대 결과:
        설정 페이지 (/settings)에 성공적으로 접근한다.
        """
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["settings_access"]
            
            # 로그인 및 홈페이지 접속 (사전 조건)
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 홈페이지 접속 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지가 제대로 로드되지 않았습니다."
            
            # 1. 네비게이션바에서 'settings' 클릭
            driver.find_element(*HomeLoc.SETTINGS_LINK).click()
            
            # 설정 페이지 접근 확인
            settingsPage = SettingsPage(driver)
            assert settings_page.wait_for_url_contains("/settings"), "설정 페이지로 이동하지 않았습니다."
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 제대로 로드되지 않았습니다."
            
            # 설정 페이지 요소 확인
            assert settingsPage.is_element_visible(SettingsLoc.UPDATE_BUTTON), "설정 페이지의 업데이트 버튼이 표시되지 않습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"설정 페이지 접근 테스트 실패: {str(e)}")
            raise
```

이 코드는 JSON 형식의 테스트케이스에 맞춰 5개의 테스트 함수를 구현했습니다:

1. `test_edit_article_button_click` - 게시글 수정 페이지 이동 및 기존 내용 확인
2. `test_edit_article_content` - 게시글 내용 수정 및 반영 확인
3. `test_edit_article_empty_content` - 게시글 내용 전체 삭제 후 발행 시도
4. `test_delete_article` - 게시글 삭제
5. `test_access_settings_page` - 설정 페이지 접근

각 테스트는 POM 구조를 따르며, 독립적으로 실행됩니다. 모든 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다. 또한 각 테스트는 `@pytest.mark.data_required` 데코레이터를 사용하여 데이터 세팅이 필요함을 표시했습니다.

테스트 데이터는 `loadTestData()` 함수를 통해 JSON 파일에서 로드하며, 각 테스트는 고유한 데이터를 사용합니다. 오류 처리는 try-except 구문을 사용하여 구현했고, 테스트 실패 시 로그를 남기도록 했습니다.

# ===== 다음 배치 =====

요청하신 대로 JSON 형식의 테스트케이스에 맞춰 Python + Selenium 기반의 Pytest 테스트 코드를 작성하겠습니다. 각 테스트는 POM 구조를 따르며 독립적으로 실행될 수 있도록 구성했습니다.

```python
import os
import json
import pytest
import inspect
from selenium.webdriver.common.by import By

from pages.settings_page import SettingsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.logger import setup_logger
import config
from locators.settings_locators import SettingsPageLocators as Loc

def loadTestData():
    """테스트 데이터 파일을 로드하는 함수"""
    dataFilePath = os.path.join(config.TEST_DATA_DIR, "test_data.json")
    with open(dataFilePath, 'r', encoding='utf-8') as file:
        return json.load(file)

logger = setup_logger(__name__)

class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 실행 전 로그인 상태로 설정 페이지에 접근하는 전처리 작업"""
        self.driver = driver
        self.loginPage = LoginPage(driver)
        self.settingsPage = SettingsPage(driver)
        self.homePage = HomePage(driver)
        
        # 테스트 데이터 로드
        self.testData = loadTestData()
        
        # 로그인 처리
        self.loginPage.navigate()
        self.loginPage.login(
            self.testData["login"]["email"], 
            self.testData["login"]["password"]
        )
        
        # 설정 페이지로 이동
        self.driver.get(f"{self.driver.current_url}settings")
        
        yield
    
    @pytest.mark.data_not_required
    def test_settings_page_layout(self):
        """
        설정 페이지의 전체적인 레이아웃을 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지 (/settings)에 접근.
        
        재현 절차:
        1. 설정 페이지의 전체적인 레이아웃을 확인한다.
        
        기대 결과:
        - 페이지 제목 "Your Settings"가 표시된다.
        - 해당 입력 필드가 순서대로 올바르게 배치되어 있다.
          1. 프로필 이미지 URL
          2. 사용자 이름
          3. 상태 소개
          4. 이메일
          5. 새 비밀번호
        - 'Update Settings' 버튼과 'Or click here to logout.' 버튼이 하단에 표시된다.
        """
        try:
            # 페이지 로드 확인
            assert self.settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 페이지 제목 확인
            page_title = self.driver.find_element(By.XPATH, Loc.PAGE_TITLE).text
            assert page_title == "Your Settings", f"페이지 제목이 일치하지 않습니다. 실제: {page_title}"
            
            # 입력 필드 순서 확인
            form_elements = [
                Loc.IMAGE_URL_INPUT,
                Loc.USERNAME_INPUT,
                Loc.BIO_INPUT,
                Loc.EMAIL_INPUT,
                Loc.PASSWORD_INPUT
            ]
            
            # 각 요소가 존재하는지 확인
            for element_locator in form_elements:
                assert self.settingsPage.is_element_present(element_locator), f"요소가 존재하지 않습니다: {element_locator}"
            
            # 버튼 확인
            assert self.settingsPage.is_element_present(Loc.UPDATE_BUTTON), "Update Settings 버튼이 존재하지 않습니다."
            assert self.settingsPage.is_element_present(Loc.LOGOUTBUTTON), "Logout 버튼이 존재하지 않습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 설정 페이지 레이아웃 테스트 성공")
        except Exception as e:
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    @pytest.mark.data_not_required
    def test_settings_page_placeholders(self):
        """
        설정 페이지의 입력 필드 플레이스홀더를 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지 (/settings)에 접근.
        
        재현 절차:
        1. 각 입력 필드의 플레이스홀더 텍스트를 확인한다.
        
        기대 결과:
        - 'URL of profile picture' 필드에 적절한 플레이스홀더가 표시된다.
        - 'Username' 필드에 적절한 플레이스홀더가 표시된다.
        - 'Short bio about you' 텍스트 영역에 적절한 플레이스홀더가 표시된다.
        - 'Email' 필드에 적절한 플레이스홀더가 표시된다.
        - 'New Password' 필드에 적절한 플레이스홀더가 표시된다.
        """
        try:
            # 각 입력 필드의 플레이스홀더 확인
            imageUrlPlaceholder = self.driver.find_element(By.XPATH, Loc.IMAGE_URL_INPUT).get_attribute("placeholder")
            assert "URL of profile picture" in imageUrlPlaceholder, f"이미지 URL 플레이스홀더가 일치하지 않습니다. 실제: {imageUrl_placeholder}"
            
            usernamePlaceholder = self.driver.find_element(By.XPATH, Loc.USERNAME_INPUT).get_attribute("placeholder")
            assert "Username" in usernamePlaceholder, f"사용자 이름 플레이스홀더가 일치하지 않습니다. 실제: {usernamePlaceholder}"
            
            bioPlaceholder = self.driver.find_element(By.XPATH, Loc.BIO_INPUT).get_attribute("placeholder")
            assert "Short bio about you" in bioPlaceholder, f"상태 소개 플레이스홀더가 일치하지 않습니다. 실제: {bioPlaceholder}"
            
            emailPlaceholder = self.driver.find_element(By.XPATH, Loc.EMAIL_INPUT).get_attribute("placeholder")
            assert "Email" in emailPlaceholder, f"이메일 플레이스홀더가 일치하지 않습니다. 실제: {emailPlaceholder}"
            
            passwordPlaceholder = self.driver.find_element(By.XPATH, Loc.PASSWORD_INPUT).get_attribute("placeholder")
            assert "New Password" in passwordPlaceholder, f"비밀번호 플레이스홀더가 일치하지 않습니다. 실제: {passwordPlaceholder}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 설정 페이지 플레이스홀더 테스트 성공")
        except Exception as e:
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    @pytest.mark.data_not_required
    def test_logout_functionality(self):
        """
        로그아웃 기능을 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지 (/settings)에 접근.
        
        재현 절차:
        1. 'Or click here to logout.' 버튼을 클릭한다.
        
        기대 결과:
        - 사용자는 로그아웃 처리되어 홈페이지로 리다이렉션된다.
        """
        try:
            # 로그아웃 버튼 클릭
            self.driver.find_element(By.XPATH, Loc.LOGOUTBUTTON).click()
            
            # 홈페이지로 리다이렉션 확인
            self.driver.wait_for_url_contains("home")
            
            # 로그아웃 상태 확인 (로그인 버튼이 표시되는지)
            assert self.login_page.is_element_visible(By.XPATH, "//a[contains(text(), 'Sign in')]"), "로그아웃 후 로그인 버튼이 표시되지 않습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 로그아웃 기능 테스트 성공")
        except Exception as e:
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    @pytest.mark.data_required
    def test_remove_profileImage(self):
        """
        프로필 이미지 URL 제거 기능을 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - currentUser에게 기존 프로필 이미지 URL이 설정되어 있음.
        
        재현 절차:
        1. 'URL of profile picture' 입력 필드의 기존 이미지 URL을 모두 삭제한다.
        2. 'Update Settings' 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바의 프로필 이미지를 확인한다.
        
        기대 결과:
        - 프로필 이미지가 기본 이미지 아이콘으로 표시된다.
        """
        try:
            # 기존 이미지 URL 삭제
            self.settingsPage.clearField(Loc.IMAGE_URL_INPUT)
            
            # 업데이트 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 홈페이지로 리다이렉션 확인
            self.driver.wait_for_url_contains("home")
            
            # 네비게이션 바의 프로필 이미지 확인
            profile_img = self.driver.find_element(By.XPATH, "//img[@class='user-pic']")
            img_src = profile_img.get_attribute("src")
            
            # 기본 이미지 확인 (기본 이미지는 일반적으로 상대 경로이거나 특정 패턴을 가짐)
            assert not img_src or "default" in img_src.lower() or img_src.startswith("data:"), "프로필 이미지가 기본 이미지로 변경되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 프로필 이미지 제거 테스트 성공")
        except Exception as e:
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    @pytest.mark.data_required
    def test_update_profileImage(self):
        """
        프로필 이미지 URL 업데이트 기능을 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'URL of profile picture' 입력 필드에 새로운 유효한 이미지 URL을 입력한다.
        2. 'Update Settings' 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바의 프로필 이미지를 확인한다.
        
        기대 결과:
        - 프로필 이미지가 새롭게 입력한 URL의 이미지로 성공적으로 변경된다.
        """
        try:
            # 새로운 이미지 URL 입력
            new_image_url = "https://picsum.photos/200"
            self.settingsPage.enterImageUrl(new_image_url)
            
            # 업데이트 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 홈페이지로 리다이렉션 확인
            self.driver.wait_for_url_contains("home")
            
            # 네비게이션 바의 프로필 이미지 확인
            profile_img = self.driver.find_element(By.XPATH, "//img[@class='user-pic']")
            img_src = profile_img.get_attribute("src")
            
            # 새로운 이미지 URL로 변경되었는지 확인
            assert new_image_url in img_src, f"프로필 이미지가 새 URL로 변경되지 않았습니다. 실제: {img_src}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 프로필 이미지 업데이트 테스트 성공")
        except Exception as e:
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
```

이 코드는 JSON 형식의 테스트케이스에 맞춰 5개의 테스트 메소드를 구현했습니다:

1. `test_settings_page_layout()` - 설정 페이지의 전체적인 레이아웃을 확인
2. `test_settings_page_placeholders()` - 각 입력 필드의 플레이스홀더 텍스트를 확인
3. `test_logout_functionality()` - 로그아웃 버튼 기능 확인
4. `test_remove_profileImage()` - 프로필 이미지 URL 제거 기능 확인
5. `test_update_profileImage()` - 프로필 이미지 URL 업데이트 기능 확인

각 테스트는 POM 구조를 따르며, 로케이터는 외부 파일에서 import하여 사용했습니다. 또한 모든 테스트는 독립적으로 실행될 수 있도록 설계되었으며, 각 테스트에 명확한 docstring과 한글 주석을 포함했습니다.

# ===== 다음 배치 =====

요청하신 테스트 케이스에 맞춰 Python + Selenium 기반의 Pytest 테스트 코드를 작성하겠습니다. 주어진 JSON 형식의 테스트 케이스를 기반으로 POM 구조를 따르는 5개의 테스트 함수를 구현하겠습니다.

```python
# qa-realworld-automation/tests/test_pages.py

import os
import json
import pytest
import inspect
import time
from selenium.webdriver.common.by import By

# 공통 코드 및 로케이터 import
from pages.settings_page import SettingsPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.home_locators import HomePageLocators as HomeLoc
from locators.profile_locators import ProfilePageLocators as ProfileLoc
from utils.logger import setup_logger
import config

# 로거 설정
logger = setup_logger(__name__)

def loadTestData():
    """테스트 데이터 파일을 로드하는 함수"""
    dataFilePath = os.path.join(config.TEST_DATA_DIR, "test_data.json")
    with open(dataFilePath, 'r', encoding='utf-8') as file:
        return json.load(file)

class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""
    
    @pytest.mark.data_required
    def test_profile_picture_update(self, driver):
        """
        프로필 이미지 URL 업데이트 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'URL of profile picture' 입력 필드에 새로운 유효한 이미지 URL을 입력한다.
        2. 'Update Settings' 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바의 프로필 이미지를 확인한다.
        
        기대 결과:
        프로필 이미지가 기본 이미지 아이콘으로 표시된다.
        """
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["profilePictureUpdate"]
            
            # 설정 페이지 접근
            settingsPage = SettingsPage(driver)
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 1. 프로필 이미지 URL 입력
            settingsPage.clearField(SettingsLoc.IMAGE_URL_INPUT)
            settingsPage.enterImageUrl(testData["image_url"])
            logger.info("프로필 이미지 URL 입력 완료")
            
            # 2. Update Settings 버튼 클릭
            settingsPage.clickUpdateButton()
            logger.info("Update Settings 버튼 클릭 완료")
            
            # 3. 홈페이지로 리다이렉션 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 4. 네비게이션 바의 프로필 이미지 확인
            # 기본 이미지 아이콘이 표시되는지 확인 (이미지 요소의 존재 여부로 확인)
            assert homePage.is_element_present(HomeLoc.USER_PROFILEIMAGE), "프로필 이미지가 표시되지 않습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def test_empty_username_update(self, driver):
        """
        빈 닉네임으로 업데이트 시도 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - currentUser에게 기존 닉네임이 설정되어 있음.
        
        재현 절차:
        1. 'Username' 입력 필드의 기존 닉네임을 모두 삭제한다.
        2. 'Update Settings' 버튼을 클릭한다.
        
        기대 결과:
        닉네임 필드가 비어있는 상태로 업데이트되지 않아야 한다.
        """
        try:
            # 설정 페이지 접근
            settingsPage = SettingsPage(driver)
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 현재 사용자명 저장
            original_username = settings_page.get_current_url().split("@")[1].split("/")[0]
            logger.info(f"현재 사용자명: {original_username}")
            
            # 1. Username 입력 필드의 기존 닉네임 삭제
            settingsPage.clearField(SettingsLoc.USERNAME_INPUT)
            logger.info("Username 필드 내용 삭제 완료")
            
            # 2. Update Settings 버튼 클릭
            settingsPage.clickUpdateButton()
            logger.info("Update Settings 버튼 클릭 완료")
            
            # 설정 페이지에 머물러 있는지 확인 (에러 메시지 표시 또는 페이지 이동 없음)
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지를 벗어났습니다."
            
            # 홈페이지로 이동하여 사용자명이 변경되지 않았는지 확인
            homePage = HomePage(driver)
            driver.get(driver.current_url.split("/settings")[0])  # 홈페이지로 이동
            
            # 네비게이션 바에서 사용자명 확인
            current_username = homePage.getNavigateUserName()
            assert current_username == original_username, f"사용자명이 변경되었습니다. 예상: {original_username}, 실제: {current_username}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def test_duplicate_username_update(self, driver):
        """
        중복된 닉네임으로 업데이트 시도 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - 시스템에 existingUser라는 닉네임의 다른 사용자가 존재.
        
        재현 절차:
        1. 'Username' 입력 필드에 이미 시스템에 존재하는 다른 사용자의 닉네임 (existingUser)을 입력한다.
        2. 'Update Settings' 버튼을 클릭한다.
        3. 오류 메시지 또는 UI 변화를 확인한다.
        
        기대 결과:
        "Username has already been taken" 또는 유사한 명확한 오류 메시지가 표시되어야 한다.
        """
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["duplicateUsername"]
            
            # 설정 페이지 접근
            settingsPage = SettingsPage(driver)
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 1. 이미 존재하는 사용자명 입력
            settingsPage.clearField(SettingsLoc.USERNAME_INPUT)
            settingsPage.enterUsername(testData["existing_username"])
            logger.info(f"이미 존재하는 사용자명 '{testData['existing_username']}' 입력 완료")
            
            # 2. Update Settings 버튼 클릭
            settingsPage.clickUpdateButton()
            logger.info("Update Settings 버튼 클릭 완료")
            
            # 3. 오류 메시지 확인
            # 에러 메시지 요소가 존재하는지 확인
            assert settingsPage.is_element_visible(SettingsLoc.ERROR_MESSAGE), "오류 메시지가 표시되지 않습니다."
            
            # 오류 메시지 내용 확인
            errorMessage = driver.find_element(*SettingsLoc.ERROR_MESSAGE).text
            assert "username has already been taken" in error_message.lower(), f"예상된 오류 메시지가 표시되지 않습니다. 실제: {error_message}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def test_valid_username_update(self, driver):
        """
        유효한 새 닉네임으로 업데이트 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'Username' 입력 필드에 새롭고, 유효하며, 시스템에 존재하지 않는 닉네임을 입력한다.
        2. 'Update Settings' 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바에서 변경된 닉네임을 확인한다.
        
        기대 결과:
        닉네임이 성공적으로 새 닉네임으로 변경된다.
        """
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["validUsernameUpdate"]
            
            # 설정 페이지 접근
            settingsPage = SettingsPage(driver)
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 1. 새로운 유효한 사용자명 입력
            settingsPage.clearField(SettingsLoc.USERNAME_INPUT)
            settingsPage.enterUsername(testData["new_username"])
            logger.info(f"새로운 사용자명 '{testData['new_username']}' 입력 완료")
            
            # 2. Update Settings 버튼 클릭
            settingsPage.clickUpdateButton()
            logger.info("Update Settings 버튼 클릭 완료")
            
            # 3. 홈페이지로 리다이렉션 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 4. 네비게이션 바에서 변경된 닉네임 확인
            current_username = homePage.getNavigateUserName()
            assert current_username == testData["new_username"], f"사용자명이 변경되지 않았습니다. 예상: {testData['new_username']}, 실제: {current_username}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def test_bio_update(self, driver):
        """
        상태소개(bio) 업데이트 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'Short bio about you' 텍스트 영역에 새로운 유효한 상태소개를 입력한다.
        2. 'Update Settings' 버튼을 클릭한다.
        3. currentUser의 프로필 페이지에서 변경된 상태소개를 확인한다.
        
        기대 결과:
        프로필 페이지에 변경된 상태소개가 올바르게 표시된다.
        """
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["bioUpdate"]
            
            # 설정 페이지 접근
            settingsPage = SettingsPage(driver)
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 1. 새로운 상태소개 입력
            settingsPage.clearField(SettingsLoc.BIO_INPUT)
            settingsPage.enterBio(testData["new_bio"])
            logger.info(f"새로운 상태소개 '{testData['new_bio']}' 입력 완료")
            
            # 2. Update Settings 버튼 클릭
            settingsPage.clickUpdateButton()
            logger.info("Update Settings 버튼 클릭 완료")
            
            # 홈페이지로 리다이렉션 확인
            homePage = HomePage(driver)
            assert homePage.isPageLoaded(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 현재 사용자명 가져오기
            username = homePage.getNavigateUserName()
            
            # 3. 프로필 페이지로 이동하여 변경된 상태소개 확인
            driver.get(f"{driver.current_url.split('#')[0]}/@{username}")
            profile_page = ProfilePage(driver)
            
            # 프로필 페이지에서 상태소개 확인
            user_bio = profile_page.getUserBio()
            assert user_bio == testData["new_bio"], f"상태소개가 변경되지 않았습니다. 예상: {testData['new_bio']}, 실제: {user_bio}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
```

위 코드는 주어진 5개의 테스트 케이스를 POM 구조에 맞게 구현한 것입니다. 각 테스트는:

1. 프로필 이미지 URL 업데이트 테스트
2. 빈 닉네임으로 업데이트 시도 테스트
3. 중복된 닉네임으로 업데이트 시도 테스트
4. 유효한 새 닉네임으로 업데이트 테스트
5. 상태소개(bio) 업데이트 테스트

각 테스트는 독립적으로 실행되며, 테스트 데이터는 `loadTestData()` 함수를 통해 JSON 파일에서 로드합니다. 모든 테스트는 `@pytest.mark.data_required` 데코레이터를 사용하여 데이터 세팅이 필요함을 표시했습니다.

각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있으며, 로케이터는 import해서 사용했습니다. 오류 처리를 위해 try-except 구문을 사용했고, 로깅을 통해 테스트 진행 상황을 기록합니다.

# ===== 다음 배치 =====

요청하신 테스트 케이스에 맞춰 Python + Selenium 기반의 Pytest 테스트 코드를 작성해드리겠습니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하는 테스트를 구현하겠습니다.

```python
# qa-realworld-automation/tests/test_pages.py

import os
import json
import pytest
import inspect
from utils.logger import setup_logger
import config
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.profile_locators import ProfilePageLocators as ProfileLoc

def loadTestData():
    """테스트 데이터 파일을 로드합니다."""
    dataFilePath = os.path.join(config.TEST_DATA_DIR, "test_data.json")
    with open(dataFilePath, 'r', encoding='utf-8') as file:
        return json.load(file)

logger = setup_logger(__name__)

class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 전에 로그인 상태로 설정합니다."""
        self.testData = loadTestData()
        self.loginPage = LoginPage(driver)
        self.settingsPage = SettingsPage(driver)
        self.profile_page = ProfilePage(driver)
        
        # 로그인
        self.loginPage.navigate()
        self.loginPage.login(
            self.testData["login"]["email"], 
            self.testData["login"]["password"]
        )
        
        # 설정 페이지로 이동
        driver.get(f"{driver.current_url}settings")
        
        yield
    
    @pytest.mark.data_required
    def test_remove_bio_from_settings(self, driver):
        """
        테스트 시나리오: 사용자 상태소개(bio) 삭제 후 프로필 페이지에서 확인
        
        사전 조건:
        - 로그인된 사용자가 설정 페이지에 접근
        - 사용자에게 기존 상태소개가 설정되어 있음
        
        재현 절차:
        1. 'Short bio about you' 텍스트 영역의 기존 내용을 모두 삭제
        2. 'Update Settings' 버튼 클릭
        3. 사용자 프로필 페이지에서 상태소개 영역 확인
        
        기대 결과:
        - 프로필 페이지에서 상태소개가 비어있는 것으로 표시되어야 함
        """
        try:
            # 1. 'Short bio about you' 텍스트 영역의 기존 내용을 모두 삭제
            self.settingsPage.clearField(SettingsLoc.BIO_INPUT)
            
            # 2. 'Update Settings' 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 3. 사용자 프로필 페이지로 이동하여 상태소개 영역 확인
            username = self.settings_page.getNavigateUserName()
            driver.get(f"{driver.current_url.split('#')[0]}@{username}")
            
            # 프로필 페이지에서 상태소개 확인
            user_bio = self.profile_page.getUserBio()
            
            # 기대 결과: 프로필 페이지에서 상태소개가 비어있는 것으로 표시되어야 함
            assert user_bio == "" or user_bio is None, f"상태소개가 비어있지 않습니다. 현재 값: {user_bio}"
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공: 상태소개가 성공적으로 삭제되었습니다.")
            
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"상태소개 삭제 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def test_multiline_bio_in_settings(self, driver):
        """
        테스트 시나리오: 여러 줄로 구성된 상태소개(bio) 입력 후 프로필 페이지에서 확인
        
        사전 조건:
        - 로그인된 사용자가 설정 페이지에 접근
        
        재현 절차:
        1. 'Short bio about you' 텍스트 영역에 여러 줄로 구성된 텍스트 입력
        2. 'Update Settings' 버튼 클릭
        3. 사용자 프로필 페이지에서 상태소개 영역 확인
        
        기대 결과:
        - 프로필 페이지에서 입력한 줄바꿈이 적용되어 여러 줄로 표시되어야 함
        """
        try:
            # 테스트 데이터 준비
            multiline_bio = "첫 번째 줄\n두 번째 줄"
            
            # 1. 'Short bio about you' 텍스트 영역에 여러 줄로 구성된 텍스트 입력
            self.settingsPage.clearField(SettingsLoc.BIO_INPUT)
            self.settingsPage.enterBio(multiline_bio)
            
            # 2. 'Update Settings' 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 3. 사용자 프로필 페이지로 이동하여 상태소개 영역 확인
            username = self.settings_page.getNavigateUserName()
            driver.get(f"{driver.current_url.split('#')[0]}@{username}")
            
            # 프로필 페이지에서 상태소개 확인
            user_bio = self.profile_page.getUserBio()
            
            # 기대 결과: 프로필 페이지에서 입력한 줄바꿈이 적용되어 여러 줄로 표시되어야 함
            assert "첫 번째 줄" in user_bio and "두 번째 줄" in user_bio, f"상태소개에 줄바꿈이 제대로 적용되지 않았습니다. 현재 값: {user_bio}"
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공: 여러 줄 상태소개가 성공적으로 적용되었습니다.")
            
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"여러 줄 상태소개 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def test_invalid_email_without_at_symbol(self, driver):
        """
        테스트 시나리오: @ 기호 없는 이메일 주소 입력 시 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자가 설정 페이지에 접근
        
        재현 절차:
        1. 'Email' 입력 필드에 @ 기호 없이 텍스트 입력
        2. 'Update Settings' 버튼 클릭
        
        기대 결과:
        - "이메일 주소에 '@'를 포함해 주세요. 'testuser.example.com'에 '@'가 없습니다." 오류 메시지 표시
        """
        try:
            # 1. 'Email' 입력 필드에 @ 기호 없이 텍스트 입력
            invalid_email = "testuser.example.com"
            self.settingsPage.clearField(SettingsLoc.EMAIL_INPUT)
            self.settingsPage.enterEmail(invalid_email)
            
            # 2. 'Update Settings' 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 오류 메시지 확인
            errorMessage = driver.find_element(*SettingsLoc.ERROR_MESSAGE).text
            expected_error = f"이메일 주소에 '@'를 포함해 주세요. '{invalid_email}'에 '@'가 없습니다."
            
            # 기대 결과: 오류 메시지가 표시되어야 함
            assert expected_error in errorMessage or "Please include an '@' in the email address" in error_message, f"예상된 오류 메시지가 표시되지 않았습니다. 현재 메시지: {error_message}"
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공: @ 기호 없는 이메일 오류 메시지 확인")
            
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"@ 기호 없는 이메일 테스트 실패: {str(e)}")
    
    @pytest.mark.data_not_required
    def test_invalid_email_with_special_chars(self, driver):
        """
        테스트 시나리오: 한글 또는 허용되지 않는 특수문자가 포함된 이메일 입력 시 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자가 설정 페이지에 접근
        
        재현 절차:
        1. 'Email' 입력 필드에 한글 또는 허용되지 않는 특수문자가 포함된 이메일 입력
        2. 'Update Settings' 버튼 클릭
        
        기대 결과:
        - "'@' 앞 부분에 '테' 기호가 포함되면 안됩니다." 오류 메시지 표시
        """
        try:
            # 1. 'Email' 입력 필드에 한글 또는 허용되지 않는 특수문자가 포함된 이메일 입력
            invalid_email = "테스트!@example.com"
            self.settingsPage.clearField(SettingsLoc.EMAIL_INPUT)
            self.settingsPage.enterEmail(invalid_email)
            
            # 2. 'Update Settings' 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 오류 메시지 확인
            errorMessage = driver.find_element(*SettingsLoc.ERROR_MESSAGE).text
            expected_error = "'@' 앞 부분에 '테' 기호가 포함되면 안됩니다."
            
            # 기대 결과: 오류 메시지가 표시되어야 함
            assert expected_error in errorMessage or "A part following '@' should not contain the symbol" in error_message, f"예상된 오류 메시지가 표시되지 않았습니다. 현재 메시지: {error_message}"
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공: 특수문자 포함 이메일 오류 메시지 확인")
            
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"특수문자 포함 이메일 테스트 실패: {str(e)}")
    
    @pytest.mark.data_required
    def test_empty_email_validation(self, driver):
        """
        테스트 시나리오: 이메일 필드를 비워둔 상태로 업데이트 시도 시 검증
        
        사전 조건:
        - 로그인된 사용자가 설정 페이지에 접근
        - 사용자에게 기존 이메일이 설정되어 있음
        
        재현 절차:
        1. 'Email' 입력 필드의 기존 이메일을 모두 삭제
        2. 'Update Settings' 버튼 클릭
        
        기대 결과:
        - 이메일 필드가 비어있는 상태로 업데이트되지 않아야 함
        """
        try:
            # 기존 이메일 저장
            original_email = driver.find_element(*SettingsLoc.EMAIL_INPUT).get_attribute("value")
            
            # 1. 'Email' 입력 필드의 기존 이메일을 모두 삭제
            self.settingsPage.clearField(SettingsLoc.EMAIL_INPUT)
            
            # 2. 'Update Settings' 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 페이지 새로고침 후 이메일 필드 확인
            driver.refresh()
            current_email = driver.find_element(*SettingsLoc.EMAIL_INPUT).get_attribute("value")
            
            # 기대 결과: 이메일 필드가 비어있는 상태로 업데이트되지 않아야 함
            assert current_email != "", "이메일 필드가 비어있는 상태로 업데이트되었습니다."
            assert current_email == original_email, f"이메일이 변경되었습니다. 원래 값: {original_email}, 현재 값: {current_email}"
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공: 빈 이메일 필드 검증 완료")
            
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"빈 이메일 필드 테스트 실패: {str(e)}")
```

이 코드는 JSON 형식의 테스트 케이스에 맞춰 5개의 테스트 함수를 구현했습니다:

1. `test_remove_bio_from_settings`: 사용자 상태소개(bio) 삭제 후 프로필 페이지에서 확인
2. `test_multiline_bio_in_settings`: 여러 줄로 구성된 상태소개(bio) 입력 후 프로필 페이지에서 확인
3. `test_invalid_email_without_at_symbol`: @ 기호 없는 이메일 주소 입력 시 오류 메시지 확인
4. `test_invalid_email_with_special_chars`: 한글 또는 허용되지 않는 특수문자가 포함된 이메일 입력 시 오류 메시지 확인
5. `test_empty_email_validation`: 이메일 필드를 비워둔 상태로 업데이트 시도 시 검증

각 테스트는 POM 구조를 따르고 있으며, 로케이터는 import하여 사용했습니다. 또한 각 테스트에는 명확한 docstring과 한글 주석을 포함했습니다. 데이터 세팅이 필요한 테스트에는 `@pytest.mark.data_required` 마커를, 필요하지 않은 테스트에는 `@pytest.mark.data_not_required` 마커를 적용했습니다.

# ===== 다음 배치 =====

요청하신 테스트 케이스에 맞게 Python + Selenium 기반의 Pytest 테스트 코드를 작성하겠습니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하는 테스트를 구현하겠습니다.

```python
# qa-realworld-automation/tests/test_pages.py

import os
import json
import pytest
import inspect
from utils.logger import setup_logger
import config
from pages.settings_page import SettingsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from locators.settings_locators import SettingsPageLocators as Loc

def loadTestData():
    """테스트 데이터 파일을 로드하는 함수"""
    dataFilePath = os.path.join(config.TEST_DATA_DIR, "test_data.json")
    with open(dataFilePath, 'r', encoding='utf-8') as file:
        return json.load(file)

# 로거 설정
logger = setup_logger(__name__)

class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 전에 로그인 상태로 설정 페이지에 접근하는 사전 조건 설정"""
        self.driver = driver
        self.testData = loadTestData()
        self.loginPage = LoginPage(driver)
        self.settingsPage = SettingsPage(driver)
        self.homePage = HomePage(driver)
        
        # 로그인 진행
        self.loginPage.navigate()
        self.loginPage.login(
            self.testData["currentUser"]["email"], 
            self.testData["currentUser"]["password"]
        )
        
        # 설정 페이지로 이동
        self.driver.get(f"{self.driver.current_url}settings")
        assert self.settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
        
    @pytest.mark.data_required
    def test_update_email_with_existing_email(self):
        """
        이미 존재하는 이메일로 업데이트 시도 시 오류 메시지 확인 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.   
        - 시스템에 existing@example.com이라는 이메일의 다른 사용자가 존재.
        
        재현 절차:
        1. 'Email' 입력 필드에 이미 시스템에 존재하는 다른 사용자의 이메일 (existing@example.com)을 입력한다.   
        2. 'Update Settings' 버튼을 클릭한다.   
        
        기대 결과:
        "Email has already been taken" 또는 유사한 명확한 오류 메시지가 표시되어야 한다.
        """
        try:
            # 1. 이미 존재하는 이메일 입력
            existing_email = self.testData["existingUser"]["email"]
            self.settingsPage.clearField(Loc.EMAIL_INPUT)
            self.settingsPage.enterEmail(existing_email)
            
            # 2. Update Settings 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 오류 메시지 확인
            errorMessage = self.driver.find_element(*Loc.ERROR_MESSAGE).text
            assert "Email has already been taken" in errorMessage or "이미 사용 중인 이메일" in error_message, \
                f"예상된 오류 메시지가 표시되지 않았습니다. 실제 메시지: {error_message}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def test_update_email_with_new_valid_email(self):
        """
        새로운 유효한 이메일로 업데이트 성공 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'Email' 입력 필드에 새롭고, 유효하며, 시스템에 존재하지 않는 이메일 (예: newValidEmail@example.com)을 입력한다.   
        2. 'Update Settings' 버튼을 클릭한다.   
        
        기대 결과:
        이메일이 성공적으로 newValidEmail@example.com으로 변경되어 홈페이지로 리다이렉션 된다.
        """
        try:
            # 1. 새로운 유효한 이메일 입력
            new_email = self.testData["newValidEmail"]
            self.settingsPage.clearField(Loc.EMAIL_INPUT)
            self.settingsPage.enterEmail(new_email)
            
            # 2. Update Settings 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 홈페이지로 리다이렉션 확인
            self.driver.wait_for_url_contains("home")
            currentUrl = self.driver.current_url
            assert "/home" in currentUrl or currentUrl.endswith('/'), \
                f"홈페이지로 리다이렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
            # 이메일 변경 확인 (설정 페이지 다시 접속하여 확인)
            self.driver.get(f"{self.driver.current_url.split('#')[0]}settings")
            email_field_value = self.driver.find_element(*Loc.EMAIL_INPUT).get_attribute("value")
            assert email_field_value == new_email, \
                f"이메일이 성공적으로 변경되지 않았습니다. 현재 이메일: {email_field_value}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def test_update_password_with_new_valid_password(self):
        """
        새로운 유효한 비밀번호로 업데이트 성공 테스트
        
        사전 조건:
        로그인된 사용자 (currentUser)가 현재 비밀번호 oldPassword로 로그인한 상태. 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'New Password' 입력 필드에 새로운 유효한 비밀번호 (예: newValidPassword123)를 입력한다.   
        2. 'Update Settings' 버튼을 클릭한다.   
        
        기대 결과:
        비밀번호 변경이 성공적으로 처리되어 홈페이지로 리다이렉션 된다.
        """
        try:
            # 1. 새로운 유효한 비밀번호 입력
            new_password = self.testData["newValidPassword"]
            self.settingsPage.clearField(Loc.PASSWORD_INPUT)
            self.settingsPage.enterPassword(new_password)
            
            # 2. Update Settings 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 홈페이지로 리다이렉션 확인
            self.driver.wait_for_url_contains("home")
            currentUrl = self.driver.current_url
            assert "/home" in currentUrl or currentUrl.endswith('/'), \
                f"홈페이지로 리다이렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
            # 비밀번호 변경 확인 (로그아웃 후 새 비밀번호로 로그인)
            # 로그아웃 처리
            logout_link = self.driver.find_element(*Loc.LOGOUTBUTTON)
            logout_link.click()
            
            # 새 비밀번호로 로그인
            self.loginPage.navigate()
            self.loginPage.login(
                self.testData["currentUser"]["email"], 
                new_password
            )
            
            # 로그인 성공 확인
            assert self.login_page.isLoggedIn(), "새 비밀번호로 로그인하지 못했습니다. 비밀번호 변경이 실패했을 수 있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def test_update_with_empty_password(self):
        """
        빈 비밀번호로 업데이트 시도 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'New Password' 입력 필드를 비워둔다.   
        2. 'Update Settings' 버튼을 클릭한다.
        
        기대 결과:
        비밀번호가 빈 값으로 변경되지 않고 홈페이지로 리다이렉션 된다.
        """
        try:
            # 1. 비밀번호 필드를 비워둠 (이미 비어있을 수 있으므로 명시적으로 비움)
            self.settingsPage.clearField(Loc.PASSWORD_INPUT)
            
            # 2. Update Settings 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 홈페이지로 리다이렉션 확인
            self.driver.wait_for_url_contains("home")
            currentUrl = self.driver.current_url
            assert "/home" in currentUrl or currentUrl.endswith('/'), \
                f"홈페이지로 리다이렉션되지 않았습니다. 현재 URL: {currentUrl}"
            
            # 비밀번호가 변경되지 않았는지 확인 (원래 비밀번호로 로그인 가능한지 확인)
            # 로그아웃 처리
            logout_link = self.driver.find_element(*Loc.LOGOUTBUTTON)
            logout_link.click()
            
            # 원래 비밀번호로 로그인
            self.loginPage.navigate()
            self.loginPage.login(
                self.testData["currentUser"]["email"], 
                self.testData["currentUser"]["password"]
            )
            
            # 로그인 성공 확인
            assert self.login_page.isLoggedIn(), "원래 비밀번호로 로그인하지 못했습니다. 비밀번호가 변경되었을 수 있습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_not_required
    def test_update_password_with_leading_space(self):
        """
        앞에 공백이 있는 비밀번호로 업데이트 시도 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'New Password' 입력 필드에 새 비밀번호(맨 앞에 공백 한 칸 + "testpassword")를 입력한다.   
        2. 'Update Settings' 버튼을 클릭한다.   
        
        기대 결과:
        "비밀번호는 앞/뒤 공백을 포함할 수 없습니다."와 같은 오류메시지가 표시 되어야한다.
        """
        try:
            # 1. 앞에 공백이 있는 비밀번호 입력
            password_with_space = " testpassword"
            self.settingsPage.clearField(Loc.PASSWORD_INPUT)
            self.settingsPage.enterPassword(password_with_space)
            
            # 2. Update Settings 버튼 클릭
            self.settingsPage.clickUpdateButton()
            
            # 오류 메시지 확인
            errorMessage = self.driver.find_element(*Loc.ERROR_MESSAGE).text
            expected_errorMessages = [
                "비밀번호는 앞/뒤 공백을 포함할 수 없습니다",
                "Password cannot include leading or trailing whitespace",
                "Password cannot contain leading or trailing spaces"
            ]
            
            error_found = any(expected in errorMessage for expected in expected_errorMessages)
            assert error_found, f"예상된 오류 메시지가 표시되지 않았습니다. 실제 메시지: {error_message}"
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            raise
```

이 코드는 JSON 형식의 테스트 케이스에 맞게 5개의 테스트 함수를 구현했습니다:

1. `test_update_email_with_existing_email`: 이미 존재하는 이메일로 업데이트 시도 시 오류 메시지 확인
2. `test_update_email_with_new_valid_email`: 새로운 유효한 이메일로 업데이트 성공 확인
3. `test_update_password_with_new_valid_password`: 새로운 유효한 비밀번호로 업데이트 성공 확인
4. `test_update_with_empty_password`: 빈 비밀번호로 업데이트 시도 시 기존 비밀번호 유지 확인
5. `test_update_password_with_leading_space`: 앞에 공백이 있는 비밀번호로 업데이트 시도 시 오류 메시지 확인

각 테스트는 POM 구조를 따르며, 공통 코드와 로케이터를 import하여 사용합니다. 또한 각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다. 테스트 데이터는 JSON 파일에서 로드하며, 오류 처리를 위해 try-except 구문을 사용했습니다.

# ===== 다음 배치 =====

요청하신 대로 Python + Selenium 기반의 Pytest 테스트 코드를 작성하겠습니다. 주어진 JSON 형식의 테스트케이스에 맞춰 POM 구조를 따르는 테스트 코드를 생성하겠습니다.

```python
# qa-realworld-automation/tests/test_pages.py

import os
import json
import pytest
import inspect
import time
from selenium.webdriver.common.by import By

# 페이지 객체 임포트
from pages.settings_page import SettingsPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.article_page import ArticlePage

# 로케이터 임포트
from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.home_locators import HomePageLocators as HomeLoc
from locators.article_locators import ArticlePageLocators as ArticleLoc

# 유틸리티 임포트
from utils.logger import setup_logger
import config

logger = setup_logger(__name__)

def loadTestData():
    """테스트 데이터 로드 함수"""
    dataFilePath = os.path.join(config.TEST_DATA_DIR, "test_data.json")
    with open(dataFilePath, 'r', encoding='utf-8') as file:
        return json.load(file)


class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""
    
    @pytest.mark.data_required
    def test_password_with_trailing_space(self, driver):
        """
        테스트 시나리오: 비밀번호 뒤에 공백이 있는 경우 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'New Password' 입력 필드에 새 비밀번호("testpassword + 뒤에 공백 한 칸")를 입력한다.
        2. 'Update Settings' 버튼을 클릭한다.
        
        기대 결과:
        "비밀번호는 앞/뒤 공백을 포함할 수 없습니다."와 같은 오류메시지가 표시 되어야한다.
        """
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["login"]
            
            # 로그인 진행
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 설정 페이지로 이동
            settingsPage = SettingsPage(driver)
            driver.get(f"{driver.current_url}settings")
            
            # 설정 페이지 로드 확인
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 비밀번호 필드에 공백이 포함된 비밀번호 입력
            password_with_space = "testpassword "  # 뒤에 공백 한 칸 추가
            settingsPage.enterPassword(password_with_space)
            
            # Update Settings 버튼 클릭
            settingsPage.clickUpdateButton()
            
            # 오류 메시지 확인 (실제 구현에 따라 로케이터 및 메시지 내용이 다를 수 있음)
            error_element = driver.find_element(By.CSS_SELECTOR, SettingsLoc.ERROR_MESSAGE)
            assert "공백을 포함할 수 없습니다" in error_element.text, "비밀번호 공백 관련 오류 메시지가 표시되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"비밀번호 뒤 공백 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required
    def test_password_with_only_space(self, driver):
        """
        테스트 시나리오: 비밀번호에 공백만 입력한 경우 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. 'New Password' 입력 필드에 새 비밀번호(" ", 빈 문자열만 입력)를 입력한다.
        2. 'Update Settings' 버튼을 클릭한다.
        
        기대 결과:
        "비밀번호는 공백을 포함할 수 없습니다."와 같은 오류메시지가 표시 되어야한다.
        """
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["login"]
            
            # 로그인 진행
            loginPage = LoginPage(driver)
            loginPage.navigate()
            loginPage.login(testData["email"], testData["password"])
            
            # 설정 페이지로 이동
            settingsPage = SettingsPage(driver)
            driver.get(f"{driver.current_url}settings")
            
            # 설정 페이지 로드 확인
            assert settingsPage.isSettingsPageLoaded(), "설정 페이지가 로드되지 않았습니다."
            
            # 비밀번호 필드에 공백만 입력
            space_only_password = " "
            settingsPage.enterPassword(space_only_password)
            
            # Update Settings 버튼 클릭
            settingsPage.clickUpdateButton()
            
            # 오류 메시지 확인 (실제 구현에 따라 로케이터 및 메시지 내용이 다를 수 있음)
            error_element = driver.find_element(By.CSS_SELECTOR, SettingsLoc.ERROR_MESSAGE)
            assert "공백을 포함할 수 없습니다" in error_element.text, "비밀번호 공백 관련 오류 메시지가 표시되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"비밀번호 공백만 입력 테스트 실패: {str(e)}")
            raise

