from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides
    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)

# 创建两个D8实例
die_1 = Die(8)
die_2 = Die(8)
# 掷几次骰子， 并将点数之和存储在一个列表中
results = []
while len(results)<1000:
    result=die_1.roll()+die_2.roll()
    results.append(result)

# 分析结果，频数统计
frequencies = []
max=die_1.num_sides+die_2.num_sides
for value in range(2, max+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
import pygal
hist = pygal.Bar()
hist.title = "Plus results of rolling two D8 1000 times."
hist.x_labels = [str(v) for v in list(range(2,max+1))]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D8+D8", frequencies)
hist.render_to_file("d8+d8.svg")