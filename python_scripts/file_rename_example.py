import pathlib
import os
import re

p = pathlib.Path('path/to/dir')

for filePath in list(p.glob('**/*.scss')):
    strPath = str(filePath)
    newPath = re.sub(r'(\w+)\.scss', r'\1.module.scss', strPath)
    os.rename(strPath, newPath)


