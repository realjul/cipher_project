from cipher import Cipher


class Bifid(Cipher):

    """Bifid cipher class takes in a message encrypts it using a dictionary
    where keys are coordinants in a grid and values are the corresponding alphabet
    characters in that GRID
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.bifid_cipher_dict = {tup:letter for tup,letter in zip(Cipher.GRID, Cipher.ALPHABET)}

    def encrypt(self):
        # encryption_keys will hold the encrypted tuples
        encryption_keys = []
        for i in self.message:
            for key,value in self.bifid_cipher_dict.items():
                if i == value:
                    encryption_keys.append(key)
        # encryption_first_key will hold the first tuple to later concatonate with the second tuple
        encryption_first_key = []
        for i in encryption_keys:
            encryption_first_key.append(i[0])

        # encryption_second_key will hold the second tuple to later concatonate with the first tuple
        encryption_second_key = []
        for i in encryption_keys:
            encryption_second_key.append(i[1])

        # concatonates first and second tuple to then make new pairs
        encrypted_line = encryption_first_key + encryption_second_key

        # creates new pairs of tuples
        new_encrypted_line_pairs = list(zip(encrypted_line[0::2], encrypted_line[1::2]))

        secrete_message_list = []

        # uses encrypted tuple to retrive corresponding characters and append to secrete_message_list
        for i in new_encrypted_line_pairs:
            for key,value in self.bifid_cipher_dict.items():
                if i == key:
                    secrete_message_list.append((value))
        secrete_message = (''.join(secrete_message_list))

        return(secrete_message)


    def decrypt(self, to_decrypt):
        # decrypted_keys will hold the encrypted tuples
        decrypted_tuple_keys = []
        for i in to_decrypt:
            for key,value in self.bifid_cipher_dict.items():
                if i == value:
                    decrypted_tuple_keys.append(key)

        # decrypted_num_list will hold all the tuples in a straight line
        decrypted_num_list = []
        for i in decrypted_tuple_keys:
            for x in i:
                decrypted_num_list.append(x)


        top_decypted_nums = decrypted_num_list[:int(len(decrypted_num_list)/2)]
        bottom_decrypted_nums = decrypted_num_list[int(len(decrypted_num_list)/2):]
        decrypted_tuples = [(x,y) for x,y in zip(top_decypted_nums,bottom_decrypted_nums)]

        # holds the encrypted characters in list
        not_secrete_message_list = []

        # uses encrypted tuple to retrive corresponding characters and append to secrete_message_list
        for i in decrypted_tuples:
            for key,value in self.bifid_cipher_dict.items():
                if i == key:
                    not_secrete_message_list.append((value))
        not_secrete_message = (''.join(not_secrete_message_list))

        return(not_secrete_message)
