#-*- coding: utf-8 -*-
WIN  =  512

LOSE =  -WIN

class Board(object):

    def __init__(self, board=[]):#게임틀 만들기

        if len(board) == 0:

            self.board = [[' ' for row in range(6)] for column in range(7)]
            
        else:

            self.board = self.board

        #board 크기 결정
        self.width = 7
        self.height = 6


    def __str__(self):#게임틀 만들기
        string = ''

        string += "\ 1 2 3 4 5 6 7\n"

        for row in range(6):

            string += str(6-row) + ' '

            for column in range(7):

                string += self.board[column][row] + ' '
                #board에 값있으면 받아오기 + " "입력하기
            string += '\n' #한행 다 입력시 한줄 바꾸기

        return string


    def checkPlay(self): #full or win

        if self.isBoardFull():
            return True

        if self.whoWin() != None:#이긴사람존재?
            return True

        return False
        
        
    def isBoardFull(self):

        for column in range(self.width):

            if self.board[column][0] == ' ':
                return False
        
        return True
    
    
    def whoWin(self):
    
        scoreX = self.winCheck('X')
        scoreO = self.winCheck('O')
        
        if scoreX == WIN:
            return 'X'
    
        elif scoreO == WIN:
            return 'O'
    
        else:
            return None
        
    def winCheck(self, man):
        state = 0
        for column in range(self.width):
            for row in range(self.height):
                try:
                    if(self.board[column][row] == man and self.board[column+1][row] == man and self.board[column+2][row] == man and self.board[column+3][row] == man):
                        state = WIN
                        return state
                    if(self.board[column][row] == man and self.board[column][row+1] == man and self.board[column][row+2] == man and self.board[column][row+3] == man):
                        state = WIN
                        return state
                    if(self.board[column][row] == man and self.board[column+1][row+1] == man and self.board[column+2][row+2] == man and self.board[column+3][row+3] == man):
                        state = WIN
                        return state
                    if(self.board[column][row] == man and self.board[column-1][row+1] == man and self.board[column-2][row+2] == man and self.board[column-3][row+3] == man):
                        state = WIN
                        return state
                except:
                    pass
                        
    def canPut(self):
        
        return [column for column in range(self.width) if self.board[column][0] == " "]


    def put(self, column, player, delete=False):

        for row in range(self.height):

            if self.board[column][row] != ' ':
                if not(delete):
      
                    row -= 1
                    
                break

        self.board[column][row] = player


def getOpponent(player):#놓여진 말 확인

    if player == 'O':
        
        return 'X'
    
    else:
        return 'O'
    
    