import os

def find(path, filename):
    # Check if the current path refers to a file
    if os.path.isfile(path):
        # Check if the filename matches the given filename
        if os.path.basename(path) == filename:
            print(path)
        

        # Recurse on all entries in the directory
        if os.path.isdir(path):
            for entry in os.listdir(path):
                # Recursively call find on the subdirectory or file
                find(os.path.join(path, entry), filename)

find('C:', 'windows')  