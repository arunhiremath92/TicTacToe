import sys
sys.setrecursionlimit(1500)
def insertIntoBoard(Board,index, choice):
    if(index < 1 and index > 10):
        print("Invalid Input")
        return False
    if(index < 4):
        Board[0][(index-1)%3] = choice
    elif (index < 7):
        Board[1][(index-1)%3] = choice
    else:
        Board[2][(index-1)%3] = choice
    return True

def checkForMoves(Board):
    for x in range(3):
        for y in range(3):
            if((Board[x][y] != 'x') and (Board[x][y] != '+')):
                return True
    return False
def evaluate(Board):
    y =0
    for x in range(3):
        if (Board[x][y] == Board[x][y+1] == Board[x][y+2]):
            if(Board[x][y] == '+'):
                #print("Row Matched")
                return -10
            elif(Board[x][y] == 'x'):
                #print("Row Matched")
                return 10
    y = 0
    for x in range(3):
        if (Board[y][x] == Board[y+1][x] == Board[y+2][x]):
            if(Board[y][x] == '+'):
                #print("Column Matched")
                return -10
            elif(Board[y][x] == 'x'):
                #print("Column Matched")
                return 10
    y,x =0,2
    if (Board[y][y] == Board[y+1][y+1] == Board[y+2][y+2]):
        if(Board[y][y] == '+'):
            #print("Diagonal Left Matched")
            return -10
        elif(Board[y][y] == 'x'):
            #print("Diagonal Left Matched")
            return 10

    if (Board[y][x] == Board[y+1][x-1] == Board[y+2][x-2]):
        if(Board[y][x] == '+'):
            #print("Diagonal Right Matched")
            return -10
        elif(Board[y][x] == 'x'):
            #print("Diagonal Right Matched")
            return 10
    return 0


def MiniMax(Board,isMaximizer):
    result = evaluate(MyBoard);
    if(result == 10):
        return 10
    if(result == -10):
        return -10
    if(checkForMoves(Board) == False):
        return 0
    
    if(isMaximizer == True):
        BestValueMax = -1000
        for x in range(3):
            for y in range(3):
                if((Board[x][y] != 'x') and (Board[x][y] != '+')):
                    original = Board[x][y]
                    Board[x][y] = 'x'
                    BestValueMax = max(BestValueMax, MiniMax(Board, False))
                    Board[x][y] = original
        return BestValueMax
    else:
        BestValueMin = 1000
        for x in range(3):
            for y in range(3):
                if(Board[x][y] != 'x' and Board[x][y]!= '+'):
                    original = Board[x][y]
                    Board[x][y] = '+'
                    BestValueMin = min(BestValueMin, MiniMax(Board, True))
                    Board[x][y] = original
        return BestValueMin

def findNextMove(Board):
    BestValue = -1000
    x1,y1 = -1,-1
    for x in range(3):
        for y in range(3):
            if(Board[x][y] != 'x' and Board[x][y] != '+'):
                original = Board[x][y]
                Board[x][y] = 'x'
                result = MiniMax(Board, False)
                Board[x][y] = original
                if(result > BestValue):
                    BestValue = result
                    x1,y1 = x,y
    Board[x1][y1] = 'x'
    


#/*Driver Program*/
r,c = 3,3
initVal = 1

MyBoard = [[str((x+1)+(y*c)) for x in range(r)] for y in range(c)]

#Now play the game between human and machine
while(True):
    for x in range(3):
        print (str(MyBoard[x]))
    playerChoice = raw_input("Human Turn")
    insertIntoBoard(MyBoard, int(playerChoice), "+")
    findNextMove(MyBoard)
    #insertIntoBoard(MyBoard, int(computerChoice),"x")
    result = evaluate(MyBoard);
    if(result != None):
        if(result == 10):
            print("Machines Rock")
            for x in range(3):
                print (str(MyBoard[x]))
            break
        elif(result == -10):
            print("Humans Rock")
            for x in range(3):
                print (str(MyBoard[x]))
            break
    if(checkForMoves(MyBoard) == False):
        break

