from simhash import *


class HashIndex:
    # Attributes
    """
    Static attribute containing all tuples (index, Simhash) of documents
    """
    __hash_table = []
    __index = 0

    def __init__(self, index=__index):
        self.__index = index

    # Getter and setter
    @staticmethod
    def get_hash_table():
        return HashIndex.__hash_table.copy()

    @staticmethod
    def get_index():
        return HashIndex.__index

    # Methods
    """
    This method adds a SimHash to the static table hash_table
    :param sim the SimHash object
    :raise TypeError if arg is not of the proper type
    """
    @staticmethod
    def add_sh(sim):
        if isinstance(sim, Simhash):
            HashIndex.__hash_table.append((HashIndex.__index, sim))
            HashIndex.__index += 1
        else:
            raise Exception("Incorrect type")

    """
    This method search a SimHash into the static table hash_table
    :param sim the SimHash object
    :param diff the number of tolerated differences on hash
    :raise TypeError if arg is not of the proper type
    """
    @staticmethod
    def search_sh(hash, diff):
        res = []
        for tup in HashIndex.__hash_table:
            current_diff = HashIndex.calc_diff(hash, tup[1].get_hash())
            if current_diff < diff:
                res.append(tup)
        return res

    """
    This method search a SimHash into the static table hash_table
    :param hash1 hash of a document
    :param hash2 hash of a document
    :return diff the number of differences between hash in parameter
    """
    @staticmethod
    def calc_diff(hash1, hash2):
        if isinstance(hash1, Simhash):
            hash1 = hash1.get_hash()
        if isinstance(hash2, Simhash):
            hash2 = hash2.get_hash()

        diff = bin(hash1 ^ hash2).count("1")
        return diff

    """
    This function unserialize the json structure
    :return the properly constructed Object
    """
    def unserialize(dct):
        print("====== EXTRACTON JSON ======")
        if dct['__class__'] == "HashIndex":
            for sim_descriptor in dct['__hash_table']:
                HashIndex.add_sh(Simhash(sim_descriptor[0], sim_descriptor[1]))
            print("-> Extraction : OK")
            return 1
        raise TypeError("This JSON doesn't describe a HashIndex.")
