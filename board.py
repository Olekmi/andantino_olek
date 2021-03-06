
import copy
import random
import math
from collections import Counter
import numpy as np
import game_rules, config

class Board():
    def __init__(self, hexagon, depth, game_over, player1_hexes,player2_hexes,score,possible_moves,player_type):
        self.hexagon = hexagon
        self.depth = depth
        self.player1_hexes = player1_hexes
        self.player2_hexes = player2_hexes
        self.game_over = 0
        self.score = score
        self.possible_moves = possible_moves
        self.player_type = player_type
        if game_over == 1:
            self.game_over = 1
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
                if hexagons_board[j].col >= hex_center.col -1 and hexagons_board[j].row >= hex_center.row -1:
                    if hexagons_board[j].col == hex_center.col -1 and hexagons_board[j].row == hex_center.row:
                        hex_neighbs.append(hexagons_board[j])
                    if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row - 1:
                        hex_neighbs.append(hexagons_board[j])            
                    if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row + 1:
                        hex_neighbs.append(hexagons_board[j])
                    if hexagons_board[j].col == hex_center.col + 1 and hexagons_board[j].row == hex_center.row - 1:
                        hex_neighbs.append(hexagons_board[j])
                    if hexagons_board[j].col == hex_center.col + 1 and hexagons_board[j].row == hex_center.row:
                        hex_neighbs.append(hexagons_board[j])
                    if hexagons_board[j].col == hex_center.col + 1 and hexagons_board[j].row == hex_center.row + 1:
                        hex_neighbs.append(hexagons_board[j]) 
        else:
            for j in range (len(hexagons_board)):
                if hexagons_board[j].col >= hex_center.col -1 and hexagons_board[j].row >= hex_center.row -1:
                    if hexagons_board[j].col == hex_center.col - 1 and hexagons_board[j].row == hex_center.row:
                        hex_neighbs.append(hexagons_board[j])
                    if hexagons_board[j].col == hex_center.col - 1 and hexagons_board[j].row == hex_center.row - 1:
                        hex_neighbs.append(hexagons_board[j])            
                    if hexagons_board[j].col == hex_center.col - 1 and hexagons_board[j].row == hex_center.row + 1:
                        hex_neighbs.append(hexagons_board[j])
                    if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row - 1:
                        hex_neighbs.append(hexagons_board[j])
                    if hexagons_board[j].col == hex_center.col and hexagons_board[j].row == hex_center.row + 1:
                        hex_neighbs.append(hexagons_board[j])
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
            child_player_type = 1# black
        else:
            child_player_type = 0 #white

        if child_player_type == 0:
            child_p1_list.append(move)
            if len(child_p1_list) > 0:
                child_score = self.evaluation_function(child_p1_list,child_p2_list,child_p2_list,child_p1_list,hexagons_board)
                # print("child p1 lines:", child_score)
        else:
            child_p2_list.append(move)
            if len(child_p2_list) > 0:
                child_score = self.evaluation_function(child_p1_list,child_p2_list,child_p1_list,child_p2_list,hexagons_board)
                # print("child p2 lines:", child_score)
        child_depth = board.depth
        # print("child depth", board.depth)
        child_gameover = board.game_over
        # print("child game over", board.game_over) 
        child_hexagon = move
        # print("child move", move.row," ", move.col,"\n") 
        child_player_hexes = child_p1_list+child_p2_list
        child_possible_moves = self.possible_move(child_player_hexes,hexagons_board)
        final_child = Board(child_hexagon,child_depth, child_gameover, child_p1_list,child_p2_list,child_score,child_possible_moves,child_player_type)
        return final_child
# def __init__(self, hexagon, depth, player1_hexes,player2_hexes,score,possible_moves,player_hexes,player_type):

    def evaluation_function (self,player,player_hexes,second_player,first_player,hexagons_board):
        child_score = 0
        self.game_over = 0
                       
        if game_rules.diag3_line5(first_player,first_player)>1:
            # self.game_over = 1
            child_score += config.coeff_len_line*game_rules.diag3_line5(first_player,first_player)# - config.coeff_len_line*game_rules.diag3_line5(player_hexes,player_hexes)
        if game_rules.diag2_line5(first_player,first_player)>1:
            child_score += config.coeff_len_line*game_rules.diag2_line5(first_player,first_player)
            # self.game_over = 1
        if game_rules.diag1_line5(first_player,first_player)>1:
            child_score += config.coeff_len_line*game_rules.diag1_line5(first_player,first_player)
        if len(first_player)>4:
            if game_rules.diag3_line5(first_player,first_player)==4:
                self.game_over = 1
                child_score += config.coeff_win_line 
            if game_rules.diag2_line5(first_player,first_player)==4:
                self.game_over = 1
                child_score += config.coeff_win_line  
            if game_rules.diag1_line5(first_player,first_player)==4:
                self.game_over = 1
                child_score += config.coeff_win_line
            if game_rules.diag3_line5(second_player,second_player)==4:
                self.game_over = 1
                child_score -= config.coeff_losing_line 
            if game_rules.diag2_line5(second_player,second_player)==4:
                self.game_over = 1
                child_score -= config.coeff_losing_line  
            if game_rules.diag1_line5(second_player,second_player)==4:
                self.game_over = 1
                child_score -= config.coeff_losing_line            
            if self.out_of_boundaries(first_player,second_player,hexagons_board):  
                self.game_over = 1
                child_score += config.coeff_win_circle
            if self.out_of_boundaries(second_player,first_player,hexagons_board):  
                self.game_over = 1
                child_score -= config.coeff_losing_circle                      
        return child_score 

    def out_of_boundaries (self,player1,player2,hexagons_board):
        if self.player_type == 1:
            if len(player1)>5:
                for i in range(len(player2)):
                    if self.encircle_check(player2[i],player1,hexagons_board):
                        return True
        else:
            if len(player2)>5:
                for i in range(len(player1)):
                    if self.encircle_check(player1[i],player2,hexagons_board):
                        return True

    def encircle_check (self,hex_center,player,hexagons_board):
        if not game_rules.flood_fill(hex_center,[],player,hexagons_board):
            # print("encircle win!")
            return True