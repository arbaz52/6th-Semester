#string board is the current cofiguration of the board
#string des is the destination configuration for the board
#functions will be defined afterwards
#functions required: go up, go down, go left, go right
#functions will return the possible board configuration after the move has been made or will return -1 if it's not possible
#the dfs, bfs will work as they should

def find_space(board):
    return board.index('0')

def swap(board, n, n1):
    l = list(board)
    temp = l[n]
    l[n] = l[n1]
    l[n1] = temp
    return "".join(l)

def go_up(board):
    ind = find_space(board)
    n_ind = ind - 3 
    if n_ind >= 0:
        return swap(board, ind, n_ind)
    else:
        return -1
    
def go_down(board):
    ind = find_space(board)
    n_ind = ind + 3 
    if n_ind < len(board):
        return swap(board, ind, n_ind)
    else:
        return -1
    
def go_left(board):
    ind = find_space(board)
    n_ind = ind - 1
    if n_ind >= 0:
        return swap(board, ind, n_ind)
    else:
        return -1
    
def go_right(board):
    ind = find_space(board)
    n_ind = ind + 1
    if n_ind < len(board):
        return swap(board, ind, n_ind)
    else:
        return -1
    
    
def bfs(board, dest):
    visited = []
    queue = [board]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            if current == dest:
                break
            moves = [go_up(current), go_down(current), go_left(current), go_right(current)]
            moves_ok = []
            for move in moves:
                if move != -1 and move not in visited:
                    queue.append(move)
                    moves_ok.append(move)
            #print("moves for {}: {}".format(current, moves_ok))
    return visited

def dfs(board, dest):
    visited = []
    queue = [board]
    while queue:
        current = queue.pop()
        if current not in visited:
            visited.append(current)
            if current == dest:
                break
            moves = [go_up(current), go_down(current), go_left(current), go_right(current)]
            moves_ok = []
            for move in moves:
                if move != -1 and move not in visited:
                    queue.append(move)
                    moves_ok.append(move)
            #print("moves for {}: {}".format(current, moves_ok))
    return visited

def manhattan_distance(current, dest):
    sum = 0
    for i, val in enumerate(current):
        """
        x is row
        y is col
        """
        x_val, y_val = i/3, i%3
        goal_ind = dest.index(val)
        x_goal, y_goal = goal_ind/3, goal_ind%3
        sum += abs(x_val - x_goal) + abs(y_val - y_goal)
    return sum


#print(dfs("283164705", "123804765"))

        
    