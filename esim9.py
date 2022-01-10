import numpy as np
import matplotlib.pyplot as pyplot 
x,y = np.loadtxt("./data1.csv", unpack=True, delimiter=',')

pyplot.plot(x, label="2020")
pyplot.plot(y, label="2021")
pyplot.xlabel("Month of the year")
pyplot.ylabel("Length / cm")
pyplot.legend()
pyplot.grid()
pyplot.show()