# brute force solution with tabulation O(n^2) time complexity with O(n) space complexity 
def solve(arr):
    length = len(arr)
    res = [1 for i in range(length)]

    for i in range(0, length):
        for j in range(0, i):
            if arr[j] < arr[i]:
                res[i] = max(res[i], res[j] + 1)
    return res

# binary search O(n log n) time complexity with O(1) space complexity
def solveWithBinarySearch(arr):
    def bsearch(sub, val):
        low, high = 0, len(sub) - 1

        while low <= high: 
            mid = low + (high - low) // 2

            if val < sub[mid]:
                high = mid - 1

            elif val > sub[mid]: 
                low = mid + 1
            
            else: 
                return mid 
        return low 



    sub_arr = []

    for num in arr:
        pos_to_replace = bsearch(sub_arr, num)

        if pos_to_replace == len(sub_arr):
            sub_arr.append(num)
        else: 
            sub_arr[pos_to_replace] = num

    return len(sub_arr)

                


def main():
    arr = [10,9,2,5,3,7,101,18]

    result = solve(arr)
    result_w_bsearch = solveWithBinarySearch(arr)

    print(result_w_bsearch)


if __name__ == '__main__':
    main()
