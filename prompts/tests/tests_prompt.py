TESTS_PROMPT = """

다음 조건에 맞춰 Python + Selenium 기반의 Pytest 테스트코드를를 작성해주세요.
테스트 코드의 개수는 반드시 JSON 형식의 테스트케이스와 동일해야 합니다.
테스트 내용은 무조건 JSON 형식의 테스트 케이스 내용과 일치해야 합니다.
테스트는 모두 독립적이며 POM 구조를 따릅니다.

✅ 저장 위치: qa-realworld-automation/tests/test_pages.py  
✅ 각 테스트에 명확한 docstring 및 간단한 한글 주석 포함  
✅ config.py, conftest.py, locator.py, base_page.py, page object는 이미 존재 (재작성 금지)  
✅ **공통코드와 로케이터는 import**해서 사용  
- 로케이터 예시: from locators.settings_locators import ArticlePageLocators as Loc  
- 모든 요소는 Loc.XXX 형식으로 사용하고 클래스 내부에 직접 정의하지 마세요  
- conftest: fixture, WAIT_SECONDS와 재시도 횟수인 RETRY_COUNT 등의 설정을 포함 
- config: 스크린샷/로그/테스트 데이터 디렉토리 생성 함수 포함 > ensureDirectoryExists(SCREENSHOT_DIR), ensureDirectoryExists(LOG_DIR), ensureDirectoryExists(TEST_DATA_DIR)

✅ 테스트 데이터:
- qa-realworld-automation/data/test_data.json  
- 각 테스트는 고유 데이터 사용

✅ 검증: 기본 assert 사용, 복잡한 경우 helper 함수 사용  
✅ 오류 처리: try-except 사용, 테스트 실패 시 conftest.py의 pytest_runtest_makereport() 훅 사용
✅ *사전 조건*에 *데이터 세팅* 필요 시: @pytest.mark.data_required  
✅ *사전 조건*에 *데이터 세팅* 필요 없을 시: @pytest.mark.data_not_required  
✅ 그대로 실행 가능해야 함
✅ 클래스명은 json 형식의 테스트 케이스 내용을 고려하여 작성


# 예시 코드:
```python
import os, json, pytest
from locators.settings_locators import ArticlePageLocators as Loc
from pages.article_page import ArticlePage

class ArticlePage(BasePage):
    def signUp(self, username, email, password):
        self._send_keys(Loc.signupUsernameInput, username)
        self._send_keys(Loc.signupEmailInput, email)
        self._send_keys(Loc.signupPasswordInput, password)
        self._click(Loc.signupSubmitButton)

@pytest.mark.data_required
def test_signUp_success(driver):
    try:
        test_data = load_test_data()["signup"]
        page = ArticlePage(driver)
        page.signUp(test_data["username"], test_data["email"], test_data["password"])
        assert page.verifySuccessfulSignUp(test_data["username"])
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")

```

다음은 JSON 형식의 테스트케이스 입니다.:
"""
