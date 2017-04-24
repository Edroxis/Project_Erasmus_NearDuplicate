# -*- coding: utf-8 -*-

import unittest
from simhash import *
from simhash_index import *
import hashlib


class TestSimhash(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(True, True)

    def test_splitter(self):
        data = "Mignonne, allons voir"
        splitted_tab = Simhash.splitter(data)
        self.assertEqual(splitted_tab[0][0], "Mign")
        self.assertEqual(splitted_tab[1][0], "igno")
        self.assertEqual(splitted_tab[17][0], "voir")

    def test_hash_part(self):
        data = "abc"
        m = hashlib.md5()
        m.update(data.encode())
        str = m.hexdigest()
        self.assertEqual(str, Simhash.hash_part(data))

    def test_calc_vector(self):
        data = [(None, "fc")]
        res = [1, 1, 1, 1, 1, 1, -1, -1]
        self.assertEqual(Simhash.calc_vector(data), res)
        data = [(None, "00")]
        res = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.assertEqual(Simhash.calc_vector(data), res)
        data = [(None, "00"), (None, "ff")]
        res = [0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(Simhash.calc_vector(data), res)

    def test_calc_final_hash(self):
        vector = [5, 4, -9, 9, 8, -7, 9, -6]
        res = 218
        self.assertEqual(Simhash.calc_final_hash(vector), res)
        vector = [-5, -4, -9, -9, 8, -7, 9, -6]
        res = 10
        self.assertEqual(Simhash.calc_final_hash(vector), res)


# class TestSimhashIndex(unittest.TestCase):
#     def test_blank(self):
#         self.assertEqual(True, True)
#
#     def test_add_sh(self):
#         sim = Simhash(0, "I like trains")
#         HashIndex.add_sh(sim)
#         self.assertEqual(len(HashIndex.hash_table), 1)
#         sim = Simhash(1, "Hey, do you wanna skateboard?")
#         HashIndex.add_sh(sim)
#         self.assertEqual(len(HashIndex.hash_table), 2)
#         sim = Simhash(1, "Suddenly, pineapples.")
#         HashIndex.add_sh(sim)
#         self.assertEqual(len(HashIndex.hash_table), 2)

if __name__ == '__main__':
    unittest.main()
