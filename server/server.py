from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_zip_codes', methods=['GET'])
def get_zip_codes():
    response = jsonify({
        'locations': util.get_zip_codes()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_graduation_level', methods=['GET'])
def get_graduation_level():
    response = jsonify({
        'locations': util.get_graduation_level()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_personal_loan', methods=['GET', 'POST'])
def predict_personal_loan():

    age = int(request.form['age'])
    experience = int(request.form['experience'])
    income = float(request.form['income'])
    family = int(request.form['family'])
    CCAvg = float(request.form['CCAvg'])
    mortgage = int(request.form['mortgage'])
    securities_acc = int(request.form['securities_acc'])
    cd_acc = int(request.form['cd_acc'])
    online = int(request.form['online'])
    credit_card = int(request.form['credit_card'])
    zip_code = int(request.form['zip_code'])
    graduation_level = int(request.form['graduation_level'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(age, experience, income, family, CCAvg, mortgage, 
                                                    securities_acc, cd_acc, online, credit_card, zip_code, 
                                                    graduation_level)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Personal Loan Prediction...")
    util.load_saved_artifacts()
    app.run()