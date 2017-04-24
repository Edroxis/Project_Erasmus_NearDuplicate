# -*- coding: utf-8 -*-
from hashlib import md5
import binascii


if __name__ == '__main__':
    m = md5()
    m.update("hello world!".encode())
    bin = binascii.unhexlify(m.hexdigest())
    print(m.hexdigest())
