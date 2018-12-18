# 组 ()s
import re
a = 'PythonPythonPythonPythonPython'
#判断字符串是否包含3个python?  Python{3}表示单个字符n重复3次
r = re.findall('(Python){3}(JS)', a)    #可以接受多个分组

# [abc]  里面每个字符之间的关系是 "或", ()实质是 "且"


print(r)