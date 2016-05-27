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

# It goes through the generated tree giving each final-leaf node
# a binary value. (only final-leaf nodes have "letter-weight"), None
# final-leaf nodes have the following structure "none-weight".
# It stores it in a hash-table "codes[index] = value" where index is
# the encoded character and value its binary result.
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

    return codes, "".join([codes[a] for a in input])

def huffmanDecompression(input):
    heapify(itemqueue)
    while len(itemqueue) > 1:
    	l = heappop(itemqueue)
    	r = heappop(itemqueue)
    	n = Node(None, r.weight+l.weight)
    	n.setChildren(l,r)
    	heappush(itemqueue, n)

    codes = {}
    codeIt("",itemqueue[0], codes)
    return codes, "".join([codes[a] for a in input])

with open("/home/mlagunas/DLart/curated/images/ambulance/Ambulance-1.png") as f:
    content = f.readlines()
print (content)
input = content
print input
codes, compression = huffmanCompression(input)
for key,value in codes.iteritems():
	print key,value
