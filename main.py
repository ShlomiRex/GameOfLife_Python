from GUI.GUI import GUI
from Life import Greedy


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Greedy.Life(board)

    app = GUI()
    app.start()