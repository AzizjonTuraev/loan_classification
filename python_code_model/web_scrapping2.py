import requests
import pdfplumber
import pandas as pd

import web_scrapping1

url = "https://qualitycountsca.net/wp-content/uploads/2018/04/california-zip-codes.pdf"
save_path = "../dataset/california_zip_codes.pdf"


def save_pdf(url=url):

    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"PDF saved successfully at {save_path}")


def read_pdf(pdf_path):
    text_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_data.extend(text.split("\n"))
    return text_data


def check_for_zip_code(zip_code_str):
    try:
        return int(zip_code_str)
    except:
        return False


def extract_city_county_names(parts, counties_names):

    success = False
    n = 2

    while not success:
        county = " ".join(parts[n:])
        if county in counties_names:
            city = " ".join(parts[1:n])
            success = True
        else:
            n+=1

    return city, county


def extract_data_from_text(text_lines, counties_names):
    data = []
    for line in text_lines:
        parts = line.split()
        if len(parts) >= 3:
            zip_code = parts[0]

            check_status = check_for_zip_code(zip_code_str=zip_code)
            if type(check_status) == bool:
                continue

            city, county = extract_city_county_names(parts, counties_names)
            data.append([zip_code, city, county])

    return pd.DataFrame(data, columns=["ZIP Code", "City", "County"])


def get_county_names(file_path):
    df = pd.read_csv(file_path)
    return list(set(df["County"]))


def main():

    web_scrapping1.main()
    counties_names = get_county_names("../dataset/zip_code.csv")

    save_pdf(url=url)
    pdf_text = read_pdf(pdf_path=save_path)
    df = extract_data_from_text(pdf_text, counties_names)

    # df.to_csv("../dataset/california_zip_codes.csv", index=False)
    df.to_json("../dataset/california_zip_codes.json", orient="records", indent=4)
    print("Process finished: Zip codes have been saved successfully as a JSON file!")


if __name__ == "__main__":
    main()




