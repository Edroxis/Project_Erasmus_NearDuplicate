import hashlib
import binascii


class Simhash:
    SPAN = 4

    # Constructor
    def __init__(self, str, hash=0, span=4):
        self.str = str
        Simhash.SPAN = span

        # Call of methods
        if hash != 0:
            self.hash = hash
        else:
            splitted_tab = Simhash.splitter(str)
            vec = Simhash.calc_vector(splitted_tab)
            self.hash = Simhash.calc_final_hash(vec)

    # Getter and Setter
    def get_str(self):
        return self.str

    def get_hash(self):
        return self.hash

    # Methods
    """
    This function returns a table of the parts of the string in parameter
    :param str the string containing our text
    :param span length of each bit of text, default value = 4
    :return splitted_tab a table containing our bits of text
    """
    @staticmethod
    def splitter(str1):
        # Detects type error
        if not isinstance(str1, str):
            raise TypeError("Invalide Type Simhash#splitter, param is not a string")

        # Take span
        span = Simhash.SPAN
        # Initialize splitted_tab
        splitted_tab = []

        # Enumerate different strings parts and stock them in a tuple (str, hash) in splitted_tab
        for n in range(0, len(str1)-span+1):
            current_str = str1[n:n+span]
            splitted_tab.append((current_str, Simhash.hash_part(current_str)))
        # If document is smaller than the span
        if len(str1) < span:
            splitted_tab.append((str1, Simhash.hash_part(str1)))
        return splitted_tab

    """
    This function hash the string in parameter with MD5 algorithm, uses hashlib module
    :param str the string to hash
    :return hash the hash calculated
    """
    @staticmethod
    def hash_part(str1):
        # Detects type error
        if not isinstance(str1, str):
            raise TypeError("Invalide Type Simhash#splitter, param is not a string")

        # Constructs MD5 object
        m = hashlib.md5()
        # Fill MD5 object
        m.update(str1.encode())
        return m.hexdigest()

    """
    This function calculate the vector containing bits counters
    :param hash_tab the table will all the hash to agregate
    :return vec the vector containing counters
    """
    @staticmethod
    def calc_vector(hash_tab):
        # Initialize result variable with the size of used hash
        res = [0] * (hash_tab[0][1].__len__()-1) * 8

        # Go through all hash in table
        for tuple in hash_tab:
            # Translate into bytes (byte table)
            bin = binascii.unhexlify(tuple[1])
            byte_index = 0

            # For each byte
            for b in bin:
                # Define mask bit at 10000000
                bit_tester = 128

                # For each bit in the byte
                for counter in range(0, 8):
                    # If current bit is 1, add 1 to result vector
                    if (b & bit_tester) != 0:
                        res[byte_index * 8 + counter] += 1
                    # Otherwise, substract 1 to result vector
                    else:
                        res[byte_index * 8 + counter] -= 1
                    bit_tester = bit_tester.__rshift__(1) # Shift test bit to the right
                byte_index += 1  # Change the byte tested
        return res

    """
    This function calculate the final hash of the initial text
    :param vec the agregation vector
    :return hash the final hash
    """
    @staticmethod
    def calc_final_hash(vec):
        res = 0
        # Go through vector
        for b in range(0, len(vec)):
            if vec[b] > 0:
                res += (1 << len(vec)-1-b)
        return res

    """
    This function unserialize the json structure
    :return the properly constructed Object
    """
    def unserialize(dct):
        return Simhash(dct['str'], dct['hash'])
