import numpy as np
board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='X'
p2='O'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if (count==3):
            print(symbol,"won!")
            return True
    return False
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if (count==3):
            print(symbol,"won!")
            return True
    return False
def check_diags(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,"won!")
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,"won!")
        return True
    return False
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diags(symbol)
def place(symbol):
    print(np.matrix(board))
    while True:
        row=int(input("Enter row- 1 or 2 or 3:"))
        col=int(input("Enter column- 1 or 2 or 3:"))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Invalid input. Please enter again.")
    board[row-1][col-1]=symbol
def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            place(p1)
            if won(p1):
                break
            else:
                print("O turn")
                place(p2)
                if won(p2):
                    break
    if not(won(p1)) and not(won(p2)):
        print('Draw')
play()          
