#Kadane Algorithm's is basically look for all positive contiguous segments of the array.

def max_subarray_w_kadane(arr):
    #1 we decide that the value of first index is the largest
    maxSum = current = arr[0]

    #2 loop array, starting from index 1, excluding first index value's
    for i in range(1, len(arr)):

        #3 reset current if the value is below zero 
        if current < 0 : 
            current = 0

        #4 add current with value of arr[i]
        current += arr[i]

        #5 assign to maxSum if its value is greater than current 
        if current > maxSum : 
            maxSum = current  

    #6 return maxSum
    return maxSum 

def max_subarray_w_inbuilt_max_func(arr):

    maxSum = current = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        maxSum = max(current, maxSum)
    
    return maxSum


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]    

    max_subarray = max_subarray_w_kadane(nums)
    w_inbuilt = max_subarray_w_inbuilt_max_func(nums)
    print(max_subarray, w_inbuilt)

if __name__ == '__main__':
    main()
