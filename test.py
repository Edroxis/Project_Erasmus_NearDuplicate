# -*- coding: utf-8 -*-

from hashlib import md5
from simhash import Simhash
from jsonmanager import JsonManager
import binascii
import json

if __name__ == '__main__':
    # sim = Simhash(0, "hello world")
    # JsonManager.save_json("test.json", sim)

    # sim = JsonManager.open_json("test.json")
    # print(sim)

    with open("data.json", "r", encoding="utf-8") as file:
        obj = json.load(file)
    print(type(obj))
    for key in obj:
        print(key + " " + obj[key])

