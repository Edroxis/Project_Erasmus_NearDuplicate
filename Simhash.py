span = 4

class SimHash:
    span = 4
    # Constructor
    def __init__(self, str, span=4):
        self.str = str
        self.span = span
        self.splitted_tab = []

    # Getter and Setter
    def get_splitted_tab(self):
        return self.splitted_tab

    # Methods
    """
    This function returns a table of the parts of the string in parameter
    :param str the string containing our text
    :param span length of each bit of text, default value = 4
    :return splitted_tab a table containing our bits of text
    """
    def splitter(self, str, span = 4):
        print("TODO: Implement splitter")
        splitted_tab = []
        return splitted_tab

    """
    This function hash the string in parameter with MD5 algorithm, uses hashlib module
    :param str the string to hash
    :return hash the hash calculated
    """
    def hash_part(self, str):
        print("TODO: Implement hash_part")

    """
    This function calculate the vector containing bits counters
    :param hash_tab the table will all the hash to agregate
    :return vec the vector containing counters
    """
    def calc_vector(self, hash_tab):
        print("TODO: Implement calc_vector")

    """
    This function calculate the final hash of the initial text
    :param vec the agregation vector
    :return hash the final hash
    """
    def calc_final_hash(self, vec):
        print("TODO: Implement calc_final_hash")