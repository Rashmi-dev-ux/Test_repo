import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import kirana_cli

def test_view_stock(capsys):
    kirana_cli.view_stock()
    captured = capsys.readouterr()
    output = captured.out
    print("output:", output)
    assert "1.  Rice" in output
