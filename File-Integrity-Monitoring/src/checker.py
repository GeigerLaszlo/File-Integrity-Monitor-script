import os
import sys
from monitor import FileIntegrityMonitor

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <directory> [hash_file]")
        sys.exit(1)

    directory = sys.argv[1]
    hash_file = sys.argv[2] if len(sys.argv) > 2 else "file_hashes.json"

    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)

    print(f"Monitoring directory: {directory}")
    print(f"Using hash file: {hash_file}")

    monitor = FileIntegrityMonitor(directory, hash_file)
    monitor.load_hashes()
    changed_files = monitor.scan_files()

    if changed_files:
        print("Changed files detected:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No changes detected.")

if __name__ == "__main__":
    main()
