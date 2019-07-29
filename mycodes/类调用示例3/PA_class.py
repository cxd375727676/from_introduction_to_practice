#注意调入父类
from U_class import User

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