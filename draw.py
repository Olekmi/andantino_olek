from math import cos, sin,radians,sqrt
import config

def draw_corners (fill,outline,canvas,start_x,start_y):
    coords = []
    for j in range(6) :
        end_x = start_x + config.size * cos(radians(60 * j-30))
        end_y = start_y + config.size * sin(radians(60 * j-30))
        coords.append([start_x, start_y])
        start_x = end_x
        start_y = end_y
    newcoords = canvas.create_polygon(coords[0][0],
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
                            fill=fill,
                            outline=outline,
                            tags="{}.{}".format("test", "tsst"))

def draw_board(canvas,hexagons_board,size):    
    for i in range(len(hexagons_board)):
        
        start_x = hexagons_board[i].x
        start_y = hexagons_board[i].y 
        coords = []
        draw_corners(config.fill_empty,config.outline_gray,canvas,start_x,start_y)

def draw_player(canvas,hexagons_board,size):      #layer of white hexes
    start_x = 0
    start_y = 0
    state = 0  
    hex_append = []
    start_order = int(input("I will ask you twice, make sure to answer the same: Enter '1' if you want to start 1st, '2' if second: "))
    if start_order == 1:
        state = 0
    else:
        state = 1
    for i in range(len(hexagons_board)):
        if hexagons_board[i].row == 9 and hexagons_board[i].col == 10:
            start_x = hexagons_board[i].x 
            start_y = hexagons_board[i].y
            hex_append.append([start_x, start_y])
            first_neighs = neighbour(hexagons_board[i],hexagons_board)
            draw_neighb(canvas,first_neighs,size) 
            draw_n_first_hex (first_neighs,canvas)
    if state == 0:        
        draw_corners(config.fill_white,config.outline_gray,canvas,start_x,start_y)
    else:
        draw_corners(config.fill_black,config.outline_gray,canvas,start_x,start_y)        

def sub_first_hex (hex,canvas):#subtractes the first drawn neighbours
    draw_board(canvas,hex,config.size) 
    return hex

def draw_n_first_hex (hex,canvas):
    elo = set(hex)
    draw_neighb(canvas,elo,config.size) 
    return elo

def draw_black(canvas,hexagon,size):      #layer of black hexes
    start_x = hexagon.x
    start_y = hexagon.y 
    coords = []
    draw_corners(config.fill_black,config.outline_gray,canvas,start_x,start_y)

def draw_neighb (canvas,neighbours, size):
    neighbours = list(neighbours)
    for i in range(len(neighbours)):
        start_x = neighbours[i].x 
        start_y = neighbours[i].y 
        coords = []
        draw_corners(config.fill_empty,config.outline_black,canvas,start_x,start_y)

def draw_white(canvas,hexagon,size):      #layer of white hexes
    start_x = hexagon.x
    start_y = hexagon.y 
    coords = []
    draw_corners(config.fill_white,config.outline_gray,canvas,start_x,start_y)



def neighbour (hex_center,hexagons_board):

    hex_neighbs = []
    if hex_center.row % 2 == 0:
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col -1 and hexagons_board[j].row == hex_center.row:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row - 1:
                hex_neighbs.append(hexagons_board[j])            
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row + 1:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col + 1 and hexagons_board[j].row == hex_center.row - 1:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col + 1 and hexagons_board[j].row == hex_center.row:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col + 1 and hexagons_board[j].row == hex_center.row + 1:
                hex_neighbs.append(hexagons_board[j]) 
    else:
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col - 1 and hexagons_board[j].row == hex_center.row:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col - 1 and hexagons_board[j].row == hex_center.row - 1:
                hex_neighbs.append(hexagons_board[j])            
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col - 1 and hexagons_board[j].row == hex_center.row + 1:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row - 1:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row + 1:
                hex_neighbs.append(hexagons_board[j])
        for j in range (len(hexagons_board)):
            if hexagons_board[j].col == hex_center.col + 1 and hexagons_board[j].row == hex_center.row:
                hex_neighbs.append(hexagons_board[j])               
    return hex_neighbs  