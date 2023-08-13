# compresses images in dirlist
# run in ieee-website-2022-2023/assets/img directory

import sys, os, subprocess
from pathlib import Path
#dirlist = os.listdir(sys.argv[1])
compressdir = "events/"# directory of images to be compressed
dirlist = os.listdir(compressdir)
print(dirlist)
for file in dirlist:

    if (file.endswith("jpg") | file.endswith("JPG") | file.endswith("png")):
        filepath = Path('./'+compressdir+file)
        print(filepath, end =" ")
        if not os.path.exists(str(filepath.with_suffix('.webp'))): # doesn't rerun on previously converted images
            print("")
            cmd = ['magick', str(filepath), '-quality', str(99),
                '-define', 'webp:near-lossless=99',
                '-define', 'webp:method=6',
                '-define', 'webp:target-size=100000',
                '-define', 'webp:thread-level=1',
                str(filepath.with_suffix('.webp'))]
            subprocess.call(cmd)
        else:
            print("--SKIPPED")
        #input("stop")
