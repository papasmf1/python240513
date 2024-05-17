import re

def check_email(email):
    # 이메일 패턴 정의
    # ^ : 문자열의 시작을 의미합니다.
    # [a-zA-Z0-9._%+-]+ : 소문자, 대문자, 숫자, '.', '_', '%', '+', '-'가 하나 이상 오는 것을 의미합니다.
    # @ : '@' 문자가 반드시 포함되어야 함을 의미합니다.
    # [a-zA-Z0-9.-]+ : 소문자, 대문자, 숫자, '.', '-'가 하나 이상 오는 것을 의미합니다.
    # \. : '.' 문자가 반드시 포함되어야 함을 의미합니다.
    # [a-zA-Z]{2,} : 소문자와 대문자가 최소 2개 이상 오는 것을 의미합니다.
    # $ : 문자열의 끝을 의미합니다.
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # 패턴과 이메일 주소 매칭
    # re.search() 함수는 주어진 패턴과 이메일 주소를 비교하여 매칭되는지 확인합니다.
    match = re.search(pattern, email)
    
    # 매칭 결과 반환 (True 또는 False)
    # match 객체가 None이 아니면 True, None이면 False를 반환합니다.
    return bool(match)

# 샘플 데이터
emails = [
    "test.email@example.com",      # 유효한 이메일
    "user@subdomain.example.com",  # 유효한 이메일
    "user+name@example.co.in",     # 유효한 이메일
    "user.name@domain.com",        # 유효한 이메일
    "user_name@domain.com",        # 유효한 이메일
    "username@domain.co",          # 유효한 이메일
    "username@domaincom",          # 유효하지 않은 이메일 (도메인 최상위 부분이 없음)
    "user@domain.com.",            # 유효하지 않은 이메일 (마지막에 점이 있음)
    "@domain.com",                 # 유효하지 않은 이메일 (사용자 이름이 없음)
    "user@.com"                    # 유효하지 않은 이메일 (도메인 이름이 없음)
]

# 이메일 체크
for email in emails:
    # 각 이메일 주소에 대해 check_email 함수를 호출하여 유효성을 검사합니다.
    result = check_email(email)
    # 이메일 주소와 유효성 검사 결과를 출력합니다.
    print(f"Email: {email}, Valid: {result}")
