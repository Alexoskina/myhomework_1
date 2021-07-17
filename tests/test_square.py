import pytest
from src.Square import Square

name = "square_1"


def test_area():
    square = Square(name, 13)
    assert square.area() == 169


def test_perimeter():
    square = Square(name, 10)
    assert square.perimeter() == 40


def test_name():
    square = Square(name, 10)
    assert square.name


def test_add_area():
    square1 = Square(name, 2)
    square2 = Square(name, 2)
    assert square1.add_area(square2) == 8


