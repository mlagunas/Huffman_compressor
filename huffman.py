# -*- coding: utf-8 -*-

# Author; Manuel Lagunas
# 29/5/2016
# Readable code implementing huffman compression/decompression

from itertools import groupby
from heapq import *
import sys
import os
import time

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """""""""""""""""""""" AUX OBJECTS/VARS """""""""""""""""""""""""""""
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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

# Auxiliar method to fast-print how to use the following application
def usage():
    print "USAGE: \npython huffman.py -c|-d file"
    print "\t-c : To compress file"
    print "\tfile: file to compress/decompress"
    print "\t-d : To decompress file\npython huffman.py -t file1 file2"
    print "\t-t : Testing mode"
    print "\tfile(1,2): files to compare"

#Set true if you want to proccedd with the canonical huffman compression/decompression
#TO-DO
canonical = False
benchmark = True
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """""""""""""""""""""""""""" COMPRESSION """"""""""""""""""""""""""""
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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

# Changes a char or string to its byte representation
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

# Stores the tree structure as a binary string, each not final-leaf will be
# a 0 and each final-leaf will be 1 followed by its item in byte representation
def treeToByte(node):
    if node.item:
        return '1' + toByte(node.item)
    else:
        return '0' + treeToByte(node.left) + treeToByte(node.right)

def fileToHash(filename):
    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c:
                break

# It returns the compressed code and its codigied tree for a given string (inputFile)
def preCompression(input):
    itemqueue = [Node(a,len(list(b))) for a,b in groupby(sorted(input))] # input sorted and grouped by character

    count = '{0:08b}'.format(len(itemqueue)) #nElements in binary an 8 digits
    heapify(itemqueue) #make the list a heap O(n)
    tree = queueToTree(itemqueue) #create the tree using the heap
    # retrieve the compressed input and the codes for each char
    codes = {}
    codeIt("", tree, codes)

    if canonical:
        codes = canonicalHuff(codes)
        code = "".join(codes[a][0] for a in input)
    else:
        # make the header of the file (nElements + treeStructure)
        cTree = count + treeToByte(tree)
        return codes, "".join([codes[a] for a in input]), cTree


# Given an element which represents a tree, it builds the codes for each final-leaf
# that represents a character
def queueToTree(queue):
    while len(queue) > 1:
        l = heappop(queue)
        r = heappop(queue)
        n = Node(None, int(r.weight)+int(l.weight))
        n.setChildren(l,r)
        heappush(queue, n)
    return queue[0]

# It retursn the canonical codes for the given input codes
def canonicalHuff(codes):
    canon = []
    codes = sorted(codes.items(), key=lambda x: (len(x[1]), x[0]))
    for i in codes:
        canon.append( (i[0], i[1], len(i[1])) )
    print canon

    minsize=canon[0][2]
    co = '0'
    if len(co)<minsize:
        co='0'*(minsize-len(co))+co

    ne = [(canon[0][0],co,len(co))]

    code = 0
    for i in range(1,len(canon)):
        code = (code+1) << canon[i][2] - canon[i-1][2]
        co = bin(code)[2:]
        l = len(co)
        if l<minsize:co='0'*(minsize-l)+co
        ne.append((canon[i][0],co,len(co)))
    for a in ne: print a
    return ne

# It recieves an input and output file, it compress the input file and stores
# the result in the output file. the structure of the outFile will be 1byte to
# know the bits needed to end the last byte, another byte to know the size of the
# header, the header and the compressed text.
def huffmanCompression(inputFile, outFile):

    inputFile="test/test"
    # Open files and read the input we will compress
    inf = open(inputFile,'r')
    outf = open("out",'wb')
    # outf = open(outFile,'wb')
    input = inf.read()
    len (input)
    # Generate the tree and codes and put it together
    if benchmark:
        start = time.time()
    codes, compression, head = preCompression(input)
    output = head+compression
    if benchmark:
        end = time.time()

    count = 0
    while len(output)%8 != 0:
        count += 1
        output += '0'
    count = chr(ord(str(count)))
    print "Precompress " + str(end-start)
    len(output)/8

    if benchmark:
        start = time.time()
    a = count.join(chr(int(output[i:i+8], 2)) for i in xrange(0, len(output), 8))
    if benchmark:
        end = time.time()
        print "To ascii " + str(end-start)

    print (len(a))
    # Make the text suit to bytes size

    # Append 8 bits of the output as a char
    if benchmark:
        start = time.time()
    bOut = count
    while output:
        bOut += chr(int(output[:8],2))
        output = output[8:]
    if benchmark:
        end = time.time()
        print "Binary output " + str(end-start)

    # Write the binaryOutput (as chars) in the binary file
    outf.write(a) #Get number of written bytes
    outf.close()
    inf.close()

    return len(bOut)


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """""""""""""""""""""""""" DECOMPRESSION """"""""""""""""""""""""""
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# It decodes a given tree with the input returning the first character found.
# if input[i] = 0 then it goes to the left children, if it is 1 it goes to the
# right one. Once it has found a final-leaf, it returns it.
def decodeIt(input, node, code = ""):
    if node.item:
        return node.item, input, code
    else:
        if input[0] == '0':
            return decodeIt(input[1:], node.left, code + '0')
        else:
            return decodeIt(input[1:], node.right, code + '1')

