
def fibonacci1 (n):
    if n == 1 or n ==2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n):
    a,b = 1, 1
    for i in range (n-1):
        a, b = b, a+b
    return a
'''
def fibonacci3():
    a,b = 1,1
    while True:
        yield a
        a,b = b, a+b
'''

for i in range (1,10000):
    print (fibonacci2(i))
'''
n = 0
for i in fibonacci3 ():
    if n >=10000:
        break;
    print (i)
    n += 1
'''
