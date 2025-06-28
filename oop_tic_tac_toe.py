import tkinter #tk-interface (graphical user interface library)

class TicTacToe:
    def __init__(self):
        #game setup
        self.playerX = "X"
        self.playerO = "O"
        self.curr_player = self.playerX
        self.board = [[0, 0, 0], 
                      [0, 0, 0], 
                      [0, 0, 0]]
        
        self.color_blue = "#4584b6"
        self.color_yellow = "#ffde57"
        self.color_gray = "#343434"
        self.color_light_gray = "#646464"

        self.turns = 0
        self.game_over = False

        self.window = tkinter.Tk() #create the game window
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)
