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