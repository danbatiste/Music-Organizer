import os
import shutil
import sys

files = os.listdir()
files.remove(sys.argv[0].split('\\')[~0])

def artist(file):
    file = file.split(' - ')
    return file[0]
    
artists = list( map(lambda f: artist(f), files) )

for artist in artists:
    try:
        os.mkdir(artist)
    except:
        continue
    
data = list( zip(files, artists) )
for v in data:
    try:
        print(v)
        shutil.move(v[0],v[1] + '/' + v[0])
        print('{} -> {}'.format(v[0],v[1]))
    except: continue