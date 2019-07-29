#16-5
import json
from country_codes import get_country_code

#COUNTRIES是一个字典，键、值存储两个字母的国别码和国家名
from pygal_maps_world.i18n import COUNTRIES

with open("population_data.json") as f:
    pop_data=json.load(f)  #pop_data中的每个单元是含4键的字典

includecountries,uninclude=[],[]
for pop_dict in pop_data:
    if pop_dict["Year"]=="2010":
        country=pop_dict["Country Name"]
        if get_country_code(country):
            includecountries.append(country)
        else:
            uninclude.append(country)
            
identycountries=COUNTRIES.values() #pygal有编码的国家名

#没有包含进来，json文件可能遗漏的国家
posible_omitcountries=[]
for country in identycountries:
    if country not in includecountries:
        posible_omitcountries.append(country)
"""
试着寻找剩下的
print(posible_omitcountries)         

for name in uninclude:
    if "egypt" in name.lower():
        print("\n"+name)
"""        
#最终添加国家：
omitcountries_1=['Bolivia, Plurinational State of', 'Congo, the Democratic Republic of the',
               'Congo', 'Egypt','Gambia', 'Hong Kong', 'Iran, Islamic Republic of', 
              "Korea, Democratic People's Republic of", 'Korea, Republic of', 
              "Lao People's Democratic Republic", 'Moldova, Republic of', 
              'Macedonia, the former Yugoslav Republic of', 'Macao','Tanzania, United Republic of',
              'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Yemen']
omitcountries_2=["Bolivia",'Congo, Dem. Rep.' , 'Congo, Rep.' ,'Egypt, Arab Rep.',
                'Gambia, The' , 'Hong Kong SAR, China' , 'Iran, Islamic Rep.' , 
                'Korea, Dem. Rep.' ,'Korea, Rep.' ,'Lao PDR', 'Moldova','Macedonia, FYR',
                'Macao SAR, China', 'Tanzania','Venezuela, RB','Vietnam','Yemen, Rep.']

code=[]#遗漏国家的代码
for name in omitcountries_1:
    code.append(get_country_code(name))

omitcountry_dict={}#遗漏国家名称及人口数
for pop_dict in pop_data:
    if pop_dict["Year"]=="2010" and pop_dict["Country Name"] in omitcountries_2:
        name=pop_dict["Country Name"]
        popu=int(float(pop_dict["Value"]))
        omitcountry_dict[name]=popu
print(omitcountry_dict)        