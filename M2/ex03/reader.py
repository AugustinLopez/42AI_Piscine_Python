#!/usr/bin/env python

from csvreader import CsvReader
import sys

if __name__ == "__main__":
    filename = None
    head = False
    tskip = 0
    bskip = 0
    arg = len(sys.argv)
    if arg > 1:
        filename = sys.argv[1]
    if arg > 2:
        head = sys.argv[2] != '0'
    if arg > 3:
        tskip = int(sys.argv[3])
    if arg > 4:
        bskip = int(sys.argv[4])
    with CsvReader(filename, header=head, skip_top=tskip,
                   skip_bottom=bskip) as file:
        if file is None:
            print("File corrupted or missing")
        else:
            print("Head: ", end='')
            print(file.getheader(), end="\n")
            data = file.getdata()
            for elem in data:
                print("      ", end='')
                print(elem, end="\n")
