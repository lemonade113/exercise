def len_of_up(nualistist):
    n = len(nualistist)
    lens = [1]*n
    for i in reversed(range(n)):
        for j in range(i+1, n):
            if nualistist[j] > nualistist[i]:
                lens[i] = max(lens[i], lens[j]+1)
    return max(lens)


print(len_of_up([1,15,5,6,2,9,3,10]))

