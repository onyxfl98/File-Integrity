#!/usr/bin/env python3
"""
Module description: Build Hash Dictionary. This function scans a specified directory and its subdirectories, computes the hash for each file using the hash_file() function, and builds a dictionary where each key is a file path and its corresponding value is the file's hash. The function returns this dictionary.
"""

import os
from hash_file import hash_file

def build_hash_dictionary(directory_to_scan: str) -> dict[str, str]:
    hash_dict: dict[str, str] = {}
    
    # Use os.walk() to go through every file in the directory
    for root, dirs, files in os.walk(directory_to_scan):
        for filename in files:
            filepath = os.path.join(root, filename)
    
            # For each file, call hash_file() to get its hash
            file_hash: str = hash_file(filepath)
            if file_hash:
    
                # Add the {filepath: hash} pair to the dictionary
                hash_dict[filepath] = file_hash
    return hash_dict


def main():
    """
    Main function to execute the script's logic.
    """
    # Your main code logic goes here
    print("Hello from the Python template!")


if __name__ == "__main__":
    main()
