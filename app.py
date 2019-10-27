from tkinter import *
import tkinter as tk
# import pygame
# from pygame.locals import *
from math import cos, sin,radians,sqrt,inf
import math
import random
import collections 
from hexagon import *
import numpy
from numpy import concatenate
import draw, config, game_rules, ai
from ai import *
import board
# import sys
# sys.stdout = open('stdout.txt', 'w') #to save in an external file
print("How to play? Hexes with black borders indicate possible moves. To activate AI's turn you also must click on one of them and then he will choose his move.")

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Andantino - Hexagon Grid")
        self.can = Canvas(self, width=config.width, height=config.height, bg= "#60ace6")
        self.depth_game = config.depth
        self.size = config.size
        self.state = 0
        self.game_type = 0
        self.can.pack(padx=0)
        self.hexagons = []
        self.hexagons_board = []
        self.hexagons_white = []
        self.hexagons_black = []
        self.neigh_append = []
        self.hex_closest1 = []
        self.first_n = []
        self.hex_glob = []
        self.first_hex = []
        self.initGrid(config.rows, config.cols, self.size)
        self.create_hexes_board()
        draw.draw_player(self.can,self.hexagons_board,self.size)
        self.can.bind("<Button-1>", self.click_pos)
        frame = Frame()
        frame.pack()
        self.click_button()
        draw.draw_board(self.can,self.hexagons_board,self.size)
        draw.draw_neighb(self.can,self.add_first_hex(),self.size)
        self.init_board_object()

    def init_board_object(self):
        first_player_hex = self.first_hex
        depth = 0
        player1_hexes = []
        player2_hexes = []
        if(len(player2_hexes) == 0) and (len(player1_hexes) == 0):
            player1_hexes = first_player_hex
            player2_hexes = []
        score = 0
        possible_moves = self.first_n
        player_type = self.state
        init_board_object = board.Board(first_player_hex,depth,player1_hexes,player2_hexes,score,possible_moves,player_type)
        self.game_board = init_board_object

    def callback0(self):
        self.game_type = 0
        print("You play against AI") 
    def callback1(self):
        self.game_type = 1 
        print("Mode: Player vs Player") 

    def click_button(self):
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
        button = tk.Button(frame, 
                       text="QUIT", 
                       fg="red",
                       command=quit)
        button.pack(side=tk.LEFT)
        slogan = tk.Button(frame,
                        text="Player vs AI",
                        command=self.callback0)
        slogan.pack(side=tk.LEFT)
        ai = tk.Button(frame,
                        text="Player vs Player",
                        command=self.callback1)
        ai.pack(side=tk.LEFT)    
      
    def add_first_hex (self):
        start_order = int(input("Enter '1' if you want to start 1st, '2' if second: "))
        if start_order == 1:
            self.state = 0
            print("You are starting")
        else:
            self.state = 1
            print("You will be second")
        for i in range(len(self.hexagons_board)):
            if self.hexagons_board[i].row == 9 and self.hexagons_board[i].col == 10:
                first_neighs = draw.neighbour(self.hexagons_board[i],self.hexagons_board)
                self.hex_glob = [self.hexagons_board[i]]
                # self.hexagons_white = [self.hexagons_board[i]]
                self.first_hex = [self.hexagons_board[i]]               
                self.neigh_append = first_neighs #adds first neighbours before second hex
                self.first_n = first_neighs
                draw.draw_n_first_hex(self.neigh_append,self.can)
                if self.state == 0:
                    self.hexagons_white = [self.hexagons_board[i]]
                else:
                    self.hexagons_black = [self.hexagons_board[i]]
        return first_neighs
                
    def initGrid(self, cols, rows, size): # prints background layer of hexes, with offset shifting layers and is of shape of rectangle
        start_x_first_hex = +0
        start_y_first_hex = +20
        for c in range(cols):
            for r in range(rows): 
                if r % 2 == 0:
                    offset = (sqrt(3)/2)*size
                else:
                    offset = 0       
                h = Hexagon(r,c,self.can,
                            start_x_first_hex + (c * (size * sqrt(3))+  offset),
                            start_y_first_hex + ((r * (size * 3/2)+0.5)+0.5)  ,
                            size,
                            "#a1e2a1")
                self.hexagons.append(h)
                # h.draw_coordinate(h.x,h.y,str(r),chr(c+97))
                # h.draw_coordinate(h.x,h.y,str(r),str(c))#to print hexes coords on the board
                # h.convert_coordinate(h.x,h.y,str(r),(c))

    def create_hexes_board(self): #continuation of grid. Takes the printed hexes and aligned them in a desired manner
        row = 0
        col = 5
        inc_row = 19
        end_row = 10
        for h in range (inc_row):#for each row
            for i in range(end_row):#for each column
                for j in range(len(self.hexagons)):   #search for the right hex with specific row and col  
                    if (self.hexagons[j].row == row and self.hexagons[j].col ==  col):
                        self.hexagons_board.append(self.hexagons[j])
                col += 1
            col -= (end_row )
            if h < 9:
                end_row += 1
                if (h%2 == 1):
                    col -= 1
            else:
                end_row -= 1
                if (h%2 == 0):
                    col +=1
            row += 1

    def closest_hex (self, click_pos):
        distances = []
        for i in self.hexagons_board:
            distance = sqrt((i.x+self.size - click_pos[0])**2 + (i.y+self.size*0.5 - click_pos[1])**2)
            distances.append(distance)
            self.hex_closest1 = self.hexagons_board[distances.index(min(distances))]
        return self.hexagons_board[distances.index(min(distances))]

    def out_of_boundaries (self,hex_center,player):
        if not game_rules.flood_fill(hex_center,[],player,self.hexagons_board):
            return True
        else:
            return False

    def click_pos (self, event):
        xy = (event.x, event.y)
        hex_closest = self.closest_hex(xy)

        if (hex_closest in self.first_n) and (hex_closest not in self.hex_glob): 
            self.depth_game += 1                      
            if self.state == 1:
                self.hex_glob.append(hex_closest)  
                for i in draw.neighbour(hex_closest,self.hexagons_board):
                    self.neigh_append.append(i)
                inter_list = self.intersection(self.neigh_append)
                self.first_n = list(inter_list )
                neighbours_temp = []
                for i in range(len(self.first_n)):
                    if self.first_n[i] not in self.hex_glob:
                        neighbours_temp.append(self.first_n[i])
                self.first_n = neighbours_temp
                if len(self.intersection(self.neigh_append)) <= 2:
                    draw.sub_first_hex(self.neigh_append,self.can)
                draw.draw_white(self.can,hex_closest,self.size)
                self.hexagons_white.append(hex_closest)
                draw.draw_neighb(self.can,self.first_n,self.size)
                self.game_board = self.game_board.child(self.game_board,hex_closest,self.hexagons_board)                
                self.state = 0
                ai.board.Board.player_type = 1             
                if len(self.hexagons_white)>4:
                    for i in range(len(self.hexagons_white)):
                        if game_rules.diag1_line5(self.hexagons_white,self.hexagons_white) == 4 or game_rules.diag2_line5(self.hexagons_white,self.hexagons_white) == 4 or game_rules.diag3_line5(self.hexagons_white,self.hexagons_white) == 4:
                            print("white - You won by line of 5!")
                            break                        
                if len(self.hexagons_white)>5:
                    for i in range(len(self.hexagons_black)):
                        if self.out_of_boundaries(self.hexagons_black[i],self.hexagons_white):
                            print("white - You won by loop!")
                            break            
            else:
                if self.game_type == 0:
                    ai.board.Board.player_type = 1
                    eval, hex_closest = ai.MinMax(self.game_board,config.depth,-math.inf,math.inf,True,self.hexagons_board)
                    # print("eval",eval)
                    self.hex_glob.append(hex_closest)
                    self.game_board = self.game_board.child(self.game_board,hex_closest,self.hexagons_board)

                else:  
                    self.hex_glob.append(hex_closest)
                # print("gamedepth",self.depth_game)                 
                for i in draw.neighbour(hex_closest,self.hexagons_board): #possible moves
                    self.neigh_append.append(i)
                inter_list = self.intersection(self.neigh_append)
                self.first_n = list(inter_list )
                neighbours_temp = []

                for i in range(len(self.first_n)):
                    if self.first_n[i] not in self.hex_glob:
                        neighbours_temp.append(self.first_n[i])
                self.first_n = neighbours_temp
                if len(self.intersection(self.neigh_append)) <= 2:
                    draw.sub_first_hex(self.neigh_append,self.can)
                draw.draw_black(self.can,hex_closest,self.size)
                self.hexagons_black.append(hex_closest)  
                draw.draw_neighb(self.can,self.first_n,self.size)
                self.state = 1
                ai.board.Board.player_type = 0
                if len(self.hexagons_black)>4:
                    for i in range(len(self.hexagons_black)):
                        if game_rules.diag1_line5(self.hexagons_black,self.hexagons_black) == 4 or game_rules.diag2_line5(self.hexagons_black,self.hexagons_black) == 4 or game_rules.diag3_line5(self.hexagons_black,self.hexagons_black) == 4:
                            print("black - You won by line of 5!")
                            break
                if len(self.hexagons_black)>5:
                    for i in range(len(self.hexagons_white)):
                        if self.out_of_boundaries(self.hexagons_white[i],self.hexagons_black):
                            print("black - You won by loop!")
                            break               
    
    def intersection (self,seq):
        seen = set()
        seen_add = seen.add
        hexes_neigh = set( x for x in seq if x in seen or seen_add(x) )
        return hexes_neigh  