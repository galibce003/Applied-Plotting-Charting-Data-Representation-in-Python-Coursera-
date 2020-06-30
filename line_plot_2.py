#Create a Line Plot

from matplotlib import pyplot as plt

x=[2,4,6,8]
y=[4,16,36,50]

plt.plot(x,"-o",y,"--r")  #-o for solid line (value is defined by dot).
                          #--r for doted line.

 
plt.fill_between(range(len(x)),       #fill the gap between two lines.
                 x,y,
                 facecolor="Yellow",  #Color of filler
                 alpha = 0.50)        #Transperancy
plt.show()
