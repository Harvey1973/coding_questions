class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        test= ''.join(wordDict)
        for i in s :
            if i not in test:
                return False
            

        result = False
        for word in wordDict:
            #print(word)

            if not s.startswith(word):
                continue 
            if len(word) == len(s) :
                result = True
                break
            else :
                #print(s[len(word):])
                result = self.wordBreak (s[len(word):],wordDict)
            if (result == True):
                return result
        return result


'''
s="aaaab"
wordDict=["a","aa","aaa"]
'''
s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


s = "abcdefg"
wordDict = ["abcde","cdef","fg","bcde","a"]
obj = Solution()
print(obj.wordBreak(s,wordDict))