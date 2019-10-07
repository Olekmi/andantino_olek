from tkinter import *
import pygame
from pygame.locals import *
from math import cos, sin,radians,sqrt
import collections 
from hexagon import *
import numpy
from numpy import concatenate

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
        self.loop_on = 0
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

        # if len(self.intersection(self.neigh_append)) <= 1:
        #     print("ile mam hexow",len(self.intersection(self.neigh_append)))
        #     self.sub_first_hex(self.neigh_append)
          
            
       #print(self.hexagons[])
        

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
                # print("glob",self.hex_glob)
                # for j in first_neighs:
                
                self.neigh_append = first_neighs #adds first neighbours before second hex
                self.first_n = first_neighs
                self.draw_n_first_hex(self.neigh_append)
                # seen = set(self.neigh_append)
                # self.first_n = seen
                # self.draw_neighb(self.can,first_neighs,self.size) 
                # print("my first hex neigh", first_neighs)  
                # print("my first hex", self.neigh_append) 


        return first_neighs

    def sub_first_hex (self, hex):
        elo = hex
        self.draw_board(self.can,elo,self.size) 
        # print("eohfweif", elo)
        #print("my first hex neigh11", self.draw_neighb(self.can,elo,self.size))  
 
        return elo

    def draw_n_first_hex (self, hex):
        elo = set(hex)
        self.draw_neighb(self.can,elo,self.size) 
        # print("eohfweif", elo)
        #print("my first hex neigh11", self.draw_neighb(self.can,elo,self.size))  
 
        return elo

    def draw_black(self,canvas,hexagon,size):      #layer of black hexes
        # print(type(hexagon))
        # print(len(hexagon))
        start_x = hexagon.x
        start_y = hexagon.y 
        coords = []
        hex_black_append = []

        # for i in range(len(hex_white_append)):
        #     #start_position =  self.hexagons_white[0]
        #     start_x = hex_white_append[i].x #tried shift
        #     start_y = hex_white_append[i].y
        #     hex_white_append.append([start_x, start_y])   
                
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
        # print(type(hexagon))
        # print(len(hexagon))
        start_x = hexagon.x
        start_y = hexagon.y 
        coords = []
        hex_white_append = []

        # for i in range(len(hex_white_append)):
        #     #start_position =  self.hexagons_white[0]
        #     start_x = hex_white_append[i].x #tried shift
        #     start_y = hex_white_append[i].y
        #     hex_white_append.append([start_x, start_y])   
                
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
        # print(type(neighbours[0][0]))
        # print(len(neighbours))
        # for t in range(len(neighbours)):
        neighbours = list(neighbours)
        for i in range(len(neighbours)):
            
            # print(neighbours[i])
            start_x = neighbours[i].x #tried shift
            start_y = neighbours[i].y 
            # print(neighbours[i].row)
            # print(neighbours[i].col) 

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




    def initGrid(self, cols, rows, size): # prints background layer of hexes, with offset shifting layers and is of shape of rectangle
        start_x_first_hex = +0
        start_y_first_hex = +20
        """
        2d grid of hexagons
        """
        print("Printing inclusive range")

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
                # self.hexagons.append(Hexagon(r,c,self.can,h.x,h.y,self.size,color_all_hexes)) #weird hex positions
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

       # print(distances)
        print("hex_closest", self.hex_closest1.row, self.hex_closest1.col)
        return self.hexagons_board[distances.index(min(distances))]

    def find_circle (self, hex_center):
        inter = []
        first = []
        inter1 = []
        look_boucle1 = []
        line2 = []
        # self.glob_inter = self.hexagons_white
        for hex_center in self.hexagons_white:
            line = []
            # first = list(hex_center)
            # print("class hex",type(first))
            # first = self.hexagons_white[hex_center]
            print("Jedziemy z hex_centrem",[hex_center.row,hex_center.col])
            for k in range(len(self.glob_inter)):
                neighs = self.neighbour(hex_center)
                neighs.append(self.hexagons_white[k])
                inter = self.intersection(neighs)
                # print("class inter",type(inter))
                # print("dlugosc inter",len(inter))
                for i in inter:
                    print("inter",[i.row,i.col]) 
                # print("inter",inter)
                if len(inter) > 0: #look if i find a hex within neighbourhood of my hex. So with have got a first pair
                    line2.append(self.glob_inter)
                    look_boucle = self.intersection(inter)
                    # inter = list(inter)
                    # for i in range(len(inter)):
                    #     line.append(i)
                    line.append(self.first_hex[0])
                    for i in inter:
                        if i not in line:
                            line.append(i)
                            print("Line_first_loop", line)
                            # print("glob line", self.glob_inter)
                    # for m in line:
                    #     print("Line:",[m.row,m.col])                     
                    # for e in range(len(line)):
                    #     print("Line:",[line[e].row,line[e].col]) 
                    # for i in look_boucle:
                    #     # print("look_boucle",[i.row, i.col]) 
                    #     if look_boucle == hex_center:
                    #         break
       
                    for i in inter:
                        print("Jedziemy z inter_centrem",[i.row,i.col])
                        self.glob_inter = list(set(self.glob_inter)- set(line))
                        neighs2 = self.neighbour(i)
                        for k in range(len(self.glob_inter)):
                            # print("ktory glob hex",[self.glob_inter[k].row,self.glob_inter[k].col])
                            # neighs1 = self.neighbour(i)
                            neighs2.append(self.glob_inter[k])
                            inter1 = self.intersection(neighs2)
                            # print("dlugosc inter1",len(inter1))
                            for i in inter1:
                                print("inter1",[i.row,i.col]) 
                            for i in inter1:
                                # print("last hex_i",i)
                                # print("first hex_i",[self.first_hex[0].row,self.first_hex[0].col])
                                look_boucle = self.neighbour(i)
                                look_boucle.append(self.first_hex[0])
                                # print("loop neigh",look_boucle)
                            look_boucle1 = self.intersection(look_boucle)
                            # for i in range(len(look_boucle1)):
                            #     print("loop last",look_boucle1[i])
                            # for i in look_boucle1:
                            #     # print("loop last",i) 
                            #     # print("loop wdwd",look_boucle1)

                            check_tail = []
                            tail_hood1 = []
                            tail_hood = []
                            for i in range(len(line)-6):
                                tail_hood1 = self.neighbour(line[i])
                                # print("YWhich i in tailhood",i)
                                # print("Yupi! tail hood",tail_hood1)
                                if tail_hood1 not in tail_hood:
                                    for i in tail_hood1:
                                        tail_hood.append(i)
                                    tail_hood.append(line[-1])
                                    # tail_hood = self.neighbour(line[i])
                                    # for i in tail_hood:
                                        # print("Yupi!2 tail hood",[i.row,i.col])
                                    # tail_hood=set(tail_hood)
                                    check_tail = self.intersection(tail_hood)
                                    # print("Yupi! checktail",check_tail) 
                                    # for i in line[-1:]:
                                        # print("Yupi! last line hex",[i.row,i.col])
                                    # for i in check_tail:
                                    #     print("Yupi! check_tail done",[i.row,i.col])
                            if len(check_tail)>0 and len(line)>5:
                                print("Yupi! La boucle est bouclee") 
                                self.loop_on = 1
                                print("loop is on",self.loop_on)

                            # if line[-1:] == self.intersection(look_boucle1):
                            #     print("Olek miales racje")
                            if self.first_hex[0] == look_boucle1 and len(line)>6:
                                print("La boucle est bouclee")
                                self.loop_on = 1
                                print("loop is on",self.loop_on)
                                break
                            if len(inter1)>0  and inter1 not in line:
                                inter = inter1
                                for i in inter:
                                    # if i not in line:
                                    line.append(i)
                                    for i in line:
                                        print("Line",[i.row,i.col] )
                                self.glob_line = line
                                    # print("glob line", self.glob_inter)
                                            
                                # for k in range(len(line)):
                                #     print("Line:",[line[k].row,line[k].col]) 
                                # for k in line:
                                #     print("Line:",[k.row,k.col]) 
                        
    def center_loop (self, hex_center):
        my_center = []
        for hex_center in self.glob_line:
            for i in range(len(self.glob_line)):
                print("int hex",hex_center)
                my_center_row = sum(hex_center.row)
                # my_center_col = (sum(self.glob_line[i].col))/len(self.glob_line) 
                # my_center.append([int(round(my_center_row)),int(round(my_center_col))])
                # print("my_loop_center",[my_center_row, my_center_col])
                print("my_loop_center",[my_center_row])
                # print("my_loop_center",my_center)
                # int(round(x))


    def flood_fill (self, hex_center,neighs):
        flag_neigh = 0
        neigh = []
        check = []
        # for i in neighs:
       
        while flag_neigh != 1:
            for a in range(len(neighs)):
                check = numpy.concatenate(([neighs[a], self.hexagons_board]), axis=None)
                # print("check",check)
                # for b in range(len(self.hexagons_board)):
                # check.append(self.hexagons_board[b])
                if self.intersection(check) == 0:
                    print("Flooded")
                    flag_neigh = 1
                    break
                else:
                    print("La boucle est bouclée!!")
            for i in range(len(neighs)):
                [neighs[i]].append(self.hexagons_board)
                print("neighs[i]",neighs[i])
                if self.intersection([neighs[i]]) == 0:
                    print("La boucle est bouclée!!")
                    flag_neigh = 1
                    break
            for k in hex_center:
                # for i in range(len(self.hexagons_board)):
                neigh = self.neighbour(k)
                for i in neigh:
                    if i.color == k.color or i.color == "" and i not in neighs:
                        neighs.append(i)
                        print("neighs",[i.row,i.col])                           
                    else:
                        flag_neigh = 1
                        break
            for neighs in range(6):
                self.flood_fill(self.hexagons_board,neighs)



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
                        # print("prezesie, sprawdzam wszystkie hexes_white",[self.hexagons_white[k].row, self.hexagons_white[k].col])
                        # white = []
                        
                # does not read whole set, just next clicked white tile          
                            
                        # self.len_diag3 = 0
                        # for h in range(4):
                            # print("print 4 times")
                        # print("eveveven",self.hexagons_white)
                        if self.hexagons_white[k].col == hex_center.col + h[i] and self.hexagons_white[k].row == hex_center.row +z[i] and self.hexagons_white[k] not in white:
                            
                            # print("print olek 4 times")
                            # print("hexes_orig",[hex_center.row, hex_center.col])
                            # print("hexes_white",[self.hexagons_white[k].row, self.hexagons_white[k].col])
                            # print("nowenowen",[self.hexagons_white[k].col,self.hexagons_white[k].row])
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
                    # print("nietei33=",o)
                    # print("nietehi33",j[o])
                    # print("zet minus",z[o])
                    for t in range(len(self.hexagons_white)):
                        # white = []
                        # print("prezesie, sprawdzam wszystkie hexes_white",[self.hexagons_white[t].row, self.hexagons_white[t].col])

                            # print("oddn",self.hexagons_white)
                            # for j in range(4):
                        if self.hexagons_white[t].col == hex_center.col + j[o] and self.hexagons_white[t].row == hex_center.row + z[o] and self.hexagons_white[t] not in white:
                            white.append(self.hexagons_white[t])
                            # print("o=",o)
                            # print("jo",j[o])                           
                            if len(white) > 3:
                                print("You won! - white.dir3") 
                                for i in range(len(white)):
                                    print("white_list",[white[i].row,white[i].col])   

    def diag3_line5_black (self, hex_center):
        # black = []
        # z = -1
        h = [1,1,2,2]
        j = [0,1,1,2]
        z = [-1,-2,-3,-4]
        
        for hex_center in self.hexagons_black:
            black = []
            # print("SPRAWDZAMY PASSE dla:",[hex_center.row, hex_center.col])
            # z = -1
            if hex_center.row % 2 == 0:
                for i in range(4):
                    # print("tei33=",i)
                    # print("tehi33",h[i])
                    for k in range(len(self.hexagons_black)):
                        # print("prezesie, sprawdzam wszystkie hexes_black",[self.hexagons_black[k].row, self.hexagons_black[k].col])
                        # black = []
                        
                # does not read whole set, just next clicked black tile          
                            
                        # self.len_diag3 = 0
                        # for h in range(4):
                            # print("print 4 times")
                        # print("eveveven",self.hexagons_black)
                        if self.hexagons_black[k].col == hex_center.col + h[i] and self.hexagons_black[k].row == hex_center.row +z[i] and self.hexagons_black[k] not in black:
                            
                            # print("print olek 4 times")
                            # print("hexes_orig",[hex_center.row, hex_center.col])
                            # print("hexes_black",[self.hexagons_black[k].row, self.hexagons_black[k].col])
                            # print("nowenowen",[self.hexagons_black[k].col,self.hexagons_black[k].row])
                            black.append(self.hexagons_black[k])
                            # print("print len blak",len(black))
                            # print("i33=",i)
                            # print("hi33",h[i])
                            # print("self.len_diag33=",self.len_diag3) 
                            # z -= 1
                            if len(black) > 3:
                                print("You won! - black.dir_3")  
                                for p in range(len(black)):
                                    print("blaczek33",[black[p].row,black[p].col]) 
                                    # if black[i].row % 2 == 0:
            else:   
                for o in range(4):
                    # z = -1
                    # print("nietei33=",o)
                    # print("nietehi33",j[o])
                    # print("zet minus",z[o])
                    for t in range(len(self.hexagons_black)):
                        # black = []
                        # print("prezesie, sprawdzam wszystkie hexes_black",[self.hexagons_black[t].row, self.hexagons_black[t].col])

                            # print("oddn",self.hexagons_black)
                            # for j in range(4):
                        if self.hexagons_black[t].col == hex_center.col + j[o] and self.hexagons_black[t].row == hex_center.row + z[o] and self.hexagons_black[t] not in black:
                            black.append(self.hexagons_black[t])
                            # print("o=",o)
                            # print("jo",j[o])
                            # print("self.len_diag3=",self.len_diag3) 
                            
                            if len(black) > 3:
                                print("You won! - black.dir_3") 
                                for i in range(len(black)):
                                    print("blaczek",[black[i].row,black[i].col])                                  

    def click_pos (self, event):
  
        new1 = []
        xy = (event.x, event.y)
        hex_closest = self.closest_hex(xy)
        # if self.start == 1:
        for i in self.first_n:
            if hex_closest == i and hex_closest not in self.hex_glob:
                self.hex_glob.append(hex_closest)  
                # print("type of hex_glob",type(self.hex_glob))           
                        #    print("type hex closest :",type(hex_closest)) 
                self.list_of_neigh = self.neighbour(hex_closest)
       #         print("list_of_neigh",self.list_of_neigh)
                for i in self.neighbour(hex_closest):
                    self.neigh_append.append(i)
                # self.neigh_append.append(self.neighbour(hex_closest))
     #           print("neigh_append",self.neigh_append)
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
                    if len(self.hexagons_white)>2:
                        # self.glob_inter = self.hexagons_white
                        for i in range(len(self.hexagons_black)):
                            self.flood_fill(self.hexagons_black,self.hexagons_black)
                            # if self.loop_on == 1:
                            #     print("found a loop =", self.loop_on)
                    if self.loop_on == 1:
                        print("found a loop =", self.loop_on)
                        for i in self.glob_line:
                            self.center_loop(i)                 
                else:
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
                    # if len(self.hexagons_black)>2:
                    #     # self.glob_inter = self.hexagons_white
                    #     for i in range(len(self.hexagons_white)):
                    #         self.flood_fill(self.hexagons_white)
                # self.start = 0
            # else:
            #     print("Impossible move")                  
    
    def intersection (self,seq):
        # hexes_neigh = []
        seen = set()
        seen_add = seen.add
        # adds all elements it doesn't know yet to seen and all other to seen_twice
        hexes_neigh = set( x for x in seq if x in seen or seen_add(x) )
        # turn the set into a list (as requested)

        # print("hexes_neigh",hexes_neigh) 
        return hexes_neigh

# root = Tk()
# root.update()
