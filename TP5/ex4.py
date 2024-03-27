import re


def is_square(s) :
    return re.fullmatch(r"(.+)\1",s,re.I) != None