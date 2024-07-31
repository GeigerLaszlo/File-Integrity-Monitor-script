# File Integrity Monitor Script

## Description
File-Integrity-Monitor script is a simple Python program designed to monitor the integrity of files in a specified directory. This tool calculates and stores hash values of files and checks these values periodically to detect any unauthorized changes. It can be particularly useful for ensuring that important files have not been tampered with or corrupted.

## Features
- Calculates and stores hash values for files in a specified directory using the MD5 algorithm.
- Regularly scans files and compares their current hash values with stored values.
- Notifies the user of any detected changes.
- Command-line interface for easy use.

## Installation
### Prerequisites
- Python 3.x is required to run this program.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/GeigerLaszlo/File-Integrity-Monitor-scriptFile-Integrity-Monitoring.git
   cd File-Integrity-Monitoring

## Usage

Run the main program with the directory you want to monitor as a required argument. You can also optionally specify a different hash file:

```sh
python src/checker.py <directory> [hash_file]
```

- `<directory>`: The path to the directory you want to monitor.
- `[hash_file]` (optional): The path to the hash file to use (default is `file_hashes.json`).


