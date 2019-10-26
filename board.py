
import copy
import random
import math
from collections import Counter
import numpy as np
import game_rules

class Board():
    def __init__(self, hexagon, depth, player1_hexes,player2_hexes,score,possible_moves,player_type):
        self.hexagon = hexagon
        self.depth = depth
        self.player1_hexes = player1_hexes
        self.player2_hexes = player2_hexes
        # self.player_hexes = player_hexes
        # self.game_over = 0
        self.score = score
        self.possible_moves = possible_moves
        self.player_type = player_type
        if(len(player2_hexes) == 0) and (len(player1_hexes) == 0):
            self.player_hexes = player1_hexes
        else:
            self.player_hexes = player1_hexes + player2_hexes

    def intersection(self,seq):
        a = []
        for i in range(len(seq)):
            for j in range(len(seq)):
                if seq[i]==seq[j] and i!=j and seq[i] not in a:
                    a.append(seq[i])
        return a

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
        return hex_neighbs

    def add_first_hexx (self,hexagons_board):
        for i in range(len(hexagons_board)):
            if hexagons_board[i].row == 9 and hexagons_board[i].col == 10:
                self.player1_hexes = hexagons_board[i]
        return self.player1_hexes    

    def possible_move (self,board,hexagons_board):
        all_neighs = []
        possible_move_list = []
        for i in board:
            all_neighs.append(self.neighbour(i,hexagons_board))
        all_neighs = [item for sublist in all_neighs for item in sublist]
        possible_move_list = self.intersection(all_neighs)
        final_list = []
        for i in possible_move_list:
            if i not in board:
                final_list.append(i)
        return final_list

    def child (self,board,move,hexagons_board):
        child_score = 0
        child_p1_list = [] + board.player1_hexes
        child_p2_list = [] + board.player2_hexes
        if(board.player_type == 0):
            child_player_type = 1# white
        else:
            child_player_type = 0 #black

        if child_player_type == 0:
            child_p1_list.append(move)
            if len(child_p1_list) > 0:
                child_score = self.evaluation_function(child_p1_list,child_p1_list)
        else:
            child_p2_list.append(move)
            if len(child_p2_list) > 0:
                child_score = self.evaluation_function(child_p2_list,child_p2_list)
        child_depth = board.depth 
        child_hexagon = move
        child_player_hexes = child_p1_list+child_p2_list
        child_possible_moves = self.possible_move(child_player_hexes,hexagons_board)
        final_child = Board(child_hexagon,child_depth,child_p1_list,child_p2_list,child_score,child_possible_moves,child_player_type)
        return final_child
# def __init__(self, hexagon, depth, player1_hexes,player2_hexes,score,possible_moves,player_hexes,player_type):

    def evaluation_function (self,player,player_hexes,second_player,hexagons_board):
        child_score = 0

        if game_rules.diag3_line5(player,player_hexes)==4:
            child_score += 100
        if game_rules.diag2_line5(player,player_hexes)==4:
            child_score += 100  
        if game_rules.diag1_line5(player,player_hexes)==4:
            child_score += 100                      
        if game_rules.diag3_line5(player,player_hexes)>0:
            child_score += 10*game_rules.diag3_line5(player,player_hexes)
        if game_rules.diag2_line5(player,player_hexes)>0:
            child_score += 10*game_rules.diag3_line5(player,player_hexes)
        if game_rules.diag1_line5(player,player_hexes)>0:
            child_score += 10*game_rules.diag3_line5(player,player_hexes)
        if not game_rules.flood_fill(second_player,[],player,hexagons_board):  
            child_score += 100                      
        else:
            child_score = 0
        return child_score

    def out_of_boundaries (self,hex_center,player,hexagons_board):
        if not game_rules.flood_fill(hex_center,[],player,hexagons_board):
            print("WIN!!!!!!!!!!!!!!!!")
            print("check",[hex_center.row,hex_center.col])
            return True
        else:
            # print("keep on trying")
            return False    



def move(self, hex,pawns):
    if hex in self.get_possible_moves(pawns):
        if(self.player_type == 0):
            child_player_type = 1# white
        else:
            child_player_type = 0 #black

        if child_player_type == 0:
            self.player1_hexes.append(hex)
#            for i in child_p1_list:
#                print("child list p1",[i.row,i.col])
        else:
            self.player2_hexes.append(hex)


def get_children(self,board,hexagons_board):
    children = []
    for possible_move in self.get_possible_moves(board,hexagons_board):
        child = copy.deepcopy(self)
        child.move(possible_move)
        children.append(child)
    return children

def get_possible_moves(self,board,hexagons_board):
    possible_moves = []
    all_neighs = []
    for i in board:
        all_neighs.append(self.neighbour(i,hexagons_board))
    all_neighs = [item for sublist in all_neighs for item in sublist]
    possible_move_list = self.intersection(all_neighs)
    possible_moves = []
    for i in possible_move_list:
        if i not in board:
            possible_moves.append(i)
    return possible_moves

