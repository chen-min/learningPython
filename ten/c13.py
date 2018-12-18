import re
#模式
language = 'PythonC#\nJavaPHP'
# 如何忽略大小写 >>> re.I
# 多个模式之间使用 | 连接在一起  >>> 表示的是且关系
# re.S 表示 . 号匹配所有字符, 包括换行符
# r = re.findall('c#.{1}', language, re.I )
r = re.findall('c#.{1}', language, re.I | re.S)
print(r)

