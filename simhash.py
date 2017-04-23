span = 4

class Simhash:
    span = 4

    # Constructor
    def __init__(self, index, str, hash = 0, span=4):
        self.index = index
        self.str = str
        Simhash.span = span
        self.hash = hash
        # Call of methods

    # Getter and Setter

    # Methods
    """
    This function returns a table of the parts of the string in parameter
    :param str the string containing our text
    :param span length of each bit of text, default value = 4
    :return splitted_tab a table containing our bits of text
    """
    @staticmethod
    def splitter(self, str, span = 4):
        print("TODO: Implement splitter")
        splitted_tab = []
        return splitted_tab

    """
    This function hash the string in parameter with MD5 algorithm, uses hashlib module
    :param str the string to hash
    :return hash the hash calculated
    """
    @staticmethod
    def hash_part(self, str):
        print("TODO: Implement hash_part")

    """
    This function calculate the vector containing bits counters
    :param hash_tab the table will all the hash to agregate
    :return vec the vector containing counters
    """
    @staticmethod
    def calc_vector(self, hash_tab):
        print("TODO: Implement calc_vector")

    """
    This function calculate the final hash of the initial text
    :param vec the agregation vector
    :return hash the final hash
    """
    @staticmethod
    def calc_final_hash(self, vec):
        print("TODO: Implement calc_final_hash")

    def unserialize(dct):
        return Simhash(dct['index'], dct['str'], dct['hash'])
