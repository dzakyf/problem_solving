

def partition(arr, low, high):

    #select pivot element, in this example i set it to the rightmost element in array
    pivot = arr[high]   

    #pointer for greater element
    i = low - 1

    #traverse through the all element
    for j in range(low, high):
        # compare current element with pivot,
        # if smaller element than pivot is found, swap it with the bigger element pointed by i  
        if arr[j] <= pivot :
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # swap pivot element with bigger element pointed by i
    arr[i + 1], arr[high] = arr[high], arr[i+1]

    # return where the partition end/start
    return i + 1


def quicksort(arr, low, high):

    if low <= high:
        # find pivot element 
        # smaller element <= pivot located on the left
        # bigger element >= pivot located on the right
        part = partition(arr,low,high)
        
        # sort left partition:
        quicksort(arr, low, part - 1)

        # sort right partition: 
        quicksort(arr, part + 1, high)
    

     

if __name__ == "__main__":
    arr = [8, 7, 2, 1, 0, 9, 6]
    quicksort(arr, 0, len(arr)-1)

    print("===sorted===")
    print(arr)
