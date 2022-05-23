from fastapi import FastAPI, status, HTTPException, Request

import datetime
from pydantic import BaseModel



app = FastAPI()
app.events_list = []

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


class EventRequest(BaseModel):
    date: str
    event: str


class EventResponse(BaseModel):
    id: int
    date: str
    name: str
    date_added: str


@app.put("/events", response_model=EventResponse)
def put_events(request: EventRequest):
    rq = request.dict()
    id = len(app.events_list)
    date = rq.get("date", None)
    try:
        datetime.date.fromisoformat(date)
    except ValueError as e:
        print("ERROR:", e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    event = rq.get("event", None)
    date_added = datetime.date.today()
    response = EventResponse(id=id, date=date, name=event, date_added=str(date_added))
    app.events_list.append(response)
    return response


@app.get("/events/{date}")
def get_events(date: str):
    try:
        datetime.date.fromisoformat(date)
    except ValueError as e:
        print("ERROR:", e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    date_events = [event for event in app.events_list if event.date == date]
    if len(date_events) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return date_events
