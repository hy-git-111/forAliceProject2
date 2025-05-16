from prompts.common_pages import COMMON_PAGE_CONTEXT

NEW_POST_PAGE_PROMPT = COMMON_PAGE_CONTEXT + """

🌟 문제:
- 새 게시글 작성 페이지(New Post)의 Page Object 클래스를 생성해주세요.
- 다음 메서드를 포함해주세요:
  - enterTitle()
  - enterDescription()
  - enterBody()
  - enterTags()
  - clickPublishButton()
  - writeNewPost(title, description, body, tags)

- 각 메서드는 BasePage의 메서드(_click, _send_keys 등)을 사용해 구현해주세요.

📁 저장 위치:
- qa-realworld-automation/pages/new_post_page.py

📌 로케이터 사용 규칙:
- 로케이터는 qa-realworld-automation/locators/new_post_page_locators.py에 정의되어 있다고 가정합니다.
- 다음과 같이 import해서 사용해야 합니다:

  from locators.new_post_page_locators import NewPostPageLocators as Loc

- 모든 요소는 Loc.TITLE_INPUT 등으로 사용하고, 클래스 내부에 직접 정의하지 마세요.

📊 기호 작성 규칙:
- 클래스명은 `NewPostPage`, PascalCase로 작성
- 함수/변수명은 camelCase로 작성
- 메서드 다음에 간단한 설명 주석 포함
- 명시적 대기 기능을 포함한 안정적인 코드 작성

📌 예시 코드 참고:

```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.new_post_page_locators import NewPostPageLocators as Loc

class NewPostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enterTitle(self, title):
        # 제목 입력
        self._send_keys(Loc.TITLE_INPUT, title)

    def enterDescription(self, description):
        # 설명 입력
        self._send_keys(Loc.DESCRIPTION_INPUT, description)

    def enterBody(self, body):
        # 본문 입력
        self._send_keys(Loc.BODY_INPUT, body)

    def enterTags(self, tags):
        # 태그 입력
        self._send_keys(Loc.TAGS_INPUT, tags)

    def clickPublishButton(self):
        # 게시 버튼 클릭
        self._click(Loc.PUBLISH_BUTTON)

    def writeNewPost(self, title, description, body, tags):
        # 새 게시글 작성 전체 프로세스
        self.enterTitle(title)
        self.enterDescription(description)
        self.enterBody(body)
        self.enterTags(tags)
        self.clickPublishButton()
        """