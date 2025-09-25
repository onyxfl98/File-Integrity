#!/usr/bin/env python3
"""
Module description: Integrity Check Function. This function loads a previously generated baseline of file hashes from a JSON file, performs a new scan of the specified directory to compute current file hashes, and compares the two sets of data to identify modified, new, and deleted files. It then prints a report summarizing the findings.

Still needs further broken out and cleaned up.
"""

import json
from check_integrity import build_hash_dictionary

def check_integrity(directory_to_scan: str, baseline_filename: str = "baseline.json") -> None:
    # Load the baseline from 'baseline.json' using json.load()
    try:
        with open(baseline_filename, 'r') as f:
            baseline = json.load(f)
    except Exception as e:
        print(f"Error loading baseline: {e}")
        return

    # Perform a new scan of the directory to get current hashes
    current_scan = build_hash_dictionary(directory_to_scan)

    # Compare the new scan with the baseline data
    # Create lists for modified, new, and deleted files
    modified_files: list[str] = []
    new_files: list[str] = []
    deleted_files: list[str] = []

    for key in baseline.keys():
        if baseline[key] != current_scan.get(key):
            #ic(f"File modified: {key}")
            modified_files.append(key)
        elif key not in current_scan:
            #ic(f"File deleted: {key}")
            deleted_files.append(key)
        
    for key in current_scan.keys():
        if key not in baseline:
            #ic(f"New file detected: {key}")
            new_files.append(key)
    
    # Print a report of the findings
    # since we're still using the simple version I'm just printing the lists but eventually the printout will likely move to it's own function
    print("\nIntegrity Check Report:")
    print("-----------------------")
    print(f"Modified files ({len(modified_files)}):")
    for file in modified_files:
        print(f" - {file}")
    print(f"\nNew files ({len(new_files)}):")
    for file in new_files:
        print(f" - {file}")
    print(f"\nDeleted files ({len(deleted_files)}):")
    for file in deleted_files:
        print(f" - {file}")
    print("\nIntegrity check complete.")

# --- Main Execution Block ---
def main():
    """
    Main function to execute the script's logic.
    """
    # Your main code logic goes here
    print("Hello from the Python template!")


if __name__ == "__main__":
    main()