# It iterates over the binary input retrieving the chars it represents
# it calls the function decodeIt to retrieve the char. At the end it returns
# the decoded string.
def preDecompression(input, tree):
    s  = ""
    codes = {}
    doH = len(input) > 80000
    if len(input) == 1:
        char, input, code = decodeIt(input, tree)
        s+= char
    else:
        while len(input) > 0:
            found = False
            if doH:
                for i in sorted(codes, reverse=False):
                    if input[0:len(i)] in codes:
                        s += codes[input[0:len(i)]]
                        found = True
                        input = input[len(i):]
                        break
            if not found:
                char, input, code = decodeIt(input, tree)
                if not code in codes:
                    codes[code] = char
                s+= char
    return s

# It recursively build the tree from a binary string input. The 0 represents
# non final-leafs and ones represent final-leafs.
def buildTree(input, count, node = None, root = None):
    if count > 0:
        if input[0] == '0': #not final-leaf node
            if not node: #create root
                root =  Node(None, 0)
                return buildTree(input[1:], count, root, root)
            else:
                if node.left and node.right: #if node has both children go to node parent and check again
                    return buildTree(input, count, node.parent, root)
                else:
                    n = Node(None,0)
                    n.setParent(node)
                    if node.left: #If left children exits new node has to be righ children
                        node.setRight(n)
                    else: #If there are no nodes, new node has to be left children
                        node.setLeft(n)
                    return buildTree(input[1:], count, n, root)
        else: #final-leaf node
            if not node: #create root with item value
                count -= 1
                root = Node(chr(int(input[1:9],2)),0)
                return buildTree(input[9:], count, root, root)
            elif node.left and node.right: #if node has both children go to node parent and check again
                return buildTree(input, count, node.parent, root)
            else:
                count -= 1
                n = Node(chr(int(input[1:9],2)),0)
                n.setParent(node)
                if node.left: #If left children exits new node has to be righ children
                    node.setRight(n)
                else: #If there are no nodes, new node has to be left children
                    node.setLeft(n)
                return buildTree(input[9:], count, node, root)
    else:
        return root, input

# It recieves the input and outputFile. It reads the input file to
# retrieve the binary representation of the outputFile. Carefully reads
# the given lenghts and the header, it builds the binary tree to decompress
# the code an decompress it. Then it stores the message in the outFile.
def huffmanDecompression(inputFile, outFile):
    inf = open(inputFile,'r')
    outf = open(outFile,'w')

    input = inf.read()

    count = int(input[0]) #Get nBits needed to complete last byte
    input = input[1:]

    code = ""
    for char in input:
        code += '{0:08b}'.format(int(ord(char)))

    tree, compression = buildTree(code[8:],int(code[:8],2)) #Get the tree and rest of the code to decompress
    res = ""
    #Decompress the code
    if count != 0: res = preDecompression(compression[:-count], tree)
    else: res = preDecompression(compression, tree)

    outf.write(res)#Write result in the file

    inf.close()
    outf.close()

def compress(file):
    start = time.time()
    compressedSize = huffmanCompression(file, file+".huf")
    end = time.time()
    uncompressedSize = os.stat(file).st_size
    percentage = compressedSize/float(uncompressedSize)
    print ("Time neeed: " + str(end - start) + "seg")
    print("Uncompressed: %s bytes"%uncompressedSize)
    print("Compressed: %s bytes"%compressedSize)
    print("Precentage: %s"%percentage)

def decompress(file):
    start = time.time()
    huffmanDecompression(file+".huf", file)
    end = time.time()
    print ("Time neeed: " + str(end - start) + "seg")

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# """""""""""""""""""""""""""""""" MAIN """""""""""""""""""""""""""""""
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# arguments
if len(sys.argv) == 2:
    type = sys.argv[1]
    if type == "-T":
        print "test1"
        print "compress"
        compress("test/test1")
        print "decompress"
        decompress("test/test1")
        os.system("diff " + "test/test1" + " " + "test/original_test1")
        print
        print "test2"
        print "compress"
        compress("test/test2")
        print "decompress"
        decompress("test/test2")
        os.system("diff " + "test/test2" + " " + "test/original_test2")
        print
        print "test3"
        print "compress"
        compress("test/test3")
        print "decompress"
        decompress("test/test3")
        os.system("diff " + "test/test3" + " " + "test/original_test3")
        print
        print "test4"
        print "compress"
        compress("test/test4")
        print "decompress"
        decompress("test/test4")
        os.system("diff " + "test/test4" + " " + "test/original_test4")
        print
        print "test5"
        print "compress"
        compress("test/test5")
        print "decompress"
        decompress("test/test5")
        os.system("diff " + "test/test5" + " " + "test/original_test5")
        print
        print "test6"
        print "compress"
        compress("test/test6")
        print "decompress"
        decompress("test/test6")
        os.system("diff " + "test/test6" + " " + "test/original_test6")
    else:
        usage()
elif len(sys.argv) == 3 :
    type = sys.argv[1]
    file = sys.argv[2]
    if type == "-c": #Compress
        compress(file)
    elif type == "-d": #decompress
        decompress(file)
    else:
        usage()
elif len(sys.argv) == 4:
    type = sys.argv[1]
    file1 = sys.argv[2]
    file2 = sys.argv[3]
    if type == "-t": #decompress
        os.system("diff " + file1 + " " + file2)
    else:
        usage()
else:
    usage()
