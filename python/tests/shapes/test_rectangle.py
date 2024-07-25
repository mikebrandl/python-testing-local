from curses.textpad import rectangle

import pytest
from python.app.shapes.rectangle import Rectangle

class TestRectangle:

    @pytest.fixture
    def test_rectangle(self):
        return Rectangle(10,20)

    def test_area(self, test_rectangle):
        assert test_rectangle.area() == 200

    @pytest.mark.skip(reason="not implemented")
    def test_perimeter(self, test_rectangle):
        assert test_rectangle.perimeter() == 60

    @pytest.mark.slow
    def test_invalid_shape(self, test_rectangle):
        assert test_rectangle.perimeter() == 60

    @pytest.mark.parametrize('side_length, expected_perimeter',  [(10, 40), (20, 80)])
    def test_parameterize(self, side_length, expected_perimeter):
        rect = Rectangle(side_length, side_length)
        assert rect.perimeter() == expected_perimeter