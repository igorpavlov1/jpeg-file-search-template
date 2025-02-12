import os
 
directory = "random_files"
 
for i in range(10, 200):
    filename = f"file{i}"
    filepath = os.path.join(directory, filename)

    try:
        with open(filepath, 'rb') as f:
            header = f.read(3)
    
            if header == b'\xff\xd8\xff':
                os.rename(filepath, filepath + '.jpg')
            else:
                os.remove(filepath)
    except Exception as e:
        print(f"Error processing {filename}: {e}")
