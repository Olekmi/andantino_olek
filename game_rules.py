import draw

def diag1_line5 (hex_center, colour):
    j = [-1,-2,-3,-4]
    for hex_center in colour:
        hexes = []
        for i in range(4):
            for k in range(len(colour)):
                if colour[k].col == hex_center.col + j[i] and colour[k].row == hex_center.row and colour[k] not in hexes:
                    hexes.append(colour[k])
                    if len(hexes) > 3:
                        print("You won! - dir_1")  
                        for p in range(len(hexes)):
                            print("the winning line",[hexes[p].row,hexes[p].col]) 

def diag2_line5 (hex_center, colour):
    h = [-1,-1,-2,-2]
    j = [0,-1,-1,-2]
    z = [-1,-2,-3,-4]
    for hex_center in colour:
        hexes = []
        if hex_center.row % 2 == 0:   
            for i in range(4):
                for k in range(len(colour)):
                    if colour[k].col == hex_center.col + j[i] and colour[k].row == hex_center.row +z[i] and colour[k] not in hexes:
                        hexes.append(colour[k])
                        if len(hexes) > 3:
                            print("You won! - dir_2")  
                            for p in range(len(hexes)):
                                print("the winning line",[hexes[p].row,hexes[p].col]) 
        else:
            for o in range(4):
                for t in range(len(colour)):
                    if colour[t].col == hex_center.col + h[o] and colour[t].row == hex_center.row + z[o] and colour[t] not in hexes:
                        hexes.append(colour[t])                    
                        if len(hexes) > 3:
                            print("You won! - dir2") 
                            for i in range(len(hexes)):
                                print("the winning line",[hexes[i].row,hexes[i].col])                                      

def diag3_line5 (hex_center, colour):
    h = [1,1,2,2]
    j = [0,1,1,2]
    z = [-1,-2,-3,-4]
    
    for hex_center in colour:
        hexes = []
        if hex_center.row % 2 == 0:
            for i in range(4):
                for k in range(len(colour)):
                    if colour[k].col == hex_center.col + h[i] and colour[k].row == hex_center.row +z[i] and colour[k] not in hexes:
                        hexes.append(colour[k])
                        if len(hexes) > 3:
                            print("You won! -dir_3")  
                            for p in range(len(hexes)):
                                print("the winning line",[hexes[p].row,hexes[p].col]) 
        else:   
            for o in range(4):
                for t in range(len(colour)):
                    if colour[t].col == hex_center.col + j[o] and colour[t].row == hex_center.row + z[o] and colour[t] not in hexes:
                        hexes.append(colour[t])
                        if len(hexes) > 3:
                            print("You won! - dir_3") 
                            for i in range(len(hexes)):
                                print("the winning line",[hexes[i].row,hexes[i].col])     
#encicrling the opponent winning condition
def flood_fill (hex_center,prev_hexes, player, hexagons_board):
    neigh = []
    
    if len(draw.neighbour(hex_center,hexagons_board)) < 6:
        # print("hex_center flood",[hex_center.row,hex_center.col])
        return True
    if hex_center in player:
        # print("hex_center in self.hexagons_ play on!")
        return False
    if  hex_center in prev_hexes:
        # print("hex_center in prev_hexes play on!")            
        return False
    else:
        prev_hexes.append(hex_center) 
        # print("hex center",[hex_center.row,hex_center.col])
        for neigh in draw.neighbour(hex_center,hexagons_board):
            # print("neigh",[neigh.row,neigh.col])
            if flood_fill(neigh,prev_hexes,player,hexagons_board):
                return True
    return False
                

