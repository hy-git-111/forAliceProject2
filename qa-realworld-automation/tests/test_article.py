
class TestContentDisplay:
    """콘텐츠 표시 관련 테스트 클래스"""
    
    @pytest.mark.data_not_required
    def test_empty_popular_tags(self, driver):
        """
        테스트 시나리오: 게시글이 없을 때 Popular Tags 섹션 표시 확인
        
        사전 조건:
        등록된 게시글이 존재하지 않는다.
        
        재현 절차:
        1. Popular Tags 섹션을 확인한다.
        
        기대 결과:
        Popular Tags 제목만 노출되고, 태그 목록은 노출되지 않는다.
        """
        try:
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            
            # Popular Tags 섹션 제목 확인
            assert home_page.is_popular_tags_title_visible(), "Popular Tags 제목이 표시되지 않음"
            
            # 태그 목록이 비어있는지 확인
            assert home_page.is_popular_tags_list_empty(), "태그 목록이 비어있지 않음"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 주어진 JSON 형식의 테스트 케이스에 맞춰 5개의 테스트 함수를 구현했습니다:

1. `test_multi_session_login_sync`: 동일 브라우저의 다른 탭에서 로그인 상태 동기화 확인
2. `test_multi_session_logout_sync`: 동일 브라우저의 다른 탭에서 로그아웃 상태 동기화 확인
3. `test_account_deletion_ui`: UI를 통한 계정 삭제 기능 테스트
4. `test_loading_indicator_during_auth`: 인증 과정 중 로딩 인디케이터 표시 확인
5. `test_empty_popular_tags`: 게시글이 없을 때 Popular Tags 섹션 표시 확인

각 테스트는 POM 구조를 따르며, 로케이터를 import하여 사용하고, 테스트 데이터를 외부 JSON 파일에서 로드합니다. 또한 각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다.

# ===== 다음 배치 =====

테스트 케이스를 분석하고 POM 구조에 맞는 테스트 코드를 작성하겠습니다. 먼저 테스트 케이스를 요약하면:

1. Popular Tags 섹션에 여러 게시글에 등록된 태그가 노출되는지 확인
2. Popular Tags 섹션에 최대 10개의 태그만 노출되는지 확인
3. 긴 태그가 화면 레이아웃을 벗어나지 않고 정상 표시되는지 확인
4. Popular Tags 섹션의 태그 클릭 시 관련 게시글 목록 페이지로 이동하는지 확인
5. 게시글 작성 기능 테스트

이제 이 테스트 케이스에 맞는 테스트 코드를 작성하겠습니다:

```python
import os
import json
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 페이지 객체 임포트
from pages.home_page import HomePage
from pages.article_page import ArticlePage
from pages.editor_page import EditorPage
from pages.tag_page import TagPage

# 로케이터 임포트
from locators.home_locators import HomePageLocators as HomeLoc
from locators.article_locators import ArticlePageLocators as ArticleLoc
from locators.editor_locators import EditorPageLocators as EditorLoc
from locators.tag_locators import TagPageLocators as TagLoc

# 테스트 데이터 로드 함수
def load_test_data():
    """테스트 데이터 JSON 파일을 로드하는 함수"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


class TestPopularTags:
    """Popular Tags 기능 테스트 클래스"""
    
    @pytest.mark.data_required
    def test_popular_tags_display(self, driver):
        """
        테스트 시나리오: Popular Tags 섹션에 여러 게시글에 등록된 태그가 노출되는지 확인
        
        사전 조건:
        - 서로 다른 두 개 이상의 게시글에 동일한 태그가 등록되어 있다.
        """
        try:
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            
            # 홈페이지 접속
            home_page.navigate_to_home()
            
            # Popular Tags 섹션이 표시되는지 확인
            assert home_page.is_element_visible(HomeLoc.POPULAR_TAGS_SECTION), "Popular Tags 섹션이 표시되지 않습니다."
            
            # Popular Tags 목록에 태그가 있는지 확인
            tags = home_page.get_popular_tags()
            assert len(tags) > 0, "Popular Tags 목록에 태그가 없습니다."
            
            # 첫 번째 태그에 대한 게시글이 2개 이상인지 확인
            first_tag = tags[0]
            home_page.click_tag(first_tag)
            
            # 태그 페이지로 이동 후 게시글 수 확인
            tag_page = TagPage(driver)
            articles = tag_page.get_articles()
            assert len(articles) >= 2, f"'{first_tag}' 태그가 있는 게시글이 2개 이상 없습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_required
    def test_popular_tags_max_display(self, driver):
        """
        테스트 시나리오: Popular Tags 섹션에 최대 10개의 태그만 노출되는지 확인
        
        사전 조건:
        - 서로 다른 두 개 이상의 게시글에 동일한 태그가 등록되어 있다.
        - 태그의 총 개수가 10개 이상이다.
        """
        try:
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            
            # 홈페이지 접속
            home_page.navigate_to_home()
            
            # Popular Tags 섹션이 표시되는지 확인
            assert home_page.is_element_visible(HomeLoc.POPULAR_TAGS_SECTION), "Popular Tags 섹션이 표시되지 않습니다."
            
            # Popular Tags 목록에 태그가 최대 10개만 있는지 확인
            tags = home_page.get_popular_tags()
            assert len(tags) <= 10, f"Popular Tags 목록에 10개 이상의 태그({len(tags)}개)가 표시됩니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_required
    def test_long_tag_display(self, driver):
        """
        테스트 시나리오: 긴 태그가 화면 레이아웃을 벗어나지 않고 정상 표시되는지 확인
        
        사전 조건:
        - 서로 다른 두 개 이상의 게시글에 동일한 20자 이상 문자열의 태그가 등록되어 있다.
        - 일이삼사오육칠팔구십일이삼사오육칠팔구십
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()
            long_tag = test_data.get("long_tag", "일이삼사오육칠팔구십일이삼사오육칠팔구십")
            
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            
            # 홈페이지 접속
            home_page.navigate_to_home()
            
            # Popular Tags 섹션이 표시되는지 확인
            assert home_page.is_element_visible(HomeLoc.POPULAR_TAGS_SECTION), "Popular Tags 섹션이 표시되지 않습니다."
            
            # 긴 태그가 있는지 확인
            tags = home_page.get_popular_tags()
            long_tags = [tag for tag in tags if len(tag) >= 20]
            
            if not long_tags:
                pytest.skip("20자 이상의 긴 태그가 Popular Tags에 없습니다.")
            
            # 긴 태그의 표시 상태 확인 (레이아웃 벗어남 여부)
            tag_element = home_page.get_tag_element(long_tags[0])
            
            # 태그 요소의 위치와 크기 확인
            tag_rect = tag_element.rect
            container_rect = home_page.get_element(HomeLoc.POPULAR_TAGS_SECTION).rect
            
            # 태그가 컨테이너 내에 있는지 확인
            assert tag_rect['x'] >= container_rect['x'], "태그가 왼쪽 경계를 벗어납니다."
            assert tag_rect['x'] + tag_rect['width'] <= container_rect['x'] + container_rect['width'], "태그가 오른쪽 경계를 벗어납니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_required
    def test_tag_click_navigation(self, driver):
        """
        테스트 시나리오: Popular Tags 섹션의 태그 클릭 시 관련 게시글 목록 페이지로 이동하는지 확인
        
        사전 조건:
        - Popular Tags 섹션에 태그가 존재한다.
        """
        try:
            # 홈페이지 객체 생성
            home_page = HomePage(driver)
            
            # 홈페이지 접속
            home_page.navigate_to_home()
            
            # Popular Tags 섹션이 표시되는지 확인
            assert home_page.is_element_visible(HomeLoc.POPULAR_TAGS_SECTION), "Popular Tags 섹션이 표시되지 않습니다."
            
            # Popular Tags 목록에서 첫 번째 태그 클릭
            tags = home_page.get_popular_tags()
            assert len(tags) > 0, "Popular Tags 목록에 태그가 없습니다."
            
            selected_tag = tags[0]
            home_page.click_tag(selected_tag)
            
            # 태그 페이지로 이동했는지 확인
            tag_page = TagPage(driver)
            
            # 새 네비바가 표시되는지 확인
            assert tag_page.is_element_visible(TagLoc.TAG_NAVBAR), "태그 페이지의 네비바가 표시되지 않습니다."
            
            # 선택한 태그 이름이 네비바에 표시되는지 확인
            navbar_text = tag_page.get_navbar_text()
            assert selected_tag.lower() in navbar_text.lower(), f"선택한 태그 '{selected_tag}'가 네비바에 표시되지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_not_required
    def test_article_creation(self, driver):
        """
        테스트 시나리오: 게시글 작성 기능 테스트
        
        사전 조건:
        - 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()
            article_data = test_data.get("article", {
                "title": "제목",
                "description": "설명",
                "body": "내용",
                "tag": "태그"
            })
            
            # 에디터 페이지 객체 생성
            editor_page = EditorPage(driver)
            
            # 에디터 페이지로 이동
            editor_page.navigate_to_editor()
            
            # 게시글 제목 입력
            editor_page.enter_title(article_data["title"])
            
            # 게시글 설명 입력
            editor_page.enter_description(article_data["description"])
            
            # 게시글 본문 입력
            editor_page.enter_body(article_data["body"])
            
            # 태그 입력
            editor_page.enter_tag(article_data["tag"])
            
            # 게시글 발행 버튼 클릭
            editor_page.publish_article()
            
            # 게시글 상세 페이지로 이동했는지 확인
            article_page = ArticlePage(driver)
            
            # 게시글 제목이 표시되는지 확인
            assert article_page.is_element_visible(ArticleLoc.ARTICLE_TITLE), "게시글 제목이 표시되지 않습니다."
            
            # 게시글 제목이 입력한 제목과 일치하는지 확인
            article_title = article_page.get_article_title()
            assert article_title == article_data["title"], f"게시글 제목이 일치하지 않습니다. 예상: {article_data['title']}, 실제: {article_title}"
            
            # 게시글 본문이 표시되는지 확인
            assert article_page.is_element_visible(ArticleLoc.ARTICLE_BODY), "게시글 본문이 표시되지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 테스트 코드는 다음과 같은 특징을 가집니다:

1. POM 구조를 따르며 각 페이지 객체와 로케이터를 적절히 임포트합니다.
2. 각 테스트 케이스는 JSON 형식의 테스트 케이스와 일치하며, 명확한 docstring과 한글 주석을 포함합니다.
3. 테스트 데이터는 JSON 파일에서 로드하여 사용합니다.
4. 사전 조건에 데이터 세팅이 필요한 테스트는 @pytest.mark.data_required 데코레이터를 사용합니다.
5. 사전 조건에 데이터 세팅이 필요 없는 테스트는 @pytest.mark.data_not_required 데코레이터를 사용합니다.
6. 각 테스트는 try-except 구문으로 오류를 처리하고, 실패 시 명확한 메시지를 제공합니다.
7. 각 테스트는 독립적으로 실행 가능하며, 필요한 페이지 객체를 생성하고 사용합니다.

이 코드는 제공된 테스트 케이스를 모두 커버하며, 실행 가능한 형태로 작성되었습니다.

# ===== 다음 배치 =====

테스트 케이스를 분석해보니 모두 게시글 작성 페이지에서의 유효성 검증에 관한 테스트입니다. 각 테스트는 특정 필드를 비워두고 게시글 등록 시 에러가 발생하는지 확인하는 내용입니다. POM 구조에 맞춰 테스트 코드를 작성하겠습니다.

```python
import os
import json
import pytest
from pages.article_page import ArticlePage
from locators.article_locators import ArticlePageLocators as Loc
from config import ensureDirectoryExists, TEST_DATA_DIR

