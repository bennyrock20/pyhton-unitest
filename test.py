import unittest
from Calc import *

class Test(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_identification(self):
        self.assertTrue(Calc("0104967500").is_valid_identification())

    def test_identification2(self):
        self.assertFalse(Calc("0104967501").is_valid_identification())

    def test_identification3(self):
        self.assertTrue(Calc("2222222222").is_valid_identification())

    def test_identification4(self):
        self.assertFalse(Calc("1").is_valid_identification())

    def test_identification5(self):
        self.assertFalse(Calc("j1049675001").is_valid_identification())

    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(Calc("weffjejfewqw").is_valid_identification())

if __name__=='__main__':
    unittest.main()
