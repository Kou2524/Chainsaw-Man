import pyxel

pyxel.init(160, 120, title="Chainsaw-Man")
pyxel.mouse(True)

# 画像読み込み（同階層・ファイル名の大小文字一致）
pyxel.image(0).load(0, 0, "title.png")

def update():
    pass

def draw():
    pyxel.cls(0)
    # 画像が160x120なら全面表示／大きい場合は左上から160x120だけ表示
    pyxel.blt(0, 0, 0, 0, 0, 160, 120)
    txt = "TAP TO PLAY BGM"
    x = (160 - len(txt) * 4) // 2
    pyxel.text(x, 110, txt, 7)

# ←これが必須！
pyxel.run(update, draw)
