import gspread, os
from google.oauth2.service_account import Credentials

class PromptGenerator:
    # 워크시트 리스트를 반환하는 함수
    @staticmethod
    def get_worksheet_list():
        try:
            SHEET_NAME = "Copy of 엘리스_2차_3조_팀프로젝트_사본"
            SCOPES = [
                "https://www.googleapis.com/auth/spreadsheets.readonly",
                "https://www.googleapis.com/auth/drive.readonly"
            ]

            base_dir = os.path.dirname(os.path.abspath(__file__))
            creds_file = os.path.join(base_dir, "credentials.json")
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_file

            if not creds_file:
                raise ValueError("GOOGLE_APPLICATION_CREDENTIALS 환경 변수가 설정되지 않았습니다.")

            # 서비스 계정 키 파일로 자격 증명 객체 생성
            creds = Credentials.from_service_account_file(
                creds_file,
                scopes=SCOPES
            )
            client = gspread.authorize(creds)   # gspread 클라이언트 초기화

            # 스프레드시트 열기
            spreadsheet = client.open(SHEET_NAME)   # 구글 드라이브의 스프레드시트 이름
            worksheets = spreadsheet.worksheets()   # [Worksheet, Worksheet, ...]
                                        
            return worksheets
        except Exception as e:
            print(f"워크시트 목록을 가져오는 중 오류 발생: {e}")
            return []
        
    # 워크시트 이름을 가져오는 함수 > 추후 수정 필요
    @staticmethod
    def get_worksheet_name():
        try:
            worksheets = PromptGenerator.get_worksheet_list()
            return [ws.title for ws in worksheets]
        except Exception as e:
            print(f"워크시트 이름을 가져오는 중 오류 발생: {e}")
            return []
    
    # 워크시트 데이터(TC)를 가져오는 함수
    @staticmethod
    def get_worksheet_data():   # 데이터 읽기
        worksheets = PromptGenerator.get_worksheet_list()
        
        all_data = []
        
        for worksheet in worksheets[1:]:
            try:
                # 헤더가 9번째 행에 있다고 가정
                header_row = worksheet.row_values(9)
                if not header_row:
                    continue  # 헤더가 없는 경우 건너뛰기
                
                # 헤더 기반으로 모든 데이터 가져오기
                records = worksheet.get_all_records(head=9)
                
                # "구분" 컬럼이 "자동화"인 행만 필터링
                filtered_records = [row for row in records if row.get("구분") == "자동화"]
                
                # 워크시트 이름과 함께 데이터 저장
                for record in filtered_records:
                    record["worksheet_name"] = worksheet.title
                    all_data.append(record)
                    
            except Exception as e:
                print(f"워크시트 '{worksheet.title}'에서 데이터 추출 중 오류 발생: {e}")
                continue
                
        return all_data  # 리스트-딕셔너리 형태로 반환

    # 워크시트 데이터(TC)를 JSON으로 변환하는 함수
    @staticmethod
    def convert_worksheet_data_to_json(test_case:list):
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