
import heapq
import os
import pickle

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(node, prefix="", code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix + "1", code_map)
    return code_map

def compress_file(input_file, output_file, tree_file):
    with open(input_file, 'r') as file:
        data = file.read()
    
    frequency = calculate_frequency(data)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    encoded_data = "".join(huffman_codes[char] for char in data)
    
    padding = 8 - len(encoded_data) % 8
    encoded_data += "0" * padding
    padded_info = "{0:08b}".format(padding)
    
    byte_array = bytearray()
    for i in range(0, len(encoded_data), 8):
        byte = encoded_data[i:i+8]
        byte_array.append(int(byte, 2))
    
    with open(output_file, 'wb') as file:
        file.write(bytes(byte_array))
    
    with open(tree_file, 'wb') as file:
        pickle.dump((huffman_tree, padded_info), file)
    
    original_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(output_file)
    print(f"Original size: {original_size} bytes")
    print(f"Compressed size: {compressed_size} bytes")
    print(f"Compression ratio: {100 * (original_size - compressed_size) / original_size:.2f}%")

def decompress_file(compressed_file, tree_file, output_file):
    with open(tree_file, 'rb') as file:
        huffman_tree, padded_info = pickle.load(file)
    
    with open(compressed_file, 'rb') as file:
        byte_array = file.read()
    
    encoded_data = ""
    for byte in byte_array:
        encoded_data += "{0:08b}".format(byte)
    
    padding = int(padded_info, 2)
    encoded_data = encoded_data[:-padding]
    
    current_node = huffman_tree
    decoded_data = ""
    
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = huffman_tree
    
    with open(output_file, 'w') as file:
        file.write(decoded_data)

# Example usage
compress_file('input.txt', 'compressed.bin', 'tree.pkl')
decompress_file('compressed.bin', 'tree.pkl', 'output.txt')
