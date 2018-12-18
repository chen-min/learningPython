import re
language = 'PythonC#JavaPHPC#'
# 查找后再替换
# r = re.sub('C#', 'GO', language, 0)
# 有0表示会无限匹配下去, 1表示值匹配1个
# 常规替换可以用replace

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

# convert函数调用流程:
# 当正则表达式匹配到一个结果时,把匹配结果传给convert函数,convert返回结果用于替换.
r = re.sub('C#', convert, language)
print(r)
