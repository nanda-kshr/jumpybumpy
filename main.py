from fastapi import FastAPI

app = FastAPI()

#uvicorn main:app




pir = 0

@app.get("/pir/{i}")
def pir(i : int):
    global pir
    pir = i
    return "success"

@app.get("/pir")
def piri():
    return pir

lpg = 0
@app.get("/lpg/{i}")
def lpgs(i : int):
    global lpg
    lpg = i
    return "success"

@app.get("/lpg")
def lppg():
    return lpg

us = 0;
@app.get("/us/{i}")
def uss(i : int):
    global us
    us = i
    return "success"

@app.get("/us")
def llfa():
    return us

motor1 = 0
@app.get("/motor1/{i}")
def dfff(i : int):
    global motor1
    motor1 = i
    return "success"

@app.get("/mototr1")
def fiojasfgio():
    return motor1
motor2 = 0
@app.get("/motor2/{i}")
def apsdgs(i : int):
    global motor2
    motor2 = i
    return "success"

@app.get("/motor2")
def faesfse():
    return motor2
s1 = 0
s2 = 0
s3 = 0
s4 = 0
@app.get("/s1/{i}")
def fsfas(i : int):
    global s1
    s1 = i
    return "success"

@app.get("/s1")
def fsewfas():
    return s1

@app.get("/s2/{i}")
def afasfs(i : int):
    global s2
    s2 = i
    return "success"

@app.get("/s2")
def faff():
    return s2

@app.get("/s3/{i}")
def asdf(i : int):
    global s3
    s3 = i
    return "success"

@app.get("/s3")
def egfs():
    return s3

@app.get("/s4/{i}")
def asdf(i : int):
    global s4
    s4 = i
    return "success"

@app.get("/s4")
def egfs():
    return s4
