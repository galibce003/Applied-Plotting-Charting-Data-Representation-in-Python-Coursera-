from matplotlib import pyplot as plt

zip_zenerator = zip([1,4,5,6],[4,7,4,1])
x,y=zip(*zip_zenerator)  #Split zip_zenerator into 2 lists

plt.scatter(x[:2],y[:2],s= 100 ,c="Red", label="Two")
plt.scatter(x[2:],y[2:],s= 50 ,c="Blue", label="Four")

#Different Elements of Plotting
plt.xlabel("X-xis")
plt.ylabel("Y-xis")
plt.title("Scatterplot")
plt.legend()
plt.show()



