# -*- coding: utf-8 -*-

import hashlib
import binascii

if __name__ == '__main__':
    # m = hashlib.md5()
    # m.update("hello ".encode())
    # m.update("world".encode())
    # print(m.digest())
    n = hashlib.md5()
    #n.update("hello world".encode())
    print(n.hexdigest())

    # Transform hex string representation to int table
    bin = binascii.unhexlify(n.hexdigest())
    print(type(bin))
    print(bin)
    int_index = 0
    for b in bin:
        bit_tester = 128
        print(b)
        for counter in range(0,8):
            print(counter.__str__()+" "+ (b & bit_tester).__str__())
            bit_tester = bit_tester.__rshift__(1)
        int_index += 1
