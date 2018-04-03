import numpy as np
import time


def fibonacci(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return fibonacci(N-1)+fibonacci(N-2)


def get_time(N):
    t0=time.time()
    fibonacci(N)
    t1=time.time()-t0
    return t1

archivo=open("times_python.csv","w")

for i in range(35):    
    archivo.write(str(i))
    archivo.write(",")
    archivo.write(str(get_time(i)))
    archivo.write("\n")
    

