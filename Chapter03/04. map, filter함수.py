# 1. map 함수
# - 사용 이유
# 기존 리스트를 수정해서 새로운 리스트를 만들 때

#  - 사용 방법
# mpa(함수, 순서가 있는 자료형)

print(list(map(int, ['3', '4', '5', '6'])))

# - 예제
# 리스트 모든 요소의 공백 제거

itmes = [' 로지덱 마우스 ', '    앱솔 키보드   ']
print(list(map(lambda x : x.strip(), itmes)))

# 2. filler 함수
# - 사용 이유
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때

print(list(filter(lambda x : x < 0, [-3, -2, 0, 2, 3])))

# - 예제
# 리스트에서 길이가 3이하인 문자들만 필터링
stlist = ['aaaa', 'aaa', 'aa', 'a', 'aaaaa']
print(list(filter(lambda x : len(x) <= 3, stlist)))