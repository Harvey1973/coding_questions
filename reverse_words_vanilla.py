class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (s.isspace()) or (s == ''):
            return ''
        tokens = s.split(" ")
        print(tokens)
        n = len(tokens)
        temp = ['']* n
        result = ['']* n
        count = 0 
        for i in range (n):
            temp [n-i-1] = tokens[i]
        for i in temp :
            print(i)
            if i =='':
                count = count + 1
        for j in range (count):
            temp.remove('')
        result = temp
        if (result == None):
            return ''
        else:        
            return (' '.join(result))