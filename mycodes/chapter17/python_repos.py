import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储相应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) #状态码200表示成功

response_dict = r.json()         # 将API响应为json格式，转换为python字典
print("Total repositories: ",response_dict['total_count']) #GitHub包含py仓库总数

repo_dicts=response_dict["items"]    #返回的仓库字典的列表

names, stars=[],[]           #遍历每个仓库字典的名称、星级并存储
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

#可视化
"""初步
my_style=LS("#333366", base_style=LCS)
chart=pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title="Most-Starred Python Projects on GitHub"
chart.x_labels=names
chart.add("", stars)
chart.render_to_file("python_repos.svg")
"""

#定制样式
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15        #缩减长标签为15字符，鼠标悬停显示全称
my_config.show_y_guides = False      #隐去水平虚线
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos1.svg')