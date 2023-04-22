"""
This script holds all the needed functions that enables
the API to load the classification model and process and
encode the data.

Author: Juan Sebastian Rojas Melendez
"""

import joblib
import pandas as pd
    
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

def encode_data(df, encoder):
  """
  The function encodes a given dataframe using a specified encoder and converting column names to
  uppercase and removing underscores from column names.

  Args:
    df: The input dataframe that needs to be encoded.
    encoder: The "encoder" parameter is an instance of a binary encoder object that has been
  previously initialized with specific encoding parameters. This object is used to transform the input
  dataframe into a binary encoded format.

  Returns:
    the encoded dataframe after applying binary encoding to it.
  """
    # Converting column names to uppercase as the encoder expects
  df.columns = df.columns.str.upper()

  # Removing underscores from column names
  df.columns = df.columns.str.replace('_', '')

  # Applying binary encoding to the dataframe
  df_encoded = encoder.transform(df)

  return df_encoded

def process_data(request, encoder):
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
    df_encoded = encode_data(df, encoder)

    return df_encoded


