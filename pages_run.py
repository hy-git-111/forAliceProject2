# pages_run.py

import os
from dotenv import load_dotenv
from prompts.pages import LOGIN_PAGE_PROMPT  # 필요한 프롬프트만 import
from ai_generate.claude_generate import generate_with_claude

load_dotenv()

PROMPT_LIST = [
    {
        "name": "login_page",
        "prompt": LOGIN_PAGE_PROMPT,
        "output_path": "qa-realworld-automation/pages/login_page.py"
    },
    # 이후 여기서 register_page, editor_page 등 확장 가능
]

def main():
    for task in PROMPT_LIST:
        print(f"\n🚀 Claude에게 '{task['name']}' 프롬프트 요청 중...\n")
        result = generate_with_claude(task["prompt"])
        print(f"✅ Claude 응답({task['name']}):\n\n{result[:300]}...\n")

        os.makedirs(os.path.dirname(task["output_path"]), exist_ok=True)
        with open(task["output_path"], "w", encoding="utf-8") as f:
            f.write(result)
        print(f"💾 저장 완료: {task['output_path']}")

if __name__ == "__main__":
    main()
