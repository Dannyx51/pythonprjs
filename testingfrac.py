import numpy 
from numba import jit
import matplotlib.pyplot as plt 

@jit
def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
        z = z*z + c

        if(z.real**2 + z.imag**2) >= 4:
            return i

    return max_iter

columns = 12000
rows = 12000

zoomxs = [-0.5697179068711984,-0.5063040508702775]
zoomys = [0.5891243463530614,0.636684738353752]

result = numpy.zeros([rows,columns])
for row_index, Re in enumerate(numpy.linspace(zoomxs[0],zoomxs[1],num=rows)):
    for column_index, Im in enumerate(numpy.linspace(zoomys[0],zoomys[1],num=columns)):
        result[row_index,column_index] = mandelbrot(Re, Im, 100)

plt.figure(dpi=100)
plt.imshow(result.T, cmap = 'hot', interpolation = 'bicubic', extent = [-2,1,-1,1])
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()