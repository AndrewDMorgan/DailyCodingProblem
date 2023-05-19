
# gets the lowest positive int not in the array
# O(n^2)  so not the most efficent
def lowestPositiveIntegerSlow(numbers: list) -> int:
    # looping through every value that should be in the array
    for i in range(1, len(numbers)):
        # returning it if that value isn't in it
        if i not in numbers: return i
    # all numbers are in order, returning the next number int he sequence
    return max(numbers) + 1

# putting all numbers into a dictionary
# searching the dictionary for the missing value
# O(n)  - faster than the other one on large data sets, slower on small data sets (more over head)
def lowestPositiveIntegerFast(numbers: list) -> int:
    # finding all values in numbers
    values = dict.fromkeys(numbers, 1)
    
    # looping through a finding the first value not present, also keeping track of the largest value
    maxVal = 0
    for value in range(1, len(numbers)):
        if values.get(value): return value
        if value > maxVal: maxVal = value
    
    # returning the next value int he sequence
    return maxVal + 1

