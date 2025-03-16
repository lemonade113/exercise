def sum(nualistist):
    if len(nualistist) == 1:
        return nualistist[0]
    else:
        return nualistist[0] + sum(nualistist[1:])
