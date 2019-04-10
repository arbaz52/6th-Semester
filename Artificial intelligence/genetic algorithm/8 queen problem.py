import random as rn
import numpy
#mutate if the random value is greater than the threshhold
mutation_thresh = 0.5
def generate_board():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(0)
        row[rn.randint(0, 7)] = 1
        board.append(row)
    return board

def initialize(n):
    boards = []
    for i in range(n):
        boards.append(generate_board())
    return boards


#additional function
def diag_attacking(board, row, col, row_der, col_der):
    while True:
        row += row_der
        col += col_der
        if not (row >= 0 and col >= 0 and row < 8 and col < 8):
            break
        
        if board[row][col] == 1:
            return True
        
    return False


def fitness(board):
    fitness = 0
    #checking row and column
    #check diags
    for i, row in enumerate(board):
        #rows
        if row.count(1) > 1:
            continue
        
        #columns
        if row.count(1) == 0:
            continue
        
        j = col = row.index(1)
        
        board = numpy.array(board)
        col = list(board[:, col])
        
        if col.count(1) > 1:
            continue
        
        if diag_attacking(board, i, j, -1, -1):
            continue
        if diag_attacking(board, i, j, -1, +1):
            continue
        if diag_attacking(board, i, j, +1, -1):
            continue
        if diag_attacking(board, i, j, +1, +1):
            continue
    
    
        fitness += 1
    
    return fitness

def display_board(board):
    print()
    for row in board:
        print(row)

def selection(boards):
    boards.sort(key = lambda entry: fitness(entry), reverse = True)
    return boards[0:3]

def crossover(selected, number_of_children, mutate = False):
    #pick a random slicing location and merge two randomly selected
    children = []
    for i in range(number_of_children):
        parents = (rn.randint(0, len(selected)-1), rn.randint(0, len(selected)-1))
        #print("Crossing over parents {} and {}".format(parents[0], parents[1]))
        #div = rn.randint(0, 7)
        div = 4
        while len(children) < number_of_children:
            child = []
            child1 = []
            for j in range(0, div):
                child.append(selected[parents[0]][j])
                child1.append(selected[parents[1]][j])
            for j in range(div, 8):
                child.append(selected[parents[1]][j])
                child1.append(selected[parents[0]][j])
            children.append(child)
            children.append(child1)
    
    
    if mutate:
        for i in range(len(children)):
            m = mutate_rep(row_rep(children[i]))
            children[i] = ext_from_rep(m)
            
    return children
                
        
def row_rep(board):
    rep = "" #representation
    for row in board:
        rep += str(row.index(1))
    return rep

def ext_from_rep(rep):
    board = []
    for i in range(len(rep)):
        row = [0 for j in range(8)]
        row[int(rep[i])] = 1
        board.append(row)
    return board

def mutate_rep(rep):
    global mutation_thresh
    if rn.random() > mutation_thresh:
        rep = list(rep)
        rep[rn.randint(0, len(rep)-1)] = str(rn.randint(0, 7))
    return "".join(rep)
    

def make_offsprings(p1, p2, n_points):
    """
        pass p1 and p2 as row_rep
        returns children in row_rep
    """
    children = []
    point = -1
    p = [p1, p2]
    pi = 0
    child = ""
    child1 = ""
    for i in range(n_points):
        start = 0
        if point > -1:
            start = point
            
        point = rn.randint(start, len(p1) - 1)
        child += p[0][start:point]
        child
        
        
    return children
        
boards = initialize(8)

best_board = []
max_fitness = -1
while max_fitness != 8:
    for board in boards:
        if fitness(board) > max_fitness:
            #display_board(board)
            best_board = board
            print("fitness of board is {}".format(fitness(board)))
            max_fitness = fitness(board)
    selected = selection(boards)
    boards = crossover(selected, 8, mutate = True)

display_board(best_board)
rep = row_rep(best_board)
print(rep)
