from tkinter import *
import pygame
from pygame.locals import *
from math import cos, sin,radians,sqrt
import collections 
from hexagon import *
from ai import *
# from winning_conditions import *
import numpy
from numpy import concatenate
import random
import math
# import sys
# sys.stdout = open('stdout.txt', 'w')


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Andantino - Hexagon Grid")
        self.can = Canvas(self, width=650, height=550, bg="#60ace6")
        self.size = 18
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
        self.dir_1 = []
        self.dir_2 = []
        self.dir_3 = []
        self.dir_4 = []
        self.dir_5 = []
        self.dir_6 = []
        self.first_hex = []
        self.len_diag1 = 0
        self.len_diag2 = 0
        self.len_diag3 = 0
        self.glob_line = []
        self.flag_neigh = 0
        self.loop_on = 0
        self.game_over = 0
        self.depth = 0
        self.initGrid(20, 20, self.size)
        # print("number of hexes in total : " + str(len(self.hexagons)))
        self.create_hexes_board()
       # self.closest_hex(hex_closest)
        # self.add_first_hex()
        self.draw_player(self.can,self.hexagons_board,self.size)
        
        # self.draw_white(self.can,self.hexagons_board,self.size)
        # self.
        # self.can.create_text(50, 50, text='text')
        self.can.bind("<Button-1>", self.click_pos)
        
        # self.draw_n_first_hex()
        frame = Frame()
        frame.pack()
    #     frame.focus_set()
    #     frame.bind("<Leave>", self.quit)
    #   # root.pack()
        # def button_click (self,Button):
        #     self.button1 = Button(frame, text="Player vs Player", command=self.func)
        #     self.button2 = Button(frame, text="Player vs AI", command=self.func)
        #     self.button1.pack(side='left')
        #     self.button2.pack(side='left')
        #     self.can.bind('f', self.func)
        
        # self.create_hexes_board(self.hexagons)
        # print("number of hexes in board : " + str(len(self.hexagons_board)))
        self.draw_board(self.can,self.hexagons_board,self.size)
        self.draw_neighb(self.can,self.add_first_hex(),self.size)

    def create_board(self):
        hex = self.hex_glob
        player = True
        score = random.randint(1,101)
        possible_moves = list(self.first_n)
        print("possible_moves",possible_moves)
        player_hexes = hex
        board = Board(hex,self.depth,player,score,possible_moves,player_hexes)
        return board

        # hexagon, depth, player,score,possible_moves,player_hexes
    def draw_board(self,canvas,hexagons_board,size):    
        for i in range(len(hexagons_board)):
            
            start_x = hexagons_board[i].x #tried shift
            start_y = hexagons_board[i].y 
            coords = []
            for j in range(6) :
                
                end_x = start_x + size * cos(radians(60 * j-30))
                end_y = start_y + size * sin(radians(60 * j-30))
                coords.append([start_x, start_y])
                start_x = end_x
                start_y = end_y
            newcoords = self.can.create_polygon(coords[0][0],
                                    coords[0][1], 
                                    coords[1][0], 
                                    coords[1][1],
                                    coords[2][0],
                                    coords[2][1],
                                    coords[3][0],
                                    coords[3][1],
                                    coords[4][0],
                                    coords[4][1], 
                                    coords[5][0],
                                    coords[5][1], 
                                    fill="",
                                    outline="gray",
                                    tags="{}.{}".format("test", "tsst"))

    def neighbour (self, hex_center):

        hex_neighbs = []
        if hex_center.row % 2 == 0:
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col -1 and self.hexagons_board[j].row == hex_center.row:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col and self.hexagons_board[j].row == hex_center.row - 1:
                    hex_neighbs.append(self.hexagons_board[j])            
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col and self.hexagons_board[j].row == hex_center.row + 1:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col + 1 and self.hexagons_board[j].row == hex_center.row - 1:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col + 1 and self.hexagons_board[j].row == hex_center.row:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col + 1 and self.hexagons_board[j].row == hex_center.row + 1:
                    hex_neighbs.append(self.hexagons_board[j]) 
        else:
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col - 1 and self.hexagons_board[j].row == hex_center.row:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col - 1 and self.hexagons_board[j].row == hex_center.row - 1:
                    hex_neighbs.append(self.hexagons_board[j])            
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col - 1 and self.hexagons_board[j].row == hex_center.row + 1:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col and self.hexagons_board[j].row == hex_center.row - 1:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col and self.hexagons_board[j].row == hex_center.row + 1:
                    hex_neighbs.append(self.hexagons_board[j])
            for j in range (len(self.hexagons_board)):
                if self.hexagons_board[j].col == hex_center.col + 1 and self.hexagons_board[j].row == hex_center.row:
                    hex_neighbs.append(self.hexagons_board[j])            
        # print("Olek Hex_neighs from neghbours fnc", hex_neighbs)       
        return hex_neighbs

    def add_first_hex (self):
        for i in range(len(self.hexagons_board)):
            if self.hexagons_board[i].row == 9 and self.hexagons_board[i].col == 10:
                first_neighs = self.neighbour(self.hexagons_board[i])
                self.hex_glob = [self.hexagons_board[i]]
                self.hexagons_white = [self.hexagons_board[i]]
                self.first_hex = [self.hexagons_board[i]]
                self.neigh_append = first_neighs #adds first neighbours before second hex
                self.first_n = first_neighs
                self.draw_n_first_hex(self.neigh_append)
        return first_neighs

    def sub_first_hex (self, hex):
        elo = hex
        self.draw_board(self.can,elo,self.size) 
        return elo

    def draw_n_first_hex (self, hex):
        elo = set(hex)
        self.draw_neighb(self.can,elo,self.size) 
        return elo

    def draw_black(self,canvas,hexagon,size):      #layer of black hexes
        start_x = hexagon.x
        start_y = hexagon.y 
        coords = []
        hex_black_append = []
        for j in range(6) :
            
            end_x = start_x + size * cos(radians(60 * j-30))
            end_y = start_y + size * sin(radians(60 * j-30))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y
        # print(coords)
        newcoords = self.can.create_polygon(coords[0][0],
                                coords[0][1], 
                                coords[1][0], 
                                coords[1][1],
                                coords[2][0],
                                coords[2][1],
                                coords[3][0],
                                coords[3][1],
                                coords[4][0],
                                coords[4][1], 
                                coords[5][0],
                                coords[5][1], 
                                fill="#000000",
                                outline="gray",
                                tags="{}.{}".format("test", "tsst"))

    def draw_white(self,canvas,hexagon,size):      #layer of white hexes
        start_x = hexagon.x
        start_y = hexagon.y 
        coords = []
        hex_white_append = []
        for j in range(6) :
            
            end_x = start_x + size * cos(radians(60 * j-30))
            end_y = start_y + size * sin(radians(60 * j-30))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y
        newcoords = self.can.create_polygon(coords[0][0],
                                coords[0][1], 
                                coords[1][0], 
                                coords[1][1],
                                coords[2][0],
                                coords[2][1],
                                coords[3][0],
                                coords[3][1],
                                coords[4][0],
                                coords[4][1], 
                                coords[5][0],
                                coords[5][1], 
                                fill="#ffffff",
                                outline="gray",
                                tags="{}.{}".format("test", "tsst"))

    def draw_player(self,canvas,hexagons_board,size):      #layer of white hexes
        start_x = 0
        start_y = 0  
        coords = []
        hex_append = []
        
        for i in range(len(hexagons_board)):
            if hexagons_board[i].row == 9 and hexagons_board[i].col == 10:
                #start_position =  self.hexagons_white[0]
                start_x = hexagons_board[i].x #tried shift
                start_y = hexagons_board[i].y
                hex_append.append([start_x, start_y])
                first_neighs = self.neighbour(hexagons_board[i])

                # print("show neighbs", first_neighs)
                self.draw_neighb(self.can,first_neighs,self.size) 
                self.draw_n_first_hex (first_neighs)
                # print("my first hex draw player", first_neighs)   
                # first_neighs = self.neighbour(self.hexagons_board[i])  
                # self.neigh_append = first_neighs

           
                
        for j in range(6) :
            
            end_x = start_x + size * cos(radians(60 * j-30))
            end_y = start_y + size * sin(radians(60 * j-30))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y
        # print(coords)
        newcoords = self.can.create_polygon(coords[0][0],
                                coords[0][1], 
                                coords[1][0], 
                                coords[1][1],
                                coords[2][0],
                                coords[2][1],
                                coords[3][0],
                                coords[3][1],
                                coords[4][0],
                                coords[4][1], 
                                coords[5][0],
                                coords[5][1], 
                                fill="#ffffff",
                                outline="gray",
                                tags="{}.{}".format("test", "tsst"))                                

    def draw_neighb (self, canvas,neighbours, size):
        neighbours = list(neighbours)
        for i in range(len(neighbours)):
            start_x = neighbours[i].x 
            start_y = neighbours[i].y 
            coords = []
            for j in range(6) :
                
                end_x = start_x + size * cos(radians(60 * j-30))
                end_y = start_y + size * sin(radians(60 * j-30))
                coords.append([start_x, start_y])
                start_x = end_x
                start_y = end_y
            # print(coords)
            newcoords = self.can.create_polygon(coords[0][0],
                                    coords[0][1], 
                                    coords[1][0], 
                                    coords[1][1],
                                    coords[2][0],
                                    coords[2][1],
                                    coords[3][0],
                                    coords[3][1],
                                    coords[4][0],
                                    coords[4][1], 
                                    coords[5][0],
                                    coords[5][1], 
                                    fill="",
                                    outline="black",
                                    tags="{}.{}".format("test", "tsst"))

    def initGrid(self, cols, rows, size):
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
            self.hex_closest1 = self.hexagons_board[distances.index(min(distances))]
        print("hex_closest", self.hex_closest1.row, self.hex_closest1.col)
        return self.hexagons_board[distances.index(min(distances))]

    def flood_fill (self, hex_center,prev_hexes, player):
        neigh = []
        
        if len(self.neighbour(hex_center)) < 6:
            print("hex_center flood",[hex_center.row,hex_center.col])
            return True
        if hex_center in player:
            print("hex_center in self.hexagons_ play on!")
            return False
        if  hex_center in prev_hexes:
            print("hex_center in prev_hexes play on!")            
            return False
        else:
            prev_hexes.append(hex_center) 
            print("hex center",[hex_center.row,hex_center.col])
            for neigh in self.neighbour(hex_center):
                print("neigh",[neigh.row,neigh.col])
                if self.flood_fill(neigh,prev_hexes,player):
                    return True
        return False
                
    def out_of_boundaries (self, hex_center,player):
        if not self.flood_fill(hex_center,[],player):
            print("WIN!!!!!!!!!!!!!!!!")
            print("check",[hex_center.row,hex_center.col])
            self.game_over = 1
            return True
        else:
            print("keep on trying")
            return False

    def diag1_line5_white (self, hex_center):
        j = [-1,-2,-3,-4]
        for hex_center in self.hexagons_white:
            white = []
            for i in range(4):
                for k in range(len(self.hexagons_white)):
                    if self.hexagons_white[k].col == hex_center.col + j[i] and self.hexagons_white[k].row == hex_center.row and self.hexagons_white[k] not in white:
                        white.append(self.hexagons_white[k])
                        if len(white) > 3:
                            print("You won! - white.dir_1")  
                            for p in range(len(white)):
                                print("white11",[white[p].row,white[p].col]) 


    def diag1_line5_black (self, hex_center):
        j = [-1,-2,-3,-4]
        for hex_center in self.hexagons_black:
            black = []
            for i in range(4):
                for k in range(len(self.hexagons_black)):
                    if self.hexagons_black[k].col == hex_center.col + j[i] and self.hexagons_black[k].row == hex_center.row and self.hexagons_black[k] not in black:
                        black.append(self.hexagons_black[k])
                        if len(black) > 3:
                            print("You won! - black.dir_1")  
                            for p in range(len(black)):
                                print("black11",[black[p].row,black[p].col]) 

    def diag2_line5_white (self, hex_center):
        h = [-1,-1,-2,-2]
        j = [0,-1,-1,-2]
        z = [-1,-2,-3,-4]
        for hex_center in self.hexagons_white:
            white = []
            if hex_center.row % 2 == 0:   
                for i in range(4):
                    for k in range(len(self.hexagons_white)):
                        if self.hexagons_white[k].col == hex_center.col + j[i] and self.hexagons_white[k].row == hex_center.row +z[i] and self.hexagons_white[k] not in white:
                            white.append(self.hexagons_white[k])
                            if len(white) > 3:
                                print("You won! - white.dir_2")  
                                for p in range(len(white)):
                                    print("white33",[white[p].row,white[p].col]) 
            else:
                for o in range(4):
                    for t in range(len(self.hexagons_white)):
                        if self.hexagons_white[t].col == hex_center.col + h[o] and self.hexagons_white[t].row == hex_center.row + z[o] and self.hexagons_white[t] not in white:
                            white.append(self.hexagons_white[t])                    
                            if len(white) > 3:
                                print("You won! - white.dir2") 
                                for i in range(len(white)):
                                    print("white_list",[white[i].row,white[i].col])    

    def diag2_line5_black (self, hex_center):
        h = [-1,-1,-2,-2]
        j = [0,-1,-1,-2]
        z = [-1,-2,-3,-4]
        for hex_center in self.hexagons_black:
            black = []
            if hex_center.row % 2 == 0:   
                for i in range(4):
                    for k in range(len(self.hexagons_black)):
                        if self.hexagons_black[k].col == hex_center.col + j[i] and self.hexagons_black[k].row == hex_center.row +z[i] and self.hexagons_black[k] not in black:
                            black.append(self.hexagons_black[k])
                            if len(black) > 3:
                                print("You won! - black.dir_2")  
                                for p in range(len(black)):
                                    print("black33",[black[p].row,black[p].col]) 
            else:
                for o in range(4):
                    for t in range(len(self.hexagons_black)):
                        if self.hexagons_black[t].col == hex_center.col + h[o] and self.hexagons_black[t].row == hex_center.row + z[o] and self.hexagons_black[t] not in black:
                            black.append(self.hexagons_black[t])                    
                            if len(black) > 3:
                                print("You won! - black.dir2") 
                                for i in range(len(black)):
                                    print("black_list",[black[i].row,black[i].col])                                      

    def diag3_line5_white (self, hex_center):
        # black = []
        # z = -1
        h = [1,1,2,2]
        j = [0,1,1,2]
        z = [-1,-2,-3,-4]
        
        for hex_center in self.hexagons_white:
            white = []
            # print("SPRAWDZAMY PASSE dla:",[hex_center.row, hex_center.col])
            # z = -1
            if hex_center.row % 2 == 0:
                for i in range(4):
                    # print("tei33=",i)
                    # print("tehi33",h[i])
                    for k in range(len(self.hexagons_white)):
                        if self.hexagons_white[k].col == hex_center.col + h[i] and self.hexagons_white[k].row == hex_center.row +z[i] and self.hexagons_white[k] not in white:
                            white.append(self.hexagons_white[k])
                            # print("print len blak",len(white))
                            # print("i33=",i)
                            # print("hi33",h[i])
                            # z -= 1
                            if len(white) > 3:
                                print("You won! - white.dir_3")  
                                for p in range(len(white)):
                                    print("white33",[white[p].row,white[p].col]) 
                                    # if white[i].row % 2 == 0:
            else:   
                for o in range(4):
                    for t in range(len(self.hexagons_white)):
                        if self.hexagons_white[t].col == hex_center.col + j[o] and self.hexagons_white[t].row == hex_center.row + z[o] and self.hexagons_white[t] not in white:
                            white.append(self.hexagons_white[t])                         
                            if len(white) > 3:
                                print("You won! - white.dir3") 
                                for i in range(len(white)):
                                    print("white_list",[white[i].row,white[i].col])   

    def diag3_line5_black (self, hex_center):
        h = [1,1,2,2]
        j = [0,1,1,2]
        z = [-1,-2,-3,-4]
        
        for hex_center in self.hexagons_black:
            black = []
            if hex_center.row % 2 == 0:
                for i in range(4):
                    for k in range(len(self.hexagons_black)):
                        if self.hexagons_black[k].col == hex_center.col + h[i] and self.hexagons_black[k].row == hex_center.row +z[i] and self.hexagons_black[k] not in black:
                            black.append(self.hexagons_black[k])
                            if len(black) > 3:
                                print("You won! - black.dir_3")  
                                for p in range(len(black)):
                                    print("blaczek33",[black[p].row,black[p].col]) 
            else:   
                for o in range(4):
                    for t in range(len(self.hexagons_black)):
                        if self.hexagons_black[t].col == hex_center.col + j[o] and self.hexagons_black[t].row == hex_center.row + z[o] and self.hexagons_black[t] not in black:
                            black.append(self.hexagons_black[t])
                            if len(black) > 3:
                                print("You won! - black.dir_3") 
                                for i in range(len(black)):
                                    print("blaczek",[black[i].row,black[i].col])                                  

    def click_pos (self, event):
  
        new1 = []
        xy = (event.x, event.y)
        hex_closest = self.closest_hex(xy)
        print("closet",hex_closest)
        # if self.start == 1:
        for i in self.first_n:
            if hex_closest == i and hex_closest not in self.hex_glob:
                self.hex_glob.append(hex_closest)  
                for i in self.neighbour(hex_closest):
                    self.neigh_append.append(i)
                inter_list = self.intersection(self.neigh_append)
                self.first_n = inter_list 
        #        print("intersection",self.first_n)
                if len(self.intersection(self.neigh_append)) <= 2:
                    # print("ile mam hexow",len(self.intersection(self.neigh_append)))
                    self.sub_first_hex(self.neigh_append)
                
                if self.state == 1:
                    self.draw_white(self.can,hex_closest,self.size)
                    self.hexagons_white.append(hex_closest)
                    # print("white hexes",self.hexagons_white)
                    self.draw_neighb(self.can,self.first_n,self.size)
                    self.state = 0
                    if len(self.hexagons_white)>4:
                        for i in range(len(self.hexagons_white)):
                            self.diag3_line5_white(self.hexagons_white)
                            self.diag2_line5_white(self.hexagons_white)
                            self.diag1_line5_white(self.hexagons_white)
                    if len(self.hexagons_white)>5:
                        for i in range(len(self.hexagons_black)):
                            if self.out_of_boundaries(self.hexagons_black[i],self.hexagons_white):
                                break            
                else:
                    hex_closest = self.MinMax(self.create_board(),2,-math.inf,math.inf,self.state == 0)
                    print("hexclosest_fromminmax",hex_closest)
                    self.draw_black(self.can,hex_closest,self.size)
                    self.hexagons_black.append(hex_closest)
                    # print("black hexes",self.hexagons_black)     
                    self.draw_neighb(self.can,self.first_n,self.size)
                    self.state = 1
                    if len(self.hexagons_black)>4:
                        for i in range(len(self.hexagons_black)):
                            self.diag3_line5_black(self.hexagons_black)
                            self.diag2_line5_black(self.hexagons_black)
                            self.diag1_line5_black(self.hexagons_black)
                    if len(self.hexagons_black)>5:
                        for i in range(len(self.hexagons_white)):
                            if self.out_of_boundaries(self.hexagons_white[i],self.hexagons_black):
                                break               
    
    def intersection (self,seq):
        seen = set()
        seen_add = seen.add
        # adds all elements it doesn't know yet to seen and all other to seen_twice
        hexes_neigh = set( x for x in seq if x in seen or seen_add(x) )
        # turn the set into a list (as requested)
        # print("hexes_neigh",hexes_neigh) 
        return hexes_neigh

    def MinMax (self,position,depth, alpha,beta,max_player): 
        print("depth",depth)
        if depth == 0 or self.game_over == 1:
            return position.score
        if max_player:
            score = -math.inf
            for i in range(len(position.possible_moves)):# .child(position,possible_moves): #i put the board as position and children are the possible moves
                new_child = position.child(position,position.possible_moves[i],self.hexagons_board)
                value = self.MinMax(new_child,depth-1, alpha,beta,False)
                print("value-min",value)
                if value > score:
                   score = value
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            # return score
        else:
            score = math.inf
            for i in range(len(position.possible_moves)):
                new_child = position.child(position,position.possible_moves[i],self.hexagons_board)
                print("newchild",new_child)
                value = self.MinMax(new_child,depth-1, alpha,beta,True)
                print("value-max",value)
                if value < score:
                    score = value
                beta = min(beta,value)
                if beta <= alpha:
                    break
            # return score
        print("score",score)
        print("value",value)
        print("newchild",new_child)
        print("positionscore",position.score)
        print("scoretyp",type(score))
        return [score, new_child]

    def evaluate (self,hex_center):
        hex_center = random.randint(1,101)
        return hex_center

# root = Tk()
# root.update()
