docker build -t anomalydetectorcore .
docker login iot.senslink.net:5000
docker tag anomalydetectorcore:latest iot.senslink.net:5000/wra/anomalydetectorcore:latest
docker push iot.senslink.net:5000/wra/anomalydetectorcore:latest

