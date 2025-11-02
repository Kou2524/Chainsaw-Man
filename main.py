import pyxel


def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.init(160, 120, title="Chainsaw-Man")
    pyxel.text(50, 100, "PRESS START", 7)

pyxel.run(update, draw)
