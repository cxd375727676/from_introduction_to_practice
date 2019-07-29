#根据json文件绘制世界地图反映2010年每个国家的人口数量
from pygal_maps_world.maps import World
import json
from country_codes import get_country_code

#加载数据
with open("population_data.json") as f:
    pop_data=json.load(f)  #pop_data中的每个单元是含4键的字典

#创建一个字典，键是两位国别码，值是相应人口
cc_populations={}
for pop_dict in pop_data:
    #只取2010年的数据
    if pop_dict["Year"]=="2010":
        country=pop_dict["Country Name"]
        code=get_country_code(country)
        if code:
            population=int(float(pop_dict["Value"]))      #数值转换
            cc_populations[code]=population

"""
这样只有印度和中国颜色较深，其他国家区别不大
wm=World()
wm.title="World Population in 2010, by Country"
wm.add("2010",cc_populations)
wm.render_to_file("world_population.svg")
"""
#依据人口数量对国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3={}, {}, {}
for cc, pop in cc_populations.items():
    if pop<10000000:
        cc_pops_1[cc]=pop
    elif pop<1000000000:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop

print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
wm=World()
wm.title="World Population in 2010, by Country"
wm.add("0-10Million",cc_pops_1)
wm.add("10M-1Billion",cc_pops_2)
wm.add(">1Billion",cc_pops_3)
wm.render_to_file("world_group_population.svg")