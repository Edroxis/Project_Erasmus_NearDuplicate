import unittest
from Simhash import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_splitter(self):
        data = "Mignonne, allons voir"
        my_simhash = SimHash(data, span)
        splitted_tab = my_simhash.get_splitted_tab()
        self.assertEqual(splitted_tab[0][0], "Mign")
        self.assertEqual(splitted_tab[1][0], "igno")
        self.assertEqual(splitted_tab[17][0], "voir")

    def test_part_hash(self):
        data = "abc"


if __name__ == '__main__':
    unittest.main()
