
# returns the number of ways a string (of intagers) can be decoded (a-z is represented as intagers 1 through 26)
def numWaysToDecode(string: str) -> int:
    # checking if the next two chars can represent a valid letter
    length = len(string)  # the length of the string
    if (length > 1 and int(string[0] + string[1]) <= 26):
        # returning the number of ways to decode it from this point
        return numWaysToDecode(string[1:]) + numWaysToDecode(string[2:])
    # continuing to decode the string or returning 1 if at the end of the search
    return numWaysToDecode(string[1:]) if length > 1 else 1

# testing the function 
print(numWaysToDecode('1111'))  # should be 5
print(numWaysToDecode('111'))   # should be 3
print(numWaysToDecode('231532'))
print(numWaysToDecode('3215231'))
print(numWaysToDecode('3214'))

