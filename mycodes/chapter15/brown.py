from random import choice

def get_step():
        """该函数获取一次随机漫步的位移"""
        return choice([-1,1]) *  choice([0,1,2,3,4]) 

class RandomWalk():
    """定义数据随机漫步类"""
    
    def __init__(self, num_points=500):
        """默认运动499次"""
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0] 
    
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_step=get_step()
            y_step=get_step()
            
            if x_step==0 and y_step==0:
                continue
            
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

            
import matplotlib.pyplot as plt

while True:
    rw=RandomWalk()
    rw.fill_walk()
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(0,0,c="green", s=60)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c="red",s=60)
    

    plt.show()
    
    answer=input("Continue?(Y/N)")
    if answer=="N":
        break