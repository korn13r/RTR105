import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import *
from matplotlib import pyplot as plt

x = linspace (0, 7, 70)
y = sin(x*x)
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x*x)$')
plt.plot(x, y)
plt.plot(x, y, color = "#34DF00")
plt.show()


