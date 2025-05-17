from prompts.common import COMMON_CONTEXT

ARTICLE_PROMPT = COMMON_CONTEXT + """

다음 조건에 맞춰 Python + Selenium 기반의 Pytest 테스트코드 5건을 작성해주세요. 테스트는 모두 독립적이며 POM 구조를 따릅니다.

✅ 저장 위치: qa-realworld-automation/tests/test_article_page.py  
✅ 페이지 클래스명: ArticlesPage (PascalCase)  
✅ 함수명: test_[기능]_[시나리오] (camelCase)  
✅ 각 테스트에 명확한 docstring 및 간단한 한글 주석 포함  
✅ config.py, conftest.py, locator.py, base_page.py, page object는 이미 존재 (재작성 금지)  
✅ **공통코드와 로케이터는 import**해서 사용  
- 로케이터: from locators.settings_locators import ArticlePageLocators as Loc  
- 모든 요소는 Loc.XXX 형식으로 사용하고 클래스 내부에 직접 정의하지 마세요  

✅ 테스트 데이터:  
- qa-realworld-automation/data/test_data.json  
- 각 테스트는 고유 데이터 사용  
- load_test_data() 함수로 로드  

✅ 검증: 기본 assert 사용, 복잡한 경우 helper 함수 사용  
✅ 오류 처리: try-except 사용  
✅ 사전 조건에 "데이터 세팅" 필요 시: @pytest.mark.data_required  
✅ 사전 조건에 "데이터 세팅" 필요 시: @pytest.mark.data_not_required  
✅ 그대로 실행 가능해야 함

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
