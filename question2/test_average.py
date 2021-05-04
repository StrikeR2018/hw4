
import unittest
import average

class TestCase(unittest.TestCase):

    def test_average_1(self):
        self.assertEqual(average.Average([1,2,3,4,5]), 3)

    def test_average_2(self):
        self.assertEqual(average.Average([1,2,3]), 2)

    def test_average_3a(self):
        self.assertEqual(average.Average(['a','b','c']), None)

    def test_average_3b(self):
        self.assertEqual(average.Average([]), -1)

    def test_average_4(self):
        self.assertEqual(average.Average("I am a string"), None)

    def test_average_5(self):
        self.assertEqual(average.Average("Hello"), "Something")

if  __name__ == "__main__":
    unittest.main()