from tkinter import *
import tkinter as tk  
import app
import player

class Game:

    """
    class representing a game state
    """
    def __init__(self):
        """
        create a new game
        """
        self.board = app.App().create_hexes_board
        self.firsthand=player.Human(player.FIRST_HAND)
        self.lasthand=player.Bot(player.LAST_HAND)
        self.can = Tk.Canvas(self, width=650, height=550, bg="#60ace6")
        self.size = 18

    def initialize(self):
        if (input("do you would like to take the first hand?(y/n)")=='n'):
            self.firsthand = player.Bot(player.FIRST_HAND)
            self.lasthand = player.Human(player.LAST_HAND)

    def ply(self):
        """
        make a ply
        Parameters:
        """
        app.App().draw_white(self.can,self.board,self.size)
        is_first_hand_turn = True
        while 1>0: #in future should be added state of end game
            if (is_first_hand_turn):
                self.firsthand.play(self.board)
            else :
                self.lasthand.play(self.board)
            is_first_hand_turn = not is_first_hand_turn
        else:
            #some get state of the game telling who wins
            print ("You won!!")