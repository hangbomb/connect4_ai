#from setting import *
from rule import *
from searchAlgorism import minMax, alphabetaPruning   
#import random

#from copy import deepcopy

def yourTurn(board, text):
    print('\n-------')
    print(text)
    move = None
    while move not in board.canPut():
        i = input('Select square to play at: ')
        try :
            move = int(i)
        except ValueError:
            print('not valid integer')
    return move

def ourTurnSearch(board, player):
#   best_moves = [0,1,2,3,4,5,6]
    best = LOSE-1 #-513
    choices = []
    for move in board.canPut():
        board.put(move, player)
        score = alphabetaPruning(board, getOpponent(player), LOSE+1, WIN+1, 6)
        board.put(move, ' ', True)
        print("Move: ",move+1," has a score of: ",score)
        if score > best:
            best = score
            choices = [move]
        elif score == best:
            choices.append(move)
    priortyList = [3,2,4,1,5,0,6]
    for i in range(len(priortyList)) :
        for j in range(len(choices)) :
            if choices[j] == priortyList[i]:
                choice = choices[j]
                print("\n[+] Selected move: ",choice+1)
                return choice

   # choice = random.choice(choices)
def playConnect4(): 
    board = Board()
    print(board)
    player1 = "YOUR"
    player2 = "OUR"
    print('{} turn is X & {} turn is O'.format(player1,player2))
    player = None
    while player not in ['X','O']:
        player = input('Who is first?(X or O) ').capitalize()
    modeX = 0
    mode = 0
    n=0
    while not board.checkPlay():
    #if not checkPlay(=boardIsFull or someone Won),
        if player == 'X':
            while modeX not in [1,2]:
                i = input('Select mode 1.alphabeta 2.Rule 3.')
                try :
                    modeX = int(i)
                except ValueError:
                    print('not valid integer')
            if modeX == 1 :
                move = ourTurnSearch(board, player)
            elif modeX ==2 :
                print("It's rule mode\n")
                move = rulePut(board, player)
            elif modeX == 3:
                move = None
            board.put(move, player)
        else:
            print("OUR's turn")
            while mode not in [1,2]:
                i = input('Select mode 1.alphabeta 2.Rule ')
                try :
                    mode = int(i)
                except ValueError:
                    print('not valid integer')
            if mode == 1 :
                move = ourTurnSearch(board, player)
            elif mode ==2 :
                print("It's rule mode\n")
                move = rulePut(board, player)
            board.put(move, player)
            textpath = str(modeX) +'-'+str(mode) +'-' + str(n) + '.txt'
            f = open(textpath, mode='wt', encoding='utf-8')
            f.write(str(board));
            f.close()
            n +=1
        print(board)
        f = open('final.txt', mode='wt', encoding='utf-8')
        f.write(str(board));
        f.close()

        player = getOpponent(player)

    if board.whoWin() == "X":
        print("{} won!".format(player1))
    elif board.whoWin() == "O":
        print("{} won!".format(player2))
    else:
        print("It's a tie!")

if __name__ == '__main__':
    playConnect4()