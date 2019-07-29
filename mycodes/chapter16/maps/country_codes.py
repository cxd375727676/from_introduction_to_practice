#COUNTRIES是一个字典，键、值存储两个字母的国别码和国家名
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据国家名返回两位国别码，如果国家名不在COUNTRIES中，返回None"""
    for code, name in COUNTRIES.items():
        if name==country_name:
            return code
    return None 