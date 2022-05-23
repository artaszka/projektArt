from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    # return {"message": "Hello World, matrix has you"}
    return {"start": "1970-01-01"}