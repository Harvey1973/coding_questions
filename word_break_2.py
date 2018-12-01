# Leet Code Num: 140: Word break 2 , difficulty : Hard 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.dp(s,wordDict,{})
    
    def dp(self,s,wordDict, memo):

        if s in memo :
            return memo[s]
        if s == '':
            return []
        res = [] 
        
        for word in wordDict:

            # check if s starts with a word in WordDict 
            if not s.startswith(word):
                # if the current string does not start with a word, try next in word dict
                continue
            # we have reached the last word, 
            # This is the base case of dp recurrence
            
            if len(word) == len(s) :
                res.append(s)
            else :
                
                resultOfrest = self.dp (s[len(word):],wordDict,memo)
                print(resultOfrest)
                for item in resultOfrest:
                    sentence = word + ' ' + item
                
                    res.append(sentence)
        memo[s] = res
        return res

s="pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
obj = Solution()
print(obj.wordBreak(s,wordDict))
