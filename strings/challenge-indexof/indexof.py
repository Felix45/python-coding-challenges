def getOccurence(phrase, sub):
    ''' returns an array with all the indices of sub in phrase '''
    indices = []
    repetitions = phrase.count(sub)

    start = 0
    for i in range(repetitions):
        index = phrase.find(sub, start)
        indices.append(index)
        start = index + len(sub)

    return indices
