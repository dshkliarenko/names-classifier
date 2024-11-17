from fastapi import FastAPI
from fastapi.params import Query

from scripts.predict import predict
from scripts.train import WEIGHTS_PATH

app = FastAPI()


@app.get("/classification/{name}")
def classification(name, n: int = Query(5, gt=0, description='Top N labels')):
        """
        Get top `n` most likely labels for the given `name`, and the scores associated with each label.
        If `n` is too big (bigger than number of available labels), the response will contain all available labels.
        """
        predictions = predict(name, n, WEIGHTS_PATH)
        return [{"score": format(prediction[0], '.2f'), "label": prediction[1]} for prediction in predictions]