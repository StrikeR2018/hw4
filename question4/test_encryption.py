
import unittest
import encryption

class TestCase(unittest.TestCase):

    def test_encryption_1(self):
        self.assertEqual(encryption.encrypt(("Sending message on social media",  "vo30df;1jd0g5ydl1d9gospf[gefd ", "abcdefghijklmnopqrstuvwxyz.,! "),"9dy0jy; 5d99v;d dy 9d3jvg 5d0jv")

    def test_encryption_2(self):
        self.assertEqual(encryption.encrypt(("Hello World", "sddsadsdfsdfsdfsdfg44spf[gefd ", "abcdefghijklmnopqrstuvwxyz.,! "), "dafff pfffs")

    def test_encryption_3(self):
        self.assertEqual(encryption.encrypt(("Bankcard password qwert", "uvhifuhsdfiuqflsdhkjhlqiuhr12 ", "abcdefghijklmnopqrstuvwxyz.,! "), "vufihuhi sukkqlhi dqfhj")

if  __name__ == "__main__":
    unittest.main()