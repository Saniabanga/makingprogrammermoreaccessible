
import time
import os

MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ':': '---...',
                    '"':'.-..-.'}
 
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher

def process_line(line):
    text = decrypt(str(line))
    print(text)
    return text

def main():
    input_file_path = 'morse.txt'
    output_file_path = 'english.txt'

    last_modified = os.path.getmtime(input_file_path)
    with open(input_file_path, 'r') as input_file:
        new_lines = input_file.readlines()

        processed_lines = [process_line(line) for line in new_lines]
        with open(output_file_path, 'w') as output_file:  # Open in write mode
            output_file.writelines(processed_lines)

    while True:
        if os.path.getmtime(input_file_path) > last_modified:
            with open(input_file_path, 'r') as input_file:
                new_lines = input_file.readlines()

            processed_lines = [process_line(line) for line in new_lines]
            with open(output_file_path, 'w') as output_file:  # Open in write mode
                output_file.writelines(processed_lines)
            last_modified = os.path.getmtime(input_file_path)

            time.sleep(1)

if __name__ == '__main__':
    main()
