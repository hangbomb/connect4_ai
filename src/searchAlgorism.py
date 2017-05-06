#-*- coding: utf-8 -*-
from setting import *

def checkWin(one, two, three, four, man):
    o_man = getOpponent(man)
    score=0
    if(one != o_man and two != o_man and three != o_man and four != o_man):
        count = 0
        if one == man:
            count += 1
        if two == man:
            count += 1
        if three == man:
            count += 1
        if four == man:
            count += 1

        if count == 4:
            score += WIN

        #50 for three Xs, no Os
        elif count == 3:
            score += 50

        #10 for two Xs, no Os
        elif count == 2:
            score += 10

        #1 for one Xs, no Os
        elif count == 1:
            score += 1

            
    return score
    
def winChance(board, man):
    o_man = getOpponent(man)
    score = 0
    for column in range(board.width):
        for row in range(board.height):
            # Horizonatal - evaluation
            try:
                #checkWin에서 score 계산(현재 player('O' 기준))
                t_score = checkWin(board[row][column], board.board[row][column+1], board.board[row][column+2], board.board[row][column+3], man)
#                print('hor man')
                if t_score >= WIN:
                    return WIN
                score += t_score
                #checkWin에서 score 계산(상대 player('X' 기준))
                t_score = checkWin(board.board[row][column], board.board[row][column+1], board.board[row][column+2], board.board[row][column+3], o_man)
#                print('hor oman')
                if t_score >= WIN:
                    return LOSE
                score -= t_score

            except:
                pass

            # Vertical | evaluation
            try:
                t_score = checkWin(board.board[row][column], board.board[row+1][column], board.board[row+2][column], board.board[row+3][column], man)
#                print('ver man')
                if t_score >= WIN:
                    return WIN
                score += t_score
                t_score = checkWin(board.board[row][column], board.board[row+1][column], board.board[row+2][column], board.board[row+3][column], o_man)
#                print('ver oman')
                if t_score >= WIN:
                    return LOSE
                score -= t_score

            except:
                pass

            # Diagonal \ evaluation
            try:
                t_score = checkWin(board.board[row][column], board.board[row+1][column+1], board.board[row+2][column+2], board.board[row+3][column+3], man)
#                print('\ man')
                if t_score >= WIN:
                    return WIN
                score += t_score
                t_score = checkWin(board.board[row][column], board.board[row+1][column+1], board.board[row+2][column+2], board.board[row+3][column+3], o_man)
#                print('\ oman')
                if t_score >= WIN:
                    return LOSE
                score -= t_score
            except:
                pass

            # Diagonal / evaluation
            try:
                t_score = checkWin(board.board[row][column], board.board[row+1][column-1], board.board[row+2][column-2], board.board[row+3][column-3], man)
#                print('/ man')
                if t_score >= WIN:
                    return WIN
                score += t_score
                t_score = checkWin(board.board[row][column], board.board[row+1][column-1], board.board[row+2][column-2], board.board[row+3][column-3], o_man)
#                print('/ oman')
                if t_score >= WIN:
                    return LOSE
                score -= t_score
            except:
                pass

    #plus a move bonus depending on whose turn it is to play            
    #if man == 'O':
    #    score += 16
    #else:
    #    score -= 16
    return score

def minMax(board, player, alpha, beta, depth):
    if board.checkPlay() or depth == 0:
        return winChance(board, 'O')

    for move in board.canPut():
        board.put(move, player)
        score = minMax(board, getOpponent(player), alpha, beta, depth-1)
        board.put(move, ' ', True)
        if player == 'O':
            if score > alpha:
                alpha = score
            if alpha >= beta:
                return beta
        else:
            if score < beta:
                beta = score
            if beta <= alpha:
                return alpha

    if player == 'O':
        return alpha
    else:
        return beta
                            
