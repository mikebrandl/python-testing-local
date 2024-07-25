from python.app.subdir.main import mainFunction
from python.app.subdir.main2 import Main2


def test_mainFunction():
    assert mainFunction() == "Hello World!"


def test_main2():
    m = Main2()
    assert m.get_name() == "Main2"
