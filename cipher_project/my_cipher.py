from cipher import Cipher
from atbash import Atbash
from bifid_cipher import Bifid
from keyword_cipher import Keyword
import atbash_funcs
import keyword_funcs
import bifid_funcs


def another_cipher():
    """
    Will give option to use another cipher.
    """
    again = input("Which cipher would you like now? ")
    if again == 'atbash':
        atbash_funcs.atbash()
    if again == 'keyword':
        keyword_funcs.keyword()
    if again == 'bifid':
        bifid_funcs.bifid()


def start():

    print("Welcome to Cipher Decrypter!","Please choose a cipher to encrypt or decrypt a message: ","Atbash,"
          ,"Bifid,","or Keyword")
    which_chiper = input("Which_chiper would you like to use? ")
    if which_chiper == 'atbash':
        atbash_funcs.atbash()
    elif which_chiper == 'keyword':
        keyword_funcs.keyword()
    elif which_chiper == 'bifid':
        bifid_funcs.bifid()

def start_over():

    print("Great let's use Cipher Decrypter again!","Please choose a cipher to encrypt or decrypt a message: ","Atbash,"
          ,"Bifid,","or Keyword")
    which_chiper = input("Which_chiper would you like to use? ")
    if which_chiper == 'atbash':
        atbash_funcs.atbash()
        another_one = input("If you would like to use another cipher? Type 'Y/N' Or type 'Start Over' to restart. ").lower()
        if another_one == 'y':
            another_cipher()
        elif another_one == 'start over':
            start_over()
    elif which_chiper == 'keyword':
        keyword_funcs.keyword()
        another_one = input("If you would like to use another cipher? Type 'Y/N' Or type 'Start Over' to restart. ").lower()
        if another_one == 'y':
            another_cipher()
        elif another_one == 'start over':
            start_over()
    elif which_chiper == 'bifid':
        bifid_funcs.bifid()
        another_one = input("If you would like to use another cipher? Type 'Y/N' Or type 'Start Over' to restart. ").lower()
        if another_one == 'y':
            another_cipher()
        elif another_one == 'start over':
            start_over()

if __name__ == '__main__':
    start()
