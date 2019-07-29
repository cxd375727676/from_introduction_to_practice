#8-1
def display_message():
    print("I'm learning writing functions.")
display_message()

#8-2
def  favorite_book(title):
    print("One of my favorite book is " + title.title() +".")
favorite_book("python")

#8-3
def make_shirt(size,character):
    print("The shirt's size is '" +size +"' with character '"  + character+"'.")
make_shirt("M","Love")

#8-4
def make_shirt1(size="L",character="I love Python"):
    print("The shirt's size is '" +size +"' with character '"  + character+"'.")
make_shirt1()
make_shirt1("M")
make_shirt1(character="Love")

#8-5
def describe_city(city,country="China"):
    print(city+ " is in " + country +".")
describe_city("Beijing")
describe_city("Shanghai")
describe_city("New York","America")

#8-6
def city_country(city,country):
    s=city + ", " +country
    return s
print(city_country("Beijing","China"))
print(city_country("Shanghai","China"))
print(city_country("New York","America"))

#8-7
def make_album(name,zhuanji):
    dict={"name":name ,"zhuanji":zhuanji}
    return dict
dic1=make_album("Jielun","niu zai hen mang")
dic2=make_album("JJ","di er tian tang")
print(dic1)
print(dic2)

def make_album1(name,zhuanji,num=""):
    dic={"name":name,"zhuanji":zhuanji}
    if num:
        dic["number"]=num
    return dic
dic1=make_album1("Jielun","niu zai hen mang")
dic2=make_album1("JJ","di er tian tang")
dic3=make_album1("cyx","shi nian",2)
print(dic1)
print(dic2)
print(dic3)
#8-8
def make_album(name,zhuanji):
    dict={"name":name ,"zhuanji":zhuanji}
    return dict

print("Please input singer and zhuan ji(You can stop by inputting 'q').")
while True:
    name=input("Please enter the name: ")
    if name=="q":
        break
    zhuanji=input("Please enter the zhuanji: ")
    if zhuanji=="q":
        break
    dic=make_album(name,zhuanji)
    print(dic)

#8-9
def show_magicians(namelist):
    for name in namelist:
        print(name)

magicians_name=["mag1","mag3","mag2"]
show_magicians(magicians_name)

#8-10
def make_great(namelist):
    for i in range(len(namelist)):
        namelist[i]="the Great "+namelist[i]
    return namelist

def show_magicians(namelist):
    for name in namelist:
        print(name)
        
magicians_name=["mag1","mag3","mag2"]
make_great(magicians_name)
show_magicians(magicians_name)

#8-11
def make_great(namelist):
    for i in range(len(namelist)):
        namelist[i]="the Great "+namelist[i]
    return namelist

def show_magicians(namelist):
    for name in namelist:
        print(name)

magicians_name=["mag1","mag3","mag2"]
#传递副本
makegreat_name=make_great(magicians_name[:])
#修改名单
show_magicians(makegreat_name)
#原始名单
show_magicians(magicians_name)

#8-12
def sandwich(*adds):
    print("\nYour sandwich is mixed with:")
    for add in adds:
        print("\t"+add)

sandwich("cong")
sandwich("jiangyou","cu","jiang")

#8-13
def build_profile(first, last, **user_info):
    """创建一个字典， 其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile

my_profile=build_profile('Chen','Xiaodong',location='China')
print(my_profile)

#8-14
def make_car(producer,style,**info):
    car_d={}
    car_d["producer"]=producer
    car_d["style"]=style
    for k,v in info.items():
        car_d[k]=v
    return car_d

car=make_car("subaru","outback",color="blue",tow_package=True)
print(car)

#8-15\8-16\8-17