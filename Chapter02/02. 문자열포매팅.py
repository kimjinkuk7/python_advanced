# format 매서드 사용
a = 'hello {2}{1}{0}'.format('apple', 'pineapple', 'pen')
print(a)

b = 'hello {}{}{}'.format('apple', 'pineapple', 'pen')
print(b)


# f-string
name1 = 'apple'
name2 = 'pineapple'
name3 = 'pen'
c = f'{name1} {name2} {name3}'
print(c)