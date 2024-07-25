import math

import pytest
from python.app.shapes.circle import Circle

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        # Would tear down anyway.
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == math.pi * self.circle.radius * 2