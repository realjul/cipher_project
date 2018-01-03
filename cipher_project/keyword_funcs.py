from keyword_cipher import Keyword
from cipher import Cipher
import my_cipher

def keyword_encrypt():

    """Will encrypt message using the keyword cipher"""

    user_message = input("What would you like to encrypt? ")
    encrypted_bifid_message = Keyword(user_message).encrypt()
    print("Great! Your encrypted message is: {}".format(encrypted_bifid_message))



def keyword_decrypt():

    """decrypts a message using the keyword cipher"""

    user_encrypted_message = input("What would you like to decrypt? ")
    user_decrypted_message = Keyword(user_encrypted_message).decrypted(user_encrypted_message)
    print("Your message reads: {}".format(user_decrypted_message))
    another_one = input("If you would like to use another cipher? Type 'Y/N' Or type 'Start Over' to restart. Or 'q' to quit. ").lower()
    if another_one == 'y':
        my_cipher.another_cipher()
    elif another_one == 'start over':
        my_cipher.start_over()
    elif another_one == 'q':
        print("Great Thanks for using the keyword Cipher!")


def keyword():

    """activates the keyword cipher"""

    user_choice = input("Keyword! Great choice! Would you like to encrypt or decrypt? ")

    if user_choice == 'encrypt':
        keyword_encrypt()
        decrypted_message = input("Would you like to decrypt a messsge? Y/N ").lower()
        if decrypted_message == 'y':
            keyword_decrypt()
        else:
            print("Great! Thanks for using the Bifid Cipher!")
            another_one = input("If you would like to use another cipher? Type 'Y/N' Or type 'Start Over' to restart. Or 'q' to quit.").lower()
            if another_one == 'y':
                my_cipher.another_cipher()
            elif another_one == 'start over':
                my_cipher.start_over()
            elif another_one == 'q':
                print("Great Thanks for using the Keyword Cipher!")

    else:
        keyword_decrypt()

if __name__ == '__main__':
    keyword()
