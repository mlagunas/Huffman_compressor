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

EOF = '000000000'

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
    codeIt("", itemqueue[0], codes)
    return codes, "".join([codes[a] for a in input]), itemqueue[0]

def decodeIt(input, node):
	if node.item:
		return node.item, input
	else:
		if input[0] == '0':
			return decodeIt(input[1:], node.left)
		else:
			return decodeIt(input[1:], node.right)

def huffmanDecompression(input):
	s  = ""
	while len(input) > 0:
		char, input = decodeIt(input, tree)
		s+= char
	return s

def storeTree(node):
    code = ''
    if not node:
		return code #EOF represented with 9 zeros
    if not node.left and not node.right: #Not final-leaf (without content)
		code += '1' + toByte(node.item) + toByte(str(node.weight))
    return code + storeTree(node.left) + storeTree(node.right)

def toByte(smth):
	if len(smth) > 1:
		res = ""
		for i in smth:
			res += toByte(i)
			return res
	else:
		res = bin(ord(smth))[2:]
		while len(res) != 8:
			res = '0'+res
		return res

def getTree(input):
	itemqueue = []
	i = 0
	eofFound = False
	while not eofFound:
		print i
		if input[i] == '1':
			itemqueue.append(Node(chr(int(input[i+1:i+9], 2)),chr(int(input[i+9:i+17],2))))
			i+=17
		else:
			print input[i:i+9]
			if input[i:i+9] == EOF:
				eofFound = True
			i+=1
	return itemqueue, i


input = ""
with open("/home/mlagunas/DLart/curated/images/ambulance/Ambulance-1.png") as f:
	    byte = f.read(1)
	    while byte != "":
	        input += byte
	        byte = f.read(1)
print input
input = "m iii s"
codes, compression, tree = huffmanCompression(input)
print compression
a = storeTree(tree) + EOF + compression
print a
b, bits = getTree(a)

print b
print getTree(a)
print charToByte(content[3][1])
print compression
type(content[3][1])


res = huffmanDecompression(compression)

print res
