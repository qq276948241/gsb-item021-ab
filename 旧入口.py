import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "散页"))
from 拍号 import 一拍, 一小节
from 附点 import 音符时值

def main():
    raw = Path("样例").read_text(encoding="utf-8")
    lines = raw.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    rows = []
    for line in lines:
        拍号, 名字, 附点 = line.split(" ")
        分子, 分母 = 拍号.split("/")
        一拍长 = 一拍(分母)
        小节长 = 一小节(分子, 分母)
        音符长 = 音符时值(名字, int(附点))
        rows.append("一拍 %s 小节 %s 音符 %s" % (一拍长, 小节长, 音符长))
    sys.stdout.write("\n".join(rows) + "\n")

if __name__ == "__main__":
    main()
