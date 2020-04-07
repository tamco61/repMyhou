import pytest
def test_empty():
    assert reverse('') == ''
def test_one_char():
    assert reverse('w') == 'w'
def test_palindrome():
    assert reverse('qweewq') == 'qweewq'
def test_default():
    assert reverse('qwerty') == 'ytrewq'
def test_wrong_type_int():
    with pytest.raises(TypeError):
        reverse(42)
def test_wrong_type_list_int():
    with pytest.raises(TypeError):
        reverse([1, 2, 3, 4])
def test_wrong_type_list_str():
    with pytest.raises(TypeError):
        reverse(['1', '2', '3', '4'])