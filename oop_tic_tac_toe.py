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

        self.frame = tkinter.Frame(self.window)
        self.label = tkinter.Label(self.frame, text=self.curr_player+"'s turn", font=("Consolas", 20), background=self.color_gray,
                                   foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        for row in range(3):
            for column in range(3):
                self.board[row][column] = tkinter.Button(self.frame, text="", font=("Consolas", 50, "bold"),
                                                         background=self.color_gray, foreground=self.color_blue, width=4, height=1,
                                                         command=lambda row=row, column=column: self.set_tile(row, column))
                self.board[row][column].grid(row=row+1, column=column)
