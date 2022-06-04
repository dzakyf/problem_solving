#find the first non-repeating character in a string and return its index. If it doesn't exist, return -1 

def first_unique_char(s: str) -> int:
        s_dict = {}
        s_arr = []
        
        #1 to simulate queue, first create array consists of s value:
        for i in range(len(s)):
            s_arr.append(s[i])

            #2 as we append s value to s_arr, count the occurence of the s value 
            if s[i] in s_dict :
                s_dict[s[i]] += 1
            else :
                s_dict[s[i]] = 1
        
        #3  remove the 0 index value on s_arr (to simulate First In First Out principle), as we remove the value, check if 
        #   the occurence of value we removed is 1, if yes return the index, else we continue to look for value which has exactly 1 occurence
        for j in range(len(s_arr)):
            deque = s_arr.pop(0)
            
            if deque in s_dict and s_dict[deque] == 1 :
                s_dict[deque] -= 1
                
                if s_dict[deque] == 0 : return j
                else : continue

        #4 return -1 if there are no unique value 
        return -1
         
def main():
    s = "leetcode"

    res = first_unique_char(s)
    print(res)

if __name__ == '__main__':
    main()
