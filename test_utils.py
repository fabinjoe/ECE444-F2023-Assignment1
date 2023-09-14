import unittest
from utils import Utils

class MyTestCase(unittest.TestCase):
  def reversed_tests(self):
    test_utils = Utils()
    self.assertEqual(test_utils.reversed(21), 12)
    with self.assertRaises(TypeError):
      test_utils.reversed(21.32)
    with self.assertRaises(TypeError):
      test_utils.reversed("23")

  def formatter_tests(self):
    test_utils = Utils()
    self.assertEqual(test_utils.formatter(2, 2), bin(2)
    self.assertEqual(test_utils.formatter(2, 8), oct(2)
    with self.assertRaises(TypeError):
      test_utils.formatter(2.23, 2)
    with self.assertRaises(TypeError):
      test_utils.formatter("23", 2)
