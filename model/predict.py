import pickle
import pandas as pd
with open("model/insurance_pipeline.pkl", "rb") as file:
    model = pickle.load(file)
    
MODEL_VERSION = "1.0.0"

def predict_output(input_data) ->float:
    """_summary_

    Args:
        data (dataframe): _description_

    Returns:
        float: _description_
    """
    """
    Predicts the insurance cost based on user input data.
    """
    output = model.predict(input_data)
    return output
    