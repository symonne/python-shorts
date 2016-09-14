def main():
    myBoard = [["^","^","^"],["^","^","^"],["^","^","^"]]
    instructions()
    printfn(myBoard)
    turnCount = 0
    keepGoing = "no"
    while (turnCount < 9) and (keepGoing != "yes"): #change turnCount in whoWon(), it should be the same as this turnCount
        sym = symbol(turnCount)
        r,c = play(sym)
        cheat = noCheat(myBoard,r,c)
        while cheat == "yes":
            print("Sorry, that spot is already taken! Please try again.")
            r,c = play(sym)
            cheat = noCheat(myBoard, r, c)
        turnCount +=1
        myBoard = editBoard(myBoard,r,c,sym)
        printfn(myBoard)
        keepGoing = whoWon(myBoard,turnCount)

#This function introduces the game and gives the instructions
def instructions():
    print("This is a game of Tic Tac Toe.")
    print("When prompted, say which row you would like your symbol (top/middle/bottom).")
    print("Then you will be prompted for which column (left/middle/right) you would like.")
    print("Make sure not place your symbol in a space that is already taken.")
    print("Best of luck!")

#This function prints the board
def printfn(grid):
    for row in grid:
        for item in row:
            print(str(item), end = " ")
        print()

#This function gets the English placement of the symbol
def play(s):
    r = 10
    while r == 10:
        r = input("Which row would you like your " +str(s)+ " to be in?")
        r = dictR(r)
    c = 10
    while c == 10:
        c = input ("Which column would you like your " +str(s)+ " to be in?")
        c = dictC(c)
    #print(r)
    #print(c)
    return(r,c)

#This function turns the row word into the row number
def dictR(r):
    dictR = {"top":0,"middle":1,"bottom":2}
    #print(dictR)
    if (r == "top") or (r == "middle") or (r == "bottom"):
        r = dictR[r]
        return(r)
    else:
        print("That is not a valid row.")
        print("Please choose another.")
        r = 10
        return(r)

#This function turns the column word into the column number
def dictC(c):
    dictC = {"left":0,"middle":1,"right":2}
    #print(dictC)
    if (c == "left") or (c == "middle") or (c == "right"):
        c = dictC[c]
        return(c)
    else:
        print("That is not a valid row.")
        print("Please choose another.")
        c = 10
        return(c)

#This function adds new moves to the board
def editBoard(myBoard,r,c,sym):
    myBoard[r][c] = sym
    return(myBoard)

#This function toggles players
def symbol(turnCount):
    if turnCount%2==0:
        sym = "X"
    else:
        sym = "O"
    return(sym)

#This function makes sure that symbols aren't written over
def noCheat(grid, r, c):
    if grid[r][c] == "X" or grid[r][c] == "O":
        cheat = "yes"
        return(cheat)
    else:
        cheat = "no"
        return(cheat)

#This function determines if there's a winner - and will end the game - or if there was a tie
def whoWon(grid, turnCount):
#horizontals
    if (grid[0][0] == grid [0][1]) and (grid[0][1] == grid [0][2]) and (grid[0][0] == grid[0][2]) and (grid[0][0] != "^"):
        print("Congratulation Player " + grid[0][0] + ", YOU WON!!")
        win = "yes" 
        return(win)
    elif (grid[1][0] == grid [1][1]) and (grid[1][1] == grid [1][2]) and (grid[1][0] == grid[1][2]) and (grid[1][0] != "^"):
        print("Congratulation Player " + grid[1][0] + ", YOU WON!!")
        win = "yes"
        return(win)
    elif (grid[2][0] == grid [2][1]) and (grid[2][1] == grid [2][2]) and (grid[2][0] == grid[2][2]) and (grid[2][0] != "^"):
        print("Congratulation Player " + grid[2][0] + ", YOU WON!!")
        win = "yes"
        return(win)
#verticals
    elif (grid[0][0] == grid [1][0]) and (grid[1][0] == grid [2][0]) and (grid[0][0] == grid[2][0]) and (grid[0][0] != "^"):
        print("Congratulation Player " + grid[0][0] + ", YOU WON!!")
        win = "yes"
        return(win)
    elif (grid[0][1] == grid [1][1]) and (grid[1][1] == grid [2][1]) and (grid[0][1] == grid[2][1]) and (grid[0][1] != "^"):
        print("Congratulation Player " + grid[0][1] + ", YOU WON!!")
        win = "yes"
        return(win)
    elif (grid[0][2] == grid [1][2]) and (grid[1][2] == grid [2][2]) and (grid[0][2] == grid[2][2]) and (grid[0][2] != "^"):
        print("Congratulation Player " + grid[0][2] + ", YOU WON!!")
        win = "yes"
        return(win)
#diagnols
    elif (grid[0][0] == grid [1][1]) and (grid[1][1] == grid [2][2]) and (grid[0][0] == grid[2][2]) and (grid[0][0] != "^"):
        print("Congratulation Player " + grid[0][0] + ", YOU WON!!")
        win = "yes"
        return(win)
    elif (grid[0][2] == grid [1][1]) and (grid[1][1] == grid [2][0]) and (grid[0][2] == grid[2][0]) and (grid[0][2] != "^"):
        print("Congratulation Player " + grid[0][2] + ", YOU WON!!")
        win = "yes"
        return(win)
#tie
    elif turnCount == 9: #change this turnCount!!
        print("You guys tied! Good job, but try harder.")
    else:
        win = "no"
        return(win)

