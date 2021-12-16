#!/usr/bin/env python3

from sys import argv
from functools import reduce


def packet_header(binary):
    bversion = int(binary[:3],2)
    btype = int(binary[3:6],2)
    binary = binary[6:]
    return bversion, btype, binary

def literal_value(binary):
    i = 0
    res = ""
    while binary[i] != '0':
        res+=binary[i+1:i+5]
        i += 5
    res += binary[i+1:i+5]
    i += 5
    binary = binary[i:]
    return res, i, binary

def len_verification(binary):
    if binary[0] == '0':
        if len(binary) < 16:
            return -1
        return 0
    if binary[0] == '1':
        if len(binary) < 12:
            return -1
        return 1
    return -1

def type_analysis(p2, btype):
    if len(p2) == 0:
        return None
    if btype == 0:
        return sum(p2)
    if btype == 1:
        return reduce(lambda x,y: x * y, p2)
    if btype == 2:
        return min(p2)
    if btype == 3:
        return max(p2)
    if btype == 5:
        return 1 if p2[0] > p2[1] else 0
    if btype == 6:
        return 1 if p2[0] < p2[1] else 0
    if btype == 7:
        return 1 if p2[0] == p2[1] else 0

def packet_analysis(binary, max_length = -1, max_number = -1, opp = -1):
    r = 0
    n = 0
    tot_version = 0
    p2 = []
    while len(binary) > 7:
        if (max_length > 0 and r >= max_length) \
        or (max_number > 0 and n >= max_number):
            break
        bversion, btype, binary = packet_header(binary)
        tot_version += bversion
        r += 6
        n += 1
        if btype == 4:
            x, y, binary = literal_value(binary)
            r += y
            x = int(x,2)
            print(x)
            p2.append(x)
        else:
            verif = len_verification(binary)
            if verif == -1:
                break
            elif verif == 0:
                length = int(binary[1:16], 2)
                r += 16
                binary = binary[16:]
                y, b_version, z = packet_analysis(binary, length)
                p2.append(type_analysis(z, btype))
                tot_version += b_version
                binary = binary[y:]
                r += y
            elif verif == 1:
                number = int(binary[1:12], 2)
                r += 12
                binary = binary[12:]
                y, b_version, z = packet_analysis(binary, -1, number)
                p2.append(type_analysis(z, btype))
                tot_version += b_version
                binary = binary[y:]
                r += y
            
    return r, tot_version, p2

#510043473521
hexs = [l.rstrip() for l in open(argv[1])]
for hex in hexs:
    binary = "".join(["{0:04b}".format(int(c, 16)) for c in hex])
    _, tot_version, p2 = packet_analysis(binary)
    print(tot_version)
    print(p2)



