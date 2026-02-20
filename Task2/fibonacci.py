#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2.21
n = int(input("How many terms?\n")) + 1
fib =[0] * n

for x in range(n):
    if x == 0:
        fib[x] = 0
    elif x == 1:
        fib[x] = 1
    else:
        fib[x] = fib[x-1] + fib[x-2]

print(f"The {n-1}th term is {fib[n-1]}")

        
        
    

