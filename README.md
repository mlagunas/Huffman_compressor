# Huffman compressor/ decompressor

Code developed for educational purposes during the course Basic algorithms at the University of Zaragoza, Spain.
It has implemented a basic Huffman compressor/ decompressor with a small improvement in decompression which optimize the time for this task.

<table>

  <tr>

    <th>File</th><th>Bytes</th><th>Original Algorithm</th><th>Improved Algorithm</th>

  </tr>

  <tr>

    <td>Test6</td><td>552721 bytes</td><td>472.17 sec</td><td>59.06 sec</td>

  </tr>
</table>

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

## RESULTS

  TO-DO
