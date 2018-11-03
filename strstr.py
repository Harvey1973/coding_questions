class Solution(object):
    def strStr(self, haystack, needle):
        if(haystack == needle):
            return 0
        for i in range (len(haystack)):
            count = 0
            index = 0
            for j in range(len(needle)):
                #print("i " + str(i))
                #print("i + j " + str(j))

                if (i + j) > len(haystack)-1:
                    return -1
                if (needle[j] != haystack[i+j]):
                    break
                else:
                    count = count + 1
                    index = i
            if (count == len(needle)):
                print("found substring")
                print(index)
                return index
        return -1
        

print(len(""))
sol = Solution()
sol.strStr("aaaaa","bba")                
    