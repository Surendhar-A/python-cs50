from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Ashwin") == "hello, Ashwin"

def test_loop():
    for name in ["Hermoine", "Harry", "Rone"]:
        assert hello(name) == f"hello, {name}"