import re
a = 'C0C++7Java8C#9Python6Javascript'

# # re.findall('正则表达式', a)
r = re.findall('\d', a)  #\d表示数字1~9 \D表示非数字
print(r)

