import os
import platform
from pathlib import Path

# 기본 URL 설정 - 테스트 환경에 따라 변경 가능
BASE_URL = "http://localhost:4100"

# 브라우저 설정
BROWSER_TYPE = "chrome"  # 기본 브라우저 타입 (chrome, firefox, edge 등)
HEADLESS = False  # 헤드리스 모드 활성화 여부

# 타임아웃 설정
TIMEOUT = 10  # 기본 타임아웃 (초)
WAIT_SECONDS = 5  # 명시적 대기 시간 (초)
RETRY_COUNT = 3  # 재시도 횟수

# 스크린샷 설정
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
TAKE_SCREENSHOT_ON_FAILURE = True  # 실패 시 스크린샷 촬영 여부

# 로깅 설정
LOG_LEVEL = "INFO"  # 로그 레벨 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

# 운영체제별 WebDriver 경로 설정
def getDriverPath():
    """
    운영체제에 따라 적절한 WebDriver 경로를 반환합니다.
    """
    rootDir = Path(__file__).parent.parent
    driversDir = rootDir / "drivers"
    systemName = platform.system()

    if systemName == "Windows":
        driverPath = driversDir / "chromedriver.exe"
    elif systemName == "Darwin":
        driverPath = driversDir / "chromedriver"
    elif systemName == "Linux":
        driverPath = driversDir / "chromedriver"
    else:
        raise Exception(f"지원하지 않는 운영체제입니다: {systemName}")

    if not driverPath.exists():
        raise FileNotFoundError(f"WebDriver를 찾을 수 없습니다: {driverPath}")
    
    return str(driverPath)

# 테스트 환경 설정
class TestEnvironment:
    @staticmethod
    def getLocalConfig():
        return {
            "baseUrl": "http://localhost:4100",
            "timeout": 10,
            "headless": False
        }

    @staticmethod
    def getDevConfig():
        return {
            "baseUrl": "https://dev.example.com",
            "timeout": 15,
            "headless": True
        }

    @staticmethod
    def getStagingConfig():
        return {
            "baseUrl": "https://staging.example.com",
            "timeout": 20,
            "headless": True
        }

# 테스트 데이터 설정
TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_data")

# 디렉토리 생성 함수
def ensureDirectoryExists(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

# 필요한 디렉토리 생성
ensureDirectoryExists(SCREENSHOT_DIR)
ensureDirectoryExists(LOG_DIR)
ensureDirectoryExists(TEST_DATA_DIR)

# 🔽 외부에서 import할 수 있도록 명시
__all__ = [
    "BASE_URL",
    "BROWSER_TYPE",
    "HEADLESS",
    "TIMEOUT",
    "WAIT_SECONDS",
    "RETRY_COUNT",
    "SCREENSHOT_DIR",
    "TAKE_SCREENSHOT_ON_FAILURE",
    "LOG_LEVEL",
    "LOG_DIR",
    "getDriverPath",
    "TestEnvironment",
    "TEST_DATA_DIR"
]
