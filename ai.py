# from app import*
import random
import math

class Board():
    def __init__(self, hexagon, depth, player,score,possible_moves,player_hexes):
        self.hexagon = hexagon
        self.depth = depth
        self.player = player
        self.player_hexes = player_hexes
        # self.game_over = 0
        self.score = score
        self.possible_moves = possible_moves

    def intersection (self,seq):
        # d = Counter(seq)
        res=[seq[i] for i in range(len(seq)) if seq[i] in seq[:i]][1:]
        # res = [k for k, v in d.items() if v > 1]
        # hexes_neigh = list(hexes_neigh)
        return res

    # def intersection (self,seq):
    #     seen = set()
    #     seen_add = seen.add
    #     hexes_neigh = [ x for x in seq if x in seen or seen_add(x) ]
    #     # hexes_neigh = list(hexes_neigh)
    #     return hexes_neigh

    def neighbour (self, hex_center, hexagons_board):

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
        # print("Olek Hex_neighs from neghbours fnc", hex_neighbs)       
        return hex_neighbs

    def possible_move (self,board,hexagons_board):
        all_neighs = []

        for i in self.player_hexes:
            all_neighs.append(self.neighbour(i,hexagons_board))
        possible_move = self.intersection(all_neighs)
        for i in range(len(possible_move)):
            print("possible_movess",possible_move[i]) 
        return possible_move
    
    def child (self,board,move,hexagons_board):
        child_player_hexes = board.player_hexes
        child_player_hexes.append(move)
        child_depth = board.depth + 1
        child_hexagon = move
        if board.player:
            child_player = False
        else:
            child_player = True
        child_score = random.randint(1,101)
        child_possible_moves = self.possible_move(child_player_hexes,hexagons_board)
        final_child = Board(child_hexagon,child_depth,child_player,child_score,child_possible_moves,child_player_hexes)
        print("child_ai",final_child) 
        return final_child




