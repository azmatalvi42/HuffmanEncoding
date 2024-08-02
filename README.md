# HuffmanEncoding

This repository contains a Python implementation of a file compression and decompression tool using the Variable Length Huffman Encoding algorithm. 

The project includes:
- Reading a text file and calculating the frequency of characters (lower-case alphabets, periods, spaces, newlines, and digits 1-9).
- Constructing a Huffman tree and generating Huffman codes.
- Compressing the file by encoding the characters and saving the compressed data along with the Huffman tree.
- Loading the Huffman tree and compressed data.
- Decoding the compressed file to restore the original content.

The tool achieves significant file size reduction, demonstrating the effectiveness of Huffman Encoding in data compression. The repository includes clear documentation and sample input/output files for testing.

Key Features:

1) Efficient Huffman tree construction and code generation.
2) Significant file size reduction (~70%).
3) Comprehensive documentation and sample usage instructions.

Technologies Used:
Python
Data Structures (Heap, Tree)
File I/O
Binary Encoding/Decoding
