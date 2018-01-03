from cipher import Cipher

class Atbash(Cipher):

    """Creates the atbash cipher text with a list comprehension in which the
    cipher is created by interchaging the letter of a word with its corresponding
    value from a reversed alphabet.
    """

    plain_text = list('abcdefghijklmnopqrstuvwxyz')
    cipher_text = list(plain_text[::-1])
    list_decoder = [(x,y) for x,y in zip(plain_text,cipher_text)]

    def __init__(self,message):
        super().__init__(message)

        self.new_message = list(message.replace(" ","").lower())
        self.encrypted_message = ''
        self.unencrypted_message = ''

    """Takes in a message to encrypt."""
    def encrypt(self):
        encrypted = []
        for i in self.new_message:
            for x in Atbash.list_decoder:
                if i == x[0]:
                    encrypted.append(x[1])
        self.encrypted_message = (''.join(encrypted))
        return(self.encrypted_message)

    """Takes in a message to decrypt."""
    def decrypt(self, to_be_decrypted):
        decrypted = []
        for i in to_be_decrypted:
            for x in Atbash.list_decoder:
                if i == x[1]:
                    decrypted.append(x[0])
        self.unencrypted_message = (''.join(decrypted))
        return(self.unencrypted_message)
