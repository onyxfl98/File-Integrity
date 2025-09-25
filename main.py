#!/usr/bin/env python3

import argparse

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

# --- Main Execution Block ---
def main() -> None:
    # Debug tests
    #ic(hash_file('./main.py'))
    #ic(build_hash_dictionary('.'))
    #ic(generate_baseline('.'))
    #check_integrity('.')
      
    # Set up argparse to handle commands ('generate', 'check') and arguments ('--dir')
    # Parse the arguments provided by the user
    parser = argparse.ArgumentParser(description="File Integrity Monitor")
    parser.add_argument('--dir', type=str, required=True, help="Directory to scan")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for 'generate'
    generate_parser = subparsers.add_parser('generate', help="Generate baseline")
    # Later change default filename to include directory name.
    generate_parser.add_argument('--output', type=str, default='baseline.json', help="Output baseline file")

    # Subparser for 'check'
    check_parser = subparsers.add_parser('check', help="Check integrity")

    args = parser.parse_args()

    ic(args)

    # If the user chose 'generate':
        # Call generate_baseline() with the specified directory
        
    # If the user chose 'check':
    if args.command == 'check':
            from check_integrity import check_integrity
            check_integrity(args.dir)

# Run the main function
if __name__ == "__main__":
    main()