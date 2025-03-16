def dpMakeChange(coinList, changes):
    minCoins = [0]*(changes+1)
    for i in range(1, changes+1):
        minCoins[i] = i
        for j in [c for c in coinList if c <= i]:
            minCoins[i] = min(minCoins[i - j]+1, minCoins[i])
    return minCoins[changes]


print(dpMakeChange([1, 5, 10, 25], 16))

