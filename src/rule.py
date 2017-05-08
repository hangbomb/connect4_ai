#-*- coding: utf-8 -*-
from setting import *

#RULE : 
"""
1.   내가 3개연결되어있으면 무조건 4개 되도록 놓아라  O
2.   상대편이 3개연결되어있으면 막아라 O
3.   상대편이 2개연결되어있고 양쪽이 비어 있으면 왼쪽을 막아라 (O)
4.   읽는 4칸 기준 2칸비고 교대로 상대방이면 가운데에 막아라
---->(3,4) : X(상대)가 3개가 연결될 가능성이 있으면, 막아라.
5.   내가 2개 연결된 것 있고 양 옆이 비어 있으면 왼쪽에 놓아라
6.   읽는 4칸기준 2칸비고 교대로 내꺼면 가운데에 놓아라
7.   내가 2개 연결된 것 있고 한 쪽이 막아져 여유 2칸이 있으면 놓아라
---->(5,6) : O(computer)가 3개가 연결될 가능성이 있으면, 놓아라.
8.   아무것도 없으면 가운데 놓아라
9.   5번째 가운데가 채워져 있지 않으면 가운데에 놓아라
10.  위의 해당사항 없으면 가운데와 가깝도록 놓아라(5번째 줄까지)
11.  맨 윗 줄 채워라
"""

def countConnect(one, two, three, four, man):
    o_man = getOpponent(man)
    #print("o_man : ", o_man )
    if(one != o_man and two != o_man and three != o_man and four != o_man):
        count = 0
        if one == man:
            #print('one')
            count += 1
        if two == man:
            #print('two')
            count += 1
        if three == man:
            #print('three')
            count += 1
        if four == man:
            #print('four')
            count += 1
    #print("count = ", count , "\n")
    return count

"""def getRow(board, column):
    for row in range(board.height):
        if board.board[column][row] != ' ':
            row -= 1
            return row
        elif row == 5 : 
            return row"""

def getCount(board, player) :
    o_player = getOpponent(player)
    O_count = 0
    X_count = 0
    for row in range(board.height):
        for column in range(board.width):
            # Horizonatal - evaluation
            if (column < 4) :
                try:
                    #countConnect에서 count계산(현재 player('O' 기준))
                    o_cnt = countConnect(board.board[row][column], board.board[row][column+1], board.board[row][column+2], board.board[row][column+3], player)
                    if o_cnt > O_count:
                        O_count = o_cnt
                except:
                    pass

                try:
                    #countConnect에서 x_cnt 계산(상대 player('X' 기준))
                    x_cnt = countConnect(board.board[row][column], board.board[row][column+1], board.board[row][column+2], board.board[row][column+3], o_player)
                    if x_cnt > X_count:
                        X_count = x_cnt
                except :
                    pass
            

            # Vertical | evaluation
            if (row < 3):
                try:
                    o_cnt = countConnect(board.board[row][column], board.board[row+1][column], board.board[row+2][column], board.board[row+3][column], player)
                    if o_cnt == 4:
                        O_count = o_cnt
                except:
                    pass

                try:
                    x_cnt = countConnect(board.board[row][column], board.board[row+1][column], board.board[row+2][column], board.board[row+3][column], o_player)
                    if x_cnt == 4:
                        X_count = x_cnt
                except:
                    pass

            # Diagonal \ evaluation
            if(column < 4 and row < 3) :
                try:
                    o_cnt = countConnect(board.board[row][column], board.board[row+1][column+1], board.board[row+2][column+2], board.board[row+3][column+3], player)
                    if o_cnt > O_count:
                        O_count = o_cnt
                except:
                    pass
                    
                try:
                    x_cnt = countConnect(board.board[row][column], board.board[row+1][column+1], board.board[row+2][column+2], board.board[row+3][column+3], o_player)
                    if x_cnt > X_count:
                        X_count = x_cnt
                except:
                    pass

            # Diagonal / evaluation
            if(column > 2 and row < 3 ) :
                try:
                    o_cnt = countConnect(board.board[row][column], board.board[row+1][column-1], board.board[row+2][column-2], board.board[row+3][column-3], player)
                    if o_cnt > O_count:
                        O_count = o_cnt
                except:
                    pass

                try:
                    x_cnt = countConnect(board.board[row][column], board.board[row+1][column-1], board.board[row+2][column-2], board.board[row+3][column-3], o_player)
                    if x_cnt > X_count:
                        X_count = x_cnt
                except:
                    pass

    #print("O_count= ", O_count, "X_count = ", X_count, "\n")
    return O_count, X_count

