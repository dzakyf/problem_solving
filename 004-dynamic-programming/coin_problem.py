from math import inf 
import timeit


def solve(target, coins):
    #base case 
    if target == 0: return 0 
    if target < 0: return inf

    best = inf 

    for coin in coins:
        best = min(best, solve(target-coin, coins) + 1)
    
    return best 

ready=dict()
value=dict()
def solveWithMemoization(target, coins):
    
    best = inf 
    #base case 
    if target < 0: return inf
    if target == 0: return 0 
    if not target in ready: ready[target] = True
    if not target in value: value[target] = best 
    else: return value[target]
    
    for coin in coins:
        best = min(best, solve(target-coin, coins) + 1)
    
    return best 

def solveWithIteration(target, coins):
    value = dict()
    value[0] = 0

    for i in range(1, target+1):
        value[i] = inf
        for coin in coins: 
            if i-coin >=0:
                value[i] = min(value[i], value[i-coin]+1)
    return value[target]

def main():
    target = 10
    coin = [1,3,4]
    
    solveWithIteration(target, coin)
    #result = solve(target, coin)
    #st = time.process_time()
    #result = solveWithMemoization(target,coin)
    #time.sleep(2)
    #et = time.process_time()
    #result_2_time = et - st 
    result_time = timeit.timeit(stmt='solve(10, [1,3,4])', globals=globals(), number=1000)
    result_2_time = timeit.timeit(stmt='solveWithMemoization(10, [1,3,4])', globals=globals(), number=1000)
    result_3_time = timeit.timeit(stmt='solveWithIteration(10, [1,3,4])', globals=globals(), number=1000) 

    print(f"execution time (without memo): {result_time},\n execution time (with memo): {result_2_time}, \nexecution time (with iteration): {result_3_time},\n")

if __name__ == '__main__':
    main()
