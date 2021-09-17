import matplotlib.pyplot
import numpy

p=numpy.arange(0,10,1)
for i in p:
    x1=numpy.array([i]*100)
    y1=numpy.linspace(0,9,100)
    matplotlib.pyplot.plot(x1,y1,color=(0,0,0),linewidth=0.5)
    x2=numpy.linspace(0,9,100)
    y2=numpy.array([i]*100)
    matplotlib.pyplot.plot(x2,y2,color=(0,0,0),linewidth=0.5)

p=numpy.arange(0,10,3)
for i in p:
    x1=numpy.array([i]*100)
    y1=numpy.linspace(0,9,100)
    matplotlib.pyplot.plot(x1,y1,color=(0,0,0),linewidth=1.5)
    x2 = numpy.linspace(0, 9, 100)
    y2 = numpy.array([i] * 100)
    matplotlib.pyplot.plot(x2, y2, color=(0, 0, 0), linewidth=1.5)

basic_axis=[]
for i in range(9,0,-3):
    for j in range(0,9,3):
        basic_axis.append([j,i])

add_axis=[]
for i in range(0,3,1):
    for j in range(0,3,1):
        add_axis.append([j,i])


exist_parts=[[1,1,2],[2,1,3],[5,5,2]]
words_li=[]

for number in exist_parts:
    words=str(number[2])
    words_li.append(words)

block_axis=[]

for number in exist_parts:
    aixs_part=slice(0,2,1)
    axis_value=number[aixs_part]
    basic_value=basic_axis[axis_value[0]]
    add_value=add_axis[axis_value[1]]
    block_axis.append([basic_value[i]+add_value[i] for i in range(len(basic_value))])


for i in range(len(block_axis)):
    points=block_axis[i]
    p_x=points[0]+0.5
    p_y=points[1]-0.5
    words=words_li[i]



matplotlib.pyplot.axis("off")
matplotlib.pyplot.show()