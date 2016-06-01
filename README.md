# Huffman compressor/ decompressor

Code developed for educational purposes during the course Basic algorithms at the University of Zaragoza, Spain.
The code implements a basic Huffman compressor/ decompressor with a small improvement in decompression which optimize the time for this task, using memoization.

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
### Compresion

<table>

  <tr>

    <th>File</th><th>Original size</th><th>Compressed size</th><th>Time</th>

  </tr>

  <tr>
    <td>Test1</td> <td>69 bytes</td> <td>65 bytes</td> <td>0.00079 sec</td>
  </tr>
    <tr>
     <td>Test2</td> <td>2850 bytes</td> <td>1382 bytes</td> <td>0.00337 sec</td>
  </tr>
    <tr>
     <td>Test3</td> <td>21040 bytes</td> <td>11925 bytes</td> <td>0.04806 sec</td>
  </tr>
    <tr>
     <td>Test4</td> <td>252723 bytes</td> <td>134484 bytes</td> <td>0.5.56854 sec</td>
  </tr>
    <tr>
     <td>Test5</td> <td>152 bytes</td> <td>181 bytes</td> <td>0.001052 sec</td>
  </tr>
    <tr>
    <td>Test6</td> <td>552721 bytes</td> <td>302833 bytes</td> <td>29.846 sec</td>
  </tr>
</table>

### Decompresion

<table>

  <tr>

    <th>File</th><th>Original Algorithm</th><th>Improved Algorithm</th>

  </tr>
  <tr>

    <td>Test2</td><td>0.010841 sec</td><td>0.01372 sec</td>

  </tr>
<tr>

    <td>Test3</td><td>0.3424 sec</td><td>0.3200 sec</td>

  </tr><tr>

    <td>Test4</td><td>69.7636 sec</td><td>12.2737 sec</td>

  </tr>
  <tr>

    <td>Test6</td><td>472.17 sec</td><td>59.06 sec</td>

  </tr>
</table>
