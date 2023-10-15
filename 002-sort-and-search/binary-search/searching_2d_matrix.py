def binary_search_2d_matrix(matrix, target):
    #1 define boundaries, left is at zero index, and right is at the end of array index
    l, r = 0, len(matrix) - 1
    
    while l <= r:
            #2 define pointer for middle array
            mid = l + (r-l) // 2
            
            #3 check if target is not existed and greater than the largest value of matrix[mid], ignore left half
            if target not in matrix[mid] and target > matrix[mid][-1]:
                l = mid + 1

            #4 check if target is not existed and greater than the largest value of matrix[mid], then ignore right half 
            elif target not in matrix[mid] and target < matrix[mid][-1]:
                r = mid - 1
            
            #5 if target preset at array matrix[mid], we return True
            else:
                return True
        
    return False


def main():
    arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3


    isTargetExists = binary_search_2d_matrix(arr, target)
    print(isTargetExists)


if __name__ == '__main__':
    main()

