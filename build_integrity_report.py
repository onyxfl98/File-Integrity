#!/usr/bin/env python3
"""
Module description: Build Integrity Check Report.
"""

# since we're still using the simple version I'm just printing the lists but eventually the printout will likely move to it's own function

def build_integrity_report(modified_files: list[str], new_files: list[str], deleted_files: list[str], report_style: str = "simple") -> str:

    report_lines: list[str] = []

    if report_style == "simple":
        report_lines.append("\nIntegrity Check Report:")
        report_lines.append("-----------------------")
        report_lines.append(f"Modified files ({len(modified_files)}):")
        for file in modified_files:
            report_lines.append(f" - {file}")
        report_lines.append(f"\nNew files ({len(new_files)}):")
        for file in new_files:
            report_lines.append(f" - {file}")
        report_lines.append(f"\nDeleted files ({len(deleted_files)}):")
        for file in deleted_files:
            report_lines.append(f" - {file}")
        report_lines.append("\nIntegrity check complete.")

    else:
        report_lines.append("Report style not recognized. Please use 'simple'.")
    
    return "\n".join(report_lines)

def main():
    """
    Main function to execute the script's logic.
    """
    # Your main code logic goes here
    print("Hello from the Python template!")


if __name__ == "__main__":
    main()
