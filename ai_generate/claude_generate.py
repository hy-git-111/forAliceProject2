# automation/claude_generate.py

import os
import anthropic
from dotenv import load_dotenv

# 기존에 등록된 환경변수가 있어도 덮어쓰기
load_dotenv(override=True)

def generate_with_claude(prompt: str, llm_payload="") -> str:
    """
    Claude API를 사용하여 프롬프트 기반 응답을 생성합니다.
    :param prompt: Claude에게 보낼 사용자 프롬프트 문자열
    :return: Claude의 응답 텍스트
    """
    if llm_payload.strip():
        full_content = f"{prompt}\n\n---\n\n{llm_payload}"
    else:
        full_content = prompt  # 구분자 넣지 않음
    
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=8000,
        temperature=0.2,
        system="당신은 테스트 자동화 전문가입니다.",
        messages=[{"role": "user", "content": full_content}]
    )
    print("✅ Claude 호출 완료")
    return message.content[0].text.strip()
