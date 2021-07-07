#File_20G
file = []
with open(filepath,'r') as f:
    for i in f: 
        file[i] = f.read(1024)