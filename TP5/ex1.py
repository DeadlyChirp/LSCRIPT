import re

case_number = 1  #

patterns = [
    ("A.C", ["abc", "AZZC", "AC", "ABC"]),
#    [ABC] means any character in the set A, B or C
    ("[ABC]",["A", "B", "AC", "ABC"]),
    # [a-k].*[1-5] means any character in the set a-k followed by any digit in the set 1-5
    ("[a-k].*[1-5]", ["a2", "A05", "ab12", "k1k"]),
    # [^a-k].*[1-5] means any character that is not in the set a-k followed by any digit in the set 1-5
    ("[^a-k].*[1-5]", ["a2", "A05", "ab12", "k1k"]),
    # [a-k].[1-5]{,3} means any character in the set a-k followed by any digit in the set 1-5,
    ("[a-k].[1-5]{,3}", ["ak1234", "a123", "ad12bd123", "z1k"]),
    # (a?b)+ means a or b followed by any number of a or b
    ("(a?b)+", ["ababab", "aaaab", "bbbbba", "bbbab"]),

    ("(a|[AB]*)[0-9]", ["aAB0", "AAB0", "0", "A-Z9"]),
    # a|[AB]*)[0-9] means a or any character in the set AB followed by any digit
    (".\\^[^^]+.", ["a^0^0", "aa^0^", "0^^^0", "A^Z9"]),
    # .\^[^^]+. means any character followed by a ^ and then any character that is not a ^,
    # followed by any character
]

for pattern, strings in patterns:
    regex = re.compile(pattern)
    for string in strings:
        if re.fullmatch(regex, string):
            print("---")
            print(f'YES Case {case_number}: "{string}" matches "{pattern}"')
        else:
            print("---")
            print(f'NO Case {case_number}: "{string}" does not match "{pattern}"')
        case_number += 1  # Increment case counter for the next iteration
