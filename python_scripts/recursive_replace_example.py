import glob
import re
from os.path import relpath

for filepath in glob.iglob('/path/to/files/**/*.ts*', recursive=True):
    with open(filepath) as file:
        rel = relpath('path/to/files/locale/i18next', filepath)
        s = file.read()
        s = re.sub('import\s{\s?t\s?}.*',
                "import { i18instance } from '" + rel[3:] + "'",
               s)
#        print(s)

    with open(filepath, "w") as file:
        file.write(s)
