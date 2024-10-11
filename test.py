from app import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(1000000, 999999) == 1

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("Tous les tests sont passés !")
