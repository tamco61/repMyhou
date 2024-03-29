from yandex_testing_lesson import is_under_queen_attack
import pytest
def test_type_first():
    with pytest.raises(TypeError):
        is_under_queen_attack(2, 'e3')
def test_type_first1():
    with pytest.raises(TypeError):
        is_under_queen_attack([], 'e3')
def test_type_second():
    with pytest.raises(TypeError):
        is_under_queen_attack('e3', 4)
def test_type_second1():
    with pytest.raises(TypeError):
        is_under_queen_attack('e3', 4)
def test_format_first():
    with pytest.raises(ValueError):
        is_under_queen_attack('aa', 'a3')
def test_format_first1():
    with pytest.raises(ValueError):
        is_under_queen_attack('a', 'e3')
def test_format_first2():
    with pytest.raises(ValueError):
        is_under_queen_attack('q2', 'e3')
def test_format_first3():
    with pytest.raises(ValueError):
        is_under_queen_attack('e9', 'e3')
def test_format_first4():
    with pytest.raises(ValueError):
        is_under_queen_attack('j9', 'e3')
def test_format_second():
    with pytest.raises(ValueError):
        is_under_queen_attack('a3', 'aa')
def test_format_second1():
    with pytest.raises(ValueError):
        is_under_queen_attack('e3', 'a')
def test_format_second2():
    with pytest.raises(ValueError):
        is_under_queen_attack('e3', 'q2')
def test_format_second3():
    with pytest.raises(ValueError):
        is_under_queen_attack('e3', 'e9')
def test_format_second4():
    with pytest.raises(ValueError):
        is_under_queen_attack('e3', 'j9')
def test_typefirst_secondformat():
    with pytest.raises(TypeError):
        is_under_queen_attack(3, 'j9')
def test_typefirst_secondformat1():
    with pytest.raises(TypeError):
        is_under_queen_attack([], 'j9')
def test_formatfirst_secondtype():
    with pytest.raises(ValueError):
        is_under_queen_attack('j9', 3)
def test_formatfirst_secondtype1():
    with pytest.raises(ValueError):
        is_under_queen_attack('sss', [])