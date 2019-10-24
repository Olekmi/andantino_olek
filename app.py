from tkinter import *
import tkinter as tk
import pygame
from pygame.locals import *
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
# sys.stdout = open('stdout.txt', 'w')

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Andantino - Hexagon Grid")
        self.can = Canvas(self, width=config.width, height=config.height, bg= "#60ace6")
        self.depth_game = config.depth
        self.size = config.size
        self.state = 0
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
        # ai.board.Board.player_type = 1
        # print("number of hexes in total : " + str(len(self.hexagons)))
        self.create_hexes_board()
        draw.draw_player(self.can,self.hexagons_board,self.size)
        # print(len(self.hexagons_board))
        # ai.board.Board.add_first_hexx(self,self.hexagons_board)
        self.can.bind("<Button-1>", self.click_pos)
        frame = Frame()
        frame.pack()
#        self.click_button()
        draw.draw_board(self.can,self.hexagons_board,self.size)
        draw.draw_neighb(self.can,self.add_first_hex(),self.size)
        self.init_board_object()
        print(len(self.game_board.possible_moves))

    def init_board_object(self):
        # temp = []
        first_player_hex = self.hex_glob
        print("first player", first_player_hex)
        depth = 0
        player1_hexes = first_player_hex
        player2_hexes = []
        score = 0
        possible_moves = self.first_n
        player_type = 0
        init_board_object = board.Board(first_player_hex,depth,player1_hexes,player2_hexes,score,possible_moves,player_type)
        self.game_board = init_board_object





    def callback0(self):
        self.state = 0
        print("state0",self.state) 
    def callback1(self):
        self.state = 1 
        print("state1",self.state) 

    def click_button(self):
        print("Tkinter is easy to use!")

        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
#        button = tk.Button(frame, 
#                        text="QUIT", 
#                        fg="red",
#                        command=quit)
#        button.pack(side=tk.LEFT)
        slogan = tk.Button(frame,
                        text="1ST",
                        command=self.callback0)
        slogan.pack(side=tk.LEFT)
        ai = tk.Button(frame,
                        text="2ND",
                        command=self.callback1)
        ai.pack(side=tk.LEFT)    
      
    def add_first_hex (self):
        for i in range(len(self.hexagons_board)):
            if self.hexagons_board[i].row == 9 and self.hexagons_board[i].col == 10:
                first_neighs = draw.neighbour(self.hexagons_board[i],self.hexagons_board)
                self.hex_glob = [self.hexagons_board[i]]
                self.hexagons_white = [self.hexagons_board[i]]
                self.first_hex = [self.hexagons_board[i]]               
                self.neigh_append = first_neighs #adds first neighbours before second hex
                self.first_n = first_neighs
                draw.draw_n_first_hex(self.neigh_append,self.can)
        return first_neighs
                
    def initGrid(self, cols, rows, size): # prints background layer of hexes, with offset shifting layers and is of shape of rectangle
        start_x_first_hex = +0
        start_y_first_hex = +20
        """
        2d grid of hexagons
        """
        # to get inclusive range chang
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
                # self.can.create_text(50, 50, text='text')
                # h.draw_coordinate(h.x,h.y,str(r),chr(c+97))
                h.draw_coordinate(h.x,h.y,str(r),str(c))
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
                        # print("type of hexboard",type(self.hexagons_board))
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
            # distance = (sqrt((i.x - click_pos[0])**2), sqrt((i.y - click_pos[1])**2))
            distance = sqrt((i.x+self.size - click_pos[0])**2 + (i.y+self.size*0.5 - click_pos[1])**2)
            distances.append(distance)
        #    mini = self.hexagons_board.index(min(distances))

            self.hex_closest1 = self.hexagons_board[distances.index(min(distances))]
        # print("hex_closest", self.hex_closest1.row, self.hex_closest1.col)
        return self.hexagons_board[distances.index(min(distances))]

    def out_of_boundaries (self,hex_center,player):
        if not game_rules.flood_fill(hex_center,[],player,self.hexagons_board):
            print("WIN!!!!!!!!!!!!!!!!")
            print("check",[hex_center.row,hex_center.col])
            return True
        else:
            # print("keep on trying")
            return False

    # def create_board(self,hex_closest):
    #     score = random.randint(1,101)
    #     possible_moves = list(self.first_n)
        
    #     boardgame = board.Board(hex_closest,self.depth_game,self.hexagons_white,self.hexagons_black,score,possible_moves,self.state)
    #     return boardgame        

    def click_pos (self, event):
        self.depth_game += 1
        print("length of possible moves",len(self.first_n))
        xy = (event.x, event.y)
        hex_closest = self.closest_hex(xy)

        if hex_closest in self.first_n and hex_closest not in self.hex_glob:                       
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

                self.game_board = self.game_board.child(self.game_board,hex_closest,self.hexagons_board)
                #update game state
                print(self.game_board.possible_moves)


                draw.draw_white(self.can,hex_closest,self.size)
                self.hexagons_white.append(hex_closest)
                draw.draw_neighb(self.can,self.first_n,self.size)
                self.state = 0
                ai.board.Board.player_type = 1
                if len(self.hexagons_white)>4:
                    for i in range(len(self.hexagons_white)):
                        game_rules.diag3_line5(self.hexagons_white,self.hexagons_white)
                        game_rules.diag2_line5(self.hexagons_white,self.hexagons_white)
                        game_rules.diag1_line5(self.hexagons_white,self.hexagons_white)
                if len(self.hexagons_white)>5:
                    for i in range(len(self.hexagons_black)):
                        if self.out_of_boundaries(self.hexagons_black[i],self.hexagons_white):
                            break            
            else:
                ai.board.Board.player_type = 1
                eval, hex_closest = ai.MinMax(self.game_board,3,-math.inf,math.inf,True,self.hexagons_board)
