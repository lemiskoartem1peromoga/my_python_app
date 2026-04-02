from app import add

def test_pos(): assert add(2, 2) == 4
def test_neg(): assert add(-1, -1) == -2
def test_zero(): assert add(5, 0) == 5
