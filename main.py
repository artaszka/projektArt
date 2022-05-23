from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    # return {"message": "Hello World, matrix has you"}
    return "message => Hello World, matrix has you"