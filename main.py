import pyxel

pyxel.init(160, 120, title="Sanity Check")
pyxel.mouse(True)

def update():
    pass

def draw():
    pyxel.cls(pyxel.frame_count % 16)
    msg = "PYXEL OK"
    x = (160 - len(msg)*4)//2
    pyxel.text(x, 58, msg, 7)

pyxel.run(update, draw)