from fastapi import FastAPI, status, Response

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


week = {'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday'}


@app.get("/day")
def zadanie1_3(day: str, num: int, response:Response):

    if num == week[day]:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return response.status_code
