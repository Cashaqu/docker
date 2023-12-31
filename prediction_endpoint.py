from fastapi import FastAPI
import torch
from pydantic import BaseModel
import contextlib
from ceasar.RNN import RNN
from ceasar.prediction_func import prediction


class PredictionInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    text: str

class RNN_model:
    def __init__(self):
        self.model = None

    def load_model(self):
        model_file = "trained_model/best_model_ceasar.pt"
        model = RNN()
        model.load_state_dict(torch.load(model_file, map_location=torch.device('cpu')))
        model.eval()
        self.model = model #.to(device)

    def predict(self, input: PredictionInput) -> PredictionOutput:
        if not self.model:
            raise RuntimeError("Model files are not found!")
        text = prediction(input.text, model=self.model)
        return PredictionOutput(text=text)


ceasar_model = RNN_model()


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    ceasar_model.load_model()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/prediction", response_model=PredictionOutput)
async def get_prediction(input: PredictionInput):
    output = ceasar_model.predict(input)
    return output