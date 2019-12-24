import random
import math
from collections import Counter
import numpy as np
import config
import board
from operator import itemgetter

class Ai ():
    def __init__(self,target):
        self.target = target

    def set_target(self, target):
        self.target = target

Ai_move = Ai(1)


def MinMax (position,depth, alpha,beta,max_player,hexagons_board): 
    global Ai_move
    if depth == 0 or position.game_over == 1:    
        return position.score
     
    if max_player:
        score = -math.inf
        sorted_children = []
        get_board = []
        if not position.game_over: #thanks to it when there's game_over it doesn't search anymore        
            for possible_move in position.possible_moves:

                sorted_children.append(position.child(position,possible_move,hexagons_board))   
        if depth < config.depth:        
            sorted_children.sort(key=lambda x: x.score, reverse=True)
            # To return a new list, use the sorted() built-in function...
            # get_board = sorted(sorted_children, key=lambda x: x.score, reverse=True)
            for possible_board in sorted_children:
                print("poss")
                # print("possible_board", possible_board.row," ", move.col,"\n")
                # new_child = position.child(position, possible_move, hexagons_board)#new board
                value = MinMax(possible_board,depth-1, alpha,beta,False,hexagons_board)
                if value > score:
                    score = value
                    alpha = max(alpha, score)
                    target = possible_board.hexagon
                    Ai_move.set_target(target)                    
                if (beta <= alpha):# and (config.depth == depth):
                    # target = possible_board.hexagon
                    # Ai_move.set_target(target)
                    break    
            target = possible_board.hexagon
            Ai_move.set_target(target)           
            return score
        else:
            for possible_board in sorted_children:
                # new_child = position.child(position, possible_move, hexagons_board)#new board
                value = MinMax(possible_board,depth-1, alpha,beta,False,hexagons_board)
                if value > score:
                    score = value

                    alpha = max(alpha, score)
                    target = possible_board.hexagon
                    Ai_move.set_target(target)
                if (beta <= alpha):# and (config.depth == depth):
                    # target = possible_board.hexagon
                    # Ai_move.set_target(target)
                    break    
            target = possible_board.hexagon
            Ai_move.set_target(target)                                       
            return score 

    else:
        score = math.inf
        sorted_children = []
        if not position.game_over:        
            for possible_move in position.possible_moves:
            # if not position.game_over:
                sorted_children.append(position.child(position,possible_move,hexagons_board))  
        if depth < config.depth:           
            sorted_children.sort(key=lambda x: x.score, reverse=False)
            # get_board = sorted(sorted_children, key=lambda x: x.score, reverse=False)       
            for possible_board in sorted_children:
                # new_child = position.child(position, possible_move,hexagons_board)
                value = MinMax(possible_board,depth-1, alpha,beta,True,hexagons_board)
                if value < score:
                    score = value

                    beta = min(beta,score)
                    target = possible_board.hexagon
                    Ai_move.set_target(target)
                if (beta <= alpha):# and (config.depth == depth):
                    # target = possible_board.hexagon
                    # Ai_move.set_target(target)
                    break    
            target = possible_board.hexagon
            Ai_move.set_target(target)                                     
            return score
        else:
            for possible_board in sorted_children:
            # new_child = position.child(position, possible_move,hexagons_board)
                value = MinMax(possible_board,depth-1, alpha,beta,True,hexagons_board)
                if value < score:
                    score = value

                    beta = min(beta,score)
                    target = possible_board.hexagon
                    Ai_move.set_target(target)   
                if (beta <= alpha):# and (config.depth == depth):
                    # target = possible_board.hexagon
                    # Ai_move.set_target(target)
                    break     
            target = possible_board.hexagon
            Ai_move.set_target(target)                                   
            return score

def NegaMax (position,depth, alpha,beta,max_player,hexagons_board): 
    if depth == 0 or position.game_over == 1:    
        return position.score, position.hexagon      
    best_move = [] 
    best_score = -math.inf
    for possible_move in position.possible_moves:
        new_child = position.child(position, possible_move, hexagons_board)#new board
        value, current_move = MinMax(new_child,depth-1, alpha,beta,False,hexagons_board)
        current_score = -value
        if current_score > best_score:
            best_score = current_score
            best_move = possible_move
            if (beta <= best_score):# and (config.depth == depth):
                return best_score, best_move  
    return best_score, best_move
