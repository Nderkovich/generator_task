import sys
from  typing import List


class SkipThisFile(Exception):
   "Tells the generator to jump to the next file in list."
   pass

def display_files(*files: List[str]) -> None:
    source: str = read_lines(*files)
    for line in source:
        print(line, end='')
        inp = input()
        if inp == 's':
            print('Moving to the next file')
            source.throw(SkipThisFile) # return value is ignored


def read_lines(*files: List[str]) -> str:
    for file in files:
        try:
            with open(file, 'r') as f:
                for line in f:
                    yield line
        except SkipThisFile:
            yield None
        except FileNotFoundError:
            print("File not found")



display_files(*sys.argv[1:])
