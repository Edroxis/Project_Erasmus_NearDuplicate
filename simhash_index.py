from simhash import *


class HashIndex:
    # Attributes
    """
    Static attribute containing all tuples (index, Simhash) of documents
    """
    hash_table = []

    # Getter and setter

    # Methods
    """
    This method adds a SimHash to the static table hash_table
    :param sim the SimHash object
    :raise TypeError if arg is not of the proper type
    """
    @staticmethod
    def add_sh(sim):
        print("TODO: Implement add_sh")
        # if isinstance(sim, SimHash(0, "")):
        #     HashIndex.hash_table.append(sim)
        # else:
        #     raise Exception("Incorrect type")

    """
    This method search a SimHash into the static table hash_table
    :param sim the SimHash object
    :param diff the number of tolerated differences on hash
    :raise TypeError if arg is not of the proper type
    """
    @staticmethod
    def search_sh(hash, diff):
        print("TODO: Implement search_sh")

    """
    This method search a SimHash into the static table hash_table
    :param hash1 hash of a document
    :param hash2 hash of a document
    :return diff the number of differences between hash in parameter
    """
    @staticmethod
    def calc_diff(hash1, hash2):
        print("TODO: Implement calc_diff")
