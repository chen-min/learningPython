#概括字符集


# 概括字符集
# \d  \D
# . 匹配除换行符之外所有其他字符
import re
# a = 'python123java456php'
# r = re.findall('[0-9]', a)
# # r = re.findall('\d', a)
# # \w 把数字和字母全部匹配出来
# print(r)



# import re
# a = 'python 11\t234242&\n'
# # \w 只匹配数字及字母， &等符号不能匹配
# # \w用字符集表示 [A-Za-z0-9_] --> \W 匹配除数字和字母外的内容
# # \s 匹配空格、 制表、换行等空白字符
# # \S 非空白字符
# r = re.findall('\s', a)
# print(r)


#数量词
# a = 'python 11java678php'
# r = re.findall('[a-z]{3}', a) #表示匹配的数量
# print(r)

#[a-z]{3,6} 表示3~6个

#数量词的贪婪与非贪婪
# 贪婪>>> 数量词在一个区间内，python尽可能多的取最大区间
# 贪婪[a-z]{3,6}
# 非贪婪[a-z]{3,6}?

# *  *前面的字符匹配0次或者无限多次
# a = 'pytho0python1pythonn2'
# r = re.findall('python*', a) #表示匹配的数量
# print(r)
# ['pytho', 'python', 'pythonn']

# + +前面的字符匹配1次或者无限多次
# ? ?前面的字符匹配0次或者1次
# [a-z]{3,6}能通过一个问号转为非贪婪 >>> 与此处意义不一样
import re
# 边界匹配
qq = '10000001'
#要求qq号在4~8位之间
# r = re.findall('\d{4,8}', qq)  #超过8位就会有问题
r = re.findall('^\d{4,8}$', qq)  #超过8位就会有问题

print(r)
01：12：21

