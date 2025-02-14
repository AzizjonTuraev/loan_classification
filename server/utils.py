import pickle
import json
import numpy as np
import logging
import os
import pandas as pd

# Global variables to store loaded artifacts
__county_names = None
__graduation_level = None
__data_columns = None
__model_xgb = None
__model_lgb = None
__model_hgb = None
__scaler = None


def get_estimated_score(age : int, income : float, family : int, ccavg : float, mortgage : float, 
                        cd_acc : int, county : str, graduation_level : int,
                        ml_model_type : str):
    """
    Estimates a score based on the provided input features using a pre-trained machine learning model.

    Parameters:
        age (int): The age of the individual.
        income (float): The income of the individual.
        family (int): The family size of the individual.
        ccavg (float): The average credit card spending of the individual.
        mortgage (float): The mortgage value of the individual.
        cd_acc (int): Whether the individual has a CD account (1 for yes, 0 for no).
        county (str): The county where the individual resides.
        graduation_level (int): The education level of the individual (1 - undergraduate,
                                                                    2 - graduate, 3 - advanced/professional)
        ml_model_type (str): The type of model to use for prediction ("hgb" for Histogram-based Gradient Boosting Classification Tree, 
                                                                "lgb" for LightGBM,
                                                                "xgb" for XGBoost).
    Returns:
        int: The predicted score rounded to the nearest integer.
    """

    county = county.upper()
    if county in __county_names:
        county_index = __data_columns.index(county)
    else:
        county_index = __data_columns.index('Other')


    graduation_level_index = __data_columns.index(str(graduation_level))

    x = np.zeros(len(__data_columns))
    x[__data_columns.index("Age")] = age
    x[__data_columns.index("Income")] = income
    x[__data_columns.index("Family")] = family
    x[__data_columns.index("CCAvg")] = ccavg
    x[__data_columns.index("Mortgage")] = mortgage
    x[__data_columns.index("CD Account")] = cd_acc

    x[county_index] = 1
    x[graduation_level_index] = 1

    x_df = pd.DataFrame([x], columns=__data_columns)
    input_data = __scaler.transform(x_df)

    if ml_model_type == "hgb":
        prediction = round(__model_hgb.predict(input_data)[0])

    elif ml_model_type == "lgb":
        prediction = round(__model_lgb.predict(input_data)[0])

    elif ml_model_type == "xgb":
        prediction = round(__model_xgb.predict(input_data)[0])

    return prediction


def load_saved_artifacts():
    """
    Loads the necessary artifacts (e.g., data columns, county names, graduation levels, scaler, and models)
    required for making predictions. The artifacts are loaded from JSON and pickle files stored in the
    project directory.
    """

    print("loading saved artifacts...start")
    global __data_columns
    global __county_names
    global __graduation_level
    global __scaler

    global __model_xgb
    global __model_lgb
    global __model_hgb

    logging.getLogger('tensorflow').setLevel(logging.ERROR)


    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    project_path = os.path.dirname(current_directory)
    # columns_file_path = os.path.join(current_directory, "artifacts", "columns.json")

    # os.chdir("..")
    # project_path = os.getcwd()
    columns_file_path = os.path.join(project_path, "models", "data_prep", "columns.json")

    with open(columns_file_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __county_names = __data_columns[6:-3]
        __graduation_level = __data_columns[-3:]

    # __county_names = [county.title() for county in __county_names]

    scaler_file_path = os.path.join(project_path, "models", "data_prep", "standard_scaler.pkl")
    if __scaler is None:
        with open(scaler_file_path, 'rb') as f:
            __scaler = pickle.load(f)

    model_file_path = os.path.join(project_path, "models", "ml", "model_xgb")
    if __model_hgb is None:
        with open(model_file_path, 'rb') as f:
            __model_hgb = pickle.load(f)

    model_file_path = os.path.join(project_path, "models", "ml", "model_lgb")
    if __model_lgb is None:
        with open(model_file_path, 'rb') as f:
            __model_lgb = pickle.load(f)

    model_file_path = os.path.join(project_path, "models", "ml", "model_hgb")
    if __model_xgb is None:
        with open(model_file_path, 'rb') as f:
            __model_xgb = pickle.load(f)

    print("loading saved artifacts...done")


def get_county_names():
    """
    Returns the list of county names loaded from the columns.json file.

    Returns:
        list: A list of county names.
    """
    return __county_names


def get_graduation_level():
    """
    Returns the list of graduation levels (education levels) loaded from the columns.json file.

    Returns:
        list: A list of graduation levels.
    """
    return __graduation_level


def get_data_columns():
    """
    Returns the list of all data columns loaded from the columns.json file.

    Returns:
        list: A list of data columns.
    """
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_county_names())
    # print(get_graduation_level())
    print(get_estimated_score(age=57, income=200, family=3, ccavg=7.4, mortgage=0, cd_acc=0, county="LOS AngelES", graduation_level=3, model_type="hgb"))
    print(get_estimated_score(age=25, income=70, family=1, ccavg=1, mortgage=0, cd_acc=0, county="KERN", graduation_level=1, model_type="lgb"))
    print(get_estimated_score(age=32, income=85, family=2, ccavg=0, mortgage=20, cd_acc=1, county="butte", graduation_level=2, model_type="xgb"))




