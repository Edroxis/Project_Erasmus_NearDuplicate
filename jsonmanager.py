import json
from simhash import Simhash


class SimhashEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Simhash):
            return {"__class__": "Simhash",
                "index": obj.index,
                "str": obj.str,
                "hash": obj.hash}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class JsonManager:
    @staticmethod
    def open_json(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            obj = json.load(file, object_hook=Simhash.unserialize)
        return obj

    @staticmethod
    def save_json(file_path, obj):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(obj, file, cls=SimhashEncoder)
