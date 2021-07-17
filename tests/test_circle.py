from src.Circle import Circle

name = "circle_1"


def test_perimeter():
    circle = Circle(name, 3)
    assert circle.perimeter() == 10


def test_area():
    circle = Circle(name, 2)
    assert circle.area() == 10


def test_create_circle_with_negative_radius():
    circle = Circle(name, -10)
    assert circle is None