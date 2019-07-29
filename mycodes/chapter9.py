#9-1/9-2
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+
              " and it's cuisine type is "+self.cuisine_type+".")
    def open_restaurant(self):
        print("The restaurant is open now.")
        
restaurant=Restaurant("chuan cai","shao")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

rest2=Restaurant("KFC","zha")
rest2.describe_restaurant()

#9-3
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print("\n"+self.first_name.title()+" "+self.last_name +
              "'s age is " + str(self.age) + ".")
    def greet_user(self):
        print("Hello, "+self.first_name.title()+" "+self.last_name + "!")

user1=User("chen","xiaodong",25)
user1.describe_user()
user1.greet_user()
user2=User("chen","xiaoyu",25)
user2.describe_user()
user2.greet_user()

#9-4
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def describe_number(self):
        print(str(self.number_served)+" people have gone here to eat.")

canguan=Restaurant("hehe","chao")
canguan.describe_number()

#直接修改属性
canguan.number_served=2
canguan.describe_number()

#通过增加一个方法set_number_served()来修改属性
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_number(self):
        print(str(self.number_served)+" people have gone here to eat.")
    
    def set_number_served(self,number):
        self.number_served=number

canguan=Restaurant("hehe","chao")
canguan.set_number_served(10)
canguan.describe_number()

#递增人数
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_number(self):
        print(str(self.number_served)+" people have gone here to eat.")
    
    def increment_number_served(self,number):
        self.number_served=self.number_served+number
canguan=Restaurant("hehe","chao")
canguan.increment_number_served(10)
canguan.increment_number_served(3)
canguan.increment_number_served(11)
canguan.describe_number()

#9-5
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0
    
    def increment_login_attempts(self):
        self.login_attempts+=1
        
    def reset_login_attempts(self):
        self.login_attempts=0

oneuser=User("chen","xiaodong",25)
oneuser.increment_login_attempts()
oneuser.increment_login_attempts()
oneuser.increment_login_attempts()
print(oneuser.login_attempts)
oneuser.reset_login_attempts()
print(oneuser.login_attempts)

#9-6
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+
              " and it's cuisine type is "+self.cuisine_type+".")
    def open_restaurant(self):
        print("The restaurant is open now.")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    
    def describe_flavors(self):
        print("The icecream has flavors: ")
        for flavor in self.flavors:
            print("\t"+flavor)

fla=["suan","tian","ku","la"]
icecreamstand=IceCreamStand("cxd","ice",flavors)

icecreamstand.describe_restaurant()
icecreamstand.open_restaurant()
icecreamstand.describe_flavors()

#9-7
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print("\n"+self.first_name.title()+" "+self.last_name +
              "'s age is " + str(self.age) + ".")
    def greet_user(self):
        print("Hello, "+self.first_name.title()+" "+self.last_name + "!")
        
class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=["can add post","can delete post","can ban user"]
    
    def show_privileges(self):
        print("Admin can do things: ")
        for every in self.privileges:
            print(every)
        
admin=Admin("Chen","Xiaodong",25)
admin.describe_user()
admin.greet_user()
admin.show_privileges()

#9-8
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print("\n"+self.first_name.title()+" "+self.last_name +
              "'s age is " + str(self.age) + ".")
    def greet_user(self):
        print("Hello, "+self.first_name.title()+" "+self.last_name + "!")

class Privileges():
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]
    
    def show_privileges(self):
        print("admin can do things: ")
        for every in self.privileges:
            print(every)

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=Privileges()

admin=Admin("Chen","Xiaodong",25)
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()

#9-9
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):#返回一个字符串摘要
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):#读里程
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):#输入合法里程数并更新
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):#输入里程增加值并更新
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):#输入电池容量创建battery实例，默认值70
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
 
    def get_range(self):#根据电池容量判断里程
        """打印一条消息， 指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):#检查容量，设置为85
        if self.battery_size!=85:
            self.battery_size=85

class ElectricCar(Car):
     """电动汽车的独特之处"""
     def __init__(self, make, model, year):
         super().__init__(make, model, year)
         self.battery=Battery() #Battery实例作为属性
        
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
#升级
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

#9-10\9-11\9-12
#9-13
from collections import OrderedDict
dictionary= OrderedDict()
dictionary["one"]=1
dictionary["two"]=2
dictionary["three"]=3
dictionary["four"]=4
for k,v in dictionary.items():
    print(k.title()+" is "+str(v)+".")

#9-14
from random import randint
class Die():
    """多面骰子"""
    def __init__(self,sides=6):
        self.sides=sides
    
    def roll_die(self,times) :    #掷times次
        n=1
        print("\n"+str(self.sides)+ " faces die tou " + str(times) + " times's results: ")
        while n<=times:
            print(randint(1,self.sides))
            n+=1

die1=Die()
die1.roll_die(10)
die2=Die(10)
die2.roll_die(10)
die3=Die(20)
die3.roll_die(10)

#9-15了解标准库