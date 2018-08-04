import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
	def testFirstNumber(self):
		self.assertEqual(add(0 ,0), 0)
		self.assertEqual(add(10.0 , 1.126) , 11.126)
	unittest.main()

