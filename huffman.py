from itertools import groupby
from heapq import *


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""" AUX OBJECTS/VARS """""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Representation of a binary tree node, it points to its left and right
# child, and to its parent. It has an item (character) and a weight which
# corresponds with the frequency of the character in a given input
class Node(object):
	left = None
	right = None
	item = None
	weight = 0
	parent = None

	def __init__(self, i, w):
		self.item = i
		self.weight = w

	def setChildren(self, ln, rn):
		self.left = ln
		self.right = rn

	def setLeft(self,ln):
		self.left = ln

	def setRight(self,rn):
		self.right = rn

	def setParent(self,pn):
		self.parent = pn

	def __repr__(self):
		return "%s - %s — %s _ %s" % (self.item, self.weight, self.left, self.right)

	def __cmp__(self, a):
		return cmp(self.weight, a.weight)

# Representation of an end of file used to read the header.
# since the algorithm always read 1 bit check if it is 1 or 0
# and 1 byte if it was one, it
EOF = 'dummyEOF'


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""" COMPRESSION """"""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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

def treeToByte(node):
	if node.item:
		return '1' + toByte(node.item)
	else:
		return '0' + treeToByte(node.left) + treeToByte(node.right)

def preCompression(input):
	itemqueue = [Node(a,len(list(b))) for a,b in groupby(sorted(input))] # input sorted and grouped by character
	count = '{0:08b}'.format(len(itemqueue)) #nElements in binary an 8 digits
	heapify(itemqueue) #make the list a heap O(n)
	tree = queueToTree(itemqueue) #create the tree using the heap

	# retrieve the compressed input and the codes for each char
	codes = {}
	codeIt("", tree, codes)

	# make the header of the file (nElements + treeStructure)
	cTree = count + treeToByte(tree)

	return codes, "".join([codes[a] for a in input]), cTree

def queueToTree(queue):
	while len(queue) > 1:
		l = heappop(queue)
		r = heappop(queue)
		n = Node(None, int(r.weight)+int(l.weight))
		n.setChildren(l,r)
		heappush(queue, n)
	return queue[0]

def huffmanCompression(inputFile, outFile):
	inf = open(inputFile,'r')
	outf = open(outFile,'wb')

	input = inf.read()

	codes, compression, head = preCompression(input)
	output = head+compression
	hexGrp = []
	while output:
		hexGrp.append(output[:8])
		output = output[8:]
	output = bytes([int(group,2) for group in hexGrp])
	size = outfp.write(output)
	outfp.close()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""" DECOMPRESSION """"""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def decodeIt(input, node):
	if node.item:
		return node.item, input
	else:
		if input[0] == '0':
			return decodeIt(input[1:], node.left)
		else:
			return decodeIt(input[1:], node.right)

def buildTree(input, count, node = None, root = None):
	print count
	if count > 0:
		if input[0] == '0':
			if not node:
				root =  Node(None, 0)
				return buildTree(input[1:], count, root, root)
			else:
				if node.left and node.right:
					return buildTree(input, count, node.parent, root)
				else:
					n = Node(None,0)
					n.setParent(node)
					if node.left:
						node.setRight(n)
					else:
						node.setLeft(n)
					return buildTree(input[1:], count, n, root)
		else:
			if not node:
				count -= 1
				root = Node(chr(int(input[1:9],2)),0)
				print (chr(int(input[1:9],2)))
				return buildTree(input[9:], count, root, root)
			elif node.left and node.right:
				return buildTree(input, count, node.parent, root)
			else:
				count -= 1
				print(chr(int(input[1:9],2)))
				n = Node(chr(int(input[1:9],2)),0)
				n.setParent(node)
				if node.left:
					node.setRight(n)
				else:
					node.setLeft(n)
				return buildTree(input[9:], count, node, root)
	else:
		return root

def huffmanDecompression(input, tree):
	s  = ""
	if len(input) == 1:
		char, input = decodeIt(input, tree)
		return char
	else:
		while len(input) > 0:
			char, input = decodeIt(input, tree)
			print char
			s+= char
		return s


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""" MAIN """""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

input = ""

input = "mlagunas arto ññ"
codes, compression, head = preCompression(input)
tree = buildTree(head[8:],int(head[:8],2))
res = huffmanDecompression(compression, tree)

print res
