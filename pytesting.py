from tictactoe import player,actions,result,winner,terminal,utility,max_value,min_value,minimax
X="X"
O="O"
seta=set()
EMPTY = None
def test_player():
    assert player([[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]) == X
    assert player([[X, X, EMPTY],[EMPTY, O, EMPTY],[EMPTY, O, EMPTY]]) == X
    assert player([[X, X, O],[X, O, EMPTY],[O, O, X]]) == X
    assert player([[X, X, O],[X, O, X],[O, O, X]]) == O

def test_actions():
    assert actions([[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]) == {(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}
    assert actions([[X, X, EMPTY],[EMPTY, O, EMPTY],[EMPTY, O, EMPTY]]) == {(2, 0), (0, 2), (2, 2), (1, 0),(1,2)}
    assert actions([[X, X, O],[X, O, EMPTY],[O, O, X]]) == {(1,2)}
    assert actions([[X, X, O],[X, O, X],[O, O, X]]) == seta

def test_result():
    assert result([['X', 'O', 'O'], [None, 'X', None], ['X', None, None]], (2, 1)) == [['X', 'O', 'O'], [None, 'X', None], ['X', 'O', None]]
    assert result([[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]], (2, 1)) == [[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, X, EMPTY]]

def test_winner():
    assert winner([[X, X, O],[X, O, X],[O, O, X]]) == O #diag
    assert winner([[X, O, O],[X, X, X],[O, O, X]]) == X #horizontal
    assert winner([[X, O, X],[O, X, X],[O, X, X]]) == X #vertical
    assert winner([[X, O, EMPTY],[EMPTY, O, EMPTY],[EMPTY, O, EMPTY]]) == O
    assert winner([[X, O, X],[O, X, X],[O, X, O]]) == None
    assert winner([[X, X, EMPTY],[EMPTY, O, EMPTY],[EMPTY, O, EMPTY]]) == None

def test_terminal():
    assert terminal([[X, O, X],[O, X, X],[O, X, O]]) == True
    assert terminal([[X, X, O],[X, O, X],[O, O, X]]) == True
    assert terminal([[X, O, O],[X, X, X],[O, O, X]]) == True
    assert terminal([[X, O, X],[O, X, X],[O, X, EMPTY]]) == False
    assert terminal([[X, X, EMPTY],[EMPTY, O, EMPTY],[EMPTY, O, EMPTY]]) == False
    assert terminal([[X, O, EMPTY],[EMPTY, O, EMPTY],[EMPTY, O, EMPTY]]) == True

def test_utility():
    assert utility([[X, X, O],[X, O, X],[O, O, X]]) == -1 #diag
    assert utility([[X, O, O],[X, X, X],[O, O, X]]) == 1 #horizontal
    assert utility([[X, O, X],[O, X, X],[O, X, X]]) == 1 #vertical
    assert utility([[X, O, X],[O, X, X],[O, X, O]]) == 0
def test_maxval():
    assert max_value([[O, X, O],[O, X, X],[X, EMPTY, O]]) == [1,(2,1)]
    assert max_value([[EMPTY, X, O],[O, X, X],[X, O, O]]) == [0,(0,0)]

def test_minval():
    assert min_value([[EMPTY, X, O],[O, X, X],[X, EMPTY, O]]) == [0,(2,1)]

def test_minimax():
    assert minimax([[EMPTY, X, O],[O, X, X],[X, EMPTY, O]]) == (2,1)
    assert minimax([[EMPTY, X, EMPTY],[O, X, X],[X, EMPTY, O]]) == (0,2)