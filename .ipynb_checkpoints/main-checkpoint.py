from numpy import random as r
from matplotlib import pyplot as p
I = r.rand(256,256)
p.imshow(I, cmap='gray')
p.show()