def load_test_data():
    """테스트 데이터 파일을 로드하는 함수"""
    data_file = os.path.join(TEST_DATA_DIR, "test_data.json")
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

class TestArticleCreation:
    """게시글 작성 페이지 테스트 클래스"""

    @pytest.mark.data_required
    def test_publish_article_with_all_fields_empty(self, driver):
        """
        테스트 시나리오: 모든 필드를 비워두고 게시글 등록 시 에러 발생 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. 모든 필드를 비워둔다.
        2. [Publish Article] 버튼을 클릭한다.
        
        기대 결과:
        - 에러 페이지로 이동되며 게시글은 등록되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_creation"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 게시글 작성 페이지로 이동 (이미 접근했다고 가정)
            
            # 모든 필드를 비워두고 게시글 등록 버튼 클릭
            article_page.click_publish_button()
            
            # 에러 페이지로 이동했는지 확인
            assert article_page.is_error_page_displayed(), "에러 페이지가 표시되지 않았습니다."
            
            # 게시글이 등록되지 않았는지 확인
            assert not article_page.is_article_published(), "게시글이 등록되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_publish_article_with_empty_title(self, driver):
        """
        테스트 시나리오: 제목 필드를 비워두고 게시글 등록 시 에러 발생 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. "Article Title" 필드를 비워둔다.
        2. [Publish Article] 버튼을 클릭한다.
        
        기대 결과:
        - 에러 페이지로 이동되며 게시글은 등록되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_creation"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 제목을 제외한 필드 입력
            article_page.enter_article_description(test_data["description"])
            article_page.enter_article_body(test_data["body"])
            article_page.enter_article_tags(test_data["tags"])
            
            # 게시글 등록 버튼 클릭
            article_page.click_publish_button()
            
            # 에러 페이지로 이동했는지 확인
            assert article_page.is_error_page_displayed(), "에러 페이지가 표시되지 않았습니다."
            
            # 게시글이 등록되지 않았는지 확인
            assert not article_page.is_article_published(), "게시글이 등록되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_publish_article_with_empty_description(self, driver):
        """
        테스트 시나리오: 설명 필드를 비워두고 게시글 등록 시 에러 발생 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. "What's this article about?" 필드를 비워둔다.
        2. [Publish Article] 버튼을 클릭한다.
        
        기대 결과:
        - 에러 페이지로 이동되며 게시글은 등록되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_creation"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 설명을 제외한 필드 입력
            article_page.enter_article_title(test_data["title"])
            article_page.enter_article_body(test_data["body"])
            article_page.enter_article_tags(test_data["tags"])
            
            # 게시글 등록 버튼 클릭
            article_page.click_publish_button()
            
            # 에러 페이지로 이동했는지 확인
            assert article_page.is_error_page_displayed(), "에러 페이지가 표시되지 않았습니다."
            
            # 게시글이 등록되지 않았는지 확인
            assert not article_page.is_article_published(), "게시글이 등록되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_publish_article_with_empty_body(self, driver):
        """
        테스트 시나리오: 본문 필드를 비워두고 게시글 등록 시 에러 발생 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. "Write your article (in markdown)" 필드를 비워둔다.
        2. [Publish Article] 버튼을 클릭한다.
        
        기대 결과:
        - 에러 페이지로 이동되며 게시글은 등록되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_creation"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 본문을 제외한 필드 입력
            article_page.enter_article_title(test_data["title"])
            article_page.enter_article_description(test_data["description"])
            article_page.enter_article_tags(test_data["tags"])
            
            # 게시글 등록 버튼 클릭
            article_page.click_publish_button()
            
            # 에러 페이지로 이동했는지 확인
            assert article_page.is_error_page_displayed(), "에러 페이지가 표시되지 않았습니다."
            
            # 게시글이 등록되지 않았는지 확인
            assert not article_page.is_article_published(), "게시글이 등록되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_publish_article_with_empty_tags(self, driver):
        """
        테스트 시나리오: 태그 필드를 비워두고 게시글 등록 시 에러 발생 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. "Enter tags" 필드를 비워둔다.
        2. [Publish Article] 버튼을 클릭한다.
        
        기대 결과:
        - 에러 페이지로 이동되며 게시글은 등록되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_creation"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 태그를 제외한 필드 입력
            article_page.enter_article_title(test_data["title"])
            article_page.enter_article_description(test_data["description"])
            article_page.enter_article_body(test_data["body"])
            
            # 게시글 등록 버튼 클릭
            article_page.click_publish_button()
            
            # 에러 페이지로 이동했는지 확인
            assert article_page.is_error_page_displayed(), "에러 페이지가 표시되지 않았습니다."
            
            # 게시글이 등록되지 않았는지 확인
            assert not article_page.is_article_published(), "게시글이 등록되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 테스트 코드는 다음과 같은 특징을 가집니다:

1. POM 구조를 따라 ArticlePage 클래스를 사용합니다.
2. 각 테스트는 JSON 형식의 테스트 케이스와 일치하며, 명확한 docstring을 포함합니다.
3. 모든 테스트는 @pytest.mark.data_required 데코레이터를 사용하여 데이터 세팅이 필요함을 표시합니다.
4. 로케이터는 import해서 사용합니다.
5. 테스트 데이터는 TEST_DATA_DIR에서 로드합니다.
6. 각 테스트는 try-except 구문으로 오류를 처리합니다.
7. 각 테스트는 독립적으로 실행 가능합니다.

테스트 데이터 파일(test_data.json)은 다음과 같은 형식으로 구성되어야 합니다:

```json
{
  "article_creation": {
    "title": "테스트 제목",
    "description": "테스트 설명",
    "body": "테스트 본문",
    "tags": "테스트,태그"
  }
}
```

# ===== 다음 배치 =====

먼저 테스트 케이스를 분석해보니, 모두 게시글 작성과 관련된 테스트들입니다. 이에 맞게 POM 구조를 활용한 테스트 코드를 작성하겠습니다.

```python
import os
import json
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 로케이터 임포트
from locators.article_locators import ArticlePageLocators as Loc
from pages.article_page import ArticlePage
from pages.home_page import HomePage
from config.config import TEST_DATA_DIR


def load_test_data():
    """테스트 데이터 로드 함수"""
    with open(os.path.join(TEST_DATA_DIR, 'test_data.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


class TestArticleCreation:
    """게시글 작성 관련 테스트 클래스"""

    @pytest.mark.data_required
    def test_duplicate_article_title_error(self, driver):
        """
        테스트 시나리오: 동일한 제목의 게시글 등록 시 오류 메시지 확인
        
        사전 조건: 사용자가 로그인 되어 있으며, 동일한 제목의 게시글이 이미 등록되어 있다.
        
        재현 절차:
        1. 게시글 작성 페이지로 이동한다.
        2. 이미 등록된 게시글과 정확히 동일한 제목으로 새로운 게시글을 작성 시도한다.
        3. [Publish Article] 버튼을 클릭한다.
        
        기대 결과: 동일한 제목으로는 게시글을 등록할 수 없다는 오류 메시지가 표시된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["duplicate_article"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            home_page = HomePage(driver)
            
            # 게시글 작성 페이지로 이동
            home_page.navigate_to_new_article_page()
            
            # 이미 등록된 게시글과 동일한 제목으로 게시글 작성
            article_page.create_article(
                title=test_data["title"],
                description=test_data["description"],
                body=test_data["body"],
                tags=test_data["tags"]
            )
            
            # 오류 메시지 확인
            assert article_page.is_error_message_displayed(), "오류 메시지가 표시되지 않았습니다."
            error_message = article_page.get_error_message()
            assert "title already exists" in error_message.lower(), f"예상된 오류 메시지가 표시되지 않았습니다. 실제: {error_message}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_markdown_rendering(self, driver):
        """
        테스트 시나리오: 마크다운 문법이 상세 페이지에서 정상적으로 렌더링 되는지 확인
        
        사전 조건: 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. "Article Title" 필드에 유효한 제목을 입력한다.
        2. "What's this article about?" 필드에 유효한 설명을 입력한다.
        3. "Write your article (in markdown)" 필드에 1자 이상의 유효한 본문 내용을 입력한다.
           - # 제목, **굵게**
        4. "Enter tags" 필드에 유효한 태그를 입력하고 Enter 키를 누른다
        5. [Publish Article] 버튼을 클릭한다.
        
        기대 결과: 입력한 마크다운 문법이 상세 페이지에서 정상적으로 렌더링 된다.
        - # 제목
        - **굵게**
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["markdown_article"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            home_page = HomePage(driver)
            
            # 게시글 작성 페이지로 이동
            home_page.navigate_to_new_article_page()
            
            # 마크다운 문법이 포함된 게시글 작성
            article_page.create_article(
                title=test_data["title"],
                description=test_data["description"],
                body=test_data["body"],
                tags=test_data["tags"]
            )
            
            # 마크다운 렌더링 확인
            # 제목 확인 (h1 태그로 렌더링)
            assert article_page.is_element_present(Loc.ARTICLE_H1_TAG), "마크다운 제목(h1)이 렌더링되지 않았습니다."
            h1_text = article_page.get_text(Loc.ARTICLE_H1_TAG)
            assert "제목" in h1_text, f"마크다운 제목이 올바르게 렌더링되지 않았습니다. 실제: {h1_text}"
            
            # 굵은 텍스트 확인 (strong 태그로 렌더링)
            assert article_page.is_element_present(Loc.ARTICLE_STRONG_TAG), "마크다운 굵은 텍스트(strong)가 렌더링되지 않았습니다."
            strong_text = article_page.get_text(Loc.ARTICLE_STRONG_TAG)
            assert "굵게" in strong_text, f"마크다운 굵은 텍스트가 올바르게 렌더링되지 않았습니다. 실제: {strong_text}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_tag_not_added_without_enter(self, driver):
        """
        테스트 시나리오: Enter 키를 누르지 않고 태그 입력 시 태그가 추가되지 않는지 확인
        
        사전 조건: 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. "Enter tags" 필드에 태그 내용을 입력한 후 Enter 키를 누르지 않고 [Publish Article] 버튼을 클릭한다.
        
        기대 결과: "Enter tags" 필드에 입력된 내용이 태그로 추가되지 않고 게시글이 등록된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["tag_without_enter"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            home_page = HomePage(driver)
            
            # 게시글 작성 페이지로 이동
            home_page.navigate_to_new_article_page()
            
            # 제목, 설명, 본문 입력
            article_page.fill_article_form(
                title=test_data["title"],
                description=test_data["description"],
                body=test_data["body"]
            )
            
            # 태그 입력 (Enter 키를 누르지 않음)
            article_page.input_tag_without_enter(test_data["tag"])
            
            # 게시글 등록
            article_page.click_publish_button()
            
            # 게시글 상세 페이지에서 태그 확인
            tags = article_page.get_article_tags()
            assert test_data["tag"] not in tags, f"Enter 키를 누르지 않았는데도 태그가 추가되었습니다: {tags}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_empty_tag_not_added(self, driver):
        """
        테스트 시나리오: 빈 태그가 추가되지 않는지 확인
        
        사전 조건: 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. "Enter tags" 필드에 아무것도 입력하지 않고 Enter 키를 누른다. (여러 번 반복)
        2. [Publish Article] 버튼을 클릭한다.
        3. 등록된 게시글을 확인한다.
        
        기대 결과: 빈 태그가 추가되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["empty_tag"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            home_page = HomePage(driver)
            
            # 게시글 작성 페이지로 이동
            home_page.navigate_to_new_article_page()
            
            # 제목, 설명, 본문 입력
            article_page.fill_article_form(
                title=test_data["title"],
                description=test_data["description"],
                body=test_data["body"]
            )
            
            # 빈 태그 입력 시도 (여러 번)
            for _ in range(3):
                article_page.input_tag_with_enter("")
            
            # 게시글 등록
            article_page.click_publish_button()
            
            # 게시글 상세 페이지에서 태그 확인
            tags = article_page.get_article_tags()
            assert len(tags) == 0, f"빈 태그가 추가되었습니다: {tags}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_tag_deletion(self, driver):
        """
        테스트 시나리오: 특정 태그만 삭제되는지 확인
        
        사전 조건: 사용자가 로그인 되어 있고, 게시글 작성 페이지에서 여러 개의 태그를 입력한 상태이다.
        
        재현 절차:
        1. 입력된 여러 태그 중 특정 태그 옆의 삭제 버튼(또는 아이콘)을 클릭한다.
        2. 남아있는 태그 목록을 확인한다.
        
        기대 결과: 클릭한 특정 태그만 삭제되고, 다른 태그들은 그대로 유지된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["tag_deletion"]
            
            # 페이지 객체 생성
            article_page = ArticlePage(driver)
            home_page = HomePage(driver)
            
            # 게시글 작성 페이지로 이동
            home_page.navigate_to_new_article_page()
            
            # 제목, 설명, 본문 입력
            article_page.fill_article_form(
                title=test_data["title"],
                description=test_data["description"],
                body=test_data["body"]
            )
            
            # 여러 태그 입력
            for tag in test_data["tags"]:
                article_page.input_tag_with_enter(tag)
            
            # 입력된 태그 목록 확인
            initial_tags = article_page.get_tag_list()
            assert len(initial_tags) == len(test_data["tags"]), f"모든 태그가 추가되지 않았습니다. 예상: {len(test_data['tags'])}, 실제: {len(initial_tags)}"
            
            # 특정 태그 삭제 (첫 번째 태그)
            tag_to_delete = test_data["tags"][0]
            article_page.delete_tag(tag_to_delete)
            
            # 삭제 후 태그 목록 확인
            remaining_tags = article_page.get_tag_list()
            assert len(remaining_tags) == len(test_data["tags"]) - 1, f"태그가 올바르게 삭제되지 않았습니다. 예상: {len(test_data['tags']) - 1}, 실제: {len(remaining_tags)}"
            assert tag_to_delete not in remaining_tags, f"삭제한 태그 '{tag_to_delete}'가 여전히 목록에 있습니다."
            
            # 다른 태그들은 그대로 유지되는지 확인
            for tag in test_data["tags"][1:]:
                assert tag in remaining_tags, f"삭제하지 않은 태그 '{tag}'가 목록에서 사라졌습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 테스트 코드는 POM 구조를 따르며, 주어진 JSON 형식의 테스트 케이스에 맞게 5개의 테스트 함수를 구현했습니다. 각 테스트는 다음과 같은 특징을 가집니다:

1. `test_duplicate_article_title_error`: 동일한 제목의 게시글 등록 시 오류 메시지 확인
2. `test_markdown_rendering`: 마크다운 문법이 상세 페이지에서 정상적으로 렌더링 되는지 확인
3. `test_tag_not_added_without_enter`: Enter 키를 누르지 않고 태그 입력 시 태그가 추가되지 않는지 확인
4. `test_empty_tag_not_added`: 빈 태그가 추가되지 않는지 확인
5. `test_tag_deletion`: 특정 태그만 삭제되는지 확인

각 테스트는 명확한 docstring과 한글 주석을 포함하고 있으며, 모든 테스트는 `@pytest.mark.data_required` 데코레이터를 사용하여 데이터 세팅이 필요함을 표시했습니다. 또한 try-except 구문을 사용하여 오류 처리를 구현했습니다.

이 코드는 기존의 POM 구조를 활용하며, 로케이터는 import하여 사용하고 있습니다. 테스트 데이터는 `load_test_data()` 함수를 통해 JSON 파일에서 로드합니다.

# ===== 다음 배치 =====

아래는 요청하신 테스트 케이스에 맞춰 작성한 Pytest 테스트 코드입니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하도록 작성했습니다.

```python
import os
import json
import pytest
from pages.article_page import ArticlePage
from pages.feed_page import FeedPage
from locators.article_locators import ArticlePageLocators as ArticleLoc
from locators.feed_locators import FeedPageLocators as FeedLoc

def load_test_data():
    """테스트 데이터 로드 함수"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

class TestArticleAndFeedFunctionality:
    """게시글 작성 및 피드 관련 기능 테스트 클래스"""

    @pytest.mark.data_required
    def test_duplicate_tags_not_allowed(self, driver):
        """
        테스트 시나리오: 동일한 태그 중복 입력 시 에러 메시지 확인
        
        사전 조건: 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. 여러 개의 동일한 태그를 입력한다.
        
        기대 결과:
        동일한 태그는 등록되지 않는다.
        - "이미 등록된 태그입니다." 에러문구 노출
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["duplicate_tags"]
            
            # 게시글 작성 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 동일한 태그 여러 번 입력
            for _ in range(3):  # 같은 태그 3번 입력
                article_page.add_tag(test_data["tag"])
            
            # 에러 메시지 확인
            assert article_page.is_element_visible(ArticleLoc.TAG_ERROR_MESSAGE)
            error_message = article_page.get_text(ArticleLoc.TAG_ERROR_MESSAGE)
            assert "이미 등록된 태그입니다" in error_message, f"예상 에러 메시지가 표시되지 않음: {error_message}"
            
            # 태그 목록에서 중복 태그가 한 번만 표시되는지 확인
            tag_count = article_page.count_tags_with_text(test_data["tag"])
            assert tag_count == 1, f"중복 태그가 여러 번 등록됨: {tag_count}번 발견됨"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_empty_fields_validation(self, driver):
        """
        테스트 시나리오: 공백만 입력된 게시글 등록 시도 시 오류 메시지 확인
        
        사전 조건: 사용자가 로그인 되어 있고, 게시글 작성 페이지에 접근한다
        
        재현 절차:
        1. 각 필드에 공백 문자만 입력한다.
        2. [Publish Article] 버튼을 클릭한다.
        
        기대 결과:
        공백만으로는 등록 불가하다는 오류 메시지가 표시된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["empty_fields"]
            
            # 게시글 작성 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 각 필드에 공백만 입력
            article_page.fill_article_form(
                title=test_data["title"],
                description=test_data["description"],
                body=test_data["body"]
            )
            
            # 게시글 등록 버튼 클릭
            article_page.click_publish_button()
            
            # 오류 메시지 확인
            assert article_page.is_element_visible(ArticleLoc.ERROR_MESSAGE_CONTAINER)
            error_messages = article_page.get_error_messages()
            
            # 각 필드별 오류 메시지 확인
            assert any("title" in msg.lower() for msg in error_messages), "제목 필드 오류 메시지가 표시되지 않음"
            assert any("description" in msg.lower() for msg in error_messages), "설명 필드 오류 메시지가 표시되지 않음"
            assert any("body" in msg.lower() for msg in error_messages), "본문 필드 오류 메시지가 표시되지 않음"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_not_required
    def test_empty_global_feed(self, driver):
        """
        테스트 시나리오: 게시글이 없을 때 Global Feed 페이지 확인
        
        사전 조건: 시스템에 등록된 게시글이 하나도 없다.
        
        재현 절차:
        1. Global Feed 페이지로 이동한다.
        
        기대 결과:
        "No articles are here... yet." 문구가 노출된다. 게시글 목록은 노출되지 않는다.
        """
        try:
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # Global Feed 페이지로 이동
            feed_page.navigate_to_global_feed()
            
            # "No articles" 메시지 확인
            assert feed_page.is_element_visible(FeedLoc.NO_ARTICLES_MESSAGE)
            message = feed_page.get_text(FeedLoc.NO_ARTICLES_MESSAGE)
            assert "No articles are here... yet." in message
            
            # 게시글 목록이 표시되지 않는지 확인
            assert not feed_page.is_element_visible(FeedLoc.ARTICLE_LIST_ITEMS)
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_global_feed_with_articles(self, driver):
        """
        테스트 시나리오: 게시글이 있을 때 Global Feed 페이지 확인
        
        사전 조건: 시스템에 등록된 게시글이 존재한다.
        
        재현 절차:
        1. Global Feed 페이지로 이동한다.
        
        기대 결과:
        등록된 게시글 목록이 노출된다.
        - 프로필 이미지
        - 타이틀
        - 서브타이틀
        """
        try:
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # Global Feed 페이지로 이동
            feed_page.navigate_to_global_feed()
            
            # 게시글 목록이 표시되는지 확인
            assert feed_page.is_element_visible(FeedLoc.ARTICLE_LIST_ITEMS)
            
            # 첫 번째 게시글의 요소들 확인
            first_article = feed_page.get_first_article()
            
            # 프로필 이미지 확인
            assert feed_page.is_element_visible_in_context(first_article, FeedLoc.ARTICLE_PROFILE_IMAGE)
            
            # 타이틀 확인
            assert feed_page.is_element_visible_in_context(first_article, FeedLoc.ARTICLE_TITLE)
            title = feed_page.get_text_from_context(first_article, FeedLoc.ARTICLE_TITLE)
            assert title, "게시글 타이틀이 비어있음"
            
            # 서브타이틀(설명) 확인
            assert feed_page.is_element_visible_in_context(first_article, FeedLoc.ARTICLE_DESCRIPTION)
            description = feed_page.get_text_from_context(first_article, FeedLoc.ARTICLE_DESCRIPTION)
            assert description, "게시글 설명이 비어있음"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_user_article_in_global_feed(self, driver):
        """
        테스트 시나리오: 로그인 사용자의 게시글이 Global Feed에 표시되는지 확인
        
        사전 조건: 사용자가 로그인 되어 있고, 해당 사용자가 작성한 게시글이 존재한다.
        
        재현 절차:
        1. Global Feed 페이지로 이동한다.
        2. 본인이 작성한 게시글이 목록에 노출되는지 확인한다.
        
        기대 결과:
        본인이 작성한 게시글이 Global Feed 목록에 정상적으로 노출된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["user_article"]
            username = test_data["username"]
            article_title = test_data["article_title"]
            
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # Global Feed 페이지로 이동
            feed_page.navigate_to_global_feed()
            
            # 게시글 목록이 표시되는지 확인
            assert feed_page.is_element_visible(FeedLoc.ARTICLE_LIST_ITEMS)
            
            # 사용자의 게시글이 목록에 있는지 확인
            found = feed_page.find_article_by_author_and_title(username, article_title)
            assert found, f"사용자({username})의 게시글({article_title})이 Global Feed에 표시되지 않음"
            
            # 게시글의 세부 정보 확인
            article = feed_page.get_article_by_title(article_title)
            
            # 작성자 이름 확인
            author_name = feed_page.get_text_from_context(article, FeedLoc.ARTICLE_AUTHOR)
            assert username in author_name, f"게시글 작성자가 일치하지 않음: {author_name} != {username}"
            
            # 프로필 이미지 확인
            assert feed_page.is_element_visible_in_context(article, FeedLoc.ARTICLE_PROFILE_IMAGE)
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 테스트 코드는 다음과 같은 특징을 가지고 있습니다:

1. JSON 형식의 테스트 케이스와 동일한 5개의 테스트 함수를 포함합니다.
2. 각 테스트는 POM 구조를 따르며 페이지 객체를 통해 요소에 접근합니다.
3. 로케이터는 import하여 사용하고 있습니다.
4. 각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다.
5. 데이터가 필요한 테스트에는 @pytest.mark.data_required 데코레이터를, 필요하지 않은 테스트에는 @pytest.mark.data_not_required 데코레이터를 사용했습니다.
6. 모든 테스트는 try-except 구문으로 감싸서 오류 처리를 하고 있습니다.
7. 테스트 데이터는 load_test_data() 함수를 통해 JSON 파일에서 로드합니다.

이 코드는 conftest.py와 config.py의 설정을 활용하며, 테스트 실패 시 스크린샷을 자동으로 저장하는 기능도 포함되어 있습니다.

# ===== 다음 배치 =====

테스트 케이스에 맞게 POM 구조를 따르는 Pytest 테스트 코드를 작성하겠습니다. 먼저 필요한 페이지 객체와 로케이터를 import하고, 테스트 데이터를 로드하는 함수를 구현한 후 각 테스트 케이스를 작성하겠습니다.

```python
import os
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 페이지 객체 import
from pages.feed_page import FeedPage
from pages.article_page import ArticlePage

# 로케이터 import
from locators.feed_locators import FeedPageLocators as Loc

def load_test_data():
    """테스트 데이터 파일을 로드하는 함수"""
    data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_data.json')
    with open(data_file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


class TestFeedPageFeatures:
    """Global Feed 페이지의 다양한 기능을 테스트하는 클래스"""

    @pytest.mark.data_required
    def test_subtitle_with_line_breaks(self, driver):
        """
        테스트 시나리오: 게시글 서브타이틀(About)에 줄바꿈이 포함된 경우 정상 노출 확인
        
        사전 조건:
        - 게시글 작성 시 서브타이틀(About)에 줄바꿈을 포함하여 등록한 게시글이 존재한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_with_line_breaks"]
            
            # Feed 페이지 객체 생성 및 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_global_feed()
            
            # 줄바꿈이 포함된 서브타이틀 확인
            article_description = feed_page.get_article_description(test_data["title"])
            
            # 줄바꿈이 HTML에서 <br> 태그나 CSS white-space 속성으로 처리되었는지 확인
            assert "\n" in article_description or "<br>" in article_description, \
                "서브타이틀에 줄바꿈이 정상적으로 적용되지 않았습니다."
            
            # 실제 화면에 줄바꿈이 적용되었는지 시각적으로 확인 (높이 체크)
            description_element = feed_page._find(Loc.ARTICLE_DESCRIPTION)
            element_height = description_element.size['height']
            
            # 줄바꿈이 있으면 일반적인 한 줄 높이보다 클 것으로 예상
            assert element_height > test_data["min_expected_height"], \
                f"서브타이틀 높이({element_height}px)가 예상 최소 높이({test_data['min_expected_height']}px)보다 작습니다. 줄바꿈이 적용되지 않았을 수 있습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_not_required
    def test_like_button_toggle(self, driver):
        """
        테스트 시나리오: 좋아요(하트) 버튼 토글 기능 확인
        
        사전 조건:
        - Global Feed에 게시글이 노출되어 있다.
        """
        try:
            # Feed 페이지 객체 생성 및 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_global_feed()
            
            # 첫 번째 게시글의 초기 좋아요 수 확인
            initial_likes_count = feed_page.get_likes_count_of_first_article()
            initial_button_state = feed_page.is_like_button_active_for_first_article()
            
            # 좋아요 버튼 클릭
            feed_page.click_like_button_for_first_article()
            
            # 좋아요 버튼 상태와 좋아요 수 변화 확인
            new_likes_count = feed_page.get_likes_count_of_first_article()
            new_button_state = feed_page.is_like_button_active_for_first_article()
            
            # 버튼 상태가 변경되었는지 확인
            assert initial_button_state != new_button_state, "좋아요 버튼 상태가 변경되지 않았습니다."
            
            # 좋아요 수가 적절히 변경되었는지 확인
            expected_count_diff = 1 if new_button_state else -1
            assert new_likes_count == initial_likes_count + expected_count_diff, \
                f"좋아요 수가 예상대로 변경되지 않았습니다. 초기: {initial_likes_count}, 변경 후: {new_likes_count}"
            
            # 다시 좋아요 버튼 클릭
            feed_page.click_like_button_for_first_article()
            
            # 좋아요 버튼 상태와 좋아요 수 다시 확인
            final_likes_count = feed_page.get_likes_count_of_first_article()
            final_button_state = feed_page.is_like_button_active_for_first_article()
            
            # 버튼 상태가 원래대로 돌아왔는지 확인
            assert final_button_state == initial_button_state, "좋아요 버튼 상태가 원래대로 돌아오지 않았습니다."
            
            # 좋아요 수가 원래대로 돌아왔는지 확인
            assert final_likes_count == initial_likes_count, \
                f"좋아요 수가 원래대로 돌아오지 않았습니다. 초기: {initial_likes_count}, 최종: {final_likes_count}"
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_tags_display(self, driver):
        """
        테스트 시나리오: 게시글에 등록된 태그 목록 노출 확인
        
        사전 조건:
        - 태그가 등록된 게시글이 Global Feed에 노출되어 있다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_with_tags"]
            
            # Feed 페이지 객체 생성 및 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_global_feed()
            
            # 특정 게시글의 태그 목록 확인
            article_tags = feed_page.get_article_tags(test_data["title"])
            
            # 등록된 모든 태그가 노출되는지 확인
            for tag in test_data["tags"]:
                assert tag in article_tags, f"태그 '{tag}'가 게시글에 노출되지 않았습니다."
            
            # 태그 개수가 일치하는지 확인
            assert len(article_tags) == len(test_data["tags"]), \
                f"노출된 태그 개수({len(article_tags)})가 예상 개수({len(test_data['tags'])})와 일치하지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_long_tag_display(self, driver):
        """
        테스트 시나리오: 긴 태그(20자 이상)가 레이아웃을 벗어나지 않고 정상 표시되는지 확인
        
        사전 조건:
        - 20자 이상인 태그가 등록된 게시글이 Global Feed에 노출되어 있다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_with_long_tag"]
            long_tag = "일이삼사오육칠팔구십일이삼사오육칠팔구십"  # 20자 이상 태그
            
            # Feed 페이지 객체 생성 및 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_global_feed()
            
            # 긴 태그가 있는 게시글 찾기
            article_element = feed_page.find_article_by_title(test_data["title"])
            assert article_element is not None, f"제목이 '{test_data['title']}'인 게시글을 찾을 수 없습니다."
            
            # 해당 게시글의 태그 요소 찾기
            tag_element = feed_page.find_tag_element_in_article(article_element, long_tag)
            assert tag_element is not None, f"태그 '{long_tag}'를 게시글에서 찾을 수 없습니다."
            
            # 태그 요소가 화면에 완전히 표시되는지 확인
            article_rect = article_element.rect
            tag_rect = tag_element.rect
            
            # 태그가 게시글 영역을 벗어나지 않는지 확인
            assert tag_rect['x'] >= article_rect['x'], "태그가 게시글 왼쪽 경계를 벗어났습니다."
            assert tag_rect['x'] + tag_rect['width'] <= article_rect['x'] + article_rect['width'], \
                "태그가 게시글 오른쪽 경계를 벗어났습니다."
            
            # 태그가 다음 게시글을 침범하지 않는지 확인
            next_article = feed_page.get_next_article_element(article_element)
            if next_article:
                next_article_rect = next_article.rect
                assert tag_rect['y'] + tag_rect['height'] <= next_article_rect['y'], \
                    "태그가 다음 게시글 영역을 침범했습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_pagination(self, driver):
        """
        테스트 시나리오: 페이지네이션 기능 확인
        
        사전 조건:
        - 시스템에 총 10개 초과의 게시글이 등록되어 있다.
        """
        try:
            # Feed 페이지 객체 생성 및 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_global_feed()
            
            # 1페이지에 노출되는 게시글 개수 확인
            articles_count = feed_page.get_articles_count_on_current_page()
            
            # 1페이지에 최대 10개의 게시글이 노출되는지 확인
            assert articles_count <= 10, f"1페이지에 {articles_count}개의 게시글이 노출되어 최대 10개를 초과했습니다."
            
            # 페이지네이션 컨트롤이 존재하는지 확인
            assert feed_page.is_pagination_control_visible(), "페이지네이션 컨트롤이 존재하지 않습니다."
            
            # 다음 페이지 버튼이 존재하는지 확인
            assert feed_page.is_next_page_button_visible(), "다음 페이지 버튼이 존재하지 않습니다."
            
            # 총 게시글 수가 10개를 초과하는지 확인 (페이지네이션이 필요한 조건)
            total_articles = feed_page.get_total_articles_count()
            assert total_articles > 10, f"총 게시글 수({total_articles})가 10개 이하이므로 페이지네이션이 필요하지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 주어진 5개의 테스트 케이스를 POM 구조에 맞게 구현했습니다. 각 테스트는 다음과 같은 특징을 가집니다:

1. **test_subtitle_with_line_breaks**: 게시글 서브타이틀에 줄바꿈이 포함된 경우 정상 노출되는지 확인
2. **test_like_button_toggle**: 좋아요 버튼 클릭 시 상태 토글 및 좋아요 수 증감 확인
3. **test_tags_display**: 게시글에 등록된 태그 목록이 정상적으로 노출되는지 확인
4. **test_long_tag_display**: 20자 이상의 긴 태그가 레이아웃을 벗어나지 않고 정상 표시되는지 확인
5. **test_pagination**: 페이지네이션 기능 및 1페이지당 최대 10개 게시글 노출 확인

각 테스트는 독립적으로 실행되며, 필요한 경우 테스트 데이터를 로드하여 사용합니다. 또한 모든 테스트는 적절한 docstring과 한글 주석을 포함하고 있으며, 예외 처리를 통해 테스트 실패 시 명확한 오류 메시지를 제공합니다.

# ===== 다음 배치 =====

아래는 요청하신 테스트 케이스에 맞게 작성한 Pytest 테스트 코드입니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하는 5개의 테스트를 구현했습니다.

```python
import os
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.feed_page import FeedPage
from locators.feed_locators import FeedPageLocators as Loc
from config import TEST_DATA_DIR

def load_test_data():
    """테스트 데이터 로드 함수"""
    data_file = os.path.join(TEST_DATA_DIR, "test_data.json")
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

class TestFeedPage:
    """Your Feed 페이지 테스트 클래스"""
    
    @pytest.mark.data_required
    def test_empty_feed_no_following(self, driver):
        """
        테스트 시나리오: 팔로우하는 사용자가 없을 때 Your Feed 페이지 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있으며, 팔로우하는 사용자가 한 명도 없다.
        
        재현 절차:
        1. Your Feed 페이지로 이동한다.
        
        기대 결과:
        - "No articles are here... yet." 문구가 노출된다.
        - 게시글 목록은 노출되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["empty_feed"]
            
            # Your Feed 페이지 객체 생성 및 페이지 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_your_feed()
            
            # 검증: "No articles are here... yet." 문구 노출 확인
            assert feed_page.is_empty_feed_message_displayed(), "빈 피드 메시지가 표시되지 않았습니다."
            
            # 검증: 게시글 목록이 노출되지 않는지 확인
            assert not feed_page.are_articles_displayed(), "게시글이 표시되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_required
    def test_empty_feed_with_following_no_articles(self, driver):
        """
        테스트 시나리오: 팔로우하는 사용자는 있으나 게시글이 없을 때 Your Feed 페이지 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있으며, 팔로우하는 사용자는 있으나 팔로우하는 사용자들이 게시글을 하나도 작성하지 않았다.
        
        재현 절차:
        1. Your Feed 페이지로 이동한다.
        
        기대 결과:
        - "No articles are here... yet." 문구가 노출된다.
        - 게시글 목록은 노출되지 않는다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["empty_feed_with_following"]
            
            # Your Feed 페이지 객체 생성 및 페이지 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_your_feed()
            
            # 검증: "No articles are here... yet." 문구 노출 확인
            assert feed_page.is_empty_feed_message_displayed(), "빈 피드 메시지가 표시되지 않았습니다."
            
            # 검증: 게시글 목록이 노출되지 않는지 확인
            assert not feed_page.are_articles_displayed(), "게시글이 표시되었습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_required
    def test_feed_with_articles(self, driver):
        """
        테스트 시나리오: 팔로우하는 사용자의 게시글이 있을 때 Your Feed 페이지 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있으며, 게시글을 작성한 사용자를 팔로우하고 있다.
        
        재현 절차:
        1. Your Feed 페이지로 이동한다.
        
        기대 결과:
        - 팔로우하는 사용자들이 작성한 게시글 목록이 노출된다.
          - 타이틀
          - 서브타이틀
          - 좋아요 버튼
          - 태그
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["feed_with_articles"]
            
            # Your Feed 페이지 객체 생성 및 페이지 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_your_feed()
            
            # 검증: 게시글 목록이 노출되는지 확인
            assert feed_page.are_articles_displayed(), "게시글이 표시되지 않았습니다."
            
            # 검증: 게시글 요소들이 모두 표시되는지 확인
            assert feed_page.check_article_elements(), "게시글 요소(타이틀, 서브타이틀, 좋아요 버튼, 태그)가 모두 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_required
    def test_like_button_toggle(self, driver):
        """
        테스트 시나리오: 좋아요 버튼 토글 기능 확인
        
        사전 조건:
        - Your Feed에 게시글이 노출되어 있다.
        
        재현 절차:
        1. 게시글 항목에 있는 좋아요(하트) 버튼을 클릭한다.
        2. 버튼 상태와 좋아요 수를 확인한다.
        3. 좋아요 버튼을 다시 클릭한다.
        4. 버튼 상태와 좋아요 수를 다시 확인한다.
        
        기대 결과:
        - 좋아요 버튼 클릭 시 상태(on/off)가 토글되며, 좋아요 수가 정상적으로 증감한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["like_button_toggle"]
            
            # Your Feed 페이지 객체 생성 및 페이지 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_your_feed()
            
            # 첫 번째 게시글의 초기 좋아요 상태와 수 확인
            initial_like_status = feed_page.is_article_liked(0)
            initial_like_count = feed_page.get_like_count(0)
            
            # 좋아요 버튼 클릭
            feed_page.toggle_like_button(0)
            
            # 좋아요 상태와 수 변경 확인
            new_like_status = feed_page.is_article_liked(0)
            new_like_count = feed_page.get_like_count(0)
            
            # 검증: 좋아요 상태가 토글되었는지 확인
            assert initial_like_status != new_like_status, "좋아요 상태가 변경되지 않았습니다."
            
            # 검증: 좋아요 수가 적절히 변경되었는지 확인
            expected_count_diff = 1 if new_like_status else -1
            assert new_like_count == initial_like_count + expected_count_diff, "좋아요 수가 올바르게 변경되지 않았습니다."
            
            # 좋아요 버튼 다시 클릭
            feed_page.toggle_like_button(0)
            
            # 좋아요 상태와 수 다시 확인
            final_like_status = feed_page.is_article_liked(0)
            final_like_count = feed_page.get_like_count(0)
            
            # 검증: 좋아요 상태가 원래대로 돌아왔는지 확인
            assert final_like_status == initial_like_status, "좋아요 상태가 원래대로 돌아오지 않았습니다."
            
            # 검증: 좋아요 수가 원래대로 돌아왔는지 확인
            assert final_like_count == initial_like_count, "좋아요 수가 원래대로 돌아오지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
    
    @pytest.mark.data_required
    def test_article_tags_display(self, driver):
        """
        테스트 시나리오: 게시글 태그 표시 확인
        
        사전 조건:
        - 태그가 등록된 게시글이 Your Feed에 노출되어 있다.
        
        재현 절차:
        1. Your Feed에서 해당 게시글 항목을 확인한다.
        
        기대 결과:
        - 해당 게시글에 등록된 태그 목록이 정상적으로 노출된다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["article_tags"]
            expected_tags = test_data.get("expected_tags", [])
            
            # Your Feed 페이지 객체 생성 및 페이지 이동
            feed_page = FeedPage(driver)
            feed_page.navigate_to_your_feed()
            
            # 검증: 게시글에 태그가 표시되는지 확인
            assert feed_page.are_article_tags_displayed(0), "게시글에 태그가 표시되지 않았습니다."
            
            # 검증: 예상 태그가 모두 표시되는지 확인 (테스트 데이터에 예상 태그가 있는 경우)
            if expected_tags:
                article_tags = feed_page.get_article_tags(0)
                for tag in expected_tags:
                    assert tag in article_tags, f"예상 태그 '{tag}'가 게시글에 표시되지 않았습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 테스트 코드는 JSON 형식의 테스트 케이스에 맞춰 5개의 테스트 함수를 구현했습니다:

1. `test_empty_feed_no_following`: 팔로우하는 사용자가 없을 때 Your Feed 페이지 확인
2. `test_empty_feed_with_following_no_articles`: 팔로우하는 사용자는 있으나 게시글이 없을 때 확인
3. `test_feed_with_articles`: 팔로우하는 사용자의 게시글이 있을 때 확인
4. `test_like_button_toggle`: 좋아요 버튼 토글 기능 확인
5. `test_article_tags_display`: 게시글 태그 표시 확인

각 테스트는 POM 구조를 따르며, 로케이터를 import하여 사용하고, 테스트 데이터를 로드하여 활용합니다. 또한 각 테스트에는 명확한 docstring과 한글 주석이 포함되어 있습니다.

# ===== 다음 배치 =====

아래는 요청하신 테스트 케이스에 맞춰 작성한 Pytest 테스트 코드입니다. POM 구조를 따르고 JSON 형식의 테스트 케이스와 일치하는 5개의 테스트를 구현했습니다.

```python
import os
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 페이지 객체 임포트
from pages.feed_page import FeedPage
from pages.article_page import ArticlePage

# 로케이터 임포트
from locators.feed_locators import FeedPageLocators as FeedLoc
from locators.article_locators import ArticlePageLocators as ArticleLoc

# 테스트 데이터 로드 함수
def load_test_data():
    """테스트 데이터 JSON 파일을 로드하는 함수"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'test_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


class TestArticleFeatures:
    """게시글 관련 기능 테스트 클래스"""

    @pytest.mark.data_required
    def test_long_tag_display(self, driver):
        """
        테스트 시나리오: 긴 태그(20자 이상)가 있는 게시글이 레이아웃을 벗어나지 않고 정상 표시되는지 확인
        
        사전 조건:
        - 20자 이상인 태그가 등록된 게시글이 Your Feed에 노출되어 있다.
        - 일이삼사오육칠팔구십일이삼사오육칠팔구십
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["long_tag_article"]
            
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # Your Feed 탭으로 이동
            feed_page.navigate_to_your_feed()
            
            # 긴 태그가 있는 게시글 확인
            tag_element = feed_page.find_article_with_tag(test_data["long_tag"])
            
            # 태그 요소가 존재하는지 확인
            assert tag_element is not None, "긴 태그를 가진 게시글을 찾을 수 없습니다."
            
            # 태그 요소가 화면에 보이는지 확인
            assert tag_element.is_displayed(), "태그 요소가 화면에 표시되지 않습니다."
            
            # 태그 요소의 위치와 크기 확인 (레이아웃 침범 여부 확인)
            tag_location = tag_element.location
            tag_size = tag_element.size
            
            # 부모 컨테이너 요소 찾기
            parent_container = feed_page._find(FeedLoc.ARTICLE_PREVIEW_CONTAINER)
            parent_location = parent_container.location
            parent_size = parent_container.size
            
            # 태그가 부모 컨테이너를 벗어나지 않는지 확인
            assert (tag_location['x'] + tag_size['width'] <= parent_location['x'] + parent_size['width']), \
                "태그가 가로 방향으로 레이아웃을 벗어납니다."
            
            # 다음 게시글 항목을 침범하지 않는지 확인
            next_article = feed_page.get_next_article_element(tag_element)
            if next_article:
                next_article_location = next_article.location
                assert (tag_location['y'] + tag_size['height'] <= next_article_location['y']), \
                    "태그가 다음 게시글 항목을 침범합니다."
                
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_pagination_control(self, driver):
        """
        테스트 시나리오: 게시글이 10개 초과일 때 페이지네이션 컨트롤이 정상 표시되는지 확인
        
        사전 조건:
        - 팔로우하는 사용자들이 작성한 총 게시글 수가 10개를 초과한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["pagination"]
            
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # Global Feed 탭으로 이동
            feed_page.navigate_to_global_feed()
            
            # 1페이지에 노출되는 게시글 개수 확인
            article_count = feed_page.get_article_count()
            
            # 최대 10개의 게시글이 노출되는지 확인
            assert article_count <= 10, f"1페이지에 {article_count}개의 게시글이 노출됩니다. 최대 10개여야 합니다."
            
            # 페이지네이션 컨트롤이 존재하는지 확인
            pagination_exists = feed_page.is_pagination_control_visible()
            
            # 페이지네이션 컨트롤이 존재해야 함
            assert pagination_exists, "페이지네이션 컨트롤이 존재하지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_not_required
    def test_article_navigation(self, driver):
        """
        테스트 시나리오: 피드에서 게시글 클릭 시 상세 페이지로 이동하는지 확인
        
        사전 조건:
        - Global Feed 또는 Your Feed에 게시글이 노출되어 있다.
        """
        try:
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # Global Feed 탭으로 이동
            feed_page.navigate_to_global_feed()
            
            # 첫 번째 게시글의 제목 가져오기
            first_article_title = feed_page.get_first_article_title()
            
            # 게시글이 존재하는지 확인
            assert first_article_title, "피드에 게시글이 존재하지 않습니다."
            
            # [Read more...] 버튼 클릭
            feed_page.click_read_more_button()
            
            # 게시글 상세 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # 상세 페이지로 이동했는지 확인 (제목 비교)
            article_title = article_page.get_article_title()
            
            # 피드에서 본 제목과 상세 페이지의 제목이 일치하는지 확인
            assert article_title == first_article_title, "게시글 상세 페이지로 이동하지 않았거나 다른 게시글로 이동했습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_own_article_edit_delete_buttons(self, driver):
        """
        테스트 시나리오: 본인이 작성한 게시글 상세 페이지에서 편집/삭제 버튼이 표시되는지 확인
        
        사전 조건:
        - 사용자가 로그인 되어 있으며, 본인이 작성한 게시글의 상세 페이지로 이동한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["own_article"]
            
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # 본인 프로필 페이지로 이동
            feed_page.navigate_to_profile(test_data["username"])
            
            # 첫 번째 게시글 클릭
            feed_page.click_first_article()
            
            # 게시글 상세 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # Edit Article 버튼이 표시되는지 확인
            edit_button_visible = article_page.is_edit_button_visible()
            
            # Delete Article 버튼이 표시되는지 확인
            delete_button_visible = article_page.is_delete_button_visible()
            
            # 두 버튼 모두 표시되어야 함
            assert edit_button_visible, "Edit Article 버튼이 표시되지 않습니다."
            assert delete_button_visible, "Delete Article 버튼이 표시되지 않습니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")

    @pytest.mark.data_required
    def test_other_article_no_edit_delete_buttons(self, driver):
        """
        테스트 시나리오: 다른 사용자가 작성한 게시글 상세 페이지에서 편집/삭제 버튼이 표시되지 않는지 확인
        
        사전 조건:
        - 사용자 A가 로그인 되어 있으며, 사용자 B가 작성한 게시글의 상세 페이지로 이동한다.
        """
        try:
            # 테스트 데이터 로드
            test_data = load_test_data()["other_article"]
            
            # 피드 페이지 객체 생성
            feed_page = FeedPage(driver)
            
            # 다른 사용자의 프로필 페이지로 이동
            feed_page.navigate_to_profile(test_data["other_username"])
            
            # 첫 번째 게시글 클릭
            feed_page.click_first_article()
            
            # 게시글 상세 페이지 객체 생성
            article_page = ArticlePage(driver)
            
            # Edit Article 버튼이 표시되지 않는지 확인
            edit_button_visible = article_page.is_edit_button_visible()
            
            # Delete Article 버튼이 표시되지 않는지 확인
            delete_button_visible = article_page.is_delete_button_visible()
            
            # 두 버튼 모두 표시되지 않아야 함
            assert not edit_button_visible, "Edit Article 버튼이 표시됩니다."
            assert not delete_button_visible, "Delete Article 버튼이 표시됩니다."
            
        except Exception as e:
            pytest.fail(f"테스트 실패: {e}")
```

이 코드는 다음과 같은 특징을 가지고 있습니다:

1. JSON 형식의 테스트 케이스와 동일한 5개의 테스트 함수를 구현했습니다.
2. 각 테스트는 POM 구조를 따르며 페이지 객체와 로케이터를 import하여 사용합니다.
3. 모든 테스트에 명확한 docstring과 한글 주석을 포함했습니다.
4. 데이터가 필요한 테스트에는 @pytest.mark.data_required 데코레이터를, 필요하지 않은 테스트에는 @pytest.mark.data_not_required 데코레이터를 사용했습니다.
5. 각 테스트는 try-except 구문으로 오류를 처리하고, 실패 시 pytest.fail()을 사용합니다.
6. 테스트 데이터는 load_test_data() 함수를 통해 JSON 파일에서 로드합니다.

이 코드는 conftest.py, config.py, 페이지 객체, 로케이터 등이 이미 구현되어 있다는 가정 하에 작성되었습니다.

# ===== 다음 배치 =====

다음은 요청하신 테스트 케이스에 맞춰 작성한 Pytest 테스트 코드입니다:

```python
import os
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.article_page import ArticlePage
from pages.edit_article_page import EditArticlePage
from pages.home_page import HomePage
from pages.settings_page import SettingsPage

from locators.article_locators import ArticlePageLocators as ArticleLoc
from locators.edit_article_locators import EditArticlePageLocators as EditLoc
from locators.home_locators import HomePageLocators as HomeLoc
from locators.settings_locators import SettingsPageLocators as SettingsLoc


def load_test_data():
    """테스트 데이터 로드 함수"""
    with open(os.path.join('data', 'test_data.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


@pytest.mark.data_required
def test_edit_article_button_navigates_to_edit_page(driver):
    """
    테스트 시나리오: 사용자가 자신의 게시글 상세 페이지에서 Edit Article 버튼을 클릭하면 
    게시글 수정 페이지로 이동하고 기존 내용이 입력 필드에 채워져 있는지 확인
    
    사전 조건: 사용자가 로그인 되어 있으며, 본인이 작성한 게시글의 상세 페이지로 이동한다.
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["article"]
        
        # 게시글 상세 페이지 객체 생성
        article_page = ArticlePage(driver)
        
        # 사전 조건: 사용자가 로그인되어 있고 본인 게시글 상세 페이지에 있음을 가정
        # 실제 테스트에서는 로그인 및 게시글 이동 로직이 필요할 수 있음
        
        # 1. [Edit Article] 버튼 클릭
        article_page.click_edit_article_button()
        
        # 게시글 수정 페이지 객체 생성
        edit_page = EditArticlePage(driver)
        
        # 기대 결과: 게시글 수정 페이지로 이동하며, 기존 게시글 내용이 입력 필드에 채워져 있음
        assert edit_page.is_edit_page_loaded(), "게시글 수정 페이지로 이동하지 않았습니다."
        
        # 기존 게시글 내용이 입력 필드에 채워져 있는지 확인
        assert edit_page.get_article_title() == test_data["title"], "게시글 제목이 입력 필드에 채워져 있지 않습니다."
        assert edit_page.get_article_description() == test_data["description"], "게시글 설명이 입력 필드에 채워져 있지 않습니다."
        assert edit_page.get_article_body() == test_data["body"], "게시글 본문이 입력 필드에 채워져 있지 않습니다."
        assert edit_page.get_article_tags() == test_data["tags"], "게시글 태그가 입력 필드에 채워져 있지 않습니다."
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")


@pytest.mark.data_required
def test_edit_article_content_successfully(driver):
    """
    테스트 시나리오: 사용자가 게시글 내용을 수정하고 Publish Article 버튼을 클릭하면
    게시글이 성공적으로 수정되고 상세 페이지에 수정된 내용이 반영되는지 확인
    
    사전 조건: 사용자가 로그인 되어 있으며, 본인이 작성한 게시글의 수정 페이지에 진입한 상태이다.
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["edit_article"]
        
        # 게시글 수정 페이지 객체 생성
        edit_page = EditArticlePage(driver)
        
        # 사전 조건: 사용자가 로그인되어 있고 게시글 수정 페이지에 있음을 가정
        
        # 1. 게시글 내용 수정
        edit_page.update_article_title(test_data["updated_title"])
        edit_page.update_article_description(test_data["updated_description"])
        edit_page.update_article_body(test_data["updated_body"])
        edit_page.update_article_tags(test_data["updated_tags"])
        
        # 2. [Publish Article] 버튼 클릭
        edit_page.click_publish_article_button()
        
        # 3. 수정된 게시글 상세 페이지로 이동
        article_page = ArticlePage(driver)
        
        # 기대 결과: 게시글 내용이 성공적으로 수정되고, 상세 페이지에 수정된 내용이 반영됨
        assert article_page.is_article_page_loaded(), "게시글 상세 페이지로 이동하지 않았습니다."
        assert article_page.get_article_title() == test_data["updated_title"], "수정된 게시글 제목이 반영되지 않았습니다."
        assert article_page.get_article_description() == test_data["updated_description"], "수정된 게시글 설명이 반영되지 않았습니다."
        assert article_page.get_article_body() == test_data["updated_body"], "수정된 게시글 본문이 반영되지 않았습니다."
        assert article_page.get_article_tags() == test_data["updated_tags"], "수정된 게시글 태그가 반영되지 않았습니다."
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")


@pytest.mark.data_required
def test_edit_article_with_empty_content(driver):
    """
    테스트 시나리오: 사용자가 게시글 내용을 모두 삭제하고 Publish Article 버튼을 클릭하면
    오류 메시지가 표시되는지 확인
    
    사전 조건: 사용자가 로그인 되어 있으며, 본인이 작성한 게시글의 수정 페이지에 진입한 상태이다.
    """
    try:
        # 게시글 수정 페이지 객체 생성
        edit_page = EditArticlePage(driver)
        
        # 사전 조건: 사용자가 로그인되어 있고 게시글 수정 페이지에 있음을 가정
        
        # 1. 기존 게시글 내용 전부 삭제
        edit_page.clear_article_title()
        edit_page.clear_article_description()
        edit_page.clear_article_body()
        edit_page.clear_article_tags()
        
        # 2. [Publish Article] 버튼 클릭
        edit_page.click_publish_article_button()
        
        # 기대 결과: 오류 메시지가 노출됨
        assert edit_page.is_error_message_displayed(), "오류 메시지가 표시되지 않았습니다."
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")


@pytest.mark.data_required
def test_delete_article_successfully(driver):
    """
    테스트 시나리오: 사용자가 자신의 게시글 상세 페이지에서 Delete Article 버튼을 클릭하면
    게시글이 성공적으로 삭제되는지 확인
    
    사전 조건: 사용자가 로그인 되어 있으며, 본인이 작성한 게시글의 상세 페이지로 이동한다.
    """
    try:
        # 테스트 데이터 로드
        test_data = load_test_data()["article"]
        
        # 게시글 상세 페이지 객체 생성
        article_page = ArticlePage(driver)
        
        # 사전 조건: 사용자가 로그인되어 있고 본인 게시글 상세 페이지에 있음을 가정
        
        # 삭제 전 게시글 제목 저장
        article_title = article_page.get_article_title()
        
        # 1. [Delete Article] 버튼 클릭
        article_page.click_delete_article_button()
        
        # 홈페이지로 리다이렉트 확인
        home_page = HomePage(driver)
        assert home_page.is_home_page_loaded(), "홈페이지로 리다이렉트되지 않았습니다."
        
        # 기대 결과: 게시글이 성공적으로 삭제되고 더 이상 노출되지 않음
        # 홈페이지에서 삭제된 게시글이 노출되지 않는지 확인
        assert not home_page.is_article_visible(article_title), "삭제된 게시글이 여전히 노출됩니다."
        
    except Exception as e:
        pytest.fail(f"테스트 실패: {e}")
