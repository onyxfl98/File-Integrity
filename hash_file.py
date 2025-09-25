#!/usr/bin/env python3
"""
Module description: Hashing Function. This function computes the SHA-256 hash of a given file and returns it as a hexadecimal string.
"""
import hashlib

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

def main():
    """
    Main function to execute the script's logic.
    """
    # Your main code logic goes here
    print("Hello from the Python template!")


if __name__ == "__main__":
    main()
