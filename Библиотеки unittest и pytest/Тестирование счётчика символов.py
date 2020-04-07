import pytest
from yandex_testing_lesson import count_chars
def test_empty():
    assert count_chars('') == {}
def test_one_char():
    assert count_chars('q') == {'q': 1}
def test_default():
    assert count_chars('Qwerty12345qwerty') == {'Q': 1, 'q': 1, 'w': 2, 'e': 2, 'r': 2, 't': 2, 'y': 2, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1}
def test_wrong_type_int():
    with pytest.raises(TypeError):
        count_chars(42)
def test_wrong_type_list_int():
    with pytest.raises(TypeError):
        count_chars([42, 2, 3])
def test_wrong_type_list_str():
    with pytest.raises(TypeError):
        count_chars(['4', 'w', '2'])