import random

class board:

    def __init__(self, height, width, mines): #This is a workaround since python does not allow constructor overloading.
        ## TODO: catch when width, height and mines are bad.
        self.generate(height, width, mines)

    def generate(self, height, width, mines):
        if(mines < 1): #Make sure they provide at lease 1 mine.
                raise Exception("There must be at least one mine")
        
        self.height = height
        self.width = width
        self.mines = mines
        self.cells = [0 for i in range(width*height)]
        indexes = random.sample([i for i in range(width*height)], mines) # initiate to all 0
        
        for i in indexes:
            self.init_mine(i)


        print(self.cells) # TODO: delete me
        print(indexes) ##

    
    def init_mine(self, idx):
        self.cells[idx] = -1

        change = [self.width+1, self.width, self.width-1, +1, -1, -self.width+1, -self.width, -self.width-1]
        if idx < self.width:
            change.remove(-self.width+1)
            change.remove(-self.width)
            change.remove( -self.width-1)
        elif idx >= self.width * (self.height - 1):
            change.remove(self.width+1)
            change.remove(self.width)
            change.remove( self.width-1)
        if idx % self.width == 0:
            change.remove(-1)
            try:
                change.remove(-self.width-1)
            except:
                pass
            try:
                change.remove(self.width-1)
            except:
                pass
        elif idx % self.width == self.width-1:
            change.remove(+1)
            try:
                change.remove(-self.width+1)
            except:
                pass
            try:
                change.remove(self.width+1)
            except:
                pass
        print(idx)
        print(change)
        for adj in change:
            print(idx + adj)
            self.inc_cell(idx + adj)

    def inc_cell(self, idx):
        self.cells[idx] += 1
    
    def display(self, Type = "csv"):
        if(Type.lower() == "csv"):
            for i in range(self.height * self.width):
                if i % self.width == 0:
                    print()
                print(self.cells[i], end=" ")

    
b2 = board(5,5,1)
b2.display()
