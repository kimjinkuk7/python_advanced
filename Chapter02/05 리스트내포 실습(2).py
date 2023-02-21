a = ['오메가3', None, '비타민C500', None, '홍상절편']
b = []

for i in a:
    if i == None:
        b.append('')
    else:
        b.append(i)
print(b)

c = [i if i != None  else '' for i in a ]
print(c)