import matplotlib.pyplot
import numpy

p=numpy.arange(0,5,1)
for i in p:
    x1=numpy.array([i]*100)
    y1=numpy.linspace(0,4,100)
    matplotlib.pyplot.plot(x1,y1,color=(0,0,0))
    x2=numpy.linspace(0,4,100)
    y2=numpy.array([i]*100)
    matplotlib.pyplot.plot(x2,y2,color=(0,0,0))

matplotlib.pyplot.axis("off")
matplotlib.pyplot.show()