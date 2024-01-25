
class cell:
    """
    Represents a cell object in a Minesweeper game.

    Attributes:
    - is_hidden (bool): Indicates whether the cell is hidden or revealed.
    - status (int): Represents the status of the cell.
                    -1 => mine; 0 - 8 non-mine, num of neighboring mines.
    """

    def __init__(self, is_hidden = True, status = 0):
        """Initialize cell instance, set to hidden and empty (0) by default."""
        self.is_hidden = is_hidden
        self.status = status
    
    def reveal(self):
        """Reveals the cell, sets is_hidden to False."""
        self.is_hidden = False

    def inc_neighbors(self):
        """Increments status by 1 (indicating neighboring mines), unless it is a mine."""
        self.status += 1 if self.status != -1 else None

    def get_status(self):
        """Returns the mine status, -1 for mine, 0-8 for num of neighboring mines."""
        return self.status
    
    def not_hidden(self): # to be used: if cell.not_hidden():
        """Returns whether cell is revealed, False if hidden."""
        return not self.is_hidden

    

