#!/usr/bin/env python3

import os
import hashlib
import json
import argparse

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

# --- Hashing Function ---
def hash_file(filepath) -> str:
    try:
        # Create a sha256 hash object
        hash_sha256 = hashlib.sha256()
        # Open the file in binary read mode ('rb')
        with open(filepath, 'rb') as f:
            # Read the file in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                # Update the hash object with each chunk
                hash_sha256.update(chunk)
        # Return the final hexadecimal hash digest
        return hash_sha256.hexdigest()
    except Exception as e:
        print(f"Error hashing file {filepath}: {e}")
        return None
    

# --- Build Hash Dictionary Function ---
def build_hash_dictionary(directory_to_scan) -> dict:
    hash_dict = {}
    # Use os.walk() to go through every file in the directory
    for root, dirs, files in os.walk(directory_to_scan):
        for filename in files:
            filepath = os.path.join(root, filename)
            # For each file, call hash_file() to get its hash
            file_hash = hash_file(filepath)
            if file_hash:
                # Add the {filepath: hash} pair to the dictionary
                hash_dict[filepath] = file_hash
    return hash_dict

# --- Baseline Generation Function ---
def generate_baseline(directory_to_scan):
    # Create baseline dictionary
    baseline = build_hash_dictionary(directory_to_scan)
    
    # Open a baseline file (e.g., 'baseline.json') for writing
    with open('baseline.json', 'w') as f:
        # Use json.dump() to save the dictionary to the file
        json.dump(baseline, f, indent=4)
    # Print a success message
    print("Baseline generated successfully.")

# --- Integrity Check Function ---
def check_integrity(directory_to_scan):
    # Load the baseline from 'baseline.json' using json.load()
    try:
        with open('baseline.json', 'r') as f:
            baseline = json.load(f)
    except Exception as e:
        print(f"Error loading baseline: {e}")
        return

    # Perform a new scan of the directory to get current hashes
    current_scan = build_hash_dictionary(directory_to_scan)

    # Compare the new scan with the baseline data

    # Create lists for modified, new, and deleted files
    # Print a report of the findings

# --- Main Execution Block ---
def main():
    # Debug tests
    #ic(hash_file('./main.py'))
    #ic(build_hash_dictionary('.'))
    ic(generate_baseline('.'))
      
    # Set up argparse to handle commands ('generate', 'check') and arguments ('--dir')
    # Parse the arguments provided by the user
    
    # If the user chose 'generate':
        # Call generate_baseline() with the specified directory
    # If the user chose 'check':
        # Call check_integrity() with the specified directory

# Run the main function
if __name__ == "__main__":
    main()