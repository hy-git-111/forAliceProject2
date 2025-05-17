

@pytest.mark.data_not_required
def test_navigate_to_settings_page(driver):
    """
    테스트 시나리오: 로그인된 사용자가 네비게이션바에서 settings를 클릭하면
    설정 페이지로 성공적으로 접근하는지 확인
    
    사전 조건: 로그인된 사용자 (currentUser)가 홈페이지에 접속.
    """
    try:
        # 홈페이지 객체 생성
        home_page = HomePage(driver)
        
        # 사전 조건: 사용자가 로그인되어 있고 홈페이지에 있음을 가정
        
        # 1. 네비게이션바에서 "settings"를 클릭
        home_page.click_settings_link()
        
        # 설정 페이지 객체 생성
        settings_page = SettingsPage(driver)
        
        # 기대 결과: 설정 페이지 (/settings)에 성공적으로 접근
        assert settings_page.is_settings_page_loaded(), "설정 페이지로 이동하지 않았습니다."
        assert "/settings" in driver.current_url, "URL이 설정 페이지 URL이 아닙니다."
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")
```

이 코드는 주어진 JSON 형식의 테스트 케이스에 맞게 5개의 테스트 함수를 구현했습니다:

1. `test_edit_article_button_navigates_to_edit_page`: 게시글 상세 페이지에서 Edit Article 버튼 클릭 시 수정 페이지로 이동하는지 확인
2. `test_edit_article_content_successfully`: 게시글 내용 수정 후 성공적으로 반영되는지 확인
3. `test_edit_article_with_empty_content`: 게시글 내용을 모두 삭제하고 저장 시 오류 메시지가 표시되는지 확인
4. `test_delete_article_successfully`: 게시글 삭제 기능이 정상 작동하는지 확인
5. `test_navigate_to_settings_page`: 네비게이션바에서 settings 클릭 시 설정 페이지로 이동하는지 확인

각 테스트는 POM 구조를 따르며, 필요한 Page 객체와 Locator를 import하여 사용합니다. 또한 테스트 데이터가 필요한 경우 `@pytest.mark.data_required` 데코레이터를, 필요하지 않은 경우 `@pytest.mark.data_not_required` 데코레이터를 사용했습니다.

# ===== 다음 배치 =====

다음은 요청하신 테스트 케이스에 맞게 작성한 Pytest 테스트 코드입니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하도록 작성했습니다.

```python
import os
import json
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.settings_page import SettingsPage
from pages.home_page import HomePage
from locators.settings_locators import SettingsPageLocators as Loc
from config.config import ensureDirectoryExists, TEST_DATA_DIR

