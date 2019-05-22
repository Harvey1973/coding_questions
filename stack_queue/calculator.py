'''
class Solution(object):
    def __init__(self):
        # initialize stacks
        # stack 1 is for storing operators
        self.stack = []
        # stack 2 is for storing the post fix expression 
        self.stack2 = []
    def trans_postfix (self,s):
        # translate the input string into post-fix fashion
        # represent the number in each closing environment 
        num = 0
        count = 0
        for e in s :
            count = count + 1
            print(e)
            if e.isdigit():
                num = num*10 + int(e)
            else :
                # push the number on stack2 
                if (num!= 0):
                    self.stack2.append(num)
                    num = 0 
            if count == len(s):
                if (num!= 0):
                    self.stack2.append(num)
                    num = 0
            
            if e == '+' or e == '-':
                self.gotOper(e,1)
            elif e == '*' or e == '/':
                self.gotOper(e,2)
            elif e == '(':
                self.stack.append(e)
            elif e== ')':
                self.gotParen()
        #print(count)
        #print(len(s))
        while (len(self.stack) != 0):
            op = self.stack.pop()
            self.stack2.append(op)
        
        return self.stack2

    def gotOper(self,opThis,prec1):
        # prec1 is the precedence for the newly read in character 
        # the precedence for the popped item on the operator stack 
        prec2 = 0
        while len(self.stack) != 0: 
            opTop = self.stack.pop() 
            # put back the popped item if it is a '(' 
            if (opTop == '('):
                self.stack.append(opTop)
                break 
            else : 
                if (opTop == '+' or opTop == '-'):
                    prec2 = 1 
                else :
                    prec2 = 2
                if prec2 < prec1 :
                    # the popped item has lower precedence than the new char , so it lies below the new operator on the stack 
                    self.stack.append(opTop)
                    break
                else :
                    self.stack2.append(opTop)
        self.stack.append(opThis)
    def gotParen(self):
        while (len(self.stack)!=0):
            op = self.stack.pop()
            if op == '(':
                break 
            else:
                self.stack2.append(op)
    def calculate(self,s):
        post_fix = self.trans_postfix(s)
        print(post_fix)
        stack3 = [] 
        #print(self.stack2)
        intermediate_res = 0
        for e in self.stack2 :
            if type(e) == int :
                stack3.append(e)
            else: 
                num2 = stack3.pop()
                num1 = stack3.pop()
                #print(num1)
                #print(num2)
                #print(e)
                if e == '+':
                    intermediate_res = num1 + num2  
                elif e == '-':
                    intermediate_res = num1 - num2  
                elif e == '*':
                    intermediate_res = num1 * num2 
                else :
                    intermediate_res = num1 / num2
                stack3.append(intermediate_res)
                intermediate_res = 0
            #print(stack3)
        
        
        return stack3.pop()
'''
class Solution(object):
'''
stack based calculator , capable of dealing with brackets, +,-,*,/ and 0- operations
'''
    def __init__(self):
        # initialize stacks
        # stack 1 is for storing operators
        self.stack = []
        # stack 2 is for storing the post fix expression 
        self.stack2 = []
    def trans_postfix (self,s):
        # translate the input string into post-fix fashion
        # represent the number in each closing environment 
        num = 0
        count = 0
        flag = False
        for e in s :
            count = count + 1
            if e.isdigit():
                num = num*10 + int(e)
                if int(e) == 0 :
                    flag = True
            if (count == len(s) and s[-1] != ')' ):
                #print("sss")
                self.stack2.append(num)            
            if e == '+' or e == '-':
                if (num != 0):
                    self.stack2.append(num)
                    flag = False
                elif (num == 0 and flag == True):
                    self.stack2.append(num)
                    flag = False
                self.gotOper(e,1)
                num = 0
            elif e == '*' or e == '/':
                if (num != 0):
                    self.stack2.append(num)
                    flag = False
                elif (num == 0 and flag == True):
                    self.stack2.append(num)
                    flag = False
                self.gotOper(e,2)
                num = 0
            elif e == '(':
                self.stack.append(e)
            elif e == ')':
                if (num != 0):
                    self.stack2.append(num)
                    flag = False
                elif (num == 0 and flag == True):
                    self.stack2.append(num)
                    flag = False
                self.gotParen()
                num = 0
            #print("stack2 ")
            #print(self.stack2)
            #print("stack")
            #print(self.stack)
        #print(count)
        #print(len(s))
        while (len(self.stack) != 0):
            op = self.stack.pop()
            self.stack2.append(op)
        
        return self.stack2

    def gotOper(self,opThis,prec1):
        # prec1 is the precedence for the newly read in character 
        # the precedence for the popped item on the operator stack 
        prec2 = 0
        while len(self.stack) != 0: 
            opTop = self.stack.pop() 
            # put back the popped item if it is a '(' 
            if (opTop == '('):
                self.stack.append(opTop)
                break 
            else : 
                if (opTop == '+' or opTop == '-'):
                    prec2 = 1 
                else :
                    prec2 = 2
                if prec2 < prec1 :
                    # the popped item has lower precedence than the new char , so it lies below the new operator on the stack 
                    self.stack.append(opTop)
                    break
                else :
                    self.stack2.append(opTop)
        self.stack.append(opThis)
    def gotParen(self):
        while (len(self.stack)!=0):
            op = self.stack.pop()
            if op == '(':
                break 
            else:
                self.stack2.append(op)
    def calculate(self,s):
        s = ''.join(s.split(' '))
        #print(s)
        post_fix = self.trans_postfix(s)
        #print(post_fix)
        stack3 = [] 
        #print(self.stack2)
        intermediate_res = 0
        for e in self.stack2 :
            if type(e) == int :
                stack3.append(e)
                
            else: 
                #print(stack3)
                num2 = stack3.pop()
                num1 = stack3.pop()
                #print(num1)
                #print(num2)
                #print(e)
                if e == '+':
                    intermediate_res = num1 + num2  
                elif e == '-':
                    intermediate_res = num1 - num2  
                elif e == '*':
                    intermediate_res = num1 * num2 
                else :
                    intermediate_res = num1 / num2
                stack3.append(intermediate_res)
                intermediate_res = 0
            #print(stack3)
        
        
        return stack3.pop()

