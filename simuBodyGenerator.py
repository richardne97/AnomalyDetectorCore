from models.DataPoint import DataPoint
import models
import datetime
import math

import models.RequestBodies
    
def PersistBody(window: int, c: float):
    
    bodydict = {
         "algorithmParameters": {
            "c": c,
            "window": window
        },
        "dataPoints": []
    }
    
    startDt = datetime.datetime(2024,7,8,0,0,0)
    for x in range(0,1000):
        
        cunDt = startDt + datetime.timedelta(minutes=10*x)
        cunValue = math.sin(x/90)
        if x == 500:
            cunValue = cunValue + 0.5
        dataPoint = DataPoint(timeStamp = cunDt, value = cunValue)
        bodydict['dataPoints'].append(dataPoint)

    return models.RequestBodies.PersistAnomalyDetectorRequest.model_validate(bodydict)

def SST(window: int):
    
    bodydict = {
         "algorithmParameters": {
            "window": window
        },
        "dataPoints": []
    }
    
    startDt = datetime.datetime(2024,7,8,0,0,0)
    for x in range(0,1000):
        
        cunDt = startDt + datetime.timedelta(minutes=10*x)
        cunValue = math.sin(x/90)
        if x == 500:
            cunValue = cunValue + 0.5
        dataPoint = DataPoint(timeStamp = cunDt, value = cunValue)
        bodydict['dataPoints'].append(dataPoint)

    return models.RequestBodies.SSTAnomalyDetectorRequest.model_validate(bodydict)

def HOBS(bins):
    
    bodydict = {
         "algorithmParameters": {
             "bins": bins
        },
        "dataPoints": []
    }
    
    startDt = datetime.datetime(2024,7,8,0,0,0)
    for x in range(0,1000):
        
        cunDt = startDt + datetime.timedelta(minutes=10*x)
        cunValue = math.sin(x/90)
        if x == 500:
            cunValue = cunValue + 50
        dataPoint = DataPoint(timeStamp = cunDt, value = cunValue)
        bodydict['dataPoints'].append(dataPoint)

    return models.RequestBodies.HBOSAnomalyDetectorRequest.model_validate(bodydict)