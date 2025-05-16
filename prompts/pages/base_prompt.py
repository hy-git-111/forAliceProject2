from prompts.common_pages import COMMON_PAGE_CONTEXT

BASE_PAGE_PROMPT = COMMON_PAGE_CONTEXT + """

🎯 목표:
- 모든 페이지에서 공통으로 상속받는 BasePage 클래스를 생성해주세요.
- 이 클래스는 qa-realworld-automation/pages/base_page.py에 위치합니다.

📌 구현 요구 사항:
- Selenium WebDriver를 생성자에서 받고, self.driver로 저장합니다.
- WebDriverWait을 활용한 명시적 대기 기반의 다음 메서드를 구현해주세요:

  - _click(locator): 요소 클릭
  - _send_keys(locator, text): 텍스트 입력
  - _get_text(locator): 요소 텍스트 가져오기
  - _find_element(locator): 단일 요소 반환
  - _find_elements(locator): 여러 요소 리스트 반환
  - get_page_title(): 현재 페이지 제목 반환
  - get_current_url(): 현재 URL 반환

📌 작성 규칙:
- 각 메서드는 try-except를 활용한 예외 처리를 포함해주세요.
- 실패 시 기본 오류 메시지를 출력하거나 로그를 찍어주세요.
- WebDriverWait은 기본 TIMEOUT 값을 사용하도록 구성해주세요.
- 모든 메서드에는 간단한 주석을 작성해주세요.
- 함수명은 camelCase, 클래스명은 PascalCase(BasePage)로 작성해주세요.
- 출력은 Python 코드만 작성해주세요. 설명은 모두 코드 내 주석으로 작성합니다.
"""