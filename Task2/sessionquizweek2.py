#!/usr/bin/env python
# coding: utf-8

# # Energy and frequency
# 
# With Planck's constant $h$, we write the relation between energy and frequency as:
# 
# $$E = hf$$

# 2.1
# $E = h c / \lambda$

# 2.2 $F = G \frac{m_1 m_2}{r^2}$

# 2.3 $\sin(2 x) = 2 \sin(x) \cos(x) = \frac{2 \tan(x)}{1 + \tan^2(x)}$

# In[1]:


#2.4

from math import *
alpha_d = 30
alpha_r = radians(alpha_d)

func1 = sin(2*alpha_r)
func2 = 2*sin(alpha_r)*cos(alpha_r)
func3 = (2*tan(alpha_r)) / (1 + tan(alpha_r) ** 2)

print(f"{func1}, {func2} and {func3} are all the same")


# 2.5 $\displaystyle\sum_{k = 0}^{\infty} \frac{1}{4 k^2 - 1} = \frac{1}{2} \\ \int_0^\pi e^{ix}dx = 2i$

# 2.6 $\lambda$

# In[4]:


from IPython.display import display, Math
from math import sin, pi

x = 9
Lambda = 0.5

s = rf"\sqrt({x}) = {x**0.5}\ and \sin(\lambda \pi)={sin(Lambda*pi)}"
print(s)
m = Math(s)
display(m)


# In[9]:


#2.8

from math import exp, log

x = 9
x_expanded = int(exp(log(x)))
if x == x_expanded:
    print("True")


# In[11]:


#2.9

from math import factorial

print("{:e}".format(factorial(100)))


# This means the maximum value for integers in python is at least 157 digits long.

# In[23]:


#2.11

from math import atan2, tan

x = 2
y = 3
tangent = 2/3
tanphi = tan(atan2(2,3))


if tanphi == tangent:
    print(f"{tanphi} and {tangent} are the same")


# In[19]:


#2.12

from math import atan2, degrees

x = float(input("Enter in the value for x\n"))
y = float(input("Enter in the value for y\n"))

angle = degrees(atan2(x,y))

print(f"The angle between the x axis and the line between origin and ({x},{y}) is {angle} ")
if x > 0 and y > 0:
    print(f"The line line {x},{y} is in the first quadrent.")
elif x < 0 and y > 0:
    print(f"The line line {x},{y} is in the second quadrent.")
elif x < 0 and y < 0:
    print(f"The line line {x},{y} is in the third quadrent.")
elif x > 0 and y < 0:
    print(f"The line line {x},{y} is in the fourth quadrent.")
else:
    print(f"The line line {x},{y} is on either axis.")


# atan2 adjusts the angle based on the x and y coordinates, so you don't have to correct them yourself to get the right angle.

# In[24]:


#2.14

X = [1.36,  1.46,  1.41,  2.12,  0.42,  0.98,  0.45,  1.97, -0.24, 2.18]
X.append(0.51)
X.remove(2.12)
print(X[6])
print(X)
print(X.index(1.46))
Xslice = X[2:-2:2]
print(Xslice)
print(f"The sum of the elements in the slice is {sum(Xslice)}")


# In[22]:


#2.15


night1 = [1,3,2,4,0,3,7,5,2,9,2,4,3]
night2 = [0,0,2,4,2,4,3,2,1,1,1,2,0]

night1s = set(night1)
night2s = set(night2)

inter = night1s.intersection(night2s)

print(f"{inter}")
print(f"5 is an element of the intersection list: {5 in inter}")
print(f"5 is an element of the list version of night 1: {5 in night1}")


# In[1]:


# 2.19

from numpy import random,std

rndm = random.normal(loc = 0.0, scale = 1.4, size = 100000)
devi = std(rndm)
print(f"The standard deviation is {devi}")


# In[17]:


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

print(f"The {n}th term is {fib[n-1]}")

        
        
    


# In[ ]:




