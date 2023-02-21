a = ['apple', 'watch', 'apolo', 'star', 'abocado']
b = []
for i in a:
    if i[0].lower() == 'a':
        b.append(i)

print(b)


c = [i for i in a if i[0].lower() == 'a']
print(c)