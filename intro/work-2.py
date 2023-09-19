import random

def gensquares(n):
    for i in range(n):
        yield i**2

for x in gensquares(10):
    # print(x)
    pass

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)
    
for num in rand_num(1,10,12):
    # print(num)
    pass

s = 'hello'
s_iter = iter(s)
for i in range(len(s)):
  print(next(s_iter))


