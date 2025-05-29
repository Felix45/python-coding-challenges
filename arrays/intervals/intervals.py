def mergeIntervals(intervals):
    ''' Merge overlapping intervals '''

    intervals.sort()

    result = []
    result.append(intervals[0])
    for i in range(1, len(intervals)):
        n = len(result) - 1
        if intervals[i][0] <= result[n][1]:
            result[n][1] = intervals[i][1]
        else:
            result.append(intervals[i])

    return result
