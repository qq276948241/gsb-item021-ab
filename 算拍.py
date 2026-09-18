import sys
from fractions import Fraction
from pathlib import Path

音符表 = {
    "全音符": Fraction(4),
    "二分音符": Fraction(2),
    "四分音符": Fraction(1),
    "八分音符": Fraction(1, 2),
    "十六分音符": Fraction(1, 4),
    "三十二分音符": Fraction(1, 8),
}
分母表 = {1, 2, 4, 8, 16, 32}


def fail(message):
    sys.stderr.write(message + "\n")
    raise SystemExit(1)


def 读拍号(text):
    parts = text.split("/")
    if len(parts) != 2:
        fail("拍号不对")
    num_s, den_s = parts
    if not num_s.isdigit() or not den_s.isdigit():
        fail("拍号不对")
    if num_s != str(int(num_s)) or den_s != str(int(den_s)):
        fail("拍号不对")
    num, den = int(num_s), int(den_s)
    if num < 1 or num > 16 or den not in 分母表:
        fail("拍号不对")
    return num, den


def main():
    path = Path("样例")
    if not path.is_file():
        fail("找不到样例")
    raw = path.read_text(encoding="utf-8")
    if raw == "":
        fail("样例不对")
    lines = raw.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    if not lines:
        fail("样例不对")
    rows = []
    for line in lines:
        parts = line.split(" ")
        if len(parts) != 3 or any(part == "" for part in parts):
            fail("样例不对")
        meter, name, dots = parts
        num, den = 读拍号(meter)
        if name not in 音符表:
            fail("音符不对")
        if dots not in {"0", "1", "2"}:
            fail("附点不对")
        beat = Fraction(4, den)
        bar = Fraction(num, 1) * beat
        factor = {0: Fraction(1), 1: Fraction(3, 2), 2: Fraction(7, 4)}[int(dots)]
        note = 音符表[name] * factor
        rows.append("一拍 %s 小节 %s 音符 %s" % (beat, bar, note))
    sys.stdout.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
