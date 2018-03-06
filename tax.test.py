# -*- coding: utf-8 -*-

import unittest
import tax



class taxTestCase(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(tax.tax(27, 23000, True),int(23000*0.1))


if __name__=="__main__":
    unittest.main(verbosity=2)
