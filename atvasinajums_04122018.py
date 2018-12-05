#print(vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print(vars())

from numpy import sin, linspace
#print(vars())

def f(x):
    return sin(x)

x = linspace(0,4,11)  # izveido masīvu ar 10 x vērtībām

y = f(x)

legend = []
#print(legend)

from matplotlib import pyplot as plt
#print(plt.__doc__)
plt.axis([0, 4, -1, 1])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcijas $sin(x)$ un tās atvasinājumi")
plt.plot(x,y,"k")
legend.append("$sin(x)$ - default - viss ir savienots ar taisām līnijām")
#print(legend)
plt.plot(x,y,"ro")
legend.append("$sin(x)$ - tikai daži punkti")
#print(legend)

N = len(x)          # noskaidro cik garš ir masīvs
deltax = x[1] - x[0]    #solis
atvasinajums = []

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    atvasinajums.append(temp)

plt.plot(x,atvasinajums,"y")
legend.append("$sin(x)$ - atvasinājums - viss ir savienots ar taisām līnijām")
plt.plot(x,atvasinajums,"go")
legend.append("$sin(x)$ atvasinājums - daži punkti")

atvasinajums_caur_masivu = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    atvasinajums_caur_masivu.append(temp)

plt.plot(x[0:N-1],atvasinajums_caur_masivu,"m")
legend.append("$sin(x)$ - atvasinājums, izmantojot masīva vērtības - viss ir savienots ar taisām līnijām")
plt.plot(x[0:N-1],atvasinajums_caur_masivu,"bo")
legend.append("$sin(x)$ atvasinājums, izmantojot masīva vērtības - daži punkti")


plt.plot(0.687, 0.617,"ch", markersize = 12)
#print(plt.legend.__doc__)
#plt.legend(legend, loc = "upper left")
plt.legend(legend, loc = 3, fancybox=True, framealpha=0.3, facecolor = "green")
plt.show()
