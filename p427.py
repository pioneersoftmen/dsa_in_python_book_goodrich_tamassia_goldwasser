import os 

def walk(path):
    # Yield the information for the current path
    yield(path, os.listdir(path), [filename for filename in os.listdr(path) if not os.path.isdir(os.path.join(path, filename))])
    
    # Recurse on each subdirectory
    for filename in os.listdir(path):
        subpath = os.path.join(path, filename)
        if os.path.isdir(subpath):
            yield from walk(subpath)