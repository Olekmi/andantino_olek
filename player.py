import app
import ai
from tkinter import *
import tkinter as tk 

  
#the ai is 1 and enemy is -1
FIRST_HAND = 1
LAST_HAND = -1

class Bot(object):
    def __init__(self,label):
        self.label = label
        self.can = Tk.Canvas(self, width=650, height=550, bg="#60ace6")
        self.size = 18
        self.depth = 2
        
    def play(self,board,depth,alpha,beta):
        for i in range(len(board.possible_moves)):# .child(position,possible_moves): #i put the board as position and children are the possible moves
                new_child = board.child(board,board.possible_moves[i],board)
        score_eval, hex_closest = app.App().MinMax(new_child,depth-1, alpha,beta,False)
        
        app.App().draw_black(self.can,hex_closest,self.size)

class Human(object):
    def __init__ (self,label):
        self.label = label
        self.can = Tk.Canvas(self, width=650, height=550, bg="#60ace6")
        self.size = 18
    def play(self,board,event):
        xy = (event.x, event.y)
        hex_closest = app.App().closest_hex(xy)
        while(not app.App().click_posnew(hex_closest) in app.App().possible_move()):
            print("Action is not valid, try another one:")
        app.App().draw_white(self.can,board,self.size)