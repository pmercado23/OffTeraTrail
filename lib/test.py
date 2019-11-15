import unittest


class Test(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        self.assertEqual(True, True, "Should be True")


if __name__ == '__main__':
    unittest.main()