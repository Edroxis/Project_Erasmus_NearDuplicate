# -*- coding: utf-8 -*-

from hashlib import md5
from simhash import Simhash
from jsonmanager import JsonManager
import binascii
import json

if __name__ == '__main__':
    # m = md5()
    # m.update("hello world!".encode())
    # # print(m.digest())
    # n = md5()
    # n.update("hello world".encode())
    # print(type(n.hexdigest()))
    #
    # # Transform hex string representation to int table
    # bin = binascii.unhexlify(m.hexdigest())
    # print(type(bin))
    # print(bin)

    # bin2 = binascii.unhexlify(n.hexdigest())
    # print(bin2)
    # bin3 = []
    # i=0
    # for b1 in bin:
    # #   bin3[i]= b1 & bin2[i] # WRONG WAY
    #     i+=1
    # print(bin3.__str__())

    # res = [0]*bin.__len__()*8
    # int_index = 0
    # for b in bin:
    #     bit_tester = 128
    #     print(b)
    #     for counter in range(0, 8):
    #         print(counter.__str__()+" "+ (b & bit_tester).__str__())
    #         if((b & bit_tester) != 0):
    #             res[int_index*8+counter] += 1
    #         else:
    #             res[int_index * 8 + counter] -= 1
    #         bit_tester = bit_tester.__rshift__(1)
    #     int_index += 1
    # print(len(res))
    # print(res)
    # i = int(binascii.hexlify(bin),16)#binascii.hexlify(bin)
    # print(i)

    # sim = Simhash(0, "hello world")
    # JsonManager.save_json("test.json", sim)

    # sim = JsonManager.open_json("test.json")
    # print(sim)

    with open("data.json", "r", encoding="utf-8") as file:
        obj = json.load(file)
    print(type(obj))
    for key in obj:
        print(key + " " + obj[key])

