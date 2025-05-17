"""
My Articles
게시글 10개 이상
게시글 10개 이하
data_required_below_ten_articles
1 : 많음
2 : 게시글만 8개
3~4 : 없음?
5 : 한개씩 있음, 팔로우x?
"""





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
from pages.article_page import ArticlePage

# 로케이터 임포트
from locators.settings_locators import SettingsPageLocators as SettingsLoc
from locators.profile_locators import ProfilePageLocators as ProfileLoc
from locators.signup_locators import SignupPageLocators as SignupLoc
from locators.editor_locators import EditorPageLocators as EditorLoc
from locators.login_locators import LoginPageLocators as LoginLoc
from locators.home_locators import HomePageLocators as HomeLoc
from locators.article_locators import ArticlePageLocators as ArticleLoc

# 유틸리티 임포트
from utils.logger import setup_logger
from config import config

logger = setup_logger(__name__)

def loadTestData():
    # 테스트 데이터 로드 함수
    dataFilePath = os.path.join(config.TEST_DATA_DIR, "test_data.json")
    with open(dataFilePath, 'r', encoding='utf-8') as file:
        return json.load(file)

def goToGlobalFeed(driver, testData):
    # 각 테스트 전에 로그인 상태로 설정하는 함수
    # 로그인 페이지로 이동
    loginPage = LoginPage(driver)
    loginPage.navigate()
    
    # 로그인
    loginPage.login(testData["email"], testData["password"])
    
    # Global Feed 탭 클릭
    homePage = HomePage(driver)
    homePage.clickGlobalFeedTab()
    
    # 게시글이 최소 1개 이상 있는지 확인
    articleTitles = homePage.getArticleTitles()
    assert len(articleTitles) >= 1, "Global Feed에 게시글이 없습니다."

