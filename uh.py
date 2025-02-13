import re

def is_pangram(st):
    pangram = re.search('a - z', st)
    if pangram:
        return True
    else:
        return False


is_pangram("the quick brown fox jumps over the lazy dog")