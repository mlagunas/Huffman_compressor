from itertools import groupby
from heapq import *


class Node(object):
	left = None
	right = None
	item = None
	weight = 0

	def __init__(self, i, w):
		self.item = i
		self.weight = w

	def setChildren(self, ln, rn):
		self.left = ln
		self.right = rn

	def __repr__(self):
		return "%s - %s — %s _ %s" % (self.item, self.weight, self.left, self.right)

	def __cmp__(self, a):
		return cmp(self.weight, a.weight)


def codeIt(s, node, codes):
    if node.item:
        if not s:
            codes[node.item] = "0"
        else:
            codes[node.item] = s
    else:
        codeIt(s+"0", node.left, codes)
        codeIt(s+"1", node.right, codes)

def huffmanCompression(input):

    itemqueue =  [Node(a,len(list(b))) for a,b in groupby(sorted(input))]
    heapify(itemqueue)
    while len(itemqueue) > 1:
    	l = heappop(itemqueue)
    	r = heappop(itemqueue)
    	n = Node(None, r.weight+l.weight)
    	n.setChildren(l,r)
    	heappush(itemqueue, n)

    codes = {}

    codeIt("",itemqueue[0], codes)

    print codes, "".join([codes[a] for a in input])

input = "aababcabcd aababcabcd"
huffmanCompression(input)
