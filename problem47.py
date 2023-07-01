def getMaxProfit(items: list) -> int:
    difs = []
    for i in range(len(items) - 1):
        difs.append(max(items[i+1:]) - items[i])
    return max(difs)

print(getMaxProfit([9, 11, 8, 5, 7, 10]))
