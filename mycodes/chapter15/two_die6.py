from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides
    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)

# 创建两个D6实例
die_1 = Die()
die_2 = Die()
# 掷几次骰子， 并将点数之积存储在一个列表中
results = []
while len(results)<1000:
    result=die_1.roll()*die_2.roll()
    results.append(result)

#乘积的所有不重复结果从小到大排列
mul=[]   
for i in list(range(1,die_1.num_sides+1)):
    for j in list(range(1,die_2.num_sides+1)):
        mul.append(i*j)
mul=list(set(mul))
mul.sort()    

# 分析结果，频数统计
frequencies = []
for value in mul:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
import pygal
hist = pygal.Bar()
hist.title = "Multiplicative results of rolling two D6 1000 times."
hist.x_labels = mul
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6*D6", frequencies)
hist.render_to_file("d6chengd6.svg")