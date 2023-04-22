"""
This script holds all the needed functions that enables
the API to load the classification model and process and
encode the data.

Author: Juan Sebastian Rojas Melendez
"""

import joblib
import pandas as pd

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
    """
    This function converts a request object into a pandas DataFrame.
    
    Args:
      request: This is data in JSON format in a specific that comes from
      a HTTP POST request.

    Returns:
      a pandas DataFrame.
    """
    # Converting the request into a dictionary
    data = request.dict()

    # Creating a pandas DF from that dictionary
    df = pd.DataFrame(data, index=[0])
    
    return df

def encode_data(df, path_to_encoder):
    """
    The function encodes a given dataframe using a pre-trained 
    encoder and returns the encoded dataframe.
    
    Args:
      df: A pandas dataframe containing the data to be encoded.
      path_to_encoder: The path to the file where the encoder object 
      is saved. This file should have been created during the training process 
      and contains the trained encoder object.
    
    Returns:
      the encoded dataframe after applying binary encoding to it.
    """
    # Load the encoder from the training process
    encoder = joblib.load(path_to_encoder)

    # Converting column names to uppercase as the encoder expects
    df.columns = df.columns.str.upper()

    # Removing underscores from column names
    df.columns = df.columns.str.replace('_', '')

    # Applying binary encoding to the dataframe
    df_encoded = encoder.transform(df)

    return df_encoded

def process_data(request, path_to_encoder):
    """
    The function processes data by converting a request into a 
    pandas dataframe and encoding it using a binary encoder.
    
    Args:
      request: The input data that needs to be processed and encoded.
      path_to_encoder: The path to the file containing the trained 
      encoder model that will be used to encode the data.
    
    Returns:
      the encoded pandas dataframe obtained by processing the input request 
      using the specified path to the encoder.
    """
    # Sending the request to be transformed into
    # a pandas dataframe
    df = convert_to_df(request)
    # Encoding the data with the Binary Encoder
    df_encoded = encode_data(df, path_to_encoder)

    return df_encoded


