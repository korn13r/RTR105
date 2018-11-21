
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import *
from matplotlib import pyplot as plt

x = linspace(0, 4, 70)
y = sin(x)
y1 = x
y2 = x - (pow(x, 3)/(1 * 2 * 3))
# var attēlot arī: y2 = y1 - x*x*x/(1*2*3)
y3 = x - (pow(x, 3)/(1 * 2 * 3)) + (pow(x, 5) / (1 * 2 * 3 * 4 * 5))
# var attēlot arī: y3 = y2 + x*x*x*x*x/(1 * 2 * 3 * 4 * 5)
y4 = x - (pow(x, 3)/(1 * 2 * 3)) + (pow(x, 5) / (1 * 2 * 3 * 4 * 5)) - (pow(x, 7) / (1 * 2 * 3 * 4 * 5 * 6 * 7))
# var attēlot arī: y4 = y3 - x**7/(1 * 2 * 3 * 4 * 5 * 6 * 7)
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$ un tās izvirzijumi rindā')

plt.plot(x, y)
plt.plot(x, y, color = "#FF0000")

plt.plot(x, y1)
plt.plot(x, y1, color = "#00FF00")

plt.plot(x, y2)
plt.plot(x, y2, color = "#0000FF")

plt.plot(x, y3)
plt.plot(x, y3, color = "#342A3C")

plt.plot(x, y4)
plt.plot(x, y4, color = "#348000")

plt.show()


