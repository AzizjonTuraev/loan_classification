import pickle
import json
import numpy as np
import warnings
import logging
import os
from sklearn.exceptions import DataConversionWarning
import pandas as pd
# DeprecationWarning
warnings.filterwarnings("ignore", category=DataConversionWarning)


__zip_code = None
__graduation_level = None
__data_columns = None
__model = None
__scaler = None

def get_estimated_score(age, experience, income, family, CCAvg,
                        mortgage, securities_acc, cd_acc, online,
                        credit_card, zip_code, graduation_level):
    try:
        zip_code_index = __data_columns.index(zip_code)
    except:
        zip_code_index = -1

    try:
        graduation_level_index = __data_columns.index(graduation_level)
    except:
        graduation_level_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = age
    x[1] = experience
    x[2] = income
    x[3] = family
    x[4] = CCAvg
    x[5] = mortgage
    x[6] = securities_acc
    x[7] = cd_acc
    x[8] = online
    x[9] = credit_card

    if zip_code_index>=0:
        x[zip_code_index] = 1
    if graduation_level_index>=0:
        x[graduation_level_index] = 1

    x_df = pd.DataFrame(x.reshape(-1,len(x)))

    x_df.columns = __data_columns
    input_data = __scaler.transform(x_df.values.reshape(1, -1))
    return round(__model.predict(input_data)[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __zip_code
    global __graduation_level
    global __model
    global __scaler

    logging.getLogger('tensorflow').setLevel(logging.ERROR)

    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    columns_file_path = os.path.join(current_directory, "artifacts", "columns.json")

    with open(columns_file_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __zip_code = __data_columns[10:-2]
        __graduation_level = __data_columns[-2:]


    model_file_path = os.path.join(current_directory, "artifacts", "model_xgb")

    if __model is None:
        with open(model_file_path, 'rb') as f:
            __model = pickle.load(f)

    scaler_file_path = os.path.join(current_directory, "artifacts", "standard_scaler.pkl")

    if __scaler is None:
        with open(scaler_file_path, 'rb') as f:
            __scaler = pickle.load(f)

    print("loading saved artifacts...done")

def get_zip_codes():
    return __zip_code

def get_graduation_level():
    return __graduation_level


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_zip_codes())
    # print(get_graduation_level())
    print(get_estimated_price(57,33,200,3,7.4, 0,0,1,1,1, 94132, 3))
    print(get_estimated_price(34,9,180,1,9,0,0,0,1,0, 93023, 3))
    print(get_estimated_price(40,15,173,4,6.6, 0,0,1,1,1, 92675, 3))
    print(get_estimated_price(55,23,200,3,1.0,0,1,0,0,1, 95929, 1))




