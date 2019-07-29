#7-1
car=input("Which car do you want to rent: ")
print("Let me see if I can find you a " + car +".")

#7-2
size=input("Please tell me how many of you have a dinner: ")
size=int(size)
if size>8:
    print("Sorry, no fit table.")
else:
    print("There is free table.")

#7-3
number=input("Please input a number: ")
number=int(number)
if number%10==0:
    print("It's 10's times.")
else:
    print("It isn't 10's times.")

#7-4\7-6
#active出口
prompt="Please input pei liao(Input 'quit' to end the program): "
active=True
while active:
    pl=input(prompt)
    if pl=="quit":
        active=False
    else:
        print("We'll add "+ pl +".")
#while条件测试出口
prompt="Please input pei liao(Input 'quit' to end the program): "
pl=""
while pl!="quit":
    pl=input(prompt)
    if pl!="quit":
        print("We'll add "+ pl +".")
#break出口
prompt="Please input pei liao(Input 'quit' to end the program): "
while True:
    pl=input(prompt)
    if pl=="quit":
        break
    else:
        print("We'll add "+ pl +".")
#7-5\7-6
#break出口
prompt="Please input your age(Input 'quit' to end): "
while True:
    age=input(prompt)
    if age=="quit":
        break
    else:
        age=int(age)
        if age<3:
            price="free"
        elif age<=12:
            price="10 dollars"
        else:
            price="15 dollars"
        print(price)
#while条件测试出口
prompt="Please input your age(Input 'quit' to end): "
age=""
while age!="quit":
    age=input(prompt)
    if age!="quit":
        age=int(age)
        if age<3:
            price="free"
        elif age<=12:
            price="10 dollars"
        else:
            price="15 dollars"
        print(price)
#active出口
prompt="Please input your age(Input 'quit' to end): "
active=True
while active:
    age=input(prompt)
    if age=="quit":
        active=False
    else:
        age=int(age)
        if age<3:
            price="free"
        elif age<=12:
            price="10 dollars"
        else:
            price="15 dollars"
        print(price)

#7-7 Ctrl+C退出循环  
        
#7-8
sandwich_orders=["a-sandwich","b-sandwich","c-sandwich"]
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("I made your " +sandwich +".")
    finished_sandwiches.append(sandwich)
print("---All sandwiches have been finished:---")
for sandwich in finished_sandwiches:
    print("\t"+sandwich)
 
#7-9
sandwich_orders1=["c-sandwich","b-sandwich","c-sandwich",
                  "pastrami","pastrami","pastrami"]
finished_sandwiches1=[]
print("Sorry,Pastrami has been sold out!")
while "pastrami" in sandwich_orders1:
    sandwich_orders1.remove("pastrami")
print(sandwich_orders1)

#7-10
poll={}
active=True
while active:
    name=input("Input your name: ")
    place=input("If you could visit one place in the world, where would you go? ")
    poll[name]=place
    response=input("Continue?(yes/no): ")
    if response=="no":
        active=False

print("\n---All poll results as follows---")
for n,p in poll.items():
    print(n.title()+ " dreams of visiting " + p.title() + ".")












    