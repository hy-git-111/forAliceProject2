from prompts.common_pages import COMMON_PAGE_CONTEXT

BASE_PAGE_PROMPT = COMMON_PAGE_CONTEXT + """
# 목표:
- Python, Selenium 기반의 Pytest코드를 생성해주세요.

# 저장 위치:
- qa-realworld-automation/tests/test_article_page.py

# 필수 작성 규칙:
1. 반드시 POM (Page Object Model) 구조로 작성하세요.
2. 테스트케이스는 총 3건입니다. 반드시 테스트 코드도 3건을 작성하세요. 절대로 빠뜨리지 마세요.
3. 테스트 케이스는 서로 독립적이어야 합니다.
4. 이미 config.py, conftest.py, locator.py, base_page.py, page object는 생성되어 있습니다. 절대로 다시 작성하지 마세요.
5. **반드시 공통 코드와 로케이터를 import해서 작성**하세요


다음은 JSON 형식의 테스트케이스 입니다.:
"""