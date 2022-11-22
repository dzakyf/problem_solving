def solve(arr):
    length = len(arr)
    res = [1 for i in range(length)]

    for i in range(0, length):
        for j in range(0, i):
            if arr[j] < arr[i]:
                res[i] = max(res[i], res[j] + 1)
    return res
                


def main():
    arr = [6,2,5,1,7,4,8,3]

    result = solve(arr)

    print(result)


if __name__ == '__main__':
    main()
