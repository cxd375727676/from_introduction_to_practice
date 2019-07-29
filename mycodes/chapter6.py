#6-1
information={"first_name":"Chen","last_name":"Xiaoyu","age":25,"city":"USA"}
print(information["first_name"])
print(information["last_name"])
print(information["age"])
print(information["city"])

#6-2
favdigit={"q":1,"w":2,"e":3,"r":4}
print(favdigit)

#6-3/6-4
dictionary={"one":1,"two":2,"three":3,"four":4}
print("one two three four mean that:\n\t"+
      str(dictionary["one"])+" "+str(dictionary["two"])+" "+
      str(dictionary["three"])+" "+str(dictionary["four"]))
for k,v in dictionary.items():
    print(k.title()+" is "+str(v)+".")

#6-5
river_city={"nile":"egypt","amazon":"brazil","changjiang":"china"}
for k,v in river_city.items():
    print("The "+k.title()+" runs through "+v.title()+".")
for k in river_city.keys():
    print(k)
for v in river_city.values():
    print(v)

#6-6
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
names=["jim","erin","jen"]

for name in names:
    if name in favorite_languages.keys():
        print(name.title()+", thank you for taking the poll.")
    else:
        print(name.title()+", you're invited to take the poll.")

#6-7
people={"people1":{"name":"jimmy","age":25,"country":"china"},
        "people2":{"name":"fancy","age":20,"country":"france"}
       }
for everyone,info in people.items():
    name=info["name"].title()
    age=str(info["age"])
    country=info["country"].title()
    print(everyone.title()+"'s name is "+name+",whose age is "+
          age+", lives in "+country+".")

#6-8
wangxingren={"style":"dog","owner":"xiaoming"}
miaoxingren={"style":"cat","owner":"xiaopang"}
pets=[wangxingren,miaoxingren]
for pet in pets:
    print(pet["owner"].title()+" has a "+pet["style"]+".")

#6-9
favorite_places={"lxc":["iceberg","sweden"],
                 "cxd":["china"],
                 "cxy":["france","england"]
                 }
for name,places in favorite_places.items():
    print("\n"+name.title()+"'s favorite places are:")
    for place in places:
        print("\t"+place.title())

#6-10
favdigit={"q":[1,2],"w":[3,4],"e":[5,6],"r":[7,8]}
for people, digits in favdigit.items():
    print("\n"+people.title()+"'s favorite digits are:")
    for digit in digits:
        print("\t"+str(digit))

#6-11
cities={"New York":{"country":"America",
                    "population":20}
        ,
        "London":{"country":"England",
                  "population":7.5}
        }
for city,info in cities.items():
    country=info["country"]
    population=str(info["population"])
    print(city+" is in "+country+", of "+population+" billion population.")

#6-12,改进favorite_languages.py
favorite_languages = {
"jen": ["python", "ruby"],
"sarah": ["c"],
"edward": ["ruby", "go"],
"phil": ["python", "haskell"]
}
for name, languages in favorite_languages.items():
    if len(languages)==1:
        print("\n"+name.title()+"'s favorite language is " + 
              languages[0].title()+".")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())