from models.DataPoint import DataPoint
from typing import List
from pydantic import BaseModel
from typing import Optional

class TimeSeriesDataBase(BaseModel):
    algorithmParameters: dict
    dataPoints: List[DataPoint]

class PersistAnomalyDetectorRequest(TimeSeriesDataBase):
    
    class PersistAnomalyDetectorParameters(BaseModel):
        c: float
        window: int
    
    algorithmParameters: Optional[PersistAnomalyDetectorParameters] = None
    
class SSTAnomalyDetectorRequest(TimeSeriesDataBase):
    
    class SSTAnomalyDetectorParameters(BaseModel):
        window: int
    
    algorithmParameters: Optional[SSTAnomalyDetectorParameters] = None
    
class HBOSAnomalyDetectorRequest(TimeSeriesDataBase):
    
    class HBOSAnomalyDetectorParameters(BaseModel):
        bins: int
        
    algorithmParameters: Optional[HBOSAnomalyDetectorParameters] = None