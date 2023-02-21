# 1. 위치 가변 매개변수
from mimetypes import common_types


def print_fruots(*args):
    for arg in args:
        print(arg)

print_fruots('a', 'b', 'c', 'd')

# 2. 키워드 가변 매개변수
def comment_info(**kagrs):
    for ket, val in kagrs.items():
        print(f"{ket}, {val}")

comment_info(name='파린이', content='감사합니다.')
