import random
import math

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
        #TODO uncomment:
        for i in indexes:
            self.init_mine(i)
        # self.init_mine(6)


        print(self.cells) # TODO: delete me
        print(indexes) ##

    
    def init_mine(self, idx):
        self.cells[idx] = -1

        change = [self.width+1, self.width, self.width-1, +1, -1, -self.width+1, -self.width, -self.width-1]
        for adj in change:
            self.inc_cell(idx + adj, idx)

    def inc_cell(self, idx, mine):
        if idx >= 0 and idx < self.width * self.height and self.cells[idx] != -1 \
        and abs(self.get_col(idx) - self.get_col(mine)) != (self.width - 1):
            print(idx, self.get_col(idx))
            self.cells[idx] += 1

    def get_col(self, idx):
        return (idx+1) % self.width or self.width

    
    def display(self, Type = "csv"):
        if(Type.lower() == "csv"):
            for i in range(self.height * self.width):
                if i % self.width == 0:
                    print()
                print(self.cells[i], end=" ")

    
b2 = board(5,5,1)
b2.display()
