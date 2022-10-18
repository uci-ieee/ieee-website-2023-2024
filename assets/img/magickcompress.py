import sys, os, subprocess
from pathlib import Path
#dirlist = os.listdir(sys.argv[1])
compressdir = "dirhere/"
dirlist = os.listdir(compressdir)
print(dirlist)
for file in dirlist:
    
    if file.endswith("jpg"):
        filepath = Path('./'+compressdir+file)
        print(filepath)
        cmd = ['magick', str(filepath), '-quality', str(99), 
            '-define', 'webp:near-lossless=99', 
            '-define', 'webp:method=6',
            '-define', 'webp:target-size=100000', 
            '-define', 'webp:thread-level=1', 
            str(filepath.with_suffix('.webp'))]
        subprocess.call(cmd)
        #input("stop")