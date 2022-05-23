from fastapi import FastAPI, status, HTTPException, Request

import datetime

app = FastAPI()


@app.get("/")
def zadanie1_1():
    return {"start": "1970-01-01"}

@app.get("/method", status_code=200)
def zadanie1_2():
    return {"method": "GET"}

@app.post("/method", status_code=201)
def zadanie1_2():
    return {"method": "POST"}

@app.put("/method", status_code=200)
def zadanie1_2():
    return {"method": "PUT"}

@app.options("/method", status_code=200)
def zadanie1_2():
    return {"method": "OPTIONS"}

@app.delete("/method", status_code=200)
def zadanie1_2():
    return {"method": "DELETE"}


days = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}


@app.get("/day")
def get_day(name: str = "", number: int = 0):
    if name in days and days[name] == number:
        return status.HTTP_200_OK
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
