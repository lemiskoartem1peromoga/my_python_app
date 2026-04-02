from app import add

def test_answer():
    assert add(2, 2) == 4

def test_negative():
    assert add(-1, -1) == -2
