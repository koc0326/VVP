
import numpy as np
import math
a=100
n=10
def odmocnina (a,n):
    x = [0] * n
    x[0] = a
    for i in range(n-1):  
        #print(i)
        x[i+1] = (a/x[i] + x[i])/2
        #print(x) 
    #print(x[n-1])
    return x[n-1]
odmocnina(a,n)
np.sqrt(100)

def Uhelniky(n):
    an,bn = 1,1
    
    if n == 0:
        return S
    else:
        for i in range(0,n+1):
            #print(i)
            if i == 0:
                an = 1
                bn = 1
                vn = math.sqrt(an**2 - ((bn/2)**2))
                #print("vn", vn)
                S = 6*(2**i)*bn*(vn/2)
                #print("S=",S)
            if i > 0:
                #print("vn", vn)
                b2n = math.sqrt((bn/2)**2 + (1-vn)**2)
                #print("b2n = ", b2n)
                v2n = math.sqrt(an**2 - (b2n/2)**2)
                #print("v2n=",v2n)
                S = 6*(2**i)*b2n*v2n/2 
                #print("S=",S)
                i = i + 1
                bn = b2n
                vn = v2n
    return S


def pi3(n):
    #a = [0]* (n+1)
    #a[1] = (1/2) * (1/2**3)
    a1 = (1/2) * (1/2**3)
    s = 1/3* a1
    for i in range(2,n+1):
        a2 = a1 * ((2*i-3)/(2*i))*(1/(2**2))
        a1 = a2
        s = s +  1/(2*i+1)*a2
    pi = 12 * (-np.sqrt(3)/8 + 1/2 - s)
    return pi
