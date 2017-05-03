# -*- coding: utf-8 -*-
from simhash import Simhash
from simhash_index import HashIndex
from jsonmanager import JsonManager

if __name__ == '__main__':
    # Open and loads previous session of program,
    hash_index = JsonManager.open_json_hash_index("output.json")

    # Add a hash to HashIndex (static attribute)
    # sim1 = Simhash("hello world")
    # HashIndex.add_sh(sim1)

    # Get all elements of HashIndex structure containing at most 20 differences (on binary sequence)
    # similar_list = HashIndex.search_sh(sim1, 20)

    # Load set of document (see rawData.json for syntaxe) and add them automatically to HashIndex structure
    JsonManager.load_json_raw_text_set("rawData.json")

    # Print whole HashIndex structure
    print(HashIndex.get_hash_table())

    # Save current HashIndex structure in "output.json"
    hash_index = HashIndex()
    JsonManager.save_json_hash_index("output.json", hash_index)
