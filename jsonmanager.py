import json
from simhash import Simhash
from simhash_index import HashIndex


class SimhashEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Simhash):
            return {"__class__": "Simhash",
                "str": obj.str,
                "hash": obj.hash}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

class SimhashIndexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HashIndex):
            hash_tab = []
            for tup in obj.get_hash_table():
                sim = [tup[1].get_str(), tup[1].get_hash()]
                hash_tab.append(sim)
            res = {"__class__": "HashIndex",
                    "__hash_table": hash_tab}
            return res
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

class JsonManager:
    @staticmethod
    def open_json_simhash(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            obj = json.load(file, object_hook=Simhash.unserialize)
        return obj

    @staticmethod
    def save_json_simhash(file_path, obj):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(obj, file, cls=SimhashEncoder)

    @staticmethod
    def open_json_hash_index(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            obj = json.load(file, object_hook=HashIndex.unserialize)
        return obj

    @staticmethod
    def save_json_hash_index(file_path, obj):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(obj, file, cls=SimhashIndexEncoder)

    @staticmethod
    def load_json_raw_text_set(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            obj = json.load(file)
        for key in obj:
            HashIndex.add_sh(Simhash(obj[key]))

