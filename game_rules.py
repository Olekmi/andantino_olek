import draw

def diag1_line5 (hex_center, colour):
    j = [-1,-2,-3,-4]
    x0 = 0
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    if len(colour)==1:
        return 0 
    for hex_center in colour:
        hexes = []
        for i in range(4):
            for k in range(len(colour)):
                if colour[k].col == hex_center.col + j[i] and colour[k].row == hex_center.row and colour[k] not in hexes:
                    hexes.append(colour[k])
                    if len(hexes) == 1:
                        x1 = len(hexes)
                    if len(hexes) == 2:
                        x2 = len(hexes)
                    if len(hexes) == 3:
                        x3 = len(hexes)
                    if len(hexes) == 4:
                        x4 = len(hexes)
                    if len(hexes) == 0:
                        x0 = len(hexes)                    
                    if len(hexes) > 3:
                        print("You won! - dir_1")
                        break  
                        # for p in range(len(hexes)):
                        #     print("the winning line",[hexes[p].row,hexes[p].col]) 
        max_line = max(x0,x1,x2,x3,x4)     
    return max_line                            

def diag2_line5 (hex_center, colour):
    h = [-1,-1,-2,-2]
    j = [0,-1,-1,-2]
    z = [-1,-2,-3,-4]
    x0 = 0
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    if len(colour)==1:
        return 0
    for hex_center in colour:
        hexes = []
        if hex_center.row % 2 == 0:   
            for i in range(4):
                for k in range(len(colour)):
                    if colour[k].col == hex_center.col + j[i] and colour[k].row == hex_center.row +z[i] and colour[k] not in hexes:
                        hexes.append(colour[k])
                        if len(hexes) == 1:
                            x1 = len(hexes)
                        if len(hexes) == 2:
                            x2 = len(hexes)
                        if len(hexes) == 3:
                            x3 = len(hexes)
                        if len(hexes) == 4:
                            x4 = len(hexes)
                        if len(hexes) == 0:
                            x0 = len(hexes)                        
                        if len(hexes) > 3:
                            print("You won! - dir_2")
                            break  
                            # for p in range(len(hexes)):
                                # print("the winning line",[hexes[p].row,hexes[p].col]) 
        else:
            for o in range(4):
                for t in range(len(colour)):
                    if colour[t].col == hex_center.col + h[o] and colour[t].row == hex_center.row + z[o] and colour[t] not in hexes:
                        hexes.append(colour[t])
                        if len(hexes) == 1:
                            x1 = len(hexes)
                        if len(hexes) == 2:
                            x2 = len(hexes)
                        if len(hexes) == 3:
                            x3 = len(hexes)
                        if len(hexes) == 4:
                            x4 = len(hexes)
                        if len(hexes) == 0:
                            x0 = len(hexes)                                            
                        if len(hexes) > 3:
                            print("You won! - dir2") 
                            break
                            # for i in range(len(hexes)):
                                # print("the winning line",[hexes[i].row,hexes[i].col]) 
        max_line = max(x0,x1,x2,x3,x4)     
    return max_line                                                              

def diag3_line5 (hex_center, colour):
    h = [1,1,2,2]
    j = [0,1,1,2]
    z = [-1,-2,-3,-4]
    x0 = 0
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    if len(colour)==1:
        return 0
    for hex_center in colour:
        hexes = []
        if hex_center.row % 2 == 0:
            for i in range(4):
                for k in range(len(colour)):
                    if colour[k].col == hex_center.col + h[i] and colour[k].row == hex_center.row +z[i] and colour[k] not in hexes:
                        hexes.append(colour[k])
                        if len(hexes) == 1:
                            x1 = len(hexes)
                        if len(hexes) == 2:
                            x2 = len(hexes)
                        if len(hexes) == 3:
                            x3 = len(hexes)
                        if len(hexes) == 4:
                            x4 = len(hexes)
                        if len(hexes) == 0:
                            x0 = len(hexes)
                        if len(hexes) > 3:
                            print("You won! -dir_3")  
                            # for p in range(len(hexes)):
                                # print("the winning line",[hexes[p].row,hexes[p].col])
                            break 
        else:   
            for o in range(4):
                for t in range(len(colour)):
                    if colour[t].col == hex_center.col + j[o] and colour[t].row == hex_center.row + z[o] and colour[t] not in hexes:
                        hexes.append(colour[t])
                        if len(hexes) == 0:
                            x0 = len(hexes)
                        if len(hexes) == 1:
                            x1 = len(hexes)
                        if len(hexes) == 2:
                            x2 = len(hexes)
                        if len(hexes) == 3:
                            x3 = len(hexes)
                        if len(hexes) == 4:
                            x4 = len(hexes)                      
                        if len(hexes) > 3:
                            print("You won! - dir_3") 
                            # for i in range(len(hexes)):
                                # print("the winning line",[hexes[i].row,hexes[i].col])
                            break
        max_line = max(x0,x1,x2,x3,x4)     
    return max_line                        
#encicrling the opponent winning condition
def flood_fill (hex_center,prev_hexes, player, hexagons_board):
    neigh = []
    
    if len(draw.neighbour(hex_center,hexagons_board)) < 6:
        return True
    if hex_center in player:
        return False
    if  hex_center in prev_hexes:      
        return False
    else:
        prev_hexes.append(hex_center) 
        for neigh in draw.neighbour(hex_center,hexagons_board):
            if flood_fill(neigh,prev_hexes,player,hexagons_board):
                return True
    return False
                

