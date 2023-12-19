import math
import random
from collections import deque

# N-Queens

# implements all possible placements in n x n board
def all_num_placement(n):
    return math.factorial(n*n) // (math.factorial(n) * math.factorial(n * n-n))

# calculates the number of possible placements of in the board such that each 
# row contains only one queens 
def one_per_row_num_placement(n):
    return n ** n

def valid_queens_n(board):
    n = len(board)
    for i in range(n):
        # comparing with Qs that comes after
        for j in range(i + 1, n):
            # checking diagonally
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True

