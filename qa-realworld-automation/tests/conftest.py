
import os
import platform
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# config.py에서 설정 가져오기
from config import HEADLESS, TIMEOUT, BROWSER_TYPE, BASE_URL

@pytest.fixture(scope="session")
def base_url():
    """
    테스트에서 사용할 기본 URL을 제공하는 fixture
    """
    return BASE_URL

@pytest.fixture(scope="session")
def driver(request):
    """
    Selenium WebDriver를 설정하고 제공하는 fixture
    세션 스코프로 모든 테스트에서 동일한 브라우저 인스턴스 사용
    """
    # 브라우저 타입에 따른 WebDriver 설정
    if BROWSER_TYPE.lower() == "chrome":
        # Chrome 옵션 설정
        chrome_options = Options()
        
        # 헤드리스 모드 설정
        if HEADLESS:
            chrome_options.add_argument("--headless")
        
        # 기타 Chrome 옵션 설정
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # 운영체제에 따른 ChromeDriver 설정
        service = Service(ChromeDriverManager().install())
        
        # WebDriver 인스턴스 생성
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        # 기본적으로 Chrome 사용 (다른 브라우저 지원 시 여기에 추가)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    
    # 암시적 대기 설정
    driver.implicitly_wait(TIMEOUT)
    
    # 브라우저 창 최대화
    driver.maximize_window()
    
    # 테스트 종료 후 정리 함수
    def finalize():
        driver.quit()
    
    # 테스트 종료 시 정리 함수 등록
    request.addfinalizer(finalize)
    
    return driver

@pytest.fixture
def wait(driver):
    """
    명시적 대기를 위한 WebDriverWait 객체를 제공하는 fixture
    """
    return WebDriverWait(driver, TIMEOUT)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    테스트 실패 시 스크린샷을 저장하는 훅
    """
    # 실행 결과 가져오기
    outcome = yield
    report = outcome.get_result()
    
    # 테스트 실패 시 스크린샷 저장
    if report.when == "call" and report.failed:
        try:
            # driver fixture 가져오기
            driver = item.funcargs.get("driver")
            if driver:
                # 스크린샷 저장 디렉토리 생성
                screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)
                
                # 스크린샷 파일명 생성 (타임스탬프 포함)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.name
                screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
                
                # 스크린샷 저장
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

@pytest.fixture
def navigate_to(driver, base_url):
    """
    특정 경로로 이동하는 헬퍼 fixture
    """
    def _navigate_to(path=""):
        url = f"{base_url}/{path.lstrip('/')}"
        driver.get(url)
        return driver
    
    return _navigate_to
