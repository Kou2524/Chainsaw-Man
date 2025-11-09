import pyxel

pyxel.init(160, 120, title="Chainsaw-Man")
pyxel.mouse(True)

# 画像読み込み（title.png は同じ階層に置く／ファイル名の大文字小文字厳密）
pyxel.image(0).load(0, 0, "title.png")

def update():
    # ここでは何もしない。入力に依存せずタイトルを常時表示する。
    pass

def draw():
    # 背景クリア
    pyxel.cls(0)
    # 画像が160x120ならフルで表示。大きい場合は左上から160x120だけを表示。
    pyxel.blt(0, 0, 0, 0, 0, 160, 120)
    # 任意のガイド
    txt = "TAP TO PLAY BGM"
    x = (160 - len(txt) * 4) // 2
    pyxel.text(x, 110, txt, 7)
