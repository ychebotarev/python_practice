__author__ = 'yuriic'
"""
Write a Sudoku verifier
"""

class SudokuSolution:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def __validate(self):
        return True

    def __check(self, res):
        for i in range(1,9):
            if res[i-1] != res[i]:
                return False
        return True

    def __check_row(self, row):
        res=[0 for _ in range(9)]
        for i in range(9):
            res[self.sudoku[row][i]]+=1

        return self.__check(res)

    def __check_column(self, col):
        res=[0 for _ in range(9)]
        for i in range(9):
            res[self.sudoku[i][col]]+=1

        return self.__check(res)

    def __check_square(self, x,y):
        res=[0 for _ in range(9)]
        for i in range(9):
            for i in range(9):
                res[self.sudoku[x+i][y+j]]+=1

        return self.__check(res)

        return True

    def verify(self):
        if not self.__validate():
            return False

        res = [0 for _ in range(9)]
        print(res)

        for i in range(9):
        if not self.__check_row(i) or self.__check_column(i):
            return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.__check_square(i,j):
                    return False

        return True

s = SudokuSolution(1)
print(s.verify())