def load_test_data():
    """테스트 데이터 파일을 로드하는 함수"""
    data_file = os.path.join(TEST_DATA_DIR, "test_data.json")
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""

    @pytest.mark.data_required
    def test_settings_page_layout(self, driver):
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
        - "Update Settings" 버튼과 "Or click here to logout." 버튼이 하단에 표시된다.
        """
        try:
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 설정 페이지로 이동
            settings_page.navigate_to_settings()
            
            # 페이지 제목 확인
            assert settings_page.is_element_visible(Loc.PAGE_TITLE), "페이지 제목이 표시되지 않습니다."
            assert settings_page.get_element_text(Loc.PAGE_TITLE) == "Your Settings", "페이지 제목이 'Your Settings'가 아닙니다."
            
            # 입력 필드 순서 확인
            fields = [
                Loc.PROFILE_PICTURE_INPUT,
                Loc.USERNAME_INPUT,
                Loc.BIO_INPUT,
                Loc.EMAIL_INPUT,
                Loc.PASSWORD_INPUT
            ]
            
            # 모든 필드가 표시되는지 확인
            for field in fields:
                assert settings_page.is_element_visible(field), f"{field} 필드가 표시되지 않습니다."
            
            # 버튼 확인
            assert settings_page.is_element_visible(Loc.UPDATE_SETTINGS_BUTTON), "Update Settings 버튼이 표시되지 않습니다."
            assert settings_page.is_element_visible(Loc.LOGOUT_BUTTON), "로그아웃 버튼이 표시되지 않습니다."
            
            # 로그아웃 버튼 텍스트 확인
            logout_text = settings_page.get_element_text(Loc.LOGOUT_BUTTON)
            assert "click here to logout" in logout_text, "로그아웃 버튼 텍스트가 올바르지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_input_field_placeholders(self, driver):
        """
        각 입력 필드의 플레이스홀더 텍스트를 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지 (/settings)에 접근.
        
        재현 절차:
        1. 각 입력 필드의 플레이스홀더 텍스트를 확인한다.
        
        기대 결과:
        - "URL of profile picture" 필드에 적절한 플레이스홀더가 표시된다.
        - "Username" 필드에 적절한 플레이스홀더가 표시된다.
        - "Short bio about you" 텍스트 영역에 적절한 플레이스홀더가 표시된다.
        - "Email" 필드에 적절한 플레이스홀더가 표시된다.
        - "New Password" 필드에 적절한 플레이스홀더가 표시된다.
        """
        try:
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 설정 페이지로 이동
            settings_page.navigate_to_settings()
            
            # 각 필드의 플레이스홀더 확인
            profile_pic_placeholder = settings_page.get_placeholder(Loc.PROFILE_PICTURE_INPUT)
            assert "URL of profile picture" in profile_pic_placeholder, "프로필 이미지 URL 필드의 플레이스홀더가 올바르지 않습니다."
            
            username_placeholder = settings_page.get_placeholder(Loc.USERNAME_INPUT)
            assert "Username" in username_placeholder, "사용자 이름 필드의 플레이스홀더가 올바르지 않습니다."
            
            bio_placeholder = settings_page.get_placeholder(Loc.BIO_INPUT)
            assert "Short bio about you" in bio_placeholder, "상태 소개 필드의 플레이스홀더가 올바르지 않습니다."
            
            email_placeholder = settings_page.get_placeholder(Loc.EMAIL_INPUT)
            assert "Email" in email_placeholder, "이메일 필드의 플레이스홀더가 올바르지 않습니다."
            
            password_placeholder = settings_page.get_placeholder(Loc.PASSWORD_INPUT)
            assert "New Password" in password_placeholder, "비밀번호 필드의 플레이스홀더가 올바르지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_logout_functionality(self, driver):
        """
        로그아웃 기능을 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지 (/settings)에 접근.
        
        재현 절차:
        1. "Or click here to logout." 버튼을 클릭한다.
        
        기대 결과:
        - 사용자는 로그아웃 처리되어 홈페이지로 리다이렉션된다.
        """
        try:
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            home_page = HomePage(driver)
            
            # 설정 페이지로 이동
            settings_page.navigate_to_settings()
            
            # 로그아웃 버튼 클릭
            settings_page.click_logout_button()
            
            # 홈페이지로 리다이렉션 확인
            assert home_page.is_at_home_page(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 로그아웃 상태 확인 (로그인/회원가입 링크가 표시되는지)
            assert home_page.is_element_visible(home_page.locators.SIGN_IN_LINK), "로그인 링크가 표시되지 않습니다."
            assert home_page.is_element_visible(home_page.locators.SIGN_UP_LINK), "회원가입 링크가 표시되지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_remove_profile_image(self, driver):
        """
        프로필 이미지 URL 제거 기능을 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - currentUser에게 기존 프로필 이미지 URL이 설정되어 있음.
        
        재현 절차:
        1. "URL of profile picture" 입력 필드의 기존 이미지 URL을 모두 삭제한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바의 프로필 이미지를 확인한다.
        
        기대 결과:
        - 프로필 이미지가 기본 이미지 아이콘으로 표시된다.
        """
        try:
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            home_page = HomePage(driver)
            
            # 설정 페이지로 이동
            settings_page.navigate_to_settings()
            
            # 프로필 이미지 URL 필드 비우기
            settings_page.clear_profile_image_url()
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지로 리다이렉션 확인
            assert home_page.is_at_home_page(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 프로필 이미지가 기본 이미지인지 확인
            # 기본 이미지는 src 속성이 비어있거나 기본 이미지 URL을 가짐
            profile_img = home_page.get_profile_image_src()
            assert not profile_img or "default" in profile_img.lower() or profile_img.startswith("data:image"), "프로필 이미지가 기본 이미지로 변경되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_update_profile_image(self, driver):
        """
        프로필 이미지 URL 업데이트 기능을 확인하는 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "URL of profile picture" 입력 필드에 새로운 유효한 이미지 URL을 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바의 프로필 이미지를 확인한다.
        
        기대 결과:
        - 프로필 이미지가 새롭게 입력한 URL의 이미지로 성공적으로 변경된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()
            new_image_url = test_data.get("profile_image_url", "https://picsum.photos/200")
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            home_page = HomePage(driver)
            
            # 설정 페이지로 이동
            settings_page.navigate_to_settings()
            
            # 새 프로필 이미지 URL 입력
            settings_page.set_profile_image_url(new_image_url)
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지로 리다이렉션 확인
            assert home_page.is_at_home_page(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 프로필 이미지가 새 URL로 변경되었는지 확인
            profile_img = home_page.get_profile_image_src()
            
            # URL이 정확히 일치하지 않을 수 있으므로 URL의 일부만 확인
            # 예: CDN이나 캐싱 서비스를 통해 URL이 변경될 수 있음
            assert profile_img and "picsum.photos" in profile_img, "프로필 이미지가 새 URL로 변경되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 JSON 형식의 테스트 케이스에 맞춰 5개의 테스트 함수를 포함하고 있습니다:

1. `test_settings_page_layout`: 설정 페이지의 전체적인 레이아웃을 확인
2. `test_input_field_placeholders`: 각 입력 필드의 플레이스홀더 텍스트 확인
3. `test_logout_functionality`: 로그아웃 기능 확인
4. `test_remove_profile_image`: 프로필 이미지 URL 제거 기능 확인
5. `test_update_profile_image`: 프로필 이미지 URL 업데이트 기능 확인

각 테스트는 POM 구조를 따르며, 로케이터를 import하여 사용하고 있습니다. 또한 각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다. 모든 테스트는 독립적으로 실행 가능하며, 테스트 데이터는 JSON 파일에서 로드합니다.

# ===== 다음 배치 =====

아래는 요청하신 테스트 케이스에 맞게 작성된 Pytest 테스트 코드입니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하는 내용으로 작성했습니다.

```python
import os
import json
import pytest
from selenium.webdriver.common.by import By
from pages.settings_page import SettingsPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.home_locators import HomePageLocators as HomeLoc
from locators.profile_locators import ProfilePageLocators as ProfileLoc
from config import TEST_DATA_DIR


def load_test_data():
    """테스트 데이터 로드 함수"""
    data_file = os.path.join(TEST_DATA_DIR, "test_data.json")
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""

    @pytest.mark.data_required
    def test_profile_picture_update(self, driver):
        """
        테스트 시나리오: 프로필 이미지 URL 업데이트 후 기본 이미지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "URL of profile picture" 입력 필드에 새로운 유효한 이미지 URL을 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바의 프로필 이미지를 확인한다.
        
        기대 결과:
        프로필 이미지가 기본 이미지 아이콘으로 표시된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["profile_picture"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 프로필 이미지 URL 입력
            settings_page.update_profile_image_url(test_data["image_url"])
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            
            # 네비게이션 바의 프로필 이미지 확인
            assert home_page.is_default_profile_image_displayed(), "프로필 이미지가 기본 이미지 아이콘으로 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_empty_username_update(self, driver):
        """
        테스트 시나리오: 빈 닉네임으로 업데이트 시도
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - currentUser에게 기존 닉네임이 설정되어 있음.
        
        재현 절차:
        1. "Username" 입력 필드의 기존 닉네임을 모두 삭제한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        닉네임 필드가 비어있는 상태로 업데이트되지 않아야 한다.
        """
        try:
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 기존 닉네임 저장
            original_username = settings_page.get_current_username()
            
            # 닉네임 필드 비우기
            settings_page.clear_username_field()
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 오류 메시지 또는 현재 페이지가 여전히 설정 페이지인지 확인
            assert settings_page.is_settings_page_displayed(), "설정 페이지를 벗어났습니다. 빈 닉네임이 허용되었을 수 있습니다."
            
            # 또는 오류 메시지 확인
            assert settings_page.is_error_message_displayed(), "빈 닉네임 오류 메시지가 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_duplicate_username_update(self, driver):
        """
        테스트 시나리오: 이미 존재하는 닉네임으로 업데이트 시도
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - 시스템에 existingUser라는 닉네임의 다른 사용자가 존재.
        
        재현 절차:
        1. "Username" 입력 필드에 이미 시스템에 존재하는 다른 사용자의 닉네임 (existingUser)을 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. 오류 메시지 또는 UI 변화를 확인한다.
        
        기대 결과:
        "Username has already been taken" 또는 유사한 명확한 오류 메시지가 표시되어야 한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["duplicate_username"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 이미 존재하는 닉네임 입력
            settings_page.update_username(test_data["existing_username"])
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 오류 메시지 확인
            error_message = settings_page.get_error_message()
            assert "username has already been taken" in error_message.lower(), f"예상된 오류 메시지가 표시되지 않았습니다. 실제 메시지: {error_message}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_valid_username_update(self, driver):
        """
        테스트 시나리오: 유효한 새 닉네임으로 업데이트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "Username" 입력 필드에 새롭고, 유효하며, 시스템에 존재하지 않는 닉네임 (예: validNewUser123)을 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. 홈페이지로 리다이렉션 된다.
        4. 네비게이션 바에서 변경된 닉네임을 확인한다.
        
        기대 결과:
        닉네임이 성공적으로 validNewUser123으로 변경된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["valid_username"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 새로운 유효한 닉네임 입력
            new_username = test_data["new_username"]
            settings_page.update_username(new_username)
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            
            # 네비게이션 바에서 변경된 닉네임 확인
            displayed_username = home_page.get_navbar_username()
            assert displayed_username == new_username, f"닉네임이 성공적으로 변경되지 않았습니다. 예상: {new_username}, 실제: {displayed_username}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_bio_update(self, driver):
        """
        테스트 시나리오: 상태소개 업데이트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "Short bio about you" 텍스트 영역에 새로운 유효한 상태소개 (예: "새로운 상태 메시지입니다.")를 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. currentUser의 프로필 페이지 (/@currentUser.username)에서 변경된 상태소개를 확인한다.
        
        기대 결과:
        프로필 페이지에 변경된 상태소개 "새로운 상태 메시지입니다."가 올바르게 표시된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["bio_update"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 현재 사용자 이름 저장 (프로필 페이지 방문용)
            current_username = settings_page.get_current_username()
            
            # 새로운 상태소개 입력
            new_bio = test_data["new_bio"]
            settings_page.update_bio(new_bio)
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            
            # 프로필 페이지로 이동
            home_page.navigate_to_profile(current_username)
            
            # 프로필 페이지 객체 생성
            profile_page = ProfilePage(driver)
            
            # 변경된 상태소개 확인
            displayed_bio = profile_page.get_bio_text()
            assert displayed_bio == new_bio, f"상태소개가 성공적으로 변경되지 않았습니다. 예상: {new_bio}, 실제: {displayed_bio}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 테스트 코드는 JSON 형식의 테스트 케이스에 맞춰 5개의 테스트 함수를 구현했습니다:

1. `test_profile_picture_update`: 프로필 이미지 URL 업데이트 후 기본 이미지 확인
2. `test_empty_username_update`: 빈 닉네임으로 업데이트 시도
3. `test_duplicate_username_update`: 이미 존재하는 닉네임으로 업데이트 시도
4. `test_valid_username_update`: 유효한 새 닉네임으로 업데이트
5. `test_bio_update`: 상태소개 업데이트

각 테스트는 POM 구조를 따르며, 로케이터를 import하여 사용하고 있습니다. 또한 모든 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다. 테스트 데이터는 `load_test_data()` 함수를 통해 JSON 파일에서 로드하며, 각 테스트는 독립적으로 실행됩니다.

# ===== 다음 배치 =====

아래는 요청하신 테스트 케이스를 POM 구조에 맞게 작성한 코드입니다. 각 테스트는 JSON 형식의 테스트 케이스와 일치하며, 독립적으로 실행 가능합니다.

```python
import os
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage
from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.profile_locators import ProfilePageLocators as ProfileLoc
from config.config import TEST_DATA_DIR


def load_test_data():
    """테스트 데이터 로드 함수"""
    data_file = os.path.join(TEST_DATA_DIR, "test_data.json")
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


class TestSettingsPage:
    """설정 페이지 관련 테스트 클래스"""

    @pytest.mark.data_required
    def test_remove_bio_from_settings(self, driver):
        """
        테스트 시나리오: 사용자 상태소개(bio) 삭제 후 프로필 페이지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - currentUser에게 기존 상태소개가 설정되어 있음.
        
        재현 절차:
        1. "Short bio about you" 텍스트 영역의 기존 내용을 모두 삭제한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. currentUser의 프로필 페이지에서 상태소개 영역을 확인한다.
        
        기대 결과:
        프로필 페이지에서 상태소개가 비어있는 것으로 표시되어야 한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            username = test_data["username"]
            
            # 설정 페이지 접근
            settings_page = SettingsPage(driver)
            settings_page.navigate_to_settings()
            
            # 1. "Short bio about you" 텍스트 영역의 기존 내용을 모두 삭제
            settings_page.clear_bio()
            
            # 2. "Update Settings" 버튼을 클릭
            settings_page.click_update_settings()
            
            # 3. currentUser의 프로필 페이지에서 상태소개 영역을 확인
            profile_page = ProfilePage(driver)
            profile_page.navigate_to_profile(username)
            
            # 기대 결과: 프로필 페이지에서 상태소개가 비어있는 것으로 표시되어야 한다
            bio_text = profile_page.get_bio_text()
            assert bio_text == "" or bio_text is None, "상태소개가 비어있지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_multiline_bio_in_settings(self, driver):
        """
        테스트 시나리오: 여러 줄로 구성된 상태소개(bio) 입력 후 프로필 페이지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "Short bio about you" 텍스트 영역에 여러 줄로 구성된 텍스트를 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        3. currentUser의 프로필 페이지에서 상태소개 영역을 확인한다.
        
        기대 결과:
        프로필 페이지에서 입력한 줄바꿈이 적용되어 여러 줄로 표시되어야 한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            username = test_data["username"]
            multiline_bio = "첫 번째 줄\n두 번째 줄"
            
            # 설정 페이지 접근
            settings_page = SettingsPage(driver)
            settings_page.navigate_to_settings()
            
            # 1. "Short bio about you" 텍스트 영역에 여러 줄로 구성된 텍스트를 입력
            settings_page.set_bio(multiline_bio)
            
            # 2. "Update Settings" 버튼을 클릭
            settings_page.click_update_settings()
            
            # 3. currentUser의 프로필 페이지에서 상태소개 영역을 확인
            profile_page = ProfilePage(driver)
            profile_page.navigate_to_profile(username)
            
            # 기대 결과: 프로필 페이지에서 입력한 줄바꿈이 적용되어 여러 줄로 표시되어야 한다
            bio_text = profile_page.get_bio_text()
            assert "첫 번째 줄" in bio_text and "두 번째 줄" in bio_text, "여러 줄 텍스트가 올바르게 표시되지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_not_required
    def test_invalid_email_without_at_symbol(self, driver):
        """
        테스트 시나리오: @ 기호 없는 이메일 입력 시 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "Email" 입력 필드에 @ 기호 없이 텍스트를 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        "이메일 주소에 "@"를 포함해 주세요. "testuser.example.com"에 "@"가 없습니다." 오류 메시지가 표시되어야 한다.
        """
        try:
            # 설정 페이지 접근
            settings_page = SettingsPage(driver)
            settings_page.navigate_to_settings()
            
            # 1. "Email" 입력 필드에 @ 기호 없이 텍스트를 입력
            invalid_email = "testuser.example.com"
            settings_page.set_email(invalid_email)
            
            # 2. "Update Settings" 버튼을 클릭
            settings_page.click_update_settings()
            
            # 기대 결과: 오류 메시지가 표시되어야 한다
            error_message = settings_page.get_error_message()
            expected_error = f'이메일 주소에 "@"를 포함해 주세요. "{invalid_email}"에 "@"가 없습니다.'
            assert expected_error in error_message, f"예상 오류 메시지가 표시되지 않습니다. 실제: {error_message}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_not_required
    def test_invalid_email_with_korean_chars(self, driver):
        """
        테스트 시나리오: 한글 또는 허용되지 않는 특수문자가 포함된 이메일 입력 시 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "Email" 입력 필드에 한글 또는 허용되지 않는 특수문자가 포함된 이메일을 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        "@ 앞 부분에 "테" 기호가 포함되면 안됩니다." 오류 메시지가 표시되어야 한다.
        """
        try:
            # 설정 페이지 접근
            settings_page = SettingsPage(driver)
            settings_page.navigate_to_settings()
            
            # 1. "Email" 입력 필드에 한글 또는 허용되지 않는 특수문자가 포함된 이메일을 입력
            invalid_email = "테스트!@example.com"
            settings_page.set_email(invalid_email)
            
            # 2. "Update Settings" 버튼을 클릭
            settings_page.click_update_settings()
            
            # 기대 결과: 오류 메시지가 표시되어야 한다
            error_message = settings_page.get_error_message()
            expected_error = '@ 앞 부분에 "테" 기호가 포함되면 안됩니다.'
            assert expected_error in error_message, f"예상 오류 메시지가 표시되지 않습니다. 실제: {error_message}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_empty_email_field(self, driver):
        """
        테스트 시나리오: 이메일 필드를 비워둔 상태로 업데이트 시도
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - currentUser에게 기존 이메일이 설정되어 있음.
        
        재현 절차:
        1. "Email" 입력 필드의 기존 이메일을 모두 삭제한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        이메일 필드가 비어있는 상태로 업데이트되지 않아야 한다.
        """
        try:
            # 설정 페이지 접근
            settings_page = SettingsPage(driver)
            settings_page.navigate_to_settings()
            
            # 기존 이메일 저장
            original_email = settings_page.get_email()
            
            # 1. "Email" 입력 필드의 기존 이메일을 모두 삭제
            settings_page.clear_email()
            
            # 2. "Update Settings" 버튼을 클릭
            settings_page.click_update_settings()
            
            # 기대 결과: 이메일 필드가 비어있는 상태로 업데이트되지 않아야 한다
            # 페이지 새로고침 후 이메일 필드 확인
            driver.refresh()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, SettingsLoc.EMAIL_INPUT))
            )
            
            current_email = settings_page.get_email()
            assert current_email != "", "이메일 필드가 비어있는 상태로 업데이트되었습니다."
            assert current_email == original_email, f"이메일이 변경되었습니다. 원래: {original_email}, 현재: {current_email}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 JSON 형식의 테스트 케이스에 맞춰 5개의 테스트 함수를 구현했습니다:

