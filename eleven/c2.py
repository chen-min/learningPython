from enum import Enum

class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIGN = 1
    GREEN = 2
    BLACK = 3
    #BLACK = 4 重复定义也会报错
    RED = 4
#用枚举的方式表示类型, 可读性强  VIP.BLACK VIP.GREEN
print(VIP.BLACK)  #打印出VIP.BLACK
#VIP.BLACK = 10 #试图改,会报错

# 获取数值
print(VIP.BLACK.value)
print(VIP.BLACK.name)  #BLACK 获取标签名
print(VIP['GREEN']) #VIP.GREEN
#枚举类型,  枚举的名字, 枚举的值

#遍历
# for v in VIP:
#     print(v)

for v in VIP.__members__.items():
    print(v)
# ('YELLOW', <VIP.YELLOW: 1>)
# ('YELLOW_ALIGN', <VIP.YELLOW: 1>)
# ('GREEN', <VIP.GREEN: 2>)
# ('BLACK', <VIP.BLACK: 3>)
# ('RED', <VIP.RED: 4>)
for v in VIP.__members__:
    print(v)
# YELLOW
# YELLOW_ALIGN
# GREEN
# BLACK
# RED

a = 4
#  如何把数字转化为枚举类型
print(VIP(a))
