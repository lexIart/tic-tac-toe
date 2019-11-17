from tkinter import *  # standard lib of Python GI
import random


root = Tk()  # graph window constructor
root.title("Крестики-Нолики")
game_run = True  # game session state
field = []  # a  list of buttons, that will realize game field
cross_count = 0  # a number of X on field. if X > 5 - draw comes


def new_game():  # game start function. field is cleared
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'  # button color
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):  # human clicks func
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')


def check_win(smb):  # smb - winner variable (X/O). func that checking all win variants
    for n in range(3):  # 3 - max/min win line length
        check_line(field[n][0], field[n][1], field[n][2], smb)  # algorithm, that checking for all winable variants
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)


def check_line(a1, a2, a3, smb):  # func that checking who's winner
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'red'  # changing buttons color if game ends
        global game_run  # global game state variable
        game_run = False  # ending game


def can_win(a1, a2, a3, smb):  # func that allow computer win if he has that chance (by 1 move)
    result = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        result = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        result = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        result = True
    return result


def computer_move():  # func that simulate computer logic
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:  # cycle that allow computer choose random button when there is no way to win or lose
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(3):  # graph interface creating
    line = []  # game field elements ll placed in this list
    for col in range(3):  # creating same buttons that ll be our 'X'/'O' fields.
        button = Button(root, text=' ', width=4, height=2,  # buttons decor
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))  # using parameters from click() func
        button.grid(row=row, column=col, sticky='nsew')  # using grid parameters from var that we use in prev command
        line.append(button)
    field.append(line)  # filling global list of buttons
new_button = Button(root, text='Новая игра', command=new_game)  # new game button
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')


root.mainloop()  # start window event processing cycle (start the window)
