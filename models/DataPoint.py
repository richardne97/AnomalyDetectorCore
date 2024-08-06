from pydantic import BaseModel
import datetime

class DataPoint(BaseModel):
    timeStamp: datetime.datetime
    value: float
