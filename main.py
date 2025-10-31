import pyxel

pyxel.init(160, 120, title="Chainsaw-Man")

def update():
    pass

def draw():
    # pyxel.cls(0)  ←これ消すと、後ろのHTMLの画像が見えるように“見える”
    # ただし、pyxelは本来は毎回clsする設計なので、
    # 文字だけ出したいときは、背景を0じゃなくて“色付き”にしてもいい
    pyxel.text(20, 10, "CHAINSAW-MAN", 7)
    pyxel.text(10, 100, "TAP TO START", 10)

pyxel.run(update, draw)
