# Counting permutations 
# n = 5, r = 3

def permutation_w_recursive(items, r):
    for _ in permute(items, 0, r):
        yield tuple(items[:r])
    
def permute(items, i, r):
  
    #base case
    if r == 0 :
        yield 
        return 
    
    for j in range(i, len(items)):
        items[i], items[j] = items[j], items[i]
        for _ in permute(items, i + 1, r - 1):
            yield 
    
    items.append(items.pop(i))

def main():
    arr = [0,1,2,3,4]
    
    permutation_w_recursive(arr, 3)
    

if __name__ == '__main__':
    main()
