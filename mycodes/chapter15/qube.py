import matplotlib.pyplot as plt

x=list(range(1,6))
y=[v**3 for v in x]

plt.scatter(x,y,s=50)  #s设置散点大小
plt.title("Qube", fontsize=20)
plt.xlabel("Value")
plt.ylabel("Qube of Value")
plt.show()

x=list(range(5001))
y=[v**3 for v in x]

plt.scatter(x,y,s=20, c=y, cmap=plt.cm.Blues)  #s设置散点大小,c，cmap颜色映射
plt.title("Qube", fontsize=10)
plt.xlabel("Value")
plt.ylabel("Qube of Value")
plt.axis([0, 5100, 0, 5100**3]) #设置坐标轴范围

plt.show()