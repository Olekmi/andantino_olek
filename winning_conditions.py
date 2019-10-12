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
        return True
    else:
        print("keep on trying")
        return False