class Pair:
    def __init__(self, i, j):
        self.i = i
        self.j = j

def quad_sum(arr, target):
    ''' Returns a list of quadruples that sum to target. '''

    map, result = {}, []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):

            sum = arr[i] + arr[j]
            if sum in map:
                map[sum].append(Pair(i, j))
            else:
                map[sum] = [Pair(i, j)]

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        for j in range(i+1, len(arr)):
            if j > i+1 and arr[j] == arr[j-1]:
                continue

            diff = target - (arr[i] + arr[j])

            if diff in map:
                for pair in map[diff]:
                    if pair.i != i and pair.i != j and pair.j != i and pair.j != j:
                        temp = [arr[i], arr[j], arr[pair.i], arr[pair.j]]
                        temp.sort()
                        if temp not in result:
                            result.append(temp)
    return result
         
