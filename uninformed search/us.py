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

#lights out

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0]) if self.rows > 0 else 0

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        #toggle the light at the given row, col
        self.board[row][col] = not self.board[row][col]

        #potential neighbors
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]


        #check if it's a valid position and toggle it for each neighbor
        for r, c in neighbors:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.board[r][c] = not self.board[r][c]


    def scramble(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if random.random() < 0.5:
                    self.perform_move(row, col)

    def is_solved(self):
        for row in self.board:
            for light in row:
                if light:
                    return False
        return True

    def copy(self):
        # create a deep copy of the board using list comp
        new_board = [row.copy() for row in self.board]
        return LightsOutPuzzle(new_board)

    def successors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                #copy currect puzzle
                new_puzzle = self.copy()
                # make teh move on the copied puzzle
                new_puzzle.perform_move(row, col)
                yield (row, col), new_puzzle
        

    def find_solution(self):
        # converting the board to tuple for hashing
        start = tuple(tuple(row) for row in self.get_board())

        # frontier contains the current state and the sequence of moves of
        # moves to get there
        frontier = deque([(start, [])])
        visited = set([start])

        while frontier:
            state, moves = frontier.popleft()
            board = [list(row) for row in state]
            puzzle = LightsOutPuzzle(board)

            # return the moves, if this state is the solution
            if puzzle.is_solved():
                return moves
            
            # successors added to the frontier
            for move, new_p in puzzle.successors():
                new_state = tuple(tuple(row) for row in new_p.get_board())
                if new_state not in visited:
                    visited.add(new_state)
                    # appeding new moves to the existing sequence of moves
                    new_moves = moves + [move]
                    frontier.append((new_state, new_moves))

        # returning none means I had exausthed all possible solutions w/o
        # sucess
        return None
    

def create_puzzle(rows, cols):
    board = [[False for _ in range(cols)] for _ in range(rows)]
    return LightsOutPuzzle(board)

#linear disk movement

def solve_identical_disks(length, n):
    # Initial and goal states
    start = 'D' * n + 'E' * (length - n)
    goal = 'E' * (length - n) + 'D' * n

    visited = set([start])
    queue = deque([(start, [])])

    while queue:
        state, moves = queue.popleft()

        if state == goal:
            return moves

        for move in possible_moves_identical(state):
            new_state = apply_move(state, move)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves + [move]))

    return None


def possible_moves_identical(state):
    for i, s in enumerate(state):
        if s == 'D':
            if i + 1 < len(state) and state[i + 1] == 'E':
                yield (i, i + 1)
            if i + 2 < len(state) and state[i + 1] == 'D' and state[i + 2] == 'E':
                yield (i, i + 2)

def apply_move(state, move):
    state_list = list(state)
    state_list[move[0]], state_list[move[1]] = state_list[move[1]], state_list[move[0]]
    return ''.join(state_list)

# Distinct disks uses similar logic but tracks distinct disks
def solve_distinct_disks(length, n):
    start = tuple(range(n)) + tuple([-1] * (length - n))
    goal = tuple([-1] * (length - n)) + tuple(range(n-1, -1, -1))

    visited = set([start])
    queue = deque([(start, [])])

    while queue:
        state, moves = queue.popleft()

        if state == goal:
            return moves

        for move in possible_moves_distinct(state):
            new_state = apply_move_distinct(state, move)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves + [move]))

    return None

def possible_moves_distinct(state):
    empty_indices = [i for i, v in enumerate(state) if v == -1]
    disk_indices = [i for i, v in enumerate(state) if v != -1]

    for disk in disk_indices:
        for empty in empty_indices:
            if abs(disk - empty) == 1 or (abs(disk - empty) == 2 and state[(disk + empty) // 2] != -1):
                yield (disk, empty)

def apply_move_distinct(state, move):
    state_list = list(state)
    state_list[move[0]], state_list[move[1]] = state_list[move[1]], state_list[move[0]]
    return tuple(state_list)