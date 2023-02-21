# 데코레이터
# 함수의 앞, 뒤로 부가적인 기능을 넣어주고 싶을 때 사용
# 로깅, 권한확인

def logger(func):
    def wrapper(arg):
        print("함수 시작")
        func(arg) # 함수시작
        print("함수 끝")
    return wrapper

@logger
def print_hello(name):
    print("hello ",name)

@logger
def print_bye(name):
    print("bye ", name)

print_hello('진국')
print_bye('진국')