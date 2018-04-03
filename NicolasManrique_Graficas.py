import numpy as np
import matplotlib.pyplot as plt

dataP=np.genfromtxt("times_python.csv",delimiter=",")

dataC=np.genfromtxt("times_cpp.csv",delimiter=",")



plt.figure(figsize=(18,9))
plt.scatter(dataP[:,0],dataP[:,1],label='Tiempos en python', c='b')
plt.scatter(dataC[:,0],dataC[:,1],label='Tiempos en cpp', c='b')
plt.title('N vs T')
plt.xlabel('$t(s)$')
plt.ylabel('$N$')
plt.grid()
plt.legend()
plt.savefig("cpp_vs_python.png")
