import os

path = os.getcwd()
outfile = open('data/train.txt','a+')

files = []
for dirpath, subdirs, files in os.walk(path):
    for x in files:
        if x.endswith(".jpg"):
            #print(os.path.join(dirpath,x))
            files.append(os.path.join(dirpath,x))
            outfile.write(os.path.join(dirpath, x))
outfile.close()
print(files)
