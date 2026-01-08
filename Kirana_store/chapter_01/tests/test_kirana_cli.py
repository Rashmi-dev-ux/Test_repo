import sys
import os

#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, r'D:\\Jen_project\\Kirana_store\\chapter_01')

import kirana_cli

def test_view_stock(capsys):
    kirana_cli.view_stock()
    captured = capsys.readouterr()
    output = captured.out
    assert "1.  Rice" in output

def test_add_stock(monkeypatch, capsys):
    input_list = ["2", "40"]
    inputs = iter(input_list)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    kirana_cli.add_stock()

    output = capsys.readouterr().out
    assert "Added 40" in output
    current_qunt = kirana_cli.stock[2-1]["quantity"]
    print(current_qunt)
    new_qunt = current_qunt + int(input_list[1])
    assert new_qunt == current_qunt + 40


def test_add_stock_01(monkeypatch):
    input = iter(["3", "100"])
    
    monkeypatch.setattr("builtins.input", lambda _:next(input))
    kirana_cli.add_stock()

    current_quant = kirana_cli.stock[2]["quantity"]
    print(current_quant)
    new_quant = current_quant + 100
    assert new_quant == 125


#======================================================================================


def test_remove_stock(monkeypatch):
    # take input before calling remove_stock method and patch with the help of monkeypatch
    input =iter([2, 10])
# 
    monkeypatch.setattr("builtins.input", lambda _: next(input))#taking input one by on

    # call method remove_stock
    kirana_cli.remove_stock()

    current_quant = kirana_cli.stock[2-1]["quantity"]
    print (current_quant)
    new_quant = current_quant - 10
    assert new_quant == 50
    
 #=======================================================

def test_buy_product(monkeypatch):
    inputs = iter(['2', '20'])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    

    initial_stock = kirana_cli.stock[2- 1]["quantity"]
    kirana_cli.buy_product()

    assert kirana_cli.stock[2-1]["quantity"] == initial_stock - 20






    
