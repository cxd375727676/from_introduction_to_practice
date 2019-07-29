#创建地图显示三个北美国家（加拿大、美国、墨西哥）的人口数量
from pygal_maps_world.maps import World
wm = World()
wm.title = "Populations of Countries in North America"
wm.add("North America", {"ca":34126000, "us":309349000, "mx":113423000})
wm.render_to_file("na_populations.svg")