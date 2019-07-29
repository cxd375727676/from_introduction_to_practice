#10-1
with open("python_learning.txt") as file:
    context=file.read()
    print(context.rstrip())
    
with open("python_learning.txt") as file:  
    for line in file:
        print(line.rstrip())
        
with open("python_learning.txt") as file: 
    lines=file.readlines()
for line in lines:
    print(line.strip())

#10-2
with open("python_learning.txt") as file:
    for line in file:
        print(line.replace("Python","C").rstrip())

#10-3
name=input("Please input your name: ")
with open("guest.txt","w") as file:
    file.write(name)

#10-4
with open("guest_book.txt","w") as file:
    while True:
        name=input("Please input your name(Enter 'q' to quit): ")
        if name=="q":
            break
        else:
            print("Hello, "+ name +" !")
            file.write(name.title() + " has visited.\n")

#10-5
with open("reasons.txt","w") as file:
    while True:
        reason=input("Why you like Python(Enter 'q' to quit): ")  
        if reason=="q":
            break
        else:
            file.write(reason+"\n")

#10-6
a=input("\nEnter first number: ") #input函数以字符串形式读入
try:
    a=int(a)
except ValueError:
    print("Sorry ,what you enter is not a number!")
else:
    b=input("Enter second number: ")
    try:
        b=int(b)
    except ValueError:
        print("Sorry ,what you enter is not a number!")
    else:
        print(a+b)

#10-7
while True:
    a=input("\nEnter first number(enter 'q' to quit): ")
    if a=="q":
        break
    try:
        a=int(a)
    except ValueError:
        print("Sorry ,what you just enter is not a number!")
        continue
    else:
        b=input("Enter second number(enter 'q' to quit): ")
        if b=="q":
            break
        try:
            b=int(b)
        except ValueError:
            print("Sorry ,what you just enter is not a number!")
            continue
        else:
            print(a+b)

#10-8
filenames=["cats.txt","dogs.txt"]
for filename in filenames:
    try:
        with open(filename) as file:
            contents=file.read()
    except FileNotFoundError:
        print("The file '" + filename +"' not exsist.")
    else:
        print(contents)
        
#10-9
filenames=["cats.txt","dogs.txt"]
for filename in filenames:
    try:
        with open(filename) as file:
            contents=file.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
        
#10-10
filenames=["Pride and Prejudice.txt"]
for filename in filenames:
    try:
        with open(filename) as file:
            contents=file.read()
    except FileNotFoundError:
        print("The file '" + filename +"' not exsist.")
    else:
        counts=contents.lower().count("the")
        print("Word 'the' appears " + str(counts) + " in file " + filename +".")
        
#10-11
import json
favnum=input("Please input your favorite number: ")
filename="favorite_number.json"
with open(filename,"w") as file:
    json.dump(favnum,file)    
with open(filename) as file:
    getnum=json.load(file)
print("I know your favorite number! It's " + getnum +".")
        
#10-12
import json
filename="favorite_number.json"
try:
    with open(filename) as file:
        get_number=json.load(file)  
except FileNotFoundError:
    fav_num=input("Please input your favorite number: ")
    print("I will remember the number when you come back.")
    with open(filename,"w") as file:
        json.dump(fav_num,file)    
else:
    print("I know your favorite number! It's " + getnum +".")       
        
#10-13
import json
def get_stored_username():
    """如果存储了用户名， 就获取它,并返回加载的用户名；否则返回None"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username       
        
def get_new_username():
    """提示新用户输入用户名并返回该用户名，同时将其写入json文件"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username       

def greet_user():
    """问候用户， 并指出其名字"""
    username = get_stored_username()
    if username:
        answer=input("Is your name " + username + " ?(Y/N)" )
        if answer=="Y":
            print("Welcome back, " + username + "!")
        else:
            username=get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")      

greet_user()