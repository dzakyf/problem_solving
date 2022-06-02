def reshape(arr, r, c):
    c_arr_len = len(arr[0])
    r_arr_len = len(arr)

    #1 check if r * c is valid 
    if c_arr_len * r_arr_len != r * c:
        return arr

    #2 fill target value with 0 with row = r, col = c
    target = [[0] * c for _ in range(r)]


    #3 loop array 
    for i in range(r*c):
        target[i // c][i % c] = arr[i // c_arr_len][i % c_arr_len]
    

    #4 return
    return target



def main():
    arr = [[1,2],[3,4]]
    r = 1
    c = 4

    res = reshape(arr, r, c)
    print(res)


if __name__ == '__main__':
    main()
