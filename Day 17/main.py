class User:
    def __init__(self,id,username): #special method and has special function--initialize an attribute
        self.id=id
        self.user_name=username
        self.followers=0
        self.following=0

    def follow(self,user): # always self parameter. Nows the object that calls it
        user.followers+=1
        self.following+=1

user_1=User(1,"Red")
user_2=User(2,"angela")

user_1.follow(user_2)

print(user_2.followers)