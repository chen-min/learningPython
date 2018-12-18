#字符集
import re
s = 'abc, acc, adc, aec, afc, ahc'
#找出中间一个字符是c或f
#使用[], 把要抽象出来的内容放在[]中
r = re.findall('a[cf]c',s)  #[^cf]表示匹配不是c也不是f的
#[c-f] 表示c~f全部匹配出来
print(r)
#出现在[]中的是或关系

