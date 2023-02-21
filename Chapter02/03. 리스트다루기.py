# 리스트 매서드
from enum import EnumMeta


a = [1,2,3,4,5,6]
a.append(7)
print(a)

a.pop()
print(a)

a.pop(1)
print(a)

a.remove(3)
print(a)

b = [5,9,87,71,23,6,8,1]
b.sort()
print(b)
b.sort(reverse=True)
print(b)

# enumerate

titles = ['제목1','제목2','제목3','제목4','제목5']

for index, title in enumerate(titles):
    print(f"{index} 번째 글입니다. 제목 : {title}")