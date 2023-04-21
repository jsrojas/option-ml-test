from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.utils import load_model, process_data
import os
#import my_model  # Import your machine learning model

# Loading environment variables
if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

# Loading path to the classification model
PATH_TO_MODEL = os.getenv('PATH_TO_MODEL')

# Creating the API
app = FastAPI()

# Defining the input data format
class InputData(BaseModel):
    opera: str
    mes: int
    tipo_vuelo: str
    sigla_des: str
    dia_nom: str


# Defining the prediction format
class Prediction(BaseModel):
    prediction: float

# Defining the prediction endpoint
@app.post("/predict", response_model=Prediction)
def predict(request: InputData):
    # Check if the request has all the class attributes
    if not any(hasattr(request, attr) for attr in vars(InputData)):
        # Raise an exception with code 412
        raise HTTPException(status_code=412, detail='the http request is empty or has missing data. Please review your request body')
    
    # Load the classification model
    #classification_model = load_model(PATH_TO_MODEL)
    
    # TODO aqui va la función de procesamiento de datos
    df_encoded = process_data(request)

    # TODO aqui va la función de predicción
    #result = classification_model.predict(df_encoded)
    result = 1
    response = Prediction(prediction=result)

    #return JSONResponse(content={'prediction':1})
    return response