obj = Solution()

test_string = "12+3-4"
test_string2 = "3*(4+5) - 6/(1+2)"
test_string_3 = "(1+(4+5+2)-3)+(6+8)"
test_string_4 = "1+1"
test_string_5 = "0-21"
test_string_6 = "(3)+1"
test_string_7 = "   (  3 ) "
test_string_8 = " 2-1 + 2 "
test_string_9 = "(1+(2-(3+ (4- (9) ) ) ) )"
test_string_10 = "(9568+(9040-(380+(2042-(7115)+(6294)-\
(4395-(5183+9744+(7746-(1099+2718))-(9370-(8561+(9302)-(7632+(8451-(1759+(7760))-\
(3377+5363+9093+(8332-(4492-(1151+(1165-8833+(775+(3749)+9399))+9112+(6273+(7285-(6112-(668-\
(7756-4316-(582+1835-(6644+690+1204-(7197+(7897))+(7009-(7262))-7782-(7858+(7644+(9461+(2224)-\
(7531-1095-(891+1022)+2197-(9855)))+(6663-(7417-(6158-(3610))+(1481))-(4182+(4761)))+(5017))+(9990)+\
(6218)))-(2904)+(5631)-(8888)+3401+(3569))+(1135))-(3695-(7713+(3479)-(9813+(8171+(8616-8026+(4634-(6973))-\
(9761-(623-4782)+(2514)+(6233)))))+(6140))-(6641)-8611+(8389)+8074-(4412))-(3703)+(9688+(9513))))-(4987)))+(9647)))))))))-(2299))-(4785))))))"
#post_fix = obj.trans_postfix(test_string)
#print(post_fix)
res = obj.calculate(test_string_10)
print(res)
                    

