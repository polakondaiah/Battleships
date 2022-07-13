"""
Battleship Project
Name:
Roll No:
"""

from sympy import jacobi
import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"] = 10
    data["cols"] = 10
    data["board_size"] = 500 
    data["cell_size"] = data["board_size"]/data["rows"]
    data["ships"] = 5
    data["t_ship"] = []
   # data["t_ship"] = test.testShip()     
    data["computer"] = emptyGrid(data["rows"],data["cols"])
    data["user"] = emptyGrid(data["rows"],data["cols"])
    data["user_ships"] = 0
 #   data["user"] = test.testGrid() 
    data["computer"] = addShips(data["computer"],data["ships"])
    # data["user"] = addShips(data[computer],data[ships]  
    
    return 


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, userCanvas, data["user"],True)
    drawGrid(data, compCanvas, data["computer"],True)
    drawShip(data,userCanvas,data["t_ship"])
    
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    cell = getClickedCell(data,event)
    if board == "user":
        clickUserBoard(data, cell[0],cell[1])
   # else:
    #    data["compuper"](cell[0],cell[1])
        
    
    
  #  pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(EMPTY_UNCLICKED)
        grid.append(col)    
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row = random.randint(1,8)
    col = random.randint(1,8)
    hv = random.randint(0,1)
    if hv == 0: 
        ship = [[row,col-1],[row,col],[row,col+1]]   
    else:
        ship = [[row-1,col],[row,col],[row+1,col]]
    return ship    
    

'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    count = 0
    for i in range(len(ship)):        
        row = ship[i][0]
        col = ship[i][1]        
        if grid[row][col] == EMPTY_UNCLICKED:
            count += 1
    return count == 3
  #  if count != 3 :
   #     return False
   # else:
   #     return True
        


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count = 0
    while count < numShips:
        x = createShip()
        if checkShip(grid,x) == True:
            for i in x:
                row = i[0]
                col = i[1]
                grid[row][col] = SHIP_UNCLICKED
            count += 1
   # print(grid) 
    return grid
           
            

        
        
    
    
        
        
        
        


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(data["rows"]):
        for j in range(data["cols"]):
            if grid[i][j] == SHIP_UNCLICKED:
                canvas.create_rectangle(j*data["cell_size"], i*data["cell_size"], (j+1)*data["cell_size"], (i+1)*data["cell_size"], fill="yellow")
            else:
                canvas.create_rectangle(j*data["cell_size"], i*data["cell_size"], (j+1)*data["cell_size"], (i+1)*data["cell_size"], fill="blue")
    return
       
    
    
    


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
  #  for i in range(len(ship))
    ship.sort()
    if ship[0][1] == ship[1][1] and ship[1][1] == ship[2][1]:
        if (ship[0][0]+1) == (ship[1][0]) and (ship[1][0]+1) == (ship[2][0]):
            return True
        else:
            return False
    else:
        return False

'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][0] == ship[1][0] and ship[1][0] == ship[2][0]:
        if (ship[0][1]+1) == (ship[1][1]) and (ship[1][1]+1) == (ship[2][1]):
            return True
        else:
            return False
    else:
        return False
    
   


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
     # print([int(event.y//data["cell_size"]),int(event.x//data["cell_size"])])
    return [int(event.y//data["cell_size"]),int(event.x//data["cell_size"])]

 
'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    #print(ship)
    for i in ship:
        canvas.create_rectangle(i[1]*data["cell_size"],i[0]*data["cell_size"],(i[1]+1)*data["cell_size"],(i[0]+1)*data["cell_size"],fill="white")
        
      
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
   # if checkShip(grid, ship) and isVertical(ship) or checkShip(grid, ship) and  isHorizontal(ship):
   return checkShip(grid, ship) and (isVertical(ship) or isHorizontal(ship))
        
       
  #  isVertical(ship)
   # isHorizontal(ship)
    
    #return True
    


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):

    if shipIsValid(data["user"], data["t_ship"]):
        for i in range(len(data["t_ship"])):
            f = data["t_ship"][i][0] 
            s = data["t_ship"][i][1] 
            data["user"][f][s] = SHIP_UNCLICKED
        data["user_ships"] += 1
    else:
        print("Ship is not valid")
    data["t_ship"] = []   
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["user_ships"] == 5:
        print("you can start the game")
        return
    for i in data["t_ship"]:
        if (row,col)==i:
            return 
    data["t_ship"].append([row,col])
    if len(data["t_ship"])==3:
        placeShip(data)
    return
    
    
    


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    root.title('BattleShip')

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testEmptyGrid()
    test.testCreateShip()
    test.testCheckShip()
    test.testAddShips()
    test.testMakeModel()
    test.testDrawGrid()
    test.testIsVertical()
    test.testIsHorizontal() 
    test.testGetClickedCell()
    test.testDrawShip()
    test.testShipIsValid()
  
    
    
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
