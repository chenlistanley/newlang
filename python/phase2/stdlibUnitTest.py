import unittest
from stdlibUnit import sum,divide

class Tester(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(sum(1,3), 4)
		# self.assertEqual(sum(1,3), 5)
	
	def test_divide(self):
		self.assertEqual(divide(3,1), 3)
		self.assertRaises(ZeroDivisionError, divide, 1, 0)

unittest.main()