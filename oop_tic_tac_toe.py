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

        button = tkinter.Button(self.frame, text="restart", font=("Consolas", 20), background=self.color_gray,
                                foreground="white", command=self.new_game)
        button.grid(row=4, column=0, columnspan=3, sticky="we")

        self.frame.pack()

        self.window.update()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_x = int((screen_width/2) - (window_width/2))
        window_y = int((screen_height/2) - (window_height/2))

        #format "(w)x(h)+(x)+(y)"
        self.window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        self.window.mainloop()

    def set_tile(self, row, column):
        if self.game_over:
            return

        if self.board[row][column]["text"] != "":
            #already taken spot
            return

        #mark the board
        self.board[row][column]["text"] = self.curr_player

        #switch player
        if self.curr_player == self.playerO:
            self.curr_player = self.playerX
        else:
            self.curr_player = self.playerO

        self.label["text"] = self.curr_player+"'s turn"

        #checking winner
        self.check_winner()

    def check_winner(self):
        self.turns += 1

        #horizontally, check 3 rows
        for row in range(3):
            if (self.board[row][0]["text"] == self.board[row][1]["text"] == self.board[row][2]["text"]
                and self.board[row][0]["text"] != ""):
                self.label.config(text=self.board[row][0]["text"]+" is the winner!", foreground=self.color_yellow)
                for column in range(3):
                    self.board[row][column].config(foreground=self.color_yellow, background=self.color_light_gray)
                self.game_over = True
                return

        #vertically, check 3 columns
        for column in range(3):
            if (self.board[0][column]["text"] == self.board[1][column]["text"] == self.board[2][column]["text"]
                and self.board[0][column]["text"] != ""):
                self.label.config(text=self.board[0][column]["text"]+" is the winner!", foreground=self.color_yellow)
                for row in range(3):
                    self.board[row][column].config(foreground=self.color_yellow, background=self.color_light_gray)
                self.game_over = True
                return

        #diagonally
        if (self.board[0][0]["text"] == self.board[1][1]["text"] == self.board[2][2]["text"]
            and self.board[0][0]["text"] != ""):
            self.label.config(text=self.board[0][0]["text"]+" is the winner!", foreground=self.color_yellow)
            for i in range(3):
                self.board[i][i].config(foreground=self.color_yellow, background=self.color_light_gray)
            self.game_over = True
            return

        #anti-diagonally
        if (self.board[0][2]["text"] == self.board[1][1]["text"] == self.board[2][0]["text"]
            and self.board[0][2]["text"] != ""):
            self.label.config(text=self.board[0][2]["text"]+" is the winner!", foreground=self.color_yellow)
            self.board[0][2].config(foreground=self.color_yellow, background=self.color_light_gray)
            self.board[1][1].config(foreground=self.color_yellow, background=self.color_light_gray)
            self.board[2][0].config(foreground=self.color_yellow, background=self.color_light_gray)
            self.game_over = True
            return

        #tie
        if self.turns == 9:
            self.game_over = True
            self.label.config(text="Tie!", foreground=self.color_yellow)