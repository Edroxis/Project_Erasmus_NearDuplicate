# -*- coding: utf-8 -*-
from simhash import Simhash
from simhash_index import HashIndex
from jsonmanager import JsonManager

if __name__ == '__main__':
    # sim1 = Simhash("hello world")
    # HashIndex.add_sh(sim1)
    #
    # sim = Simhash("hello world.")
    # HashIndex.add_sh(sim)
    #
    # sim = Simhash("hello world!")
    # HashIndex.add_sh(sim)
    #
    # sim = Simhash("hello aetqye tworlqy qyr d.")
    # HashIndex.add_sh(sim)
    #
    # sim = Simhash("""Demain, dès l'aube, à l'heure où blanchit la campagne,\nJe partirai. Vois-tu, je sais que tu m'attends.\nJ'irai par la forêt, j'irai par la montagne.\nJe ne puis demeurer loin de toi plus longtemps.""")
    # HashIndex.add_sh(sim)
    #
    # sim = Simhash("""Demain, dès l'aube, à l'heure où blanchit la campagne,\nJe partirai. Vois-tu, je sais que tu m'attends.\nJ'irai par la forêt, j'irai par la montagne.\nJe ne puis demeurer loin de toi plus longtemps.\n[...]\nEt quand j'arriverai, je mettrai sur ta tombe\nUn bouquet de houx vert et de bruyère en fleur.""")
    # HashIndex.add_sh(sim)

    # print(HashIndex.search_sh(sim1, 20))

    # hash_index = HashIndex()
    # JsonManager.save_json_hash_index("test.json", hash_index)

    hash_index = JsonManager.open_json_hash_index("test.json")
    print(HashIndex.get_hash_table())
