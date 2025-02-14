import pandas as pd
import os


def reformat_data_type(data):
    age = int(data['age'])
    income = float(data['income'])
    family = int(data['family'])
    ccavg = float(data['ccavg'])
    mortgage = int(data['mortgage'])
    cd_acc = int(data['cd_acc'])
    county = str(data['county'])
    graduation_level = int(data['graduation_level'])

    check_age(age)
    check_income(income)
    check_family(family)
    check_ccavg(ccavg)
    check_mortgage(mortgage)
    check_cd_acc(cd_acc)
    check_county(county)
    check_graduation_level(graduation_level)
    return age, income, family, ccavg, mortgage, cd_acc, county, graduation_level


def check_age(age):
    if type(age) != int:
        raise Exception("Age must be an integer")
    if age < 18:
        raise Exception("Age must be minimum 18")


def check_income(income):
    if type(income) not in [int, float]:
        raise Exception("Income must be either integer or float and must be in thousands. For example, if income 50.000$ then enter 50")
    if income < 0:
        raise Exception("Income must be greater than 0")
    if income > 1000:
        raise Exception("Income must be less and denoted in thousand. For example, if income 50.000$ then enter 50")


def check_family(family):
    if type(family) != int:
        raise Exception("Family must be an integer")
    if family<=0:
        raise Exception("Family must be greater than 0. At least 1 for singles")
    if family>20:
        raise Exception("Please double check your input to Family")


def check_ccavg(ccavg):
    if type(ccavg) not in [int, float]:
        raise Exception("ccavg must be either integer or float and must be in thousands. For example, if income 6.000$ then enter 6")
    if ccavg < 0:
        raise Exception("ccavg can not be negative")


def check_mortgage(mortgage):
    if type(mortgage) not in [int, float]:
        raise Exception("mortgage must be either integer or float and must be in thousands. For example 50.000, then enter 50")
    if mortgage < 0:
        raise Exception("mortgage can not be negative")
    

def check_cd_acc(cd_acc):
    if cd_acc not in [0, 1]:
        raise Exception("cd_acc must be an integer. it shows if the customer have a certificate of deposit with the bank? (1=Yes, 0=No)")


def check_county(county_name):

    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    project_path = os.path.dirname(current_directory)
    zip_code_path = os.path.join(project_path, "dataset", "zip_code.csv")

    zip_codes = pd.read_csv(zip_code_path)
    CA_counties = list(set(zip_codes["County"]))
    CA_counties = [i.lower() for i in CA_counties]

    if county_name.lower() in CA_counties:
         return True
    else:
         raise Exception(f"Check for the correct Califoria County name you entered: {county_name}")

def check_graduation_level(graduation_level):
    if graduation_level not in [1, 2, 3]:
        raise Exception("graduation_level must be an integer. it shows the customer's  (1) undergraduate, (2) graduate, (3) advanced/professional")

