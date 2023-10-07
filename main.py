import os
import time
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://<username>:<password>@cluster0.jicmnyi.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("failed connect to db.")

db = client["userdata"] # replace your database
userdb = db["data"] # replace your collection

def register(usr, pwd):
    if userdb.find_one({"username": usr}):
        return "Username already exist."
    userdb.insert_one({"username": usr, "password": pwd})
    return "Account succesfully registered."

def login(usr, pwd):
    user = userdb.find_one({"username": usr, "password": pwd})
    if user:
        print("[   INFO    ] Succesfully Login.")
    else:
        print("[   INFO    ] Login Failed.")
        time.sleep(2.0)
        main()

    

def main():
    os.system("cls")
    print("[1] login")
    print("[2] register")
    sel = input("Input => ")
    if sel == "1":
        print("Login page")
        username = input("Username : ")
        password = input("Password : ")
        r = login(username, password)
        print(r)
    elif sel == "2":
        print("Register Page")
        username = input("Username : ")
        password = input("Password : ")
        r = register(username, password)
        print(r)
    
main()
        
