import pyxel

pyxel.init(160, 120, title="Chainsaw-Man")

def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(50, 100, "PRESS START", 7)

pyxel.run(update, draw)
