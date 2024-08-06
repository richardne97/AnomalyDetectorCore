from adtk.data import validate_series
from matplotlib.pyplot import plot
import pandas as pd
import banpei
from adtk.detector import PersistAD
import models.RequestBodies as RequestModels
import simuBodyGenerator
from pyod.models.hbos import HBOS as HBOS_PyOD
import torch

def Persist(body: RequestModels.PersistAnomalyDetectorRequest):
    """
    Persist Anomaly Detector is a ensemble model
    - **body**: The time series datapoint to be detected
    """
    if body.algorithmParameters is not None:
       window = body.algorithmParameters.window
       c = body.algorithmParameters.c 
    else:
        window = 10
        c = 2.0
    
    #simulator
    #body = simuBodyGenerator.PersistBody(window=10, c=2.0)
    #c = body.algorithmParameters.c
    #window = body.algorithmParameters.window
    
    persist_ad = PersistAD(c=c, window=window, side="both")
    dates = []
    values = []
    for dataPoint in body.dataPoints:
        dates.append(dataPoint.timeStamp)
        values.append(dataPoint.value)

    time_series = pd.Series(data=values, index=dates)
    anomalies = persist_ad.fit_detect(validate_series(time_series))
    anomalyDateTimes = [item[0].to_pydatetime() for item in anomalies.items() if item[1] == True]
    return anomalyDateTimes
    

def SST(body: RequestModels.SSTAnomalyDetectorRequest):

    #simulator
    #body = simuBodyGenerator.SST(window=10)
    #window = body.algorithmParameters.window

    window = 10
    if body.algorithmParameters is not None:
        window = body.algorithmParameters.window
    
    model = banpei.SST(w=window)
    values = []
    for dataPoint in body.dataPoints:
        values.append(dataPoint.value)

    errs = model.detect(values).tolist()
    abnormalValueIndexes = [errs.index(f) for f in errs if f > 0.001]
    prevIndex = abnormalValueIndexes[0] - 1
    startIndex = abnormalValueIndexes[0] 
    sections = []
    
    for abnormalValueIndex in abnormalValueIndexes:
        if abnormalValueIndex != prevIndex + 1 or abnormalValueIndex == abnormalValueIndexes[-1]:
            sections.append( { "start": body.dataPoints[startIndex].timeStamp, "end": body.dataPoints[prevIndex].timeStamp } )
            startIndex = abnormalValueIndex
        prevIndex = abnormalValueIndex

    return sections

def HBOS(body: RequestModels.HBOSAnomalyDetectorRequest):
    
    #simulator
    body = simuBodyGenerator.HOBS(bins='auto')
   
    values = []
    for dataPoint in body.dataPoints:
        values.append(dataPoint.value)

    tvalues = torch.as_tensor(values)
    clf = HBOS_PyOD(n_bins=body.bins)
    clf.fit(tvalues.reshape(-1,1))
    # get the prediction label and outlier scores of the training data
    results = clf.labels_.tolist()  # binary labels (0: inliers, 1: outliers)
    return [body.dataPoints[results.index(r)].timeStamp for r in results if r == 1]
