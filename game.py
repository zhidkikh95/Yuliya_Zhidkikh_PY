import os
import time
cell = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
player_num = [1, 2]
move = ""
active_player = 0
h1 = input("Игрок 1, выберите 0 или X: ")
while h1 != "0" and h1 != "X":
    print("Ошибка")
    h1 = input("Игрок 1, выберите 0 или X: ")
else:
    if h1 == "0":
        h2 = "X"
        print("Игрок 2 ходит X")
    if h1 == "X":
        h2 = "0"
        print("Игрок 2 ходит 0")  
time.sleep(2.0)
player = False 
for i in cell:
    os.system('cls' if os.name=='nt' else 'clear')
    player = not player
    if player is True:
        move = h1
        active_player = player_num[0]
    else:
        move = h2
        active_player = player_num[1]    
    board = (f""" 
    {cell[0]} | {cell[1]} | {cell[2]}
    ----------
    {cell[3]} | {cell[4]} | {cell[5]}
    ----------
    {cell[6]} | {cell[7]} | {cell[8]}
    """)
    print(board)
    inp = input(f"Ход игрока {active_player} ({move}): ") 
    while int(inp) not in cell:
        if int(inp) in range(1,10) :
            print("Ячейка занята")
        else:
            print("Ошибка ввода")    
        inp = input(f"Ход игрока {active_player} ({move}): ")
    else:  
        if int(inp) in cell:
            cell[int(inp)-1] = move
    if cell[0] == move and (cell[0] == cell[1] and cell[0] == cell[2]) or cell[3] == move and (cell[3] == cell[4] and cell[3] == cell[5]) or cell[6] == move and (cell[6] == cell[7] and cell[6] == cell[8]) or cell[0] == move and (cell[0] == cell[4] and cell[0] == cell[8])\
        or cell[2] == move and (cell[2] == cell[4] and cell[2] == cell[6]) or cell[0] == move and (cell[0] == cell[3] and cell[0] == cell[6]) or cell[1] == move and (cell[1] == cell[4] and cell[1] == cell[7]) or cell[2] == move and (cell[2] == cell[5] and cell[2] == cell[8]):
            os.system('cls' if os.name=='nt' else 'clear')
            board = (f""" 
            {cell[0]} | {cell[1]} | {cell[2]}
            ----------
            {cell[3]} | {cell[4]} | {cell[5]}
            ----------
            {cell[6]} | {cell[7]} | {cell[8]}
            """)
            print(board)
            print(f"Игрок {active_player}: Победа")
            break
else:
     print("Ничья")