1. `test_remove_bio_from_settings`: 사용자 상태소개(bio) 삭제 후 프로필 페이지 확인
2. `test_multiline_bio_in_settings`: 여러 줄로 구성된 상태소개(bio) 입력 후 프로필 페이지 확인
3. `test_invalid_email_without_at_symbol`: @ 기호 없는 이메일 입력 시 오류 메시지 확인
4. `test_invalid_email_with_korean_chars`: 한글 또는 허용되지 않는 특수문자가 포함된 이메일 입력 시 오류 메시지 확인
5. `test_empty_email_field`: 이메일 필드를 비워둔 상태로 업데이트 시도

각 테스트는 POM 구조를 따르며, 로케이터를 import하여 사용하고 있습니다. 또한 데이터 세팅이 필요한 테스트에는 `@pytest.mark.data_required` 데코레이터를, 필요하지 않은 테스트에는 `@pytest.mark.data_not_required` 데코레이터를 적용했습니다.

# ===== 다음 배치 =====

요청하신 대로 Python + Selenium 기반의 Pytest 테스트 코드를 작성하겠습니다. 주어진 JSON 형식의 테스트케이스에 맞춰 POM 구조를 따르는 테스트 코드를 작성하겠습니다.

```python
import os
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.settings_page import SettingsPage
from pages.home_page import HomePage
from locators.settings_locators import SettingsPageLocators as Loc
from config import TEST_DATA_DIR

def load_test_data():
    """테스트 데이터 파일을 로드하는 함수"""
    data_file = os.path.join(TEST_DATA_DIR, "test_data.json")
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

class TestSettingsPage:
    """설정 페이지 기능 테스트 클래스"""

    @pytest.mark.data_required
    def test_update_email_with_existing_email(self, driver):
        """
        이미 존재하는 이메일로 업데이트 시도 시 오류 메시지 표시 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        - 시스템에 existing@example.com이라는 이메일의 다른 사용자가 존재.
        
        재현 절차:
        1. "Email" 입력 필드에 이미 시스템에 존재하는 다른 사용자의 이메일 (existing@example.com)을 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        "Email has already been taken" 또는 유사한 명확한 오류 메시지가 표시되어야 한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            existing_email = test_data["existing_email"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 이미 존재하는 이메일 입력
            settings_page.update_email(existing_email)
            
            # 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 오류 메시지 확인
            assert settings_page.is_error_message_displayed(), "오류 메시지가 표시되지 않았습니다."
            assert "Email has already been taken" in settings_page.get_error_message(), "이메일 중복 오류 메시지가 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_update_email_with_new_valid_email(self, driver):
        """
        새로운 유효한 이메일로 업데이트 성공 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "Email" 입력 필드에 새롭고, 유효하며, 시스템에 존재하지 않는 이메일 (예: newValidEmail@example.com)을 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        이메일이 성공적으로 newValidEmail@example.com으로 변경되어 홈페이지로 리다이렉션 된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            new_valid_email = test_data["new_valid_email"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 새로운 유효한 이메일 입력
            settings_page.update_email(new_valid_email)
            
            # 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지로 리다이렉션 확인
            home_page = HomePage(driver)
            assert home_page.is_home_page_displayed(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 이메일이 성공적으로 변경되었는지 확인 (설정 페이지 다시 접근하여 확인)
            settings_page.navigate_to_settings()
            assert settings_page.get_email_value() == new_valid_email, "이메일이 성공적으로 변경되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_update_password_with_new_valid_password(self, driver):
        """
        새로운 유효한 비밀번호로 업데이트 성공 테스트
        
        사전 조건:
        로그인된 사용자 (currentUser)가 현재 비밀번호 oldPassword로 로그인한 상태. 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "New Password" 입력 필드에 새로운 유효한 비밀번호 (예: newValidPassword123)를 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        비밀번호 변경이 성공적으로 처리되어 홈페이지로 리다이렉션 된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            new_valid_password = test_data["new_valid_password"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 새로운 유효한 비밀번호 입력
            settings_page.update_password(new_valid_password)
            
            # 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지로 리다이렉션 확인
            home_page = HomePage(driver)
            assert home_page.is_home_page_displayed(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 비밀번호가 성공적으로 변경되었는지 확인 (로그아웃 후 새 비밀번호로 로그인)
            home_page.logout()
            home_page.login(test_data["username"], new_valid_password)
            assert home_page.is_logged_in(), "새 비밀번호로 로그인할 수 없습니다. 비밀번호 변경이 실패했을 수 있습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_not_required
    def test_update_with_empty_password(self, driver):
        """
        빈 비밀번호로 업데이트 시 비밀번호 유지 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "New Password" 입력 필드를 비워둔다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        비밀번호가 빈 값으로 변경되지 않고 홈페이지로 리다이렉션 된다.
        """
        try:
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 비밀번호 필드를 비워둠 (명시적으로 빈 문자열 입력)
            settings_page.update_password("")
            
            # 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 홈페이지로 리다이렉션 확인
            home_page = HomePage(driver)
            assert home_page.is_home_page_displayed(), "홈페이지로 리다이렉션되지 않았습니다."
            
            # 로그인 상태 유지 확인 (비밀번호가 변경되지 않았음을 간접적으로 확인)
            assert home_page.is_logged_in(), "사용자가 로그아웃되었습니다. 빈 비밀번호로 변경되었을 수 있습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_update_password_with_leading_space(self, driver):
        """
        앞에 공백이 있는 비밀번호로 업데이트 시도 시 오류 메시지 표시 테스트
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "New Password" 입력 필드에 새 비밀번호(맨 앞에 공백 한 칸 + "testpassword")를 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        "비밀번호는 앞/뒤 공백을 포함할 수 없습니다."와 같은 오류메시지가 표시 되어야한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            password_with_leading_space = " " + test_data["password_base"]
            
            # 설정 페이지 객체 생성
            settings_page = SettingsPage(driver)
            
            # 앞에 공백이 있는 비밀번호 입력
            settings_page.update_password(password_with_leading_space)
            
            # 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 오류 메시지 확인
            assert settings_page.is_error_message_displayed(), "오류 메시지가 표시되지 않았습니다."
            error_message = settings_page.get_error_message()
            assert "공백" in error_message or "space" in error_message.lower(), "비밀번호 공백 관련 오류 메시지가 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 주어진 JSON 형식의 테스트케이스에 맞춰 5개의 테스트 함수를 포함하고 있습니다. 각 테스트는 POM 구조를 따르며, 설정 페이지에서의 이메일 및 비밀번호 업데이트 기능을 테스트합니다.

각 테스트 함수는:
1. 명확한 docstring으로 테스트 목적, 사전 조건, 재현 절차, 기대 결과를 설명합니다.
2. 필요한 경우 테스트 데이터를 로드합니다.
3. Page Object를 사용하여 UI 조작을 수행합니다.
4. assert를 사용하여 결과를 검증합니다.
5. 오류 처리를 위해 try-except 구문을 사용합니다.

또한 데이터 세팅이 필요한 테스트에는 @pytest.mark.data_required 데코레이터를, 필요하지 않은 테스트에는 @pytest.mark.data_not_required 데코레이터를 적용했습니다.

# ===== 다음 배치 =====

다음은 요청하신 테스트 케이스에 맞게 작성한 Pytest 테스트 코드입니다:

```python
import os
import json
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.settings_page import SettingsPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.article_page import ArticlePage

