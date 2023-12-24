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

class TilePuzzle(object):
    def __init__(self, board):
        self.board = [row.copy() for row in board]
        self.rows, self.cols = len(board), len(board[0])
        self._visited_states = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == 0:
                    self.empty = (r, c)

    def get_board(self):
        return [row.copy() for row in self.board]