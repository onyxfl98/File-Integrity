# Project Plan

- [x] Create the Hashing Function: Start by writing a single function that takes a file path as input, reads the file in binary mode ('rb'), and returns its SHA-256 hash. Test this on a few sample files to ensure it works correctly.

- [x] Implement Directory Scanning: Use os.walk() to write a script that recursively lists every file in a target directory. Combine this with your hashing function to print the path and hash of every file.

- [x] Develop Baseline Generation: Modify the directory scanning script to store the results. Create a dictionary where keys are file paths and values are their hashes. Use the json library to save this dictionary to a file (e.g., baseline.json).

- [x] Develop Integrity Checking: This is the core logic.

- [x] Load the baseline.json file into a dictionary.

- [x] Perform a fresh scan of the directory to get the current file hashes.

- [x] Compare the two sets of data to identify modified, new, and deleted files.

- [x] Implement Reporting: Create a clean, user-friendly printout that summarizes the findings from the integrity check.
  - [x] First pass will be a plain text printout of each list

- [x] Add Command-Line Arguments: Use the argparse library to tie everything together. The user should be able to run the script with commands like python monitor.py generate --dir \<path\> and python monitor.py check --dir \<path\>.

## Future Expansion

- [ ] Add a configuration file to let the user easily specify which directories to watch and which files or directories to ignore.

- [ ] Allow user to choose output type  
  - [ ] Use Rich library for pagination
  - [ ] Sort by file path and name
  - [ ] Sort by Deleted/Modified/New
  - [ ] List only 1 of the 3

- [ ] Implement an alerting mechanism, like sending an email if a change is detected.

- [ ] Schedule the check to run automatically at regular intervals.
