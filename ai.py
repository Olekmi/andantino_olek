# from app import*
import random
import math
from collections import Counter
import numpy as np
import board

def MinMax (position,depth, alpha,beta,max_player,hexagons_board): 
    # print("depth",depth)
    if depth == 0:# or self.game_over == 1:
        return position.score, position.hexagon
    target = []    
    print("depth", depth)
    if max_player:
        # try:
        score = -math.inf
        for i in range(len(position.possible_moves)):# .child(position,possible_moves): #i put the board as position and children are the possible moves
            new_child = position.child(position,position.possible_moves[i],hexagons_board)
            # max_player = False
            value, child = MinMax(new_child,depth-1, alpha,beta,False,hexagons_board)
            # print("value-min",value)
            if value > score:
                score = value
#                if depth == 2:
#                    target = position.possible_moves[i]
                # if depth == 2:
                #     target = position.possible_moves[i]
                target = position.possible_moves[i]
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return score, target
        # except Exception as e:
        #     print("error in max:",e)
    else:
        # try:

        score = math.inf
        for i in range(len(position.possible_moves)):
#            print(type(position.possible_moves[i]))
            # print("call from minimax min part")
            # for j in position.player_hexes:
            #     print(type(j))
            # print("done")
            # max_player = True
            new_child = position.child(position,position.possible_moves[i],hexagons_board)
            # print("newchild",new_child)
            value, child = MinMax(new_child,depth-1, alpha,beta,True,hexagons_board)
            # print("value-max",value)
            if value < score:
                score = value
#                print("possible moves i",i)
#                print(len(position.possible_moves))
#                if depth == 2:
#                    target = position.possible_moves[i]
                target = position.possible_moves[i]
                # if depth == 2:
                #     target = position.possible_moves[i]
                beta = min(beta,score)
                if beta <= alpha:
                    break
        return score, target
        # except Exception as e:
        #     print("error in min:",e)
    # print("score",score)
    # print("value",value)
    # print("newchild",new_child)
    # print("positionscore",position.score)
    # print("scoretyp",type(score))
    # return score, target

def evaluate (hex_center):
    hex_center = random.randint(1,101)
    return hex_center








