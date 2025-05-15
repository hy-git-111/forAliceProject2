import gspread, os
from google.oauth2.service_account import Credentials

class PromptGenerator:
    # 워크시트 리스트를 반환하는 함수
    @staticmethod
    def get_worksheet_list():
        # 접근 권한 범위 설정
        SHEET_NAME = "Copy of 엘리스_2차_3조_팀프로젝트_사본"
        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets.readonly",
            "https://www.googleapis.com/auth/drive.readonly"
        ]

        # 서비스 계정 키 파일로 자격 증명 객체 생성
        creds = Credentials.from_service_account_file(
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
            scopes=SCOPES
        )

        client = gspread.authorize(creds)   # gspread 클라이언트 초기화

        # 스프레드시트 열기
        spreadsheet = client.open(SHEET_NAME)   # 구글 드라이브의 스프레드시트 이름
        worksheets = spreadsheet.worksheets()   # [Worksheet, Worksheet, ...]
        
        return worksheets
    
    # 워크시트 이름을 가져오는 함수
    @staticmethod
    def get_worksheet_name(worksheets):
        return [ws.title for ws in worksheets]
    
    # 워크시트 데이터(TC)를 가져오는 함수
    @staticmethod
    def get_worksheet_data(worksheet):   # 데이터 읽기
        header_rows = worksheet.row_values(9)[1:]
        target_rows = worksheet.get_all_records(head=9, expected_headers=header_rows)   # [{"Header1": "A1", "Header2": "B1", ...}, {...}]   
        target_rows = [row for row in target_rows if row.get("구분") == "자동화"]
        
        if not target_rows:
            return []

        return target_rows  # 리스트-딕셔너리 형태로 반환

    # 워크시트 데이터(TC)를 JSON으로 변환하는 함수
    @staticmethod
    def convert_worksheet_data_to_json(test_case):
        test_id = test_case.get("No.", "unnamed")
        title = test_case.get("Title", "")
        precondition = test_case.get("Precondition", "")
        steps = test_case.get("Steps", "")
        expected = test_case.get("Expected Result", "")

        content = f"""
테스트 ID: {test_id}
시나리오: {title}

사전 조건:
{precondition}

재현 절차:
{steps}
기대 결과:
{expected}
"""
        formatted_content = {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": content
                }
            ]
        }
        
        return formatted_content
