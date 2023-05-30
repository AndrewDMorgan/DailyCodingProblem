
def GetSubstring(string: str, numUnique: int) -> str:
    i = 0
    substring = []
    length = len(string)
    while len(set(substring)) <= numUnique and i < length:
        substring += string[i]
        i += 1
    return "".join(substring[:-1])

def LongestSubstring(string: str, numUnique: int=2) -> str:
    return sorted(
        [GetSubstring(string[i:], numUnique) for i in range(len(string))]
    , key=lambda v: len(v))[-1]

print(LongestSubstring("abcba"))  # should be bcb
