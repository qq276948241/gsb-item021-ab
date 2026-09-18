from fractions import Fraction

def 一拍(分母):
    return Fraction(1, int(分母))

def 一小节(分子, 分母):
    return Fraction(int(分子), 1) * 一拍(分母)
