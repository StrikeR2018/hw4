import unittest
import full

class test_case(unittest.TestCase):

    def test_full_1(self):
        self.assertEqual(full.full("Mingx", "Li"), "Mingx Li")
    
    def test_full_2(self):
        self.assertEqual(full.full("M1ngx", "Li"), None)

    def test_full_3(self):
        self.assertEqual(full.full("M1ngx", "Li"), "M1ngx Li")

    def test_full_4(self):
        self.assertEqual(full.full("?Mingx", "Li"), None)

if __name__=="__main__":
    unittest.main()