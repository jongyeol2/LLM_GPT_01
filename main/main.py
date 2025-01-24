import openai
from dotenv import load_dotenv
import os


# .env 파일에서 환경 변수 로드
load_dotenv()

# API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# 프롬프트 명령
prompt = "You are a very scary computer teacher."

# 초기 대화 설정
message = [{"role": "system", "content": prompt}]

# 대화내용을 저장할 파일 설정
log_file = "chat_log.txt"

# 대화내용을 파일에 기록하는 함수 -> while 문 맨밑에 넣어서 대화할때마다 추가할거임
def log_chat(user_input, ai_response):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"사용자 : {user_input}\n")
        f.write(f"AI : {ai_response}\n")
        f.write("-----"*18 + "\n")

# exit가 입력되기 전까지 계속 대화할거에요
while True:
    user_input = input("사용자: ")

    if user_input.lower() == "exit":
        print("종료합니다.")
        break

    message.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=message
    )
    
    ai_response = response['choices'][0]['message']['content']

    print("AI: " + ai_response)
    
    # 대화내용 로그파일에 저장
    log_chat(user_input, ai_response)
