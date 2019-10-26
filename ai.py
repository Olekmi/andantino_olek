import random
import math
from collections import Counter
import numpy as np
import config
import board
from operator import itemgetter

def MinMax (position,depth, alpha,beta,max_player,hexagons_board): 
    # print("depth",depth)
    if depth == 0:# or self.game_over == 1:
        # print("position.score",position.score)
        # print("position.hexagon",[position.hexagon.row, position.hexagon.col])        
        return position.score, position.hexagon#he becomes a board instead of a new hex
    target = []    
    
    if max_player:
        score = -math.inf
        sorted_children = []
        get_board = []
        for possible_move in position.possible_moves:
            sorted_children.append(position.child(position,possible_move,hexagons_board))   
        # get_board = sorted(sorted_children,key=itemgetter(position.score))
        # sorted_children.sort(key=position.score)
        # sorted_children.sort()
        sorted_children.sort(key=lambda x: x.score, reverse=True)
        # To return a new list, use the sorted() built-in function...
        get_board = sorted(sorted_children, key=lambda x: x.score, reverse=True)
        for possible_board in get_board:# .child(position,possible_moves): #i put the board as position and children are the possible moves
            # new_child = position.child(position, possible_move, hexagons_board)#new board
            value, best_move = MinMax(possible_board,depth-1, alpha,beta,False,hexagons_board)
            # print("value-min",value)
            if value > score:
                score = value
                target = possible_move
                alpha = max(alpha, score)
                if (beta <= alpha):# and (config.depth == depth):
                    target = possible_move
                    # print("target",target)
                    break
        # print("target",[target.row,target.col])
        # print("score max",score)       
        return score, target
    else:
        score = math.inf
        sorted_children = []
        for possible_move in position.possible_moves:
            sorted_children.append(position.child(position,possible_move,hexagons_board))   
        sorted_children.sort(key=lambda x: x.score, reverse=True)
        # To return a new list, use the sorted() built-in function...
        get_board = sorted(sorted_children, key=lambda x: x.score, reverse=True)       
        for possible_board in get_board:
            # new_child = position.child(position, possible_move,hexagons_board)
            value, child = MinMax(possible_board,depth-1, alpha,beta,True,hexagons_board)
            # print("value-max",value)
            if value < score:
                score = value
                target = possible_move
                beta = min(beta,score)
                if (beta <= alpha):# and (config.depth == depth):
                    break
        # print("target",[target.row,target.col])
        # print("score min",score)
        return score, target
