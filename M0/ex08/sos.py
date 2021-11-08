#!/usr/bin/env python
from sys import argv

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----'}

if (len(argv) >= 2):
    argv.pop(0)
    error = 0
    for arg in argv:
        if not all(x.isalnum() or x.isspace() for x in arg):
            error = 1
            break
    if (error == 1):
        print("ERROR")
    else:
        i = 1
        for arg in argv:
            arg = arg.upper()
            for c in arg:
                if (c.isalnum()):
                    print(MORSE_CODE_DICT[c], end=' ')
                else:
                    print("/", end=' ')
            if (i < len(argv)):
                print("/", end=' ')
            i = i + 1
        print()
