# app.py
# This is a test commit

#Anurag is making some changes 
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0


def test_sub():
    assert sub(5, 2) == 3
    assert sub(1, 2) == -1
