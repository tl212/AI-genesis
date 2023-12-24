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
    
    def perform_move(self, direction):
        r, c = self.empty
        if direction == "up" and r > 0:
            temp = self.board[r][c]
            self.board[r][c] = self.board[r - 1][c]
            self.board[r - 1][c] = temp
            self.empty = (r - 1, c)
            return True
        if direction == "down" and r < self.rows - 1:
            temp = self.board[r][c]
            self.board[r][c] = self.board[r + 1][c]
            self.board[r + 1][c] = temp
            self.empty = (r + 1, c)
            return True
        if direction == "left" and c > 0:
            temp = self.board[r][c]
            self.board[r][c] = self.board[r][c - 1]
            self.board[r][c - 1] = temp
            self.empty = (r, c - 1)
            return True
        if direction == "right" and c < self.cols - 1:
            temp = self.board[r][c]
            self.board[r][c] = self.board[r][c + 1]
            self.board[r][c + 1] = temp
            self.empty = (r, c + 1)
            return True
        return False
    
    def scramble(self, num_moves):
        for _ in range(num_moves):
            self.perform_move(random.choice(["up", "down", "left", "right"]))