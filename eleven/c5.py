from enum import Enum
from enum import IntEnum, unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1 #避免相同的值
    BLACK = 3
    RED = 4
