#!/usr/bin/env python


from sys import argv

lst = [str(x).rstrip() for x in open(argv[1])]
zero =[0]* len(lst[0])
one = [0]* len(lst[0])
res = [0]* len(lst[0])
tes = [1]* len(lst[0])
for i in range(len(lst[0])):
      for elem in lst:
            if elem[i] == '0':
                  zero[i] += 1
            else:
                  one[i] += 1
      if one[i] > zero[i]:
            res[i] = 1
            tes[i] = 0
gamma = 0
epsilon = 0
for i in range(len(res)):
      gamma += res[len(res) - 1 - i] * (2 ** i)
      epsilon += tes[len(res) - 1 - i] * (2 ** i)
print(gamma * epsilon)
oxygen = lst.copy()
for i in range(len(lst[0])):
      tmp0 = []
      tmp1 = []
      zero = 0
      one = 0
      for elem in oxygen:
            if elem[i] == '0':
                  zero += 1
                  tmp0.append(elem)
            else:
                  one += 1
                  tmp1.append(elem)
      if one >= zero:
            oxygen = tmp1
      else:
            oxygen = tmp0
      if len(oxygen) == 1:
            break
co2 = lst.copy()
for i in range(len(lst[0])):
      tmp0 = []
      tmp1 = []
      zero = 0
      one = 0
      for elem in co2:
            if elem[i] == '0':
                  zero += 1
                  tmp0.append(elem)
            else:
                  one += 1
                  tmp1.append(elem)
      if one < zero:
            co2 = tmp1
      else:
            co2 = tmp0
      if len(co2) == 1:
            break
oxygen2 = 0
co22 = 0
for i in range(len(oxygen[0])):
      oxygen2 += int(oxygen[0][len(oxygen[0]) - 1 - i]) * (2 ** i)
      co22 += int(co2[0][len(oxygen[0]) - 1 - i]) * (2 ** i)
print(oxygen2*co22)