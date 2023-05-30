
def GetNumCombinations(maxDepth: int, stepSizes: list=[1,2], depth: int=0) -> int:
    if depth < maxDepth-1:
        return sum(GetNumCombinations(maxDepth, stepSizes, depth+stepSize) for stepSize in stepSizes)
    else: return 1

print(GetNumCombinations(4, [1, 3, 5]))

