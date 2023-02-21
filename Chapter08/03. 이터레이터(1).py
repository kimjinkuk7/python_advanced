# 1. 이터러블 객체
# 문자열, 리스트, 튜플, 딕셔너리, range객체

iter_obj = [10, 20, 30].__iter__()
print(iter_obj)

# for i in iter_obj : 
#     print(i)

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())