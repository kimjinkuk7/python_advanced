
time = input("표준시간 입력 >> ")
# 1. 분만 있는 경우 ex) 30분
# 2. 시간만 있는 경우 ex) 2시간
# 3. 시간과 분이 있는 경우 ex) 1시간 30분
result = 0
if time.find('시간') == -1 :
    # 분만 있는 경우
    result = int(time.split('분')[0])
else :
    if time.find('분') == -1 :
        # 시간만 있는 경우
        result = int(time.split('시간')[0]) * 60
    else :
        #시간과 분이 있는경우
        result = int(time.split()[0].split('시간')[0]) * 60 + int(time.split()[1].split('분')[0])

print(result)
