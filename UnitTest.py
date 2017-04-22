# -*- coding: utf-8 -*-

import unittest
from Simhash import *
import hashlib

class MyTestCase(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(True, True)

    def test_splitter(self):
        data = "Mignonne, allons voir"
        my_simhash = SimHash(data, span)
        splitted_tab = my_simhash.get_splitted_tab()
        self.assertEqual(splitted_tab[0][0], "Mign")
        self.assertEqual(splitted_tab[1][0], "igno")
        self.assertEqual(splitted_tab[17][0], "voir")

    def test_hash_part(self):
        data = "abc"
        m = hashlib.md5()
        m.update(data.encode())
        str = m.hexdigest()
        self.assertEqual(str, SimHash.hash_part(None,data))

    def test_calc_vector(self):
        data = b'\xfc'
        res = [1, 1, 1, 1, 1, 1, -1, -1]
        self.assertEqual(SimHash.calc_vector(data), res)
        data = b'\x00'
        res = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.assertEqual(SimHash.calc_vector(data), res)

    def test_calc_final_hash(self):
        vector = [5, 4, -9, 9, 8, -7, 9, -6]
        res = 218
        self.assertEqual(SimHash.calc_final_hash(vector), res)
        vector = [-5, -4, -9, -9, 8, -7, 9, -6]
        res = 9
        self.assertEqual(SimHash.calc_final_hash(vector), res)

if __name__ == '__main__':
    unittest.main()
