import unittest

class TestPinValidation(unittest.TestCase):

    def test_pin_validation_success(self):
       actual = self()
       expected= ("Pin succesful")
       self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