class TestComment:
    # 게시글 댓글 관련 테스트 클래스
    
    @pytest.mark.data_required_below_ten_articles
    def testAddCommentToArticle(self, driver):
        # COM-AUTO-001: 테스트 시나리오: 게시글에 댓글 추가 기능 확인
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]
            
            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)
            
            # 첫 번째 게시글 클릭 (CSS 선택자 사용)
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()
            
            # 댓글 입력 및 게시
            article_page = ArticlePage(driver)
            comment_text = "테스트 댓글"
            article_page.addComment(comment_text)
            
            # 댓글이 성공적으로 추가되었는지 확인
            comments = article_page.getComments()
            assert comment_text in comments[-1], f"추가한 댓글 '{comment_text}'이 댓글 목록에 없습니다."
            
            # 댓글 카드의 요소들 확인
            last_comment_card = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_LAST_CARD)
            
            # 1. 댓글 텍스트 확인
            assert article_page.getComments() != []

            # 2. 프로필 이미지 확인
            profile_img = last_comment_card.find_element(*ArticleLoc.ARTICLE_COMMENT_PROFILE)
            assert profile_img.is_displayed(), "프로필 이미지가 표시되지 않았습니다."
            
            # 3. 닉네임 링크 확인
            author_link = last_comment_card.find_element(*ArticleLoc.ARTICLE_COMMENT_USERNAME)
            assert author_link.is_displayed(), "닉네임 링크가 표시되지 않았습니다."
            
            # 4. 작성 날짜 확인
            date_element = last_comment_card.find_element(*ArticleLoc.ARTICLE_COMMENT_DATE)
            assert date_element.is_displayed(), "작성 날짜가 표시되지 않았습니다."
            
            # 5. 휴지통 아이콘 확인
            trash_icon = last_comment_card.find_element(*ArticleLoc.ARTICLE_COMMENT_DELETE)
            assert trash_icon.is_displayed(), "휴지통 아이콘이 표시되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"댓글 추가 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required_below_ten_articles
    def testAddLongEnglishComment(self, driver):
        # COM-AUTO-002: 긴 영문 댓글 추가 시 레이아웃 확인
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]
            testComment = loadTestData()["longEnComment"]
            
            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)
            
            # 첫 번째 게시글 클릭 (CSS 선택자 사용)
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()
            
            # 긴 영문 댓글 입력 및 게시 (TEST를 30번 반복)
            article_page = ArticlePage(driver)
            article_page.addComment(testComment)
            time.sleep(1)  # 댓글이 추가될 때까지 잠시 대기
            
            # 댓글 카드와 컨테이너의 너비 확인
            last_comment_card = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_LAST_CARD)
            comment_container = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_CONTAINER)
            
            # 댓글 카드 너비가 컨테이너 너비보다 작거나 같은지 확인
            assert last_comment_card.size['width'] <= comment_container.size['width'], "댓글 카드 너비가 컨테이너 너비를 초과합니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"긴 영문 댓글 추가 테스트 실패: {str(e)}")
            raise
    
    @pytest.mark.data_required_below_ten_articles
    def testAddLongSpecialCharComment(self, driver):
        # COM-AUTO-003: 긴 특수문자 댓글 추가 시 레이아웃 확인
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]
            testComment = loadTestData()["longSpecialCharComment"]
            
            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)
            
            # 첫 번째 게시글 클릭 (CSS 선택자 사용)
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()
            
            # 긴 특수문자 댓글 입력 및 게시 ("!@#%"를 30번 반복)
            article_page = ArticlePage(driver)
            article_page.addComment(testComment)
            time.sleep(1)  # 댓글이 추가될 때까지 잠시 대기
            
            # 댓글 카드와 컨테이너의 너비 확인
            last_comment_card = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_LAST_CARD)
            comment_container = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_CONTAINER)
            
            # 댓글 카드 너비가 컨테이너 너비보다 작거나 같은지 확인
            assert last_comment_card.size['width'] <= comment_container.size['width'], "댓글 카드 너비가 컨테이너 너비를 초과합니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(f"긴 특수문자 댓글 추가 테스트 실패: {str(e)}")
            raise

    @pytest.mark.data_required_below_ten_articles
    def testLongCommentDisplay(self, driver):
        # COM-AUTO-004: 긴 댓글(120자 이상 숫자)이 정상적으로 표시되는지 테스트합니다.
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]
            testComment = loadTestData()["longNumComment"]
            
            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)

            # 첫 번째 게시글 클릭 (CSS 선택자 사용)
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()

            # 댓글 추가
            article_page = ArticlePage(driver)
            article_page.addComment(testComment)
            time.sleep(1)  # 댓글이 추가될 때까지 잠시 대기

            # 댓글 카드와 컨테이너의 너비 확인
            last_comment_card = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_LAST_CARD)
            comment_container = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_CONTAINER)
            
            # 댓글 카드 너비가 컨테이너 너비보다 같거나 작은지 확인
            assert last_comment_card.size['width'] <= comment_container.size['width'], "댓글 카드 너비가 컨테이너 너비보다 큽니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 긴 댓글 표시 테스트 성공")
        except Exception as e:
            pytest.fail(f"긴 댓글 표시 테스트 실패: {str(e)}")
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    @pytest.mark.data_required_below_ten_articles
    def testMultilineCommentDisplay(self, driver):
        # COM-AUTO-005: 여러 줄 댓글이 정상적으로 표시되는지 테스트합니다.
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]
            testComment = loadTestData()["newLineComment"]
            
            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)

            # 첫 번째 게시글 클릭 (CSS 선택자 사용)
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()

            # 댓글 추가
            article_page = ArticlePage(driver)
            article_page.addComment(testComment)
            
            # 마지막 댓글 카드의 텍스트 내용 확인
            last_comment_text = driver.find_element(*ArticleLoc.ARTICLE_COMMENT_LAST_CARD).get_attribute('innerHTML')

            # 줄바꿈이 HTML에서 <br> 태그나 두 개의 블록 요소로 표현되는지 확인
            assert "<br>" in last_comment_text or "<p>" in last_comment_text or "\n" in last_comment_text, "댓글에 줄바꿈이 표시되지 않습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 여러 줄 댓글 표시 테스트 성공")
        except Exception as e:
            pytest.fail(f"여러 줄 댓글 표시 테스트 실패: {str(e)}")
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    @pytest.mark.data_required_below_ten_articles
    def testDeleteComment(self, driver):
        # COM-AUTO-006: 댓글 삭제 기능을 테스트합니다.
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]
            testComment = loadTestData()["deleteComment"]
            
            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)

            # 첫 번째 게시글 클릭 (CSS 선택자 사용)
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()

            # 먼저 "삭제 대상" 댓글이 없으면 생성
            article_page = ArticlePage(driver)
            comments = article_page.getComments()
            delete_target_exists = False
            
            for i, comment in enumerate(comments):
                if testComment in comment:
                    delete_target_exists = True
                    break
            
            if not delete_target_exists:
                # "삭제 대상" 댓글 생성
                article_page.addComment(testComment)
            
            # 댓글 목록 다시 가져오기
            comments = article_page.getComments()
            
            # "삭제 대상" 댓글 찾기
            for i, comment in enumerate(comments):
                if testComment in comment:
                    # 해당 인덱스의 댓글 삭제
                    article_page.deleteCommentByIndex(i)
                    break
            
            # 삭제 후 댓글이 없는지 확인
            article_page = ArticlePage(driver)
            delete_target_elements = driver.find_elements(*ArticleLoc.ARTICLE_COMMENT_CARD)
            assert len(delete_target_elements) == 0, "댓글이 삭제되지 않았습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 댓글 삭제 테스트 성공")
        except Exception as e:
            pytest.fail(f"댓글 삭제 테스트 실패: {str(e)}")
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    @pytest.mark.data_not_required
    def testEmptyCommentSubmission(self, driver):
        # COM-AUTO-007: 빈 댓글 제출 시 동작을 테스트합니다.
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]
            
            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)

            # 첫 번째 게시글 클릭 (CSS 선택자 사용)
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()
            
            # 현재 댓글 개수 확인
            article_page = ArticlePage(driver)
            before_count = len(article_page.getComments())
            
            # 빈 댓글 제출
            article_page.addComment("")
            
            # 제출 후 댓글 개수 확인
            after_count = len(article_page.getComments())
            
            # 댓글 개수가 변하지 않았는지 확인
            assert before_count == after_count, "빈 댓글 제출 후 댓글 개수가 변경되었습니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 빈 댓글 제출 테스트 성공")
        except Exception as e:
            pytest.fail(f"빈 댓글 제출 테스트 실패: {str(e)}")
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise
    
    comment_list = loadTestData()["addComment"]

    @pytest.mark.parametrize("comment", comment_list)
    @pytest.mark.data_required
    def testNewCommentAddition(self, driver, comment):
        # COM-AUTO-008: 새 댓글 추가 시 기존 댓글이 유지되는지 테스트합니다.
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]

            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)

            # 첫 번째 게시글 클릭
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()

            # 기존 댓글 목록과 첫 댓글 저장
            article_page = ArticlePage(driver)
            before_comments = article_page.getComments()
            before_count = len(before_comments)
            first_comment_text = before_comments[0] if before_count > 0 else None

            # 댓글 작성
            article_page.addComment(comment)

            # 제출 후 댓글 목록 다시 조회
            after_comments = article_page.getComments()
            after_count = len(after_comments)

            # ✅ 검증 1: 댓글 수가 1 증가
            assert after_count == before_count + 1, f"댓글 개수가 증가하지 않았습니다. 이전: {before_count}, 이후: {after_count}"

            # ✅ 검증 2: 마지막 댓글 내용이 우리가 입력한 내용과 일치하는지
            last_comment_text = after_comments[-1]
            assert comment == last_comment_text, f"마지막 댓글이 예상과 다릅니다. 입력: '{comment}', 실제: '{last_comment_text}'"

            # ✅ 검증 3: 첫 번째 댓글이 여전히 존재하고 그대로인지
            if first_comment_text:
                current_first_comment_text = after_comments[0]
                assert current_first_comment_text == first_comment_text, \
                    f"첫 번째 댓글 내용이 변경되었습니다. 이전: '{first_comment_text}', 이후: '{current_first_comment_text}'"

            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 새 댓글 추가 테스트 성공")
        except Exception as e:
            pytest.fail(f"새 댓글 추가 테스트 실패: {str(e)}")
            logger.warning(f"❗ {inspect.currentframe().f_code.co_name} : {e}")
            raise

    @pytest.mark.data_not_required
    def testArticleCommentSectionForNonLoggedUser(self, driver):
        # COM-AUTO-009: 비로그인 상태에서 게시글 상세 페이지의 댓글 섹션 확인 테스트
        try:
            # 테스트 데이터 로드
            testData = loadTestData()["belowTenArticlesUser"]

            # 글로벌 피드로 이동
            goToGlobalFeed(driver, testData)

            # 첫 번째 게시글 클릭
            driver.find_element(*HomeLoc.HOME_ARTICLE_PREVIEW).click()
            
            # 1. 댓글 입력 영역 및 제출 버튼 없음 확인
            comment_textarea = driver.find_elements(*ArticleLoc.ARTICLE_COMMENT_INPUT)
            submit_button = driver.find_elements(*ArticleLoc.ARTICLE_POST_COMMENT_BUTTON)
            
            assert len(comment_textarea) == 0, "비로그인 상태에서 댓글 입력 영역이 표시됩니다."
            assert len(submit_button) == 0, "비로그인 상태에서 댓글 제출 버튼이 표시됩니다."
            
            logger.info(f"✅ {inspect.currentframe().f_code.co_name} 테스트 성공")
        except Exception as e:
            logger.error(f"❌ {inspect.currentframe().f_code.co_name} 테스트 실패: {str(e)}")
            pytest.fail(str(e))
    