#!/usr/bin/env python

from csvreader import CsvReader
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with CsvReader(filename, header=False, skip_top=18, skip_bottom=0) as file:
        if file is None:
            print("File corrupted or missing")
        else:
            print(file.getheader(), end="\n")
            print(file.getdata(), end="\n\n")
            data = file.getdata()
            for elem in data:
                print(elem, end="\n")
