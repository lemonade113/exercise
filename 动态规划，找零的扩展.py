def dpMakeChange(coinList, changes, coinsUsed):
    minCoins = [0]*(changes+1)
    for i in range(1, changes+1):
        minCoins[i] = i
        for j in [c for c in coinList if c <= i]:
            if minCoins[i - j] + 1 < minCoins[i]:
                minCoins[i] = minCoins[i - j] + 1
                coinsUsed[i] = j
    return minCoins[changes]

def printCoins(coinsUsed, changes):
    coin = changes
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin, end=' ')
        coin = coin - thisCoin


coinsUsed = [0]*17
print(dpMakeChange([1, 5, 10, 25], 16, coinsUsed))
printCoins(coinsUsed, 16)
