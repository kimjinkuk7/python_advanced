# ^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$

import re

regex = re.compile('^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

datas = [
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.co.kr',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver'
]

for data in datas : 
    matchObj = regex.match(data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f"{data} {result}")