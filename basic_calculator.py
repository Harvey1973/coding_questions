class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # running total
        res = 0
        # current sign
        sign = 1
        # represent number in each closing environment
        num = 0
        stack = []

        for e in s :
            if e.isdigit():
                num = 10*num + int(e)

            # res will keep the running total before the sign
            # and the sign is actully used to calculate the running total 
            # until the next expression (number or () ) comes in
            elif e == '+':
                res = res + (num*sign)
                num = 0
                sign = 1
            elif e == '-':
                res = res + (num*sign)
                num = 0
                sign = -1
            elif e == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif e == ')':
                res = res + num*sign
                num = 0
                res = res*stack.pop()
                res = res + stack.pop()
        return res + sign*num