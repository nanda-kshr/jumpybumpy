
from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()
cluster = MongoClient("mongodb+srv://arunrnair:rYDMASQUaegdRMpS@cluster0.kusswi6.mongodb.net/?retryWrites=true&w=majority")
db = cluster["arun"]
collection = db["jumpybumpy"]

#uvicorn main:app


@app.get("/update/{user}/{score}")
def get_user(user : str, score : int):
    update_result = collection.update_one({'user': user}, {'$set': {"score": score}})
    return "success"

@app.get("/new/{user}/{password}")
def get_user(user : str, password : str):
    for doc in collection.find({"user": user}):
        return "user exists"
    details = {
        "user":user,
        "password":password,
        "score":0
    }
    collection.insert_one(details)
    return "success"


@app.get("/login/{user}/{password}")
def get_userslist(user: str, password : str):
    for x in collection.find({},{ "_id": 0, "user": 1, "password": 1}):
        print(x)
        userr = x["user"]
        passwordd = x["password"]
        if password == passwordd:
            return "success"
        else:
            return "wrong"
    return "signup"
