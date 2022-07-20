import json
import re

print("welcome to my login signup page")
user=input("do you  what to \n.signup\n.)login:")
if user =="signup":
    username=input("enter your username")
    print("create a strong password use specail characters")
    password1=input("enter a password")
    if re.search("[a-z A-Z]",password1) and re.search("[@%$#!]",password1) and re.search("[0-9]",password1):
        password2=input("enter your password agian")
        if password1==password2:
            print("confirm password")
            date_of_birth=input("enter your date of birth")
            Mo=int(input("enter your mo number"))
            email=input("enter your email id")
            print("Regtration susscsfull")
            a=[{"username":username,"password":password1,"password":password2,"date_of_birth":date_of_birth,"Mo":Mo,"email":email},]
            b=open("date signup.json","a")
            json.dump(a,b,indent=4)
        else:
            print("password not matching")
    else:
        print("weak password please use specail charcters")
else:
    if user=="login":
        username=input("enter your username")
        password=input("enter your password")
        if ["username"]==username and ["password"]==password:
            # with open("data signup.json","r") as file:
            #     json.load(file)
            print("login successful")
        else:
            print(("wrong username"))
    else:
        print("wrong id")
        









