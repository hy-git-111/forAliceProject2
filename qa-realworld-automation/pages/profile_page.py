from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators as Loc

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def getUsername(self):
        try:
            return self._get_text(Loc.PROFILE_USERNAME)
        except (TimeoutException, NoSuchElementException) as e:
            self._log_error(f"사용자 이름을 가져오는데 실패했습니다: {str(e)}")
            return None
    
    def getUserBio(self):
        try:
            return self._get_text(Loc.PROFILE_USER_BIO)
        except (TimeoutException, NoSuchElementException) as e:
            self._log_error(f"사용자 자기소개를 가져오는데 실패했습니다: {str(e)}")
            return None
    
    def clickFollowButton(self):
        try:
            self._click(Loc.PROFILE_FAVORITE_BTN)
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(Loc.PROFILE_FAVORITE_BTN, "Unfollow")
            )
            return True
        except (TimeoutException, NoSuchElementException) as e:
            self._log_error(f"Follow 버튼 클릭에 실패했습니다: {str(e)}")
            return False
    
    def clickUnfollowButton(self):
        try:
            self._click(Loc.PROFILE_FAVORITE_BTN)
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(Loc.PROFILE_FAVORITE_BTN, "Follow")
            )
            return True
        except (TimeoutException, NoSuchElementException) as e:
            self._log_error(f"Unfollow 버튼 클릭에 실패했습니다: {str(e)}")
            return False
    
    def isFollowing(self):
        try:
            button_text = self._get_text(Loc.PROFILE_FAVORITE_BTN)
            return "Unfollow" in button_text
        except (TimeoutException, NoSuchElementException) as e:
            self._log_error(f"팔로우 상태 확인에 실패했습니다: {str(e)}")
            return False

    def _log_error(self, message):
        print(f"[ProfilePage Error] {message}")
