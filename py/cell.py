from enum import Enum


class Status(Enum):
    hidden = 0
    revealed = 1
    

class Value(Enum):
    mine = -1
    noSurrounding = 0
    surround1 = 1



class cell:
    def __init__(self, state, value):
        self.state = Status(state)
        self.value = Value(value)

    def setValue(self, value):
        self.value = Value(value)
        
    def getValue(self):
        return self.value.value
