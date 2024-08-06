
from fastapi import FastAPI
from models.RequestBodies import PersistAnomalyDetectorRequest
from controllers import UnSupervised

app = FastAPI(  
    title="時間序列異常偵測 APIs",
    description="提供各種機器學習之時間序列異常偵測方法，包括監督是與非監督式，並且回傳偵測結果",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "UnSupervised",
            "description": "非監督式演算法"
        }
    ])
   
#Get Product Info
@app.post("/persist", tags=["items"], summary="Persist Anomaly Detector", description="The alogrithm compares each time series value with its previous values. It is implemented with transformer DoubleRollingAggregate.")
def PersistAnomalyDetector(body: PersistAnomalyDetectorRequest):
    """
    Persist Anomaly Detector
    - **body**: The time series datapoint to be detected
    """
    return UnSupervised.Persist(body)
        
#Get Product Info
@app.post("/sst", tags=["items"], summary="Singular spectrum transfer", description="Singular spectrum transfer anomaly detector")
def PersistAnomalyDetector(body: PersistAnomalyDetectorRequest):
    """
    Singular spectrum transfer Anomaly Detector
    - **body**: The time series datapoint to be detected
    """
    return UnSupervised.SST(body)
        
#Get Product Info
@app.post("/hbos", tags=["items"], summary="Histogram-Based Outlier Score", description="Histogram-Based Outlier Score Anomaly Detector")
def PersistAnomalyDetector(body: PersistAnomalyDetectorRequest):
    """
    Histogram-Based Outlier Score Anomaly Detector
    - **body**: The time series datapoint to be detected
    """
    return UnSupervised.HBOS(body)
        
