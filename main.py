from app import *
import game

app =App()
app.mainloop()
g = game.Game()
g.initialize()
g.ply()
# root.mainloop()