from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.login_locators import LoginPageLocators as LoginLoc
from locators.home_locators import HomePageLocators as HomeLoc
from locators.article_locators import ArticlePageLocators as ArticleLoc

from config import TEST_DATA_DIR


def load_test_data():
    """테스트 데이터 로드 함수"""
    with open(os.path.join(TEST_DATA_DIR, 'test_data.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


class TestSettingsAndArticlePages:
    """설정 페이지와 게시글 페이지 관련 테스트 클래스"""

    @pytest.mark.data_required
    def test_password_with_trailing_space(self, driver):
        """
        테스트 시나리오: 비밀번호 뒤에 공백이 있는 경우 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "New Password" 입력 필드에 새 비밀번호("testpassword + 뒤에 공백 한 칸")를 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        "비밀번호는 앞/뒤 공백을 포함할 수 없습니다."와 같은 오류메시지가 표시 되어야한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            
            # 로그인 및 설정 페이지 접근
            login_page = LoginPage(driver)
            login_page.login(test_data["email"], test_data["password"])
            
            # 설정 페이지로 이동
            settings_page = SettingsPage(driver)
            settings_page.navigate_to_settings()
            
            # 새 비밀번호 입력 (뒤에 공백 추가)
            password_with_trailing_space = "testpassword "
            settings_page.enter_new_password(password_with_trailing_space)
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 오류 메시지 확인
            assert settings_page.is_error_message_displayed(), "오류 메시지가 표시되지 않았습니다."
            error_message = settings_page.get_error_message()
            assert "공백" in error_message or "space" in error_message.lower(), f"예상된 오류 메시지가 표시되지 않았습니다. 실제: {error_message}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_password_with_only_space(self, driver):
        """
        테스트 시나리오: 비밀번호에 공백만 입력한 경우 오류 메시지 확인
        
        사전 조건:
        - 로그인된 사용자 (currentUser)가 설정 페이지(/settings)에 접근.
        
        재현 절차:
        1. "New Password" 입력 필드에 새 비밀번호(" ", 빈 문자열만 입력)를 입력한다.
        2. "Update Settings" 버튼을 클릭한다.
        
        기대 결과:
        "비밀번호는 공백을 포함할 수 없습니다."와 같은 오류메시지가 표시 되어야한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["settings"]
            
            # 로그인 및 설정 페이지 접근
            login_page = LoginPage(driver)
            login_page.login(test_data["email"], test_data["password"])
            
            # 설정 페이지로 이동
            settings_page = SettingsPage(driver)
            settings_page.navigate_to_settings()
            
            # 새 비밀번호 입력 (공백만 입력)
            space_only_password = " "
            settings_page.enter_new_password(space_only_password)
            
            # 설정 업데이트 버튼 클릭
            settings_page.click_update_settings()
            
            # 오류 메시지 확인
            assert settings_page.is_error_message_displayed(), "오류 메시지가 표시되지 않았습니다."
            error_message = settings_page.get_error_message()
            assert "공백" in error_message or "space" in error_message.lower(), f"예상된 오류 메시지가 표시되지 않았습니다. 실제: {error_message}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
