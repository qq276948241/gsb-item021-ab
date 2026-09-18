# 以这份为准
import sys
from fractions import Fraction
from pathlib import Path

音符表 = {
    "全音符": Fraction(1),
    "二分音符": Fraction(1, 2),
    "四分音符": Fraction(1, 4),
    "八分音符": Fraction(1, 8),
    "十六分音符": Fraction(1, 16),
    "三十二分音符": Fraction(1, 32),
}


def fail(message):
    sys.stderr.write(message + "\n")
    raise SystemExit(1)


def main():
    path = Path("样例")
    if not path.is_file():
        fail("没有样例")
    raw = path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    rows = []
    for line in lines:
        parts = line.split(" ")
        if len(parts) != 3:
            fail("拍子写错")
        meter, name, dots = parts
        bits = meter.split("/")
        if len(bits) != 2 or not bits[0].isdigit() or not bits[1].isdigit():
            fail("拍子写错")
        num, den = int(bits[0]), int(bits[1])
        if den == 0 or name not in 音符表 or dots not in {"0", "1", "2"}:
            fail("拍子写错")
        beat = Fraction(1, den)
        bar = Fraction(num, 1) * beat
        factor = {0: Fraction(1), 1: Fraction(3, 2), 2: Fraction(2)}[int(dots)]
        note = 音符表[name] * factor
        rows.append("一拍 %s 小节 %s 音符 %s" % (beat, bar, note))
    sys.stdout.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
