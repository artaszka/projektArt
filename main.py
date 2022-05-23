from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def zadanie1():
    return {"start": "1970-01-01"}

@app.get("/method", status_code=200)
def zadanie2():
    return {"method": "GET"}