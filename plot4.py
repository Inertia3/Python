from scipy import interpolate

import matplotlib.pyplot as plt

x = (1,2,3,4,5)
y = (3,4,5,6,7)

f = interpolate.interp1d(x,y)

xnew= (1,2,5)
ynew = f(xnew)
plt.plot(x,y,'*',xnew,ynew,'-',color = "green")

plt.show();

