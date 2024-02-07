import argparse


class CaesarCipherEncryptor:
    def __init__(self, file_path):
        self.file_path = file_path

    def caesar_cipher_algorithm(self, text, shift_key):
        """
        This function  encrypts /decrypts the string/text using caesar cipher Algorithm
        :return: encrypts /decrypts text
        """
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isalpha():
                ascii_val = 65 if char.isupper() else 97
                result += chr((ord(char) + shift_key - ascii_val) % 26 + ascii_val)
            else:
                result += char
        return result

    def process_file(self, key, encrypt):
        with open(self.file_path, 'r') as file:
            text = file.read()

        shift_key = key if encrypt else 26 - key
        result = self.caesar_cipher_algorithm(text, shift_key)

        with open(self.file_path, 'w') as file:
            file.write(result)

    def encrypt_file(self, key):
        self.process_file(key, encrypt=True)

    def decrypt_file(self, key):
        self.process_file(key, encrypt=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a text file using Caesar cipher algo.")
    parser.add_argument("file_path", help="Path to the text file")
    parser.add_argument("key", type=int, help="Encryption/decryption key  for Caesar  algo")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--encrypt", action="store_true", help="Encrypt the text file")
    group.add_argument("--decrypt", action="store_true", help="Decrypt the text file")

    args = parser.parse_args()
    crypto_object = CaesarCipherEncryptor(args.file_path)

    if args.encrypt:
        crypto_object.encrypt_file(args.key)
        print("File encrypted successfully.")
    elif args.decrypt:
        crypto_object.decrypt_file(args.key)
        print("File decrypted successfully.")
    else:
        print("Please enter valid command")

"""
provided below text in file:
I have used Caesar cipher algorithm to encrypt or decrypt the text file
"""
