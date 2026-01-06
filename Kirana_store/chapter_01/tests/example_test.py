# import logging


# def test_example_01():
#     a = 5
#     assert a ==5

# def test_checkCase():
#     assert 'hello'.upper() == 'HELLO'
# #==========================================
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b


# def test_add():
#     assert add(2,3) == 5

# def print_me():
#     print("Hello World")
#     print("It is me here")

# def test_subtract():
#     assert subtract(5,2) == 3

# #from inventory import view_stock


# def test_print_me(capsys):
#     print_me()
#     cap = capsys.readouterr()
#     out = cap.out
#     print( out)
#     assert "Hello World" in out

def addition(a,b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number:"))
    c = a+b
    print(c)
    return c

def test_additon(monkeypatch):
    #call the method to test
    input = iter(["4", '5'])
    monkeypatch.setattr("builtins.input",lambda _: next(input))
    c = addition(4,5)
    assert c ==9