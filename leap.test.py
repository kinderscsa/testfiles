# -*- coding: utf-8 -*- 

 
import unittest 
import leap

 
class yearTestCase(unittest.TestCase):
    def test_year(self): 
        self.assertEqual(leap.leap(1950),'평년') 
        self.assertEqual(leap.leap(2012),'윤년') 
        self.assertEqual(leap.leap(2000),'윤년') 

if __name__=="__main__": 
    unittest.main(verbosity=2) 
