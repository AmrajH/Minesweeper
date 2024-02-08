import board as b
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the template directory to the 'html' directory in the parent directory
app.template_folder = os.path.join(current_dir, '../html')

class Game:
    def __init__(self, height = 0, width = 0, mines = 0):
        if (height > 4 and width > 4 and mines > 0):
            self.generate(height, width, mines)

    def generate(self, height, width, mines):
        if (height > 4 and width > 4 and mines > 0):
            self.__board = b.Board(height, width, mines)
            self.revealed = [[" " for i in range(width)] for i in range(height)]

    def reveal_cell(self, row, col):
        if (not (row >= 0 and row < self.__board.height and col >= 0 and col < self.__board.width)):
            raise Exception("Invalid row/col values, in Game class.")
        value = self.__board.get_cell(row, col)
        return value
    
game = Game()

# Set the template directory to the 'html' directory in the parent directory
app.template_folder = os.path.join(current_dir, '../html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reveal/<int:row>/<int:col>')
def cell_clicked(row, col):
    print(row, col)
    return jsonify({'value' : game.reveal_cell(row, col)})

@app.route('/init_board/<int:row>/<int:col>/<int:mines>')
def init_board(row, col, mines):
    game.generate(row, col, mines)
    return jsonify({'message': 'Grid Created!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True)