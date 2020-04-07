import unittest
from yandex_testing_lesson import reverse
class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')
    def test_one_char(self):
        self.assertEqual(reverse('w'), 'w')
    def test_palindrome(self):
        self.assertEqual(reverse('qweewq'), 'qweewq')
    def test_default(self):
        self.assertEqual(reverse('qwerty'), 'ytrewq')
    def test_wrong_type_int(self):
        with self.assertRaises(TypeError):
            reverse(42)
    def test_wrong_type_list_int(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3, 4])
    def test_wrong_type_list_str(self):
        with self.assertRaises(TypeError):
            reverse(['1', '2', '3', '4'])
if __name__ == '__main__':
     unittest.main()
