#4-1
food=["beef","duck","pig"]
for meat in food:
    print(meat)
for meat in food:
    print("I like "+meat+".")
print("I really like the food.")

#4-2
animals=["dog","cat","snake"]
for animal in animals:
    print(animal)
for animal in animals:
    print("A "+animal+" would make a great pet.")
print("Any of these animals would make a great pet!")

#4-3
for value in range(1,21):
    print(value)

#4-4  ctrl+C终止输出
for value in range(1,1000001):
    print(value)

#4-5
numlist=list(range(1,1000000+1))
print("min is "+str(min(numlist))+" and max is "+str(max(numlist))+".")
print(sum(numlist)) 

#4-6
for value in range(1,20,2):
    print(value)
    
#4-7
for value in range(3,31,3):
    print(value)

#4-8
sq3=[]
for value in range(1,10+1):
    sq3.append(value**3)
print(sq3)
for value in sq3:
    print(value)
    
#4-9
sq3_2=[value**3 for value in range(1,10+1)]
print(sq3_2)

#4-10
print("The first three items in the sq3 list are:")
for value in sq3[:3]:
    print(value)   
print("Three items fromthe middle of the list are:")
for value in sq3[3:6]:
    print(value)
print("The last three items in the list are:")
for value in sq3[7:]:
    print(value)

#4-11
my_pizzas=["piz1","piz2","piz3"]
friend_pizzas=my_pizzas[:]
my_pizzas.append("piz4")
friend_pizzas.append("piz5")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
    
#4-12
    
#4-13
simpfood=("egg","vegtable","rice","noodles","dumplings")
for food in simpfood:
    print(food)
simpfood[0]="nuts"#不允许更改
simpfood=("egg","nuts","rice","beef","dumplings")
for food in simpfood:
    print(food)

#4-14\4-15