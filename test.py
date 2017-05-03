# -*- coding: utf-8 -*-
import json
from simhash import Simhash

if __name__ == '__main__':
    # sim = Simhash(0, "hello world")
    # JsonManager.save_json("output.json", sim)

    # sim = JsonManager.open_json("output.json")
    # print(sim)

    # with open("rawData.json", "r", encoding="utf-8") as file:
    #     obj = json.load(file)
    # print(type(obj))
    # for key in obj:
    #     print(key + " " + obj[key])

    sim = Simhash("*")
    i = bin(sim.get_hash()).count("1") + bin(sim.get_hash()).count("0")
    print(i)

