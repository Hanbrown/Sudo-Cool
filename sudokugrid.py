import random

class SudokuGrid(object):
    def __init__(self):
        self.grid = [4,6,9,5,1,8,7,2,3,3,8,1,2,9,7,5,4,6,5,2,7,6,3,4,9,8,1,6,1,3,7,4,5,2,9,8,9,7,4,3,8,2,1,6,5,8,5,2,9,6,1,3,7,4,2,3,5,8,7,6,4,1,9,1,9,8,4,2,3,6,5,7,7,4,6,1,5,9,8,3,2]

    def getGrid(self):
        return self.grid

    def getRow(self, row):
        result = [0,0,0,0,0,0,0,0,0]
        i = (row - 1) * 9
        for j in range (0, 9):
            result[j] = self.grid[i]
            i += 1
        return result

    def getCol(self, col):
        result = [0,0,0,0,0,0,0,0,0]
        i = col - 1
        while i < 81:
            result[int(i / 9)] = self.grid[i]
            i += 9
        return result

    def getBlock(self, blo):
        result = [0,0,0,0,0,0,0,0,0]
        i = int((blo - 1)/ 3) * 27 + ((blo - 1) % 3) * 3
        for j in range (0, 9):
            result[j] = self.grid[i + int(j / 3) * 6]
            i += 1
        return result

    def getCell(self, vert, hori):
        return self.grid[(vert - 1) * 9 + (hori - 1)]

class SudokuPuzzle(SudokuGrid):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        super(SudokuPuzzle, self).__init__()
        for i in range (0, difficulty * 9):
            i = random.randrange(0, 81)
            while self.grid[i] == 0:
                i = random.randrange(0, 81)
            self.grid[i] = 0;

    def enterAns(self, vert, hori, val):
        self.grid[(vert - 1) * 9 + (hori - 1)] = val
