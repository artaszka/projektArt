# Do not put any other code or imports here
from fastapi import FastAPI, Response, status, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from datetime import datetime, timedelta
from time import strptime

app = FastAPI()

class HerokuApp:
#     app_url = "http://0.0.0.0:5000"
    app_url = "https://arturp.herokuapp.com/"  # Fill your heroku app url here


@app.get("/start", response_class=HTMLResponse)
def zadanie3_1():
    return """
        <html>
            <head>
                <title>HTML Title</title>
            </head>
            <body>
                <h1>The unix epoch started at 1970-01-01</h1>
            </body>
        </html>
    """



#
# @app.get("/")
# def zadanie1_1():
#     return {"start": "1970-01-01"}
#
# @app.get("/method", status_code=200)
# def zadanie1_2():
#     return {"method": "GET"}
#
# @app.post("/method", status_code=201)
# def zadanie1_2():
#     return {"method": "POST"}
#
# @app.put("/method", status_code=200)
# def zadanie1_2():
#     return {"method": "PUT"}
#
# @app.options("/method", status_code=200)
# def zadanie1_2():
#     return {"method": "OPTIONS"}
#
# @app.delete("/method", status_code=200)
# def zadanie1_2():
#     return {"method": "DELETE"}
#
#
# days = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
#
#
# @app.get("/day")
# def get_day(name: str = "", number: int = 0):
#     if name in days and days[name] == number:
#         return status.HTTP_200_OK
#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
#
#
# class EventRequest(BaseModel):
#     date: str
#     event: str
#
#
# class EventResponse(BaseModel):
#     id: int
#     date: str
#     name: str
#     date_added: str
#
#
# @app.put("/events", response_model=EventResponse)
# def put_events(request: EventRequest):
#     rq = request.dict()
#     id = len(app.events_list)
#     date = rq.get("date", None)
#     try:
#         datetime.date.fromisoformat(date)
#     except ValueError as e:
#         print("ERROR:", e)
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
#     event = rq.get("event", None)
#     date_added = datetime.date.today()
#     response = EventResponse(id=id, date=date, name=event, date_added=str(date_added))
#     app.events_list.append(response)
#     return response


# @app.get("/events/{date}")
# def get_events(date: str):
#     try:
#         datetime.date.fromisoformat(date)
#     except ValueError as e:
#         print("ERROR:", e)
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
#     date_events = [event for event in app.events_list if event.date == date]
#     if len(date_events) == 0:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return date_events
