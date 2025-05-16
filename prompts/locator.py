# ✅ locator.py 생성용 프롬프트
LOCATOR_PROMPT = """
당신은 selenium + pytest 기반 QA 자동화 엔지니어입니다.
다음 우선순위 규칙에 따라 **모든 요소의 로케이터를 하나씩 추출해주세요**

우선순위 규칙:
1순위: ID
2순위: CSS Selector
3순위: XPATH (ID, CSS가 불가능할 때만 사용) 

출력 형식:
아래 파이썬 형식으로 각 페이지별 로케이터를 정리해서 출력해주세요.
문자 사이에 공백을 넣지 말고 일반적인 파이썬 코드로 출력하세요.
응답 시작, 종료에 대한 안내 없이 **코드만 주세요**

```python
# 웹 요소 로케이터 목록

## [페이지명(영문)]

페이지명(영문)_LOCATORS = {
    "username_input": "//input[@id='username']",
    "password_input": "//input[@id='password']",
    "login_button": "//button[@type='submit']",
    "error_message": "//div[@class='error-message']"
}
```

아래는 HTML입니다:
"""