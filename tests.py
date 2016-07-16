import unittest
from mymodule import add_integers

class TestMyModule(unittest.TestCase):

    def test_add_integers_with_integers(self):
        self.assertEqual(add_integers(1, 2), 3)

    def test_add_integers_negative(self):
        n1 = -2
        n2 = 0
        expected_value = n1 + n2
        self.assertEqual(
            add_integers(n1, n2),
            expected_value
        )

    def test_add_integers_error_if_not_int(self):
        pass

    def test_assert_int_int_raises_no_error(self):
        pass

    def test_assert_int_non_int_raises_typeerror(self):
        pass

if __name__ == '__main__':
    unittest.main()

