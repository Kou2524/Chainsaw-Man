import pyxel

pyxel.init(160, 120, title="Chainsaw-Man")

# ここで画像を読み込む（0番の画像バンクに入れる）
pyxel.image(0).load(0, 0, "title.png")

def update():
    pass

def draw():
    pyxel.cls(0)  # ここは基本あったほうがいい
    # 読み込んだ画像を画面に貼る
    pyxel.blt(0, 0, 0, 0, 0, 160, 120)
    pyxel.text(20, 10, "CHAINSAW-MAN", 7)

pyxel.run(update, draw)
