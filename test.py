print(type(4/2))
print(type(4//2))
print(type(4%2))
print(type(4*2))

def fun2(x,y):
    if not x:
        return x
    return y
a = True
b = False
print(fun2(a,a))
print(fun2(a,b))
print(fun2(b,a))
print(fun2(b,b))
    
def fun3(x,y):
    if  x:
        return x
    return y

print(fun3(a,a))
print(fun3(a,b))
print(fun3(b,a))
print(fun3(b,b))