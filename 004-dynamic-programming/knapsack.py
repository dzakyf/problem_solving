def accumulate(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]

    return sum

def solveWith1dArray(weights):
    weight_length = len(weights)
    sum_of_weights = accumulate(weights)
    possible = [False for _ in range(sum_of_weights+1)]
    possible[0] = True

    for k in range(1, weight_length+1):
        for x in range(sum_of_weights, -1, -1):
            if possible[x] : possible[x+weights[k-1]] = True

    print(possible)

def solveWith2dArray(weights):
    weight_length = len(weights)
    sum_of_weights = accumulate(weights)
    possible = [[ False for _ in range(0, weight_length + 1)] for _ in range(0, sum_of_weights + 1)]
    possible[0][0]= True

    for k in range(1, weight_length+1):
        for x in range(0, sum_of_weights + 1):
            if x-weights[k-1] >= 0: possible[x][k] |= possible[x-weights[k-1]][k-1] 
            possible[x][k] |= possible[x][k-1]
    
    return possible

    

def main():
    weights = [1,3,3,5]
    result = solveWith1dArray(weights)
    print(result)

if __name__ == '__main__':
    main()
