from cipher import Cipher
from bifid_cipher import Bifid
import my_cipher


def bifid_encrypt():

    """ encrypts using the bifid cipher """

    user_message = input("What would you like to encrypt? ")

    encrypted_bifid_message = Bifid(user_message).encrypt()
    print("Great! Your encrypted message is: {}".format(encrypted_bifid_message))


def bifid_decrypt():

    """decrypts a message using the bifid cipher"""

    user_encrypted_message = input("What would you like to decrypt? ")
    user_decrypted_message = Bifid(user_encrypted_message).decrypt(user_encrypted_message)
    print("Your message reads: {}".format(user_decrypted_message))
    another_one = input("If you would like to use another cipher? Type 'Y/N' Or type 'Start Over' to restart. Or 'q' to quit. ").lower()
    if another_one == 'y':
        my_cipher.another_cipher()
    elif another_one == 'start over':
        my_cipher.start_over()
    elif another_one == 'q':
        print("Great Thanks for using the Bifid Cipher!")


def bifid():

    """activates the bifid cipher"""

    user_choice = input("Bifid! Great choice! Would you like to encrypt or decrypt? ")

    if user_choice == 'encrypt':
        bifid_encrypt()
        decrypted_message = input("Would you like to decrypt a messsge? Y/N ").lower()
        if decrypted_message == 'y':
            bifid_decrypt()
        else:
            print("Great! Thanks for using the Bifid Cipher!")
            another_one = input("If you would like to use another cipher? Type 'Y/N' Or type 'Start Over' to restart. Or 'q' to quit. ").lower()
            if another_one == 'y':
                my_cipher.another_cipher()
            elif another_one == 'start over':
                my_cipher.start_over()
            elif another_one == 'q':
                print("Great Thanks for using the Bifid Cipher!")
    else:
        bifid_decrypt()


if __name__ == '__main__':
    bifid()
