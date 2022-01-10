import numpy as np
import matplotlib.pyplot as pyplot
x=np.linspace(-3,3)
y=x**2
pyplot.plot(x,y)
pyplot.title("y=x\u00b2")
pyplot.xlabel("x axis")
pyplot.ylabel("y axis")
pyplot.grid()
pyplot.show()