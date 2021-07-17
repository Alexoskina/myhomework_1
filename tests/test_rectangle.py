import pytest
from src.Rectangle import Rectangle

name = "rectangle_1"


def test_create_class():
    rectangle = Rectangle(name, 2, 4)
    assert isinstance(rectangle, Rectangle)
    assert rectangle.a == 2
    assert rectangle.b == 4
    assert rectangle.name == name
    assert rectangle.angl == 4


def test_perimeter():
    rectangle = Rectangle(name, 10, 10)
    assert rectangle.perimeter() == 12


def test_area():
    rectangle = Rectangle(name, 2, 4)
    assert rectangle.area() == 10

def test_add_area():
    rectangle1 = Rectangle(name, 2, 4)
    rectangle2 = Rectangle(name, 2, 4)
    assert rectangle1.add_area(rectangle2)




