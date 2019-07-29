#5-1
car="subaru"
print("Is car=='subaru'? I predict True.")
print(car=="subaru")
print("\nIs car=='audi'? I predict False.")
print(car=="audi")

#5-2
a1="Audi"
a2="audi"
a1==a2
a1.lower()==a2
3>1 and 4>3
3>1 or  3>4
cxdlist=["c","x","d"]
print("x" in cxdlist)
print("y" not in cxdlist)

#5-3
alien_color="green"
if alien_color=="green":
    print("player gets five points.")
alien_color="red"
if alien_color=="green":
    print("player gets five points.")

#5-4
alien_color="green"
if alien_color=="green":
    print("player gets five points.")
else:
    print("player gets ten points.")    

alien_color="red"
if alien_color=="green":
    print("player gets five points.")
else:
    print("player gets ten points.")

#5-5
#alien_color="green"
#alien_color="yellow"
#alien_color="red"
if alien_color=="green":
    print("player gets five points.")
elif alien_color=="yellow":
    print("player gets ten poingts.")
else:
    print("player gets 15 points.")

#5-6
age=25

if age<2:
    print("infant")
elif age<4:
    print("pan shan xue bu.")
elif age<13:
    print("child")
elif age<20:
    print("teenager")
elif age<65:
    print("adult")
elif age>=65:
    print("old")

#5-7
favorite_fruits=["apple","orange","banana"]
if "apple" in favorite_fruits:
    print("I really like apple!")
if "pear" in favorite_fruits:
    print("I really like pear!")

#5-8
yhm=["admin","q","w","e","r"]
for each in yhm:
    if each=="admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+each+", thank you for logging in again.")

#5-9
yhm=[]
if yhm:
    for each in yhm:
        if each=="admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+each+", thank you for logging in again.")
else:
    print("We need to find some users!")

#5-10
current_users=["xiaoming","xiaohong","xiaoqiang","xiaopang","xiaodong"]
new_users=["Xiaodong","xiaogang","xiaojun","xiaoyu","xiaoming"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, "+new_user+" has been used and you need have another name.")
    else:
        print("Congratulations, "+new_user+" isn't used.")

#5-11
numlist=list(range(1,9+1))
for value in numlist:
    if value==1:
        print("1st")
    elif value==2:
        print("2nd")
    elif value==3:
        print("3rd")
    else:
        print(str(value)+"th")

#5-12\5-13