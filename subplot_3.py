#Subplot

from matplotlib import pyplot as plt
x=[1,2,3,4]
y=[1,4,9,16]

plt.subplot(1,2,1)   #Row = 1, Col = 2, Last 1 = pos of this plot
plt.plot(x,"-o")

ax1=plt.subplot(1,2,1)  
ax2=plt.subplot(1,2,2,sharey=ax1)  #Locks the Y-axis. Y-axis of 2 plots will be same now.
plt.plot(y,"-x")

plt.subplot(1,2,1)
plt.plot(y,"-x")

plt.show()
