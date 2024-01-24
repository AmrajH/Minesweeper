# Define the class
# Define public methods
    # Generate board (Width, Height, #Mines)
    # Display (CSV, CMD)
    # Regenerate board(Width, Height, #Mines)
    # Reveal all mines

# Private (__method__):
    # clear -> clear the board
    # Calculate nearby mines (set status)
# ** 
import random
from cell import cell

class board:

    def __init__(self, *args): #This is a workaround since python does not allow constructor overloading.
        self.height = 1
        self.width = 1
        self.mines = 1
        self.cells = []
        
        if(len(args)==1 or len(args) == 2 or len(args) > 3): # Only accept 0 or arguments. Todo: Make sure all 3 args are Integers.
            raise Exception("Please provide 0 or 3 arguments")
        
        elif(len(args) == 3):  #If there are 3 arguments do generate function.
            if(args[2] < 1): #Make sure they provide at lease 1 mine.
                raise Exception("There must be at least one mine")
            self.generate(args[0], args[1], args[2])
    
    def generate(self, Height, Width, Mines):
        if(Mines < 1): #Make sure they provide at lease 1 mine.
                raise Exception("There must be at least one mine")
        tempList = []
        self.height = Height
        self.width = Width
        self.mines = Mines
        for count in range(Height * Width):
            self.cells.append(cell(0,0))
            tempList.append(count)

        for numMines in range(Mines):
            x = random.choice(tempList)
            print(x," ", tempList) #for debug purposes
            self.cells[x].setValue(-1)
            tempList.remove(x)
    
    def display(self, Type):
        if(Type.lower() == "csv"):
            tempStr = ""
            for count in range(self.height * self.width):
                tempStr += str(self.cells[count].getValue()) + ","
        return tempStr[:-1]




    
b1 = board()
b2 = board(2,2,3)
print(b2.display("CSV"))