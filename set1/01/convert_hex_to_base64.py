'Convert hex to base64'
# https://cryptopals.com/sets/1/challenges/1

# Crpytopals Rule: Always operate on raw bytes, never on encoded strings.
# Only use hex and base64 for pretty-printing.

import base64


def convert_hex_to_base64(input_file):

    'Takes an input file and prints the base64 encoding.'

    # open a file
    with open(input_file, 'r', encoding='UTF-8') as file:

        # read file into an object
        data_string: str = file.read()
        data_string = data_string.strip()

        # convert input to bytes
        data_bytes: bytes = bytes.fromhex(data_string)

        # convert to base64
        data_base64: bytes = base64.b64encode(data_bytes)

        print(data_base64)


if __name__ == '__main__':
    import sys
    convert_hex_to_base64(sys.argv[1])
