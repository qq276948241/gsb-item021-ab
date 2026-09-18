from fractions import Fraction

音符表 = {
    "全音符": Fraction(4),
    "二分音符": Fraction(2),
    "四分音符": Fraction(1),
    "八分音符": Fraction(1, 2),
    "十六分音符": Fraction(1, 4),
    "三十二分音符": Fraction(1, 8),
}

def 音符时值(名字, 附点):
    原长 = 音符表[名字]
    if 附点 == 0:
        return 原长
    if 附点 == 1:
        return 原长 * Fraction(3, 2)
    if 附点 == 2:
        return 原长 * 2
    raise ValueError("附点不收")