def rulePut(board,player):
    o_player = getOpponent(player)
    cnt_O = 0
    cnt_X = 0
    #rule number 1.내가 3개 연결 되어 있으면 무조건 4개 되도록 놓아라
    #넣을수 있는 자리에 나의 수를 다 넣어본다.
    for move in board.canPut():
        board.put(move, player)
        cnt_O, cnt_X = getCount(board,player)
        #넣었을때, 무조건 이기는 자리면, 그곳에 둔다
        if cnt_O == 4:
            print('O가 4개가 되기 때문에, Computer will play at square: {}'.format(move+1))
            board.put(move, ' ', True)
            return move
        #넣었을때, 무조건 이기는 자리가 아니면, 다시 빈칸으로 둔다.
        board.put(move, ' ', True)
    #2.상대편이 3개 연결 되어 있으면 막아라.
    #넣을 수 있는 자리에 상대방의 수를 다 넣어본다.    
    for move in board.canPut():
        board.put(move, o_player)
        cnt_O, cnt_X = getCount(board,player)
        print("try case 22, move = ", move)
        print(board)
        #넣었을때, 상대방이 무조건 이기는 자리면, 그곳에 두어 막는다.
        if cnt_X == 4:
            print('X가 4개가 되기 때문에, Computer will block at square: {}'.format(move+1))
            board.put(move, ' ', True)
            return move
        #Undo the move
        board.put(move, ' ', True)
    #3,4상대편이 3개가 연결될 수 있으면(4개가 될 가능성이 있는 3개) 막아라.
    #문제점 : 4개가 될 가능성이 있는 3개 중 막을때, 잘 ... 막아야 됨... (현재 : 무조건 1부터...)
    for move in board.canPut():
        board.put(move, o_player)
        cnt_O, cnt_X = getCount(board,player)
        if cnt_X == 3:
            print("emergency")
            board.put(move, ' ',True)
            cnt_O, cnt_X = getCount(board,player)
            if cnt_X == 2 :
                print("x has possiblity of connect3")
                return move
            #board.put(move, o_player)
            #가운데에서 먼 순서대로(낮은순서대로....)
            defenseList = [6,0,5,1,4,2,3]
            for move in defenseList:
                if board.board[5][move] != ' ' : continue
                return move
            for move in defenseList:
                if board.board[4][move] != ' ' : continue
                return move
            for move in defenseList:
                if board.board[3][move] != ' ' : continue
                return move
            for move in defenseList:
                if board.board[2][move] != ' ' : continue
                return move
            for move in defenseList:
                if board.board[1][move] != ' ' : continue
                return move
            board.put(move, o_player)
        board.put(move, ' ', True)
    #5,6,7 내가 3개가 연결될 수 있으면(4개가 될 가능성이 있는 3개) 막아라.
    for move in board.canPut():
        board.put(move, player)
        cnt_O, cnt_X = getCount(board,player)
        if cnt_O == 3:
            board.put(move,' ',True)
            cnt_O, cnt_X = getCount(board,player)
            if cnt_O == 2 :    
                return move
            board.put(move, player)
        board.put(move,' ',True)
            
    #8,9 아무것도 없으면 가운데 두어라 + 5번째 줄까지 가운데가 비어있으면, 가운데 두어라
    if board.board[1][3] == ' ' :
        move = 3
        return move
    #10.
    priortyList = [3,2,4,1,5,0,6]
    for move in priortyList:
        if board.board[1][move] != ' ' : continue
        return move
    #Default
    #아무것도 아님.....ㅎㅎ
    for move in board.canPut():
        print('default')
        return move