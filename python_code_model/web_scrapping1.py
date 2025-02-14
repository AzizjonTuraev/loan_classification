import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://www.zipcodestogo.com/California/"


def check_for_zip_code(zip_code_str):
    try:
        return int(zip_code_str)
    except:
        return False


def web_scrap(url=url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")

    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:

            zip_code = cols[0].text.strip()
            check_status = check_for_zip_code(zip_code_str=zip_code)
            if type(check_status) == bool:
                continue

            city = cols[1].text.strip()
            county = cols[2].text.strip()
            data.append([zip_code, city, county])

    df = pd.DataFrame(data, columns=["ZIP Code", "City", "County"])
    return df


def main():

    df = web_scrap(url=url)
    os.chdir("../dataset")
    df.to_csv("zip_code.csv", index=False)
    print("Data has been saved as a zip_code.csv under dataset folder")


if __name__ == "__main__":
    main()


