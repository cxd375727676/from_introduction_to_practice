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