from cipher import Cipher


class Keyword(Cipher):

    """ Keyword creates a cipher interchaging the letter of the word as it
     corresponds to the kryptos alphabet.
     """

    Plaintext = list('abcdefghijklmnopqrstuvwxyz')
    Encrypted = list('kryptosabcdefghijlmnquvwxz')
    keyword_encrypted = [(x,y) for x,y in zip(Plaintext,Encrypted)]

    def __init__(self, message):
        super().__init__(message)
        self.new_message = list(message.replace(" ","").lower())
        self.decrypted_message = ''
        self.encrypted = ''

    def encrypt(self):
        secrete_word = []
        for i in self.new_message:
            for x in Keyword.keyword_encrypted:
                if i == x[0]:
                    secrete_word.append(x[1])
        self.encrypted = (''.join(secrete_word))
        return(self.encrypted)

    def decrypted(self, to_be_decrypted):
        secrete_word = []
        for i in to_be_decrypted:
            for x in Keyword.keyword_encrypted:
                if i == x[1]:
                    secrete_word.append(x[0])
        self.decrypted_message = (''.join(secrete_word))
        return(self.decrypted_message)
