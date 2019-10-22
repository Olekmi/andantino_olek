from tkinter import *
import pygame
from pygame.locals import *
from math import cos, sin,radians,sqrt
import collections 
from hexagon import *
import numpy
from numpy import concatenate
import draw, config, game_rules
# import sys
# sys.stdout = open('stdout.txt', 'w')

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Andantino - Hexagon Grid")
        self.can = Canvas(self, width=config.width, height=config.height, bg= "#60ace6")
        self.size = config.size
        self.state = 0
        self.start = 1
        self.can.pack(padx=0)
        self.hexagons = []
        self.hexagons_board = []
        self.hexagons_white = []
        self.hex_append = []
        self.list_of_neigh = []
        self.hexagons_black = []
        self.neigh_append = []
        self.hex_closest1 = []
        self.first_n = []
        self.hex_glob = []
        self.glob_inter = []
        self.first_hex = []
        self.glob_line = []
        self.initGrid(config.rows, config.cols, self.size)
        # print("number of hexes in total : " + str(len(self.hexagons)))
        self.create_hexes_board()
        draw.draw_player(self.can,self.hexagons_board,self.size)
        self.can.bind("<Button-1>", self.click_pos)
        frame = Frame()
        frame.pack()
        draw.draw_board(self.can,self.hexagons_board,self.size)
        draw.draw_neighb(self.can,self.add_first_hex(),self.size)
      
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
        hex_closest1 = []
        hex_append = []
        for i in self.hexagons_board:
            # distance = (sqrt((i.x - click_pos[0])**2), sqrt((i.y - click_pos[1])**2))
            distance = sqrt((i.x+self.size - click_pos[0])**2 + (i.y+self.size*0.5 - click_pos[1])**2)
            distances.append(distance)
        #    mini = self.hexagons_board.index(min(distances))

            self.hex_closest1 = self.hexagons_board[distances.index(min(distances))]
        print("hex_closest", self.hex_closest1.row, self.hex_closest1.col)
        return self.hexagons_board[distances.index(min(distances))]

    def out_of_boundaries (self,hex_center,player):
        if not game_rules.flood_fill(hex_center,[],player,self.hexagons_board):
            print("WIN!!!!!!!!!!!!!!!!")
            print("check",[hex_center.row,hex_center.col])
            return True
        else:
            print("keep on trying")
            return False

    def click_pos (self, event):
  
        new1 = []
        xy = (event.x, event.y)
        hex_closest = self.closest_hex(xy)
        # if self.start == 1:
        for i in self.first_n:
            if hex_closest == i and hex_closest not in self.hex_glob:
                self.hex_glob.append(hex_closest)  
                self.list_of_neigh = draw.neighbour(hex_closest,self.hexagons_board)
       #         print("list_of_neigh",self.list_of_neigh)
                for i in draw.neighbour(hex_closest,self.hexagons_board):
                    self.neigh_append.append(i)
                inter_list = self.intersection(self.neigh_append)
                self.first_n = inter_list 
        #        print("intersection",self.first_n)
                if len(self.intersection(self.neigh_append)) <= 2:
                    # print("ile mam hexow",len(self.intersection(self.neigh_append)))
                    draw.sub_first_hex(self.neigh_append,self.can)
                
                if self.state == 1:
                    draw.draw_white(self.can,hex_closest,self.size)
                    self.hexagons_white.append(hex_closest)
                    # print("white hexes",self.hexagons_white)
                    draw.draw_neighb(self.can,self.first_n,self.size)
                    self.state = 0
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
                    draw.draw_black(self.can,hex_closest,self.size)
                    self.hexagons_black.append(hex_closest)  
                    draw.draw_neighb(self.can,self.first_n,self.size)
                    self.state = 1
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
        # adds all elements it doesn't know yet to seen and all other to seen_twice
        hexes_neigh = set( x for x in seq if x in seen or seen_add(x) )
        return hexes_neigh

# root = Tk()
# root.update()