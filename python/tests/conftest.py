from python.app.shapes.circle import Circle
import pytest

@pytest.fixture
def test_circle(self):
    return Circle(10)