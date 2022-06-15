def encode(strs):
    res = ""

    for i in range(len(strs)):

        if strs[i].isalpha(): 
            shift = ((ord(strs[i]) - 65 + 13) % 26) + 65 #subtract your ascii by 65, add step to shift, take mod 26, finally add 65 back again
            shifted = chr(shift)
            res += shifted
        else: 
            res += strs[i]

    return res


def main():
    str = "SHIFT THIS BY 13"
    res = encode(str)
    print(res)

if __name__ == '__main__':
    main()
