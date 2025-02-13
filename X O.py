import os
from colorama import *
grid = [' ',' ',' ',
        ' ',' ',' ',
        ' ',' ',' ']
player = Fore.RED+'X'+Fore.WHITE
winner = " "
running = True

def tictac():
    global player
    global running
    global winner
    global grid
    #print board
    def board(grid):
        print("\n\n\n\n")
        print(f"{Style.BRIGHT}                      ",grid[0]," | ",grid[1], " | ",grid[2])
        print(f"                      "+"---------------")
        print(f"                      ",grid[3]," | ",grid[4], " | ",grid[5])
        print(f"                      "+"---------------")
        print(f"                      ",grid[6]," | ",grid[7], " | ",grid[8],Style.RESET_ALL,end = "\n\n\n")

    #moves of the player 
    def move(grid):
        global player
        while True:
            try:
                playermove = int(input(f"{Style.BRIGHT}                   ENTER BOX NO. 1-9 ({player}) : "))
                if playermove <=9 and playermove >=1 and grid[playermove-1]==' ':
                    grid[playermove-1] = player
                    break
                else:
                    os.system('cls')
                    board(grid)
                    print(f"                           {Fore.RED+Style.BRIGHT}OOPS!{Style.RESET_ALL}")
            except ValueError:
                os.system('cls')
                board(grid)
                print(f"                           {Fore.CYAN+Style.BRIGHT}RETRY{Style.RESET_ALL}")
        

    #Check win OR Tie
    def winrow(grid):
        global winner
        if grid[0]==grid[1]==grid[2] and grid[0] != ' ':
            winner == grid[1]
            return True
        elif grid[3]==grid[4]==grid[5] and grid[3] != ' ':
            winner = grid[3]
            return True
        elif grid[6]==grid[7]==grid[8] and grid [6] != ' ':
            winner = grid[6]
            return True
        

    #column victory
    def wincol(grid):
        global winner
        if grid[0]==grid[3]==grid[6] and grid[0]!=' ':
            winner = grid[0]
            return True
        elif grid[1]==grid[4]==grid[7] and grid[1] != ' ':
            winner = grid[1]
            return True
        elif grid[2]==grid[5]==grid[8] and grid[2]!=' ':
            winner = grid[2]
            return True

    #Diagonal Victory
    def windiag(grid):
        global winner
        if grid[0]==grid[4]==grid[8] and grid[0] != ' ':
            winner = grid[0]
            return True

        elif grid[2]==grid[4]==grid[6] and grid[2] != ' ':
            winner = grid[2]
            return True
        

    #Tie if every block if occupied and no conditions above are satisfied
    def tie(grid):
        global winner
        if ' ' not in grid:
            winner = "tie"
            print(f"                        {Fore.LIGHTGREEN_EX+Style.BRIGHT}IT'S A DRAW !{Style.RESET_ALL}")
            return True
        

    #if one of the condition from Wins are true, the game 'breaks'
    def WIN():
        if winrow(grid) or wincol(grid) or windiag(grid):
            print(f"                     {Style.BRIGHT}THE WINNER IS '{winner}'{Style.RESET_ALL}!")
            return True

    #switching players
    def switch():
        global player
        if player == Fore.BLUE+"O"+Fore.WHITE:
            player = Fore.RED+"X"+Fore.WHITE
        else:
            player = Fore.BLUE+"O"+Fore.WHITE

    #Resets the game, prepares a new grid
    #alternate player starts
    while running:
        os.system('cls')
        board(grid)
        if WIN():
            break
        if tie(grid):
            break
        move(grid)
        switch()
    grid = [' ',' ',' ',
            ' ',' ',' ',
            ' ',' ',' ']
    if winner == Fore.BLUE+"O"+Fore.WHITE:
        player = Fore.RED+"X"+Fore.WHITE
    else:
        player = Fore.BLUE+"O"+Fore.WHITE
    running = True
tictac()
while True:
    try:
        choice = int(input(f"\n\n                {Fore.WHITE+Style.BRIGHT}1 . {Fore.YELLOW+Style.BRIGHT}NEW GAME            {Fore.WHITE+Style.BRIGHT}2 . {Fore.LIGHTRED_EX+Style.BRIGHT}EXIT {Style.RESET_ALL} : "))
        if choice == 1:
            os.system('cls')
            tictac()
        elif choice == 2:
            quit()
        else:
            print(f"                                 {Fore.CYAN+Style.BRIGHT}RETRY{Style.RESET_ALL}")
    except ValueError:
        print(f"                                 {Fore.CYAN+Style.BRIGHT}RETRY{Style.RESET_ALL}")
