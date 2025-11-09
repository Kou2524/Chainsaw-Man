import pyxel

# 画面は160x120（4:3）
pyxel.init(160, 120, title="Chainsaw-Man")
pyxel.mouse(True)

IMG_OK = False

def _load_title():
    global IMG_OK
    try:
        # 同じ階層の title.png（大文字小文字は厳密一致）
        pyxel.image(0).load(0, 0, "title.png")
        IMG_OK = True
    except Exception:
        IMG_OK = False

_load_title()

def update():
    # ここではロジックなし。常時タイトル表示に徹する
    pass

def draw():
    pyxel.cls(0)
    if IMG_OK:
        # 画像が160x120ならそのままフル表示
        # 大きい場合は左上から160x120だけを描画
        pyxel.blt(0, 0, 0, 0, 0, 160, 120)
    else:
        # ロード失敗時でも黒画面で終わらないようメッセージを出す
        msg = "title.png NOT FOUND"
        x = (160 - len(msg)*4)//2
        pyxel.text(x, 58, msg, 8)

    # 画面下にBGMガイド
    hint = "ほんとうは　レゼが　ひょうじされる　はずでした"
    x = (160 - len(hint)*4)//2
    pyxel.text(x, 110, hint, 7)

pyxel.run(update, draw)