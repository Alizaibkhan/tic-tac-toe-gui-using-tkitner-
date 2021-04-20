from tkinter import *
import winsound
import random
import time
from tkinter import messagebox

game_won_lost_draw = False
play_sound = False
sound = False
done_list = []
board = ['x' for x in range(9)]


class TicTacToeGui:
    def __init__(self):  # main gui window constructor
        self.tic_tac = Tk()
        self.tic_tac.geometry('940x800')  # Window size
        self.tic_tac.config(bg='bisque2')  # Window background colour
        self.tic_tac.resizable(0, 0)  # making window un resizeable
        self.tic_tac.title('TIC TAC TOE'.center(275))  # window title at center
        self.tic_tac.iconbitmap('tictac.ico')  # add favicon favicon
        # First row-----------------------------------------------------
        self.col1_row1 = Label(self.tic_tac, text=' ▣ |', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               anchor='ne', underline=True)
        self.col1_row1.grid(column=0, row=0)
        self.col1_row1.bind("<Button-1>", lambda e: self.user_click(0))

        self.col2_row1 = Label(self.tic_tac, text=' ▣ |', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col2_row1.grid(column=1, row=0)
        self.col2_row1.bind("<Button-1>", lambda e: self.user_click(1))

        self.col3_row1 = Label(self.tic_tac, text=' ▣ ', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col3_row1.grid(column=2, row=0)
        self.col3_row1.bind("<Button-1>", lambda e: self.user_click(2))

        # Second row--------------------------------
        self.col1_row2 = Label(self.tic_tac, text=' ▣ |', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col1_row2.grid(column=0, row=2, ipady=0, sticky='ne')
        self.col1_row2.bind("<Button-1>", lambda e: self.user_click(3))

        self.col2_row2 = Label(self.tic_tac, text=' ▣ |', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col2_row2.grid(column=1, row=2)
        self.col2_row2.bind("<Button-1>", lambda e: self.user_click(4))

        self.col3_row2 = Label(self.tic_tac, text=' ▣ ', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col3_row2.grid(column=2, row=2)
        self.col3_row2.bind("<Button-1>", lambda e: self.user_click(5))

        # Third row ----------------------------------
        self.col1_row3 = Label(self.tic_tac, text=' ▣ |', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col1_row3.grid(column=0, row=3)
        self.col1_row3.bind("<Button-1>", lambda e: self.user_click(6))

        self.col2_row3 = Label(self.tic_tac, text=' ▣ |', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col2_row3.grid(column=1, row=3)
        self.col2_row3.bind("<Button-1>", lambda e: self.user_click(7))

        self.col3_row3 = Label(self.tic_tac, text=' ▣ ', font=("Britannic Bold", 150, 'bold'), bg='bisque2', fg='red2',
                               underline=True)
        self.col3_row3.grid(column=2, row=3)
        self.col3_row3.bind("<Button-1>", lambda e: self.user_click(8))

        # End message box------------------------------------
        col1_row4 = Label(self.tic_tac, text="WELCOME TO TIC TAC TOE", font=('Bouncy Black PERSONAL USE ONLY', 45),
                          bg='orange red', fg='purple4', width=24, height=0)
        col1_row4.grid(column=0, row=4, columnspan=3, pady=35, sticky=W)

        # Sound Button
        self.sound_button_image = PhotoImage(file="stop_sound.png")
        self.sound_button = Label(self.tic_tac, image=self.sound_button_image, bg='orange red', border=0)
        self.sound_button.bind("<Button-1>", self.sound_fun)
        self.sound_button.grid(column=0, row=4, pady=0, sticky=W)

    def user_click(self, user_select):
        if game_won_lost_draw:
            winsound.PlaySound("error.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(0.5)
            if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                              winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        else:
            if user_select == 0:
                if 0 not in done_list:
                    self.col1_row1.config(text="x |", underline=False, fg='purple')
                    self.ticking(0)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

            if user_select == 1:
                if 1 not in done_list:
                    self.col2_row1.config(text="x |", underline=False, fg='purple')
                    self.ticking(1)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

            if user_select == 2:
                if 2 not in done_list:
                    self.col3_row1.config(text="x |", underline=False, fg='purple')
                    self.ticking(2)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

            if user_select == 3:
                if 3 not in done_list:
                    self.col1_row2.config(text="x |", underline=False, fg='purple')
                    self.ticking(3)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            if user_select == 4:
                if 4 not in done_list:
                    self.col2_row2.config(text="x |", underline=False, fg='purple')
                    self.ticking(4)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

            if user_select == 5:
                if 5 not in done_list:
                    self.col3_row2.config(text="x |", underline=False, fg='purple')
                    self.ticking(5)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

            if user_select == 6:
                if 6 not in done_list:
                    self.col1_row3.config(text="x |", underline=False, fg='purple')
                    self.ticking(6)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

            if user_select == 7:
                if 7 not in done_list:
                    self.col2_row3.config(text="x |", underline=False, fg='purple')
                    self.ticking(7)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

            if user_select == 8:
                if 8 not in done_list:
                    self.col3_row3.config(text="x |", underline=False, fg='purple')
                    self.ticking(n1=8)
                else:
                    print("Already selected")
                    winsound.PlaySound("already selected.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    time.sleep(1)
                    if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                                      winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    def ticking(self, n1):  # Ticking ----------------------------------------------
        winsound.PlaySound("tick.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        time.sleep(0.5)
        if play_sound: winsound.PlaySound("mixkit-game-show.wav",
                                          winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        board[n1] = 's'
        done_list.append(n1)
        self.win_lose()
        self.check_draw()
        if not game_won_lost_draw:
            self.cpu_turn()
            self.win_lose()
            self.check_draw()

    def cpu_turn(self):
        global done_list
        while True:
            if game_won_lost_draw:
                break
            else:
                cpu_select = random.randint(0, 8)
                if cpu_select not in done_list:
                    board[cpu_select] = "o"
                    done_list.append(cpu_select)
                    if cpu_select == 0:
                        self.col1_row1.config(text="O |", fg='green', underline=False)
                    if cpu_select == 1:
                        self.col2_row1.config(text="0 |", fg='green', underline=False)
                    if cpu_select == 2:
                        self.col3_row1.config(text="O |", fg='green', underline=False)
                    if cpu_select == 3:
                        self.col1_row2.config(text="O |", fg='green', underline=False)
                    if cpu_select == 4:
                        self.col2_row2.config(text="O |", fg='green', underline=False)
                    if cpu_select == 5:
                        self.col3_row2.config(text="O |", fg='green', underline=False)
                    if cpu_select == 6:
                        self.col1_row3.config(text="O |", fg='green', underline=False)
                    if cpu_select == 7:
                        self.col2_row3.config(text="O |", fg='green', underline=False)
                    if cpu_select == 8:
                        self.col3_row3.config(text="O |", fg='green', underline=False)
                    break

    def win_lose(self):  # win lose checker
        global game_won_lost_draw
        for tick in ["s", 'o']:
            if board[0] == tick and board[1] == tick and board[2] == tick:
                game_won_lost_draw = True
                self.col1_row1.config(fg='black'), self.col2_row1.config(fg='black'), self.col3_row1.config(fg="black")
                if tick == "s": print("User win"), winsound.PlaySound("clapping.wav",
                                                                      winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    won=True)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

            if board[3] == tick and board[4] == tick and board[5] == tick:
                game_won_lost_draw = True
                self.col1_row2.config(fg='black'), self.col2_row2.config(fg='black'), self.col3_row2.config(fg="black")
                if tick == "s": print("User win"), winsound.PlaySound("clapping.wav",
                                                                      winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    won=True)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

            if board[6] == tick and board[7] == tick and board[8] == tick:
                game_won_lost_draw = True
                self.col1_row3.config(fg='black'), self.col2_row3.config(fg='black'), self.col3_row3.config(fg="black")
                if tick == "s": print("User win"), winsound.PlaySound("clapping.wav",
                                                                      winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    won=True)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

            if board[0] == tick and board[3] == tick and board[6] == tick:
                game_won_lost_draw = True
                self.col1_row1.config(fg='black'), self.col1_row2.config(fg='black'), self.col1_row3.config(fg="black")
                if tick == "s": print("User win"), winsound.PlaySound("clapping.wav",
                                                                      winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    won=True)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

            if board[1] == tick and board[4] == tick and board[7] == tick:
                game_won_lost_draw = True
                self.col2_row1.config(fg='black'), self.col2_row2.config(fg='black'), self.col2_row3.config(fg="black")
                if tick == "s": print("User win"), winsound.PlaySound("clapping.wav",
                                                                      winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    won=True)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

            if board[2] == tick and board[5] == tick and board[8] == tick:
                game_won_lost_draw = True
                self.col3_row1.config(fg='black'), self.col3_row2.config(fg='black'), self.col3_row3.config(fg="black")
                if tick == "s": print("User win"), pop_up_win_lose_window(won=True), winsound.PlaySound(
                    "audience-clapping.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

            if board[0] == tick and board[4] == tick and board[8] == tick:
                game_won_lost_draw = True
                self.col1_row1.config(fg='black'), self.col2_row2.config(fg='black'), self.col3_row3.config(fg="black")
                if tick == "s": print("User win"), winsound.PlaySound("clapping.wav",
                                                                      winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    won=True)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

            if board[2] == tick and board[4] == tick and board[6] == tick:
                game_won_lost_draw = True
                self.col3_row1.config(fg='black'), self.col2_row2.config(fg='black'), self.col1_row3.config(fg="black")
                if tick == "s": print("User win"), winsound.PlaySound("clapping.wav",
                                                                      winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    won=True)
                if tick == "o": print("Cpu win"), winsound.PlaySound("boo.wav",
                                                                     winsound.SND_FILENAME | winsound.SND_ASYNC), pop_up_win_lose_window(
                    lose=True)

    def check_draw(self):
        global game_won_lost_draw
        if game_won_lost_draw:
            pass
        else:
            if "x" not in board:
                game_won_lost_draw = True
                print("Game draw")
                winsound.PlaySound("Round Draw.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                pop_up_win_lose_window(draw=True)

    def closing_window_loop(self):
        self.tic_tac.mainloop()

    def quit_game(self, n):
        if n:
            global board, game_won_lost_draw, done_list, play_sound
            board = ['x' for x in range(9)]
            done_list = []
            game_won_lost_draw = False
            play_sound = False
            self.tic_tac.destroy()
        if not n:
            self.tic_tac.destroy()

    def sound_fun(self, e):  # Sound function
        global play_sound
        if not play_sound:
            play_sound = True
            play_sound_image = PhotoImage(file='play_sound.png')
            self.sound_button.config(image=play_sound_image)
            self.sound_button.photo = play_sound_image
            winsound.PlaySound("mixkit-game-show.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        else:
            winsound.PlaySound(None, winsound.SND_FILENAME)
            play_sound = False
            self.sound_button.config(image=self.sound_button_image)


def pop_up_win_lose_window(won=None, lose=None, draw=None):
    global s
    if won:
        window_lose_pop = messagebox.askyesno(title="Game end", message='You win! Play Again?')
        if not window_lose_pop:
            s.quit_game(n=False)
        else:
            s.quit_game(n=True)
            time.sleep(0.5)
            s = TicTacToeGui()
            s.closing_window_loop()
    elif lose:
        window_lose_pop = messagebox.askyesno(title="Game end", message='You lose! Play Again?')
        if not window_lose_pop:
            s.quit_game(n=False)
        else:
            s.quit_game(n=True)
            time.sleep(0.5)
            s = TicTacToeGui()
            s.closing_window_loop()
    elif draw:
        window_lose_pop = messagebox.askyesno(title="Game Draw", message='Game Draw! Play Again?')
        if not window_lose_pop:
            s.quit_game(n=False)
        else:
            s.quit_game(n=True)
            time.sleep(0.5)
            s = TicTacToeGui()
            s.closing_window_loop()


s = TicTacToeGui()
s.closing_window_loop()
