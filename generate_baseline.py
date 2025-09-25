#!/usr/bin/env python3
"""
Module description: Generate a baseline of file hashes for a specified directory.
"""

import json
import build_hash_dictionary

# --- Baseline Generation Function ---
def generate_baseline(directory_to_scan: str) -> None:
    # Create baseline dictionary
    baseline: dict[str, str] = build_hash_dictionary(directory_to_scan)
    
    # Open a baseline file (e.g., 'baseline.json') for writing
    with open('baseline.json', 'w') as f:
        # Use json.dump() to save the dictionary to the file
        json.dump(baseline, f, indent=4)
    # Print a success message
    print("Baseline generated successfully.")

def main():
    """
    Main function to execute the script's logic.
    """
    # Your main code logic goes here
    print("Hello from the Python template!")


if __name__ == "__main__":
    main()
