import random
import heapq
from collections import deque
from queue import PriorityQueue
from math import sqrt
from heapq import heappush, heappop

# tile puzzle
def create_tile_puzzle(rows, cols):
    board = [[i * cols + j +1 for j in range(cols)] for i in range(cols)]
    board[-1][-1] = 0
    return TilePuzzle(board)

