import unittest


class SmokeTest(unittest.TestCase):
    def test_func_false_is_not_true(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
