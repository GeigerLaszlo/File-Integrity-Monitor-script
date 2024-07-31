import os
import hashlib
import json

class FileIntegrityMonitor:
    def __init__(self, directory, hash_file):
        self.directory = directory
        self.hash_file = hash_file
        self.hashes = {}

    def calculate_hash(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def load_hashes(self):
        if os.path.exists(self.hash_file):
            with open(self.hash_file, 'r') as f:
                self.hashes = json.load(f)
        else:
            self.hashes = {}

    def save_hashes(self):
        with open(self.hash_file, 'w') as f:
            json.dump(self.hashes, f)

    def scan_files(self):
        changed_files = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = self.calculate_hash(file_path)
                if file_path in self.hashes:
                    if self.hashes[file_path] != file_hash:
                        changed_files.append(file_path)
                self.hashes[file_path] = file_hash
        self.save_hashes()
        return changed_files
