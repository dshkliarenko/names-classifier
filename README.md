# Name classification API
## Description

Application for classification of names in various languages

## Setup
```
pip install -r requirements.txt
```
## Train the model
```
python scripts/train.py
```
This will save the weights file in the current directory. Training takes a few mins on CPU.
## Run inference via CLI
Example of ruunning the script:
```
python scripts/predict.py Quang
```
Output will look like so
```
(-0.02) Vietnamese
(-4.66) Chinese
(-5.43) Korean
```

## Run API locally
```
uvicorn scripts.api:app --host HOST --port PORT
```

## Deployment
### Set up minikube
Start cluster
```
minikube start
```
Configure to use minikube's docker-daemon 
```
eval $(minikube -p minikube docker-env)
```
### Build image
```
docker build -f Dockerfile -t classifier .
```

### Install app

```
helm install release1 classifier
```

## Send request to API
Get top `N` most likely labels for the given `name` (default N = 5), and the scores associated with each label.
If `N` is too big (bigger than number of available labels), the response will contain all available labels.
```
curl -X GET http://{minikube_ip}:nodePort/{name}?n=N
```
