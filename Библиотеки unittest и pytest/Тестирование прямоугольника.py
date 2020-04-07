import pytest
from yandex_testing_lesson import Rectangle
def test_1():
    with pytest.raises(TypeError):
        Rectangle('1', 12)
def test_2():
    with pytest.raises(TypeError):
        Rectangle([], 12)
def test_3():
    with pytest.raises(TypeError):
        Rectangle(12, '1')
def test_4():
    with pytest.raises(TypeError):
        Rectangle(12, [])
def test_5():
    with pytest.raises(ValueError):
        Rectangle(12, -1)
def test_6():
    with pytest.raises(ValueError):
        Rectangle(-1, 12)
def test_7():
    with pytest.raises(TypeError):
        Rectangle(-1, '1')
def test_8():
    with pytest.raises(TypeError):
        Rectangle('1', -1)
def test_9():
    assert Rectangle(5, 7).get_area() == 35
def test_10():
    assert Rectangle(5, 7).get_perimeter() == 24