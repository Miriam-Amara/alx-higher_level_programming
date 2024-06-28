import unittest

max_i = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_i([]), None)
        self.assertEqual(max_i([3, 4, 5, 6]), 6)
        self.assertEqual(max_i([3.0, -5.8, -9]), 3.0)
        self.assertEqual(max_i([9, 4, 3, 2]), 9)
        self.assertEqual(max_i([4, 5, 50, 7, 8]), 50)
        self.assertEqual(max_i([-7, -5, -2, -10]), -2)
        self.assertEqual(max_i([5]), 5)


if __name__ == "__main__":
    unittest.main()
