import string
from sys import argv

def text_analyzer(*arg):
    """The `text_analyzer(string)` function counts the number of:
    - upper characters,
    - lower characters,
    - punctuation marks,
    - spaces,

in a given text. If less than one argument is provided, \
the program ask for input.
If more than 2 arguments are provided, the program print an error."""

    if (len(arg) > 1):
        print("ERROR")
        # print(text_analyzer.__doc__, file=stderr)
        return
    if (len(arg) == 0):
        print("What is the text to analyse?")
        text = input(">> ")
    else:
        text = arg[0]
    u = 0
    lo = 0
    p = 0
    s = 0
    i = 0
    for c in text:
        i = i + 1
        if c in string.punctuation:
            p = p + 1
        elif c.isspace():
            s = s + 1
        elif c.isalpha() and c.isupper():
            u = u + 1
        elif c.isalpha() and c.islower():
            lo = lo + 1
    print("The text contains", lo, "character(s):")
    print("-", u, "upper letter(s)")
    print("-", lo, "lower letter(s)")
    print("-", p, "punctuation mark(s)")
    print("-", s, "space(s)")

if __name__ == "__main__":
    if len(argv) > 2:
        print("ERROR")
    elif len(argv) == 0:
        text_analyzer()
    else:
        text_analyzer(argv[1])