
# Program działa na zasadzie nawrotów, wiem, że zadanie miało być wykonane jako brute force i taką wersję zamieszczam 
# zakomentowaną niżej, lecz niestety nie działa poprawnie

# function checking if we can put specific number in specific place
def solve(s, row, col, num):
    for x in range(9):
        # checking row
        if s[row][x] == num:
            return False
        # checking column
        if s[x][col] == num:
            return False
    # checking the 3x3 square
    for x in range(3):
        for y in range(3):
            if s[x + row - row % 3][y + col - col % 3] == num:
                return False
    return True

# functino for printing out the solution
def write_out(s):
    for row in range(9):
        for col in range(9):
            print(s[row][col], end=" ")
        print()

def sudoku(s, row, col):
    if s[row][col] == 0:
        for num in range(1, 10):
            if solve(s, row, col, num):
                s[row][col] = num
                if col < 8:
                    if sudoku(s, row, col + 1):
                        return True
                    else:
                        s[row][col] = 0
                elif row < 8:
                    if sudoku(s, row + 1, 0):
                        return True
                    else:
                        s[row][col] = 0
                else:
                    write_out(s)
                    return True
        return False
    else:
        if col < 8:
            if sudoku(s, row, col + 1):
                return True
            else:
                return False
        elif row < 8:
            if sudoku(s, row + 1, 0):
                return True
            else:
                return False
        else:
            write_out(s)
            return True


def sudoku_solver(s):
    if sudoku(s, 0, 0):
        return True
    else:
        print("Nie ma rozwiązań")

game = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

sudoku_solver(game)

solutions = []

# def solution_check(s):
#     for x in range(9):
#         sums = 0 
#         for y in range(9):
#             sums += s[x][y]
#         if sums != 45:
#             return False
#     for y in range(9):
#         sums = 0
#         for x in range(9):
#             sums += s[x][y]
#         if sums != 45:
#             return False
#     for i in range(0, 7, 3):
#         for j in range(0, 7, 3):
#             sums = 0
#             for x in range(i, 3 + i):
#                 for y in range(j, 3 + j):
#                     sums += s[i][j]
#             if sums != 45:
#                 return False
#     return True
                    
# def write_out(s):
#     for row in range(9):
#         for col in range(9):
#             print(s[row][col], end=" ")
#         print()
#     print()

# def sudoku(s, row, col):
#     if col > 8:
#         return sudoku(s, row + 1, 0)
#     if row > 8:
#         if solution_check(s):
#             solutions.append(s)
#     elif s[row][col] == 0:
#         for i in range(1, 10):
#             s[row][col] = i
#             sudoku(s, row, col + 1)
#     else:
#         sudoku(s, row, col + 1)

# def sudoku_solver(s):
#     sudoku(s, 0, 0)
#     for solution in solutions:
#         write_out(solution)
#     print("to już wszystkie rozwiązania")


# game = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
#         [0, 1, 0, 0, 0, 4, 0, 0, 0],
#         [4, 0, 7, 0, 0, 0, 2, 0, 8],
#         [0, 0, 5, 2, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 9, 8, 1, 0, 0],
#         [0, 4, 0, 0, 0, 3, 0, 0, 0],
#         [0, 0, 0, 3, 6, 0, 0, 7, 2],
#         [0, 7, 0, 0, 0, 0, 0, 0, 3],
#         [9, 0, 3, 0, 0, 0, 6, 0, 4]]

# sudoku_solver(game)