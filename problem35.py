
def SortRGB(l: list) -> list:
    num = [0,0,0]  # the number of each character
    for char in l:
        num["RGB".index(char)] += 1  # adding up the number of each character
    return list("R"*num[0] + "G"*num[1] + "B"*num[2])  # returning the sorted version

# testing it
print(SortRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
