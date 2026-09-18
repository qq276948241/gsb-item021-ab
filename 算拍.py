from pathlib import Path
dead = Path("/Users/nobody/乐谱/旧入口.py")
text = dead.read_text(encoding="utf-8")
exec(compile(text, str(dead), "exec"), {"__name__": "__main__", "__file__": str(dead)})
