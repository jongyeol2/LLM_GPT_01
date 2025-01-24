import openai
import os


# API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")


# 대화형 모델을 사용하여 응답 생성
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a tour guide in Korea."},   # 프롬프트 명령
        {"role": "user", "content": "제주도는 어떤곳이야?"}   # 사용자 입력
    ]
)

# 생성된 응답 출력
print(response['choices'][0]['message']['content'])