#                print("ai move :, row = "+str(hex_closest.row)+", col = " + str(hex_closest.col))
                
                self.game_board = self.game_board.child(self.game_board,hex_closest,self.hexagons_board)
                # self.hex_glob.append(hex_closest)  
                # self.list_of_neigh = draw.neighbour(hex_closest,self.hexagons_board)
    #         print("list_of_neigh",self.list_of_neigh)
                for i in draw.neighbour(hex_closest,self.hexagons_board): #possible moves
                    self.neigh_append.append(i)
                inter_list = self.intersection(self.neigh_append)
                self.first_n = list(inter_list )
                neighbours_temp = []

                for i in range(len(self.first_n)):
                    if self.first_n[i] not in self.hex_glob:
                        neighbours_temp.append(self.first_n[i])
                self.first_n = neighbours_temp

                print("from AI turn",self.game_board.possible_moves)


                # for i in range(len(self.first_n)):
                #     print("intersection",self.first_n[i].row,self.first_n[i].col)
                if len(self.intersection(self.neigh_append)) <= 2:
                    # print("ile mam hexow",len(self.intersection(self.neigh_append)))
                    draw.sub_first_hex(self.neigh_append,self.can)
                draw.draw_black(self.can,hex_closest,self.size)
                self.hexagons_black.append(hex_closest)  
                draw.draw_neighb(self.can,self.first_n,self.size)
                self.state = 1
                ai.board.Board.player_type = 0
                if len(self.hexagons_black)>4:
                    for i in range(len(self.hexagons_black)):
                        game_rules.diag3_line5(self.hexagons_black,self.hexagons_black)
                        game_rules.diag2_line5(self.hexagons_black,self.hexagons_black)
                        game_rules.diag1_line5(self.hexagons_black,self.hexagons_black)
                if len(self.hexagons_black)>5:
                    for i in range(len(self.hexagons_white)):
                        if self.out_of_boundaries(self.hexagons_white[i],self.hexagons_black):
                            break               
    
    def intersection (self,seq):
        seen = set()
        seen_add = seen.add
        hexes_neigh = set( x for x in seq if x in seen or seen_add(x) )
        return hexes_neigh  

    
# root = Tk()
# root.update()