from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

#Returns starting state of the board.
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#Returns player who has the next turn on a board
def player(board):
    count = sum([row.count(X) for row in board]) - sum([row.count(O) for row in board])
    return X if count == 0 else O

#Returns set of all possible actions (i, j) available on the board.
def actions(board):
    set_possible_actions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                set_possible_actions.add((i,j))
    return set_possible_actions

#Returns the board that results from making move (i, j) on the board.
def result(board, action):
    i,j=action
    set_possible_actions = actions(board)
    if action not in set_possible_actions or i not in [0,1,2] or j not in [0,1,2]:
        raise NameError('Invalid_action')
    gameboard= deepcopy(board)
    gameboard[i][j]= player(board)
    return gameboard

#Returns the winner of the game, if there is one.
def winner(board):
    for player in [X, O]:
        # check rows
        for row in board:
            if all([cell == player for cell in row]):
                return player
        # check columns
        for col in range(3):
            if all([board[row][col] == player for row in range(3)]):
                return player
        # check diagonals
        if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
            return player
        
    # No winner of the game either because the game is in progress, or because it ended in a tie.
    return None

#Returns True if game is over, False otherwise.
def terminal(board):
    if (winner(board) == X) or (winner(board) == O):
        return True
    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True

#Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    match winner(board):
        case "X":   return 1
        case "O":   return -1
        case other: return 0

#Returns the optimal action for the current player on the board.
def minimax(board):
    if terminal(board):
        return None
    return max_value(board)[1] if player(board) == X else min_value(board)[1]

def max_value(board):
    if terminal(board):
        return [utility(board),None]

    v = float("-inf")
    move = None
    for action in actions(board):
        min_val = min_value(result(board, action))[0]
        if v<min_val:
            v = min_val
            move = action
        if v==1: break
    return [v,move]

def min_value(board):
    if terminal(board):
        return [utility(board),None]

    v = float("inf")
    move=None
    for action in actions(board):
        max_val = max_value(result(board, action))[0]
        if v>max_val:
            v = max_val
            move = action
        if v==-1: break
    return [v,move]