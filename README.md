# Huffman compressor/ decompressor

Code developed for educational purposes during the course Basic algorithms at the University of Zaragoza, Spain.
The code implements a basic Huffman compressor/ decompressor.

## USAGE 

### Compress/ decompress

To compress or decompress call the script with -c (compress) or -d (decompress)
```
python huffman.py -c|-d file
```
    -c : To compress file, compressed file will be "file.huf"
    
    -d : To decompress file without .huf at the end, decompressed file will be "file"
    
    file: file to compress/decompress

### Checking the resulting file
 
In case you want to test 2 files call the script with -t flag, it will print the differences between both files.
```	
python huffman.py -t file1 file2
```
    -t : Testing mode
    
    file(1,2): files to compare
