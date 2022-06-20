# Basically we check if there exist anagram of s1 in s2

def checkInclusion(s1, s2):
    #1 case 1 : there is no permutation of s1 in s2 if the length of s2 is greater than s1
    if len(s2) < len(s1): return False

    #2 we initiate array to keep track alphabet in s1 and to keep track s2 based on s1
    dic_s1 = [0] * 26  # length of alphabet a-z
    dic_s2 = [0] * 26 

    #3 include all s1 to dic_s1
    for char in s1:
        dic_s1[ord(char) - ord('a')] += 1
    
    for j in range(len(s2)):
        dic_s2[ord(s2[j])- ord('a')] += 1
        
        if j >= len(s1):
            dic_s2[ord(s2[j - len(s1)]) - ord('a')] -= 1
        
        if dic_s1 == dic_s2 : 
            return True
        
    return False
    



def main():

    s1= "ab"
    s2 = "eidbaooo"
    res = checkInclusion(s1,s2)
    print(res)



if __name__ == '__main__':
    main()
