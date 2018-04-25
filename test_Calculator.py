import unittest
import Calculator


class TestCalculator (unittest.TestCase):
    # testing -1 + 0
    # testing -1 + -1
    # testing 0 + 0
    # testing that both values not equal null
    # both values are integers

    def test_add(self):
        self.assertEqual(Calculator.add(5, 12), 17)
        self.assertEqual(Calculator.add(-1, 0), -1)
        self.assertEqual(Calculator.add(-1, -1), -2)
        self.assertEqual(Calculator.add(0, 0), 0)


        self.assertEqual(Calculator.add(0, "10"), 10)
#test 5*0 = 0
#test 5*-1 = -5
#test in both values are integers

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(5, 0), 0)
        self.assertEqual(Calculator.multiply(5, -1), -5)


        #testing that both values are integers and it raise errors
        self.assertRaises(ValueError, Calculator.add, "1", 0)
        self.assertRaises(ValueError, Calculator.add, 1, "0")

        #testing that there is only 2 arguments passing
        self.assertRaises(TypeError, Calculator.multiply, 1, 0, 3)

#Testing 5/2 Not =2 "by keep track bl float"
#Testing 5/2 =2.5
#Make sure that it raises error lma a3ml int/0
    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertRaises(ValueError, Calculator.divide, 10, 0)
        self.assertNotEqual(Calculator.divide(5, 2), 2)
        self.assertEqual(Calculator.divide(5, 2), 2.5)


#testing sub small numbers out of big numbers 5-12 = -7
# testing -1 - -1 = 0
    def test_sub(self):
        self.assertEqual(Calculator.sub(5, 12), -7)
        self.assertEqual(Calculator.sub(-1, -1), 0)
