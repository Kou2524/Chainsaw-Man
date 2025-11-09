import pyxel

# 画面は160x120（4:3）
pyxel.init(160, 120, title="Chainsaw-Man")

# マウス入力を使う（タップ=左クリック扱いになる）
pyxel.mouse(True)

# タイトル画像を読み込み（左上(0,0)に）
# ※ title.png が 160x120 ならそのままフィット
#    256x256 等でもロードはできるが、描画時に 160x120 だけ抜き出して表示する
pyxel.image(0).load(0, 0, "title.png")

started = False  # 初回タップで True にしてタイトル表示ON

def update():
    global started
    # 初回タップ/クリック or 任意キー押下で開始
    if not started:
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) or pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN):
            started = True

def draw():
    pyxel.cls(0)

    if not started:
        # 黒背景に「TAP TO START」表示（任意）
        msg = "TAP TO START"
        x = (160 - len(msg) * 4) // 2  # 4pxフォント幅のざっくりセンタリング
        pyxel.text(x, 58, msg, 7)
        return

    # タイトル画像を画面いっぱいに描画
    # 画像が160x120ならそのままフル表示
    # 画像が大きい場合でも、左上から160x120を切り出して描画（はみ出し防止）
    pyxel.blt(0, 0, 0, 0, 0, 160, 120)
