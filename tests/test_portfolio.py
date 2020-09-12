""" Tests for 'portfolio' package """
import pytest

from portfolio import portfolio


def test_helloworld(capsys):
    """ Correct object argument prints """
    portfolio.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


# This is supposed to fail
def test_helloworld_exception():
    with pytest.raises(TypeError):
        portfolio.helloworld(1)
