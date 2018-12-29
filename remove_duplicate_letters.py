class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        frequency_list = [0]*26
        visited = [False]*26
        # count frequencies for characters appear in string 
        for e in s :
            frequency_list[ord(e) - ord('a')] += 1
        print(frequency_list)
        for c in s :
            # decrement count 
            index = ord(c) - ord("a")
            frequency_list[index] -= 1

            # if already visited ,skip 
            if visited[index]:
                continue
            
            while stack and c < stack[-1] and frequency_list[ord(stack[-1]) - ord("a")] > 0:
                visited[ord(stack[-1]) - ord("a")] = False
                stack.pop()
                
            stack.append(c)
            visited[index] = True
        return ''.join(stack)





obj = Solution()
s = "bcabc"
print(obj.removeDuplicateLetters(s))