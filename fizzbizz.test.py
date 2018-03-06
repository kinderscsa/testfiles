# -*- coding: utf-8 -*-

import unittest 
import fizzbizz
 
 
class FizzBizzTestCase(unittest.TestCase): 
    def test_fizzbizz(self): 
        self.assertEqual(fizzbizz.fizzbizz(30),'Fizz') 
        self.assertEqual(fizzbizz.fizzbizz(40),'Bizz') 
        self.assertEqual(fizzbizz.fizzbizz(0),'ValueError') 

if __name__=="__main__":
    unittest.main(verbosity=2) 
