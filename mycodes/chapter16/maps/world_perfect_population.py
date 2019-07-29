#根据json文件绘制世界地图反映2010年每个国家的人口数量

from pygal_maps_world.maps import World #世界地图模块
import json
import pygal
from pygal.style import RotateStyle    #设定pygal样式（如基色）模块
from country_codes import get_country_code   #获取国别码
from pygal.style import LightColorizedStyle  #加亮颜色

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


#依据人口数量将cc_population拆分成三个字典
cc_pops_1, cc_pops_2, cc_pops_3={}, {}, {}
for cc, pop in cc_populations.items():
    if pop<10000000:
        cc_pops_1[cc]=pop
    elif pop<1000000000:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop
"""
仅导入RotateStyle可以指定颜色，比如如下指定淡蓝色基色，但是颜色太暗
wm_style = RotateStyle('#336699')    

仅导入LightColorizedStyle可以加亮颜色，但是无法指定颜色
wm_style = LightColorizedStyle
"""
#为此利用 RotateStyle和LightColorizedStyle
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm=World(style=wm_style)
wm.title="World Population in 2010, by Country"
wm.add("0-10Million",cc_pops_1)
wm.add("10M-1Billion",cc_pops_2)
wm.add(">1Billion",cc_pops_3)
wm.render_to_file("world_perfect_population.svg")