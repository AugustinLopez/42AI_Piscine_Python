#!/usr/bin/env python

from generator import generator


text = "Le Lorem Ipsum est simplement du faux texte."
test = []
for word in generator(text, sep=" "):
    test.append(word)
print(test)
test = []
for word in generator(text, sep=" ", option="shuffle"):
    test.append(word)
print(test)
test = []
for word in generator(text, sep=" ", option="ordered"):
    test.append(word)
print(test)
text = "A A a a B B b b"
test = []
for word in generator(text, sep=" ", option="unique"):
    test.append(word)
print(test)
test = []
text = 1.0
for word in generator(text, sep=" "):
    test.append(word)
print(test)
test = []