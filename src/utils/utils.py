import joblib
import pandas as pd
import category_encoders as ce
from sklearn.pipeline import Pipeline

def load_model(path_to_model:str):
    """
    The function loads a saved joblib model from a specified path and returns it, or raises a
    FileNotFoundError if the file is not found.
    
    Args:
      path_to_model (str): The path to the saved joblib model file that needs to be loaded.
    
    Returns:
      The function `load_model` returns the loaded joblib model if the file exists in the provided path,
    otherwise it raises a `FileNotFoundError` with a message indicating that the file could not be found
    in the provided path.
    """
    try:
        # Load the saved joblib model
        classification_model = joblib.load(path_to_model)
        
        return classification_model
    except FileNotFoundError:
        raise FileNotFoundError(f'The model file could not be found in the provided path: {path_to_model}')
    
def convert_to_df(request):
    # Create the dataframe
    data = request.dict()
    df = pd.DataFrame(data)
    
    return df

def encode_data(df):
    # Load the encoder from the training
    encoder = ce.BinaryEncoder()

    # Apply binary encoding to the dataframe
    df_encoded = encoder.transform(df)

    return df_encoded

def process_data(request):
    df = convert_to_df(request)
    df_encoded = encode_data(df)

    return df_encoded


