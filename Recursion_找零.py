def recDC(coinValueList, change, knownResults):#添加了查询表，即可得到特定金额
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


'''
第一个硬币是1，第二个是1，第三个是1
                     第三个是5
                     第三个是10
                     第三个是25

            第二个是5，第三个1
                     第三个是5
                     第三个是10
                     第三个是25
                     
            第二个是10
                     ……
                     
            第二个是25
                     ……
'''


n = recDC([1, 5, 10, 25], 16, [0]*17)
print(n)

