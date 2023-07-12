import os

# Create a function to verify if a directory exists
def verify_dir(path):
    return os.path.exists(path)

# Create a function to create a directory
def create_dir(path):
    return os.makedirs(path, exist_ok=True)