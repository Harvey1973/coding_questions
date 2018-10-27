# checking if a input string is a panlindrom 
# some assumption :  1. an empty string is panlindrom 2. a string containing ONLY non-alphanumeric characters are considered as panlindrom
# 3. not case sensitive (i.e Aba is considered a valid solution )
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Idea : keey two pointers , one at head and one at tail , keep incrementing them until they meet 
        , skipping any non-alphanumeric characters 
        """
        length = len(s)
        i = 0
        j = length -1
        while (i < j):
            # each iteration we want to skip non-alphanumeric values
            while(i < j and (not s[i].isalnum())): 
                i = i + 1 
            while(i < j and (not s[j].isalnum())): 
                j = j - 1
            if (s[i].lower() != s[j].lower()):
                return False
            i += 1
            j -= 1
        return True
obj = Solution()        
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))