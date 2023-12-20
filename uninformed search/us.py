import math
import random
from collections import deque

# N-Queens

# implements all possible placements in n x n board
def num_placements_all(n):
    return math.factorial(n*n) // (math.factorial(n) * math.factorial(n*n -n))

def num_placements_one_per_row(n):
    return n ** n

def n_queens_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n): #comparing with the Qs that comes after
            #checking diagonally
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True


def n_queens_solutions(n):
    def n_queens_helper(n, board):
        if len(board) == n: #if board is complete
            yield board
            return
        
        for col in range(n): #place queen in current column and recursevily
            if n_queens_valid(board + [col]):
                yield from n_queens_helper(n, board + [col])
                
    return list(n_queens_helper(n, []))
