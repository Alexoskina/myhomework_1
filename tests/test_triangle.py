from src.Triangle import Triangle

name = "triangle_1"


def test_create_class():
    triangle = Triangle(name, 4, 4, 4)
    assert isinstance(triangle, Triangle)
    assert triangle.a == 4
    assert triangle.b == 4
    assert triangle.c == 4
    assert triangle.name == name
    assert triangle.angl == 3


def test_perimeter():
    triangle = Triangle(name, 10, 10, 10)
    assert triangle.perimeter() == 12


def test_area():
    triangle = Triangle(name, 4, 4, 4)
    assert triangle.area == 10


def test_add_area():
    triangle1 = Triangle(name, 4, 4, 4)
    triangle2 = Triangle(name, 6, 6, 6)
    assert triangle1.add_area(triangle2)
