import unittest
import homework
from parameterized import parameterized


class test_functions(unittest.TestCase):
    @parameterized.expand([
        [-2, 0, 123, "Triangle sides have to be positive number"],
        ["2134", 12, 46, "Triangle sides is not numeric"],
        [25, 30, 123456.456, "Triangle with this sides not exist"],
        [2, 3, 4, 2.90474],
        [3, 4, 5, 6]
    ])
    def test_triangle(self, a, b, c, result):
        self.assertEqual(homework.square_triangle(a, b, c), result, f"Test_triangle for function homework.square_triangle FAILED with error {result}")

if __name__ == "__main__":
    unittest.main()