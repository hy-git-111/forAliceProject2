from ai_generate.claude_generate import generate_with_claude
from prompts.tests.article_prompt import ARTICLE_PROMPT
from prompts.tests.base_prompt import BASE_PAGE_PROMPT
from file_manage import save_data_append
import os
import json

PROMPT_LIST = [
    {
        "name": "config",
        "prompt": ARTICLE_PROMPT,
        "output_path": "qa-realworld-automation/tests/test_article_page.py"
    },
    # {
    #     "name": "config",
    #     "prompt": BASE_PAGE_PROMPT,
    #     "output_path": "qa-realworld-automation/tests/test_base_page.py"
    # },
    # {
    #     "name": "config",
    #     "prompt": HOME_PROMPT,
    #     "output_path": "qa-realworld-automation/tests/test_home_page.py"
    # },
    # {
    #     "name": "config",
    #     "prompt": LOGIN_PROMPT,
    #     "output_path": "qa-realworld-automation/tests/test_login_page.py"
    # },
    # {
    #     "name": "config",
    #     "prompt": PROFILE_PROMPT,
    #     "output_path": "qa-realworld-automation/tests/test_profile_page.py"
    # },
    # {
    #     "name": "config",
    #     "prompt": SETTINGS_PROMPT,
    #     "output_path": "qa-realworld-automation/tests/test_settings_page.py"
    # },
    # {
    #     "name": "config",
    #     "prompt": SIGNUP_PROMPT,
    #     "output_path": "qa-realworld-automation/tests/test_signup_page.py"
    # }
]
def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        # JSON 파일을 읽어서 바로 파싱
        json_data = json.load(f)
        print(f"{file_path} 파일 읽기 완료: {len(json_data)}개 항목")
    return json_data  # 이미 파싱된 객체 반환

# json 데이터를 5개씩 보내는 함수
def split_json_data_generator(prompt, data, batch_size=5):
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        print(f"배치 {i//batch_size + 1}: {len(batch)}개 항목")
        
        # 디버깅: 각 항목의 타입 확인
        for idx, item in enumerate(batch):
            try:
                # 안전하게 접근
                content_text = item.get("content", [{}])[0].get("text", "")
                lines = content_text.split("\n")
                test_id = lines[1].strip() if len(lines) > 1 else "테스트 ID 없음"
                print(f"  항목 {idx+1}: {test_id}")
            except Exception as e:
                print(f"  항목 {idx+1}: 처리 중 오류 - {e}")
                print(f"  항목 내용: {item}")

        batch_json = json.dumps(batch, ensure_ascii=False)
        yield generate_with_claude(prompt, batch_json)

def main():
    for task in PROMPT_LIST:
        print(f"\n🚀 Claude에게 '{task['name']}' 프롬프트 요청 중...\n")

        data = read_json("json_data/testcase.json")
        os.makedirs(os.path.dirname(task["output_path"]), exist_ok=True)
        
        for result in split_json_data_generator(task["prompt"], data):
            print(data)
            print(f"✅ Claude 응답({task['name']}):\n\n{result[:300]}...\n")

            with open(task["output_path"], "a", encoding="utf-8") as f:
                f.write(result)
        print(f"💾 저장 완료: {task['output_path']}")

if __name__ == "__main__":
    main()
    
