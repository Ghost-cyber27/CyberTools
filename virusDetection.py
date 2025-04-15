# This file is for the testing for virus detection
# With the possibility of adding machine learning component later on
import hashlib
import os

# List of known virus hashes (you can add more hashes here for real testing)
known_virus_hashes = [
    "d41d8cd98f00b204e9800998ecf8427e",  # Example hash (MD5 of an empty file)
    "e99a18c428cb38d5f260853678922e03",  # Example hash (MD5 of 'abc123')
    # Add real hashes for testing if you're working with known viruses
]

# Function to calculate file hash (MD5 in this case)
def calculate_file_hash(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to avoid memory overload with large files
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Function to scan directory for files
def scan_directory_for_viruses(directory):
    print(f"Scanning directory: {directory}...")
    suspicious_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)

            if file_hash and file_hash in known_virus_hashes:
                suspicious_files.append(file_path)

    return suspicious_files

# Function to report findings
def report_findings(suspicious_files):
    if suspicious_files:
        print("\nFound suspicious files (potential viruses):")
        for file in suspicious_files:
            print(f"  - {file}")
    else:
        print("\nNo suspicious files found.")

# Main function
if __name__ == "__main__":
    # Directory to scan (you can change this to any directory)
    directory_to_scan = "/path/to/scan"  # Replace with the directory to scan

    suspicious_files = scan_directory_for_viruses(directory_to_scan)
    report_findings(suspicious_files)
