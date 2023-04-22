"""
This script holds the main logic to deploy a FastAPI
that allows to obtain predictions from an XGBoost
classification model that predicts if a flight will have
delays or not in a binary format (0 not delay - 1 delay)

Author: Juan Sebastian Rojas Melendez
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os
from pydantic import BaseModel
from utils.utils import load_model, process_data

# Loading environment variables
if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

# Loading path to the classification model
PATH_TO_MODEL = os.getenv('PATH_TO_MODEL')
PATH_TO_ENCODER = os.getenv('PATH_TO_ENCODER')

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
    """
    This function is an endpoint that takes an input data request of a flight, 
    loads a classification model, processes the data to obtain an encoded dataframe 
    and obtains a prediction from the model that is returned as a response from the API 
    with the prediction.
    
    Args:
      request (InputData): The input data for the prediction, which is an instance of 
      the InputData
    class.
    
    Returns:
      a Prediction that is 0 if the flight will not have delays and 1 if it has delays.
    """
    # Check if the request has all the class attributes
    if not any(hasattr(request, attr) for attr in vars(InputData)):
        # Raise an exception with code 412
        raise HTTPException(status_code=412, detail='the http request is empty or has missing data. Please review your request body')
    
    # Load the classification model
    classification_model = load_model(PATH_TO_MODEL)
    
    # Process the data to obtain the encoded df
    df_encoded = process_data(request, PATH_TO_ENCODER)

    # Obtain the prediction from the model
    result = classification_model.predict(df_encoded)
    
    # Create the Prediction object for the response
    response = Prediction(prediction=result)

    return response