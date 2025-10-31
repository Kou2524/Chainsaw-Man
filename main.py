import pyxel

pyxel.init(160, 120, title="Chainsaw-Man")

def update():
    # 今は何もしない。後でここに画面遷移とか書く
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(30, 40, "CHAINSAW-MAN", 7)
    pyxel.text(20, 70, "TAP SCREEN TO PLAY BGM", 10)

pyxel.run(update, draw)
