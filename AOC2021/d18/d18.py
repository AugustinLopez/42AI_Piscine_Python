#!/usr/bin/env python3

from sys import argv

class Node(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.parent: Node = None
        self.add_left(left)
        self.add_right(right)

    def add_left(self, node):
        self.left: Node = node
        if node is not None:
            node.parent = self
        return self.left

    def add_right(self, node):
        self.right: Node  = node
        if node is not None:
            node.parent = self
        return self.right

    def read(self, lvl=-1, left=True):
        if self.left is not None:
            print("[", end='')
            self.left.read(lvl+1)
            print(',', end='')
        if self.right is not None:
            self.right.read(lvl+1, False)
            print("]", end='')
        if self.data is not None:
            print(self.data, end='')

    def find_right(node):
        if node.data is not None:
            return node
        if node.right is not None:
            return Node.find_right(node.right)
        if node.left is not None:
            return Node.find_right(node.left)
        return None

    def find_left(node):
        if node.data is not None:
            return node
        if node.left is not None:
            return Node.find_left(node.left)
        if node.right is not None:
            return Node.find_left(node.right)
        return None

    def explode(self, lvl=1):
        ret = 0
        if self.left.data is None:
            if self.left.explode(lvl+1) != 0:
                return 1
        if lvl > 4 and self.left.data is not None and self.right.data is not None:
            left = None
            right = None
            tmp = self
            while tmp.parent:
                if left is None and tmp == tmp.parent.left:
                    left = tmp.parent.right
                elif right is None and tmp == tmp.parent.right:
                    right = tmp.parent.left
                tmp = tmp.parent
            if left:
                x = Node.find_left(left)
                if x is not None:
                    x.data += self.right.data
            if right:
                y = Node.find_right(right)
                if y is not None:
                    y.data += self.left.data
            self.left = None
            self.right = None
            self.data = 0
            return 1
        if self.right.data is None:
            if self.right.explode(lvl+1) != 0:
                return 1
        return 0

    def reduce(self):
        if self.left.data is None:
            if self.left.reduce() != 0:
                return 1
        node = None
        if self.left.data is not None:
            if self.left.data >= 10:
                node = self.left
        if node is None and self.right.data is not None:
            if self.right.data >= 10:
                node = self.right
        if node is not None:
            x = node.data // 2
            y = x + 1 if x * 2 < node.data else x
            node.add_left(Node(x))
            node.add_right(Node(y))
            node.data = None
            return 1
        if self.right.data is None:
            if self.right.reduce() != 0:
                return 1
        return 0

    def magnitude(self):
        left = 0
        if self.left.data is None:
            left = self.left.magnitude()
        else:
            left = self.left.data
        if self.right.data is None:
            right = self.right.magnitude()
        else:
            right = self.right.data
        return left * 3 + right * 2

def p1(lst):
    tree = None
    for elem in lst:
        if tree is None:
            tree = Node()
            tmp = tree
        else:
            tmp = Node()
            tree = Node(left=tree, right=tmp)
        for c in elem:
            if c == '[':
                tmp = tmp.add_left(Node())
            elif c == ']':
                tmp = tmp.parent
            elif c == ',':
                tmp = tmp.add_right(Node())
            else:
                tmp.data=int(c)
                tmp = tmp.parent
        while True:
            if tree.explode():
                continue
            if tree.reduce():
                continue
            break
    ret = tree.magnitude()
    return ret

lst = [x.rstrip() for x in open(argv[1])]
#p1(lst)
maxlst=[]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        tmp = [lst[i], lst[j]]
        maxlst.append(p1(tmp))
        tmp = [lst[j], lst[i]]
        maxlst.append(p1(tmp))
print(max(maxlst))