### TicTacToe game. ###


class TicTacToe:

    #Creating a board and icons for the game 
    def __init__(self): 
        self.user_sign = 'O' 
        self.cpu_sign = 'X' 
        self.the_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 

    #Creating a board
    def print_board(self): 
        print(self.the_board[0] + '|' + self.the_board[1] + '|' + self.the_board[2]) 
        print('-+-+-') 
        print(self.the_board[3] + '|' + self.the_board[4] + '|' + self.the_board[5]) 
        print('-+-+-') 
        print(self.the_board[6] + '|' + self.the_board[7] + '|' + self.the_board[8]) 
        print() 

    #AI movement function
    def _ai_move(self): 
        i = 0 
        while i < len(self.the_board): 
            if self.the_board[i] == ' ': 
                self.the_board[i] = self.cpu_sign 
                break 
            i += 1 

    #User movment function
    def _user_move(self, field_number): 
        self.the_board[field_number] = self.user_sign 

    #Win check function
    def who_win(self): 
        result = [] 

        result.append(self.the_board[0] + self.the_board[1] + self.the_board[2]) 
        result.append(self.the_board[3] + self.the_board[4] + self.the_board[5]) 
        result.append(self.the_board[6] + self.the_board[7] + self.the_board[8]) 
        result.append(self.the_board[0] + self.the_board[3] + self.the_board[6]) 
        result.append(self.the_board[1] + self.the_board[4] + self.the_board[7]) 
        result.append(self.the_board[2] + self.the_board[5] + self.the_board[8]) 
        result.append(self.the_board[0] + self.the_board[4] + self.the_board[8]) 
        result.append(self.the_board[2] + self.the_board[4] + self.the_board[6]) 

        if 'XXX' in result: 
            return 'Winer is ' + self.cpu_sign 

        if 'OOO' in result: 
            return 'Winer is ' + self.user_sign 

        return None
     
    #Function that checks the possibility of making a move
    def move(self, field_number): 
        if field_number >= len(self.the_board):
            print('Number is to high')
            return False 

        if self.the_board[field_number] == self.cpu_sign:
            print('This field is occupied')
            return False 

        if self.the_board[field_number] == self.user_sign:
            print('This field is occupied')
            return False 

        if self.who_win() != None:
            print('End game')
            return False 

        self._user_move(field_number) 
        if self.who_win() != None:
            print('End game')
            return False 

        self._ai_move() 
        return True 
    
    #Reset game function
    def reset_game(self): 
        self.__init__()

#Game
game = TicTacToe() 
game.move(2) 
game.print_board() 

game.move(8) 
game.print_board() 

game.move(3) 
game.print_board() 

game.move(5) 
game.print_board() 

result = game.move(7) 
game.print_board()

print(game.who_win())

game.reset_game()
game.print_board()
