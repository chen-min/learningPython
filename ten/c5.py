# 概括字符集
# \d  \D
import re
a = 'python123java456php'
r = re.findall('[0-9]', a)
# r = re.findall('\d', a)
# \w 把数字和字母全部匹配出来
print(r)
