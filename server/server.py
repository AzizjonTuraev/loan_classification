from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Personal Loan Prediction API!"

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


@app.route('/get_data_columns', methods=['GET'])
def get_data_columns():
    response = jsonify({
        'locations': util.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_personal_loan', methods=['POST']) # 'GET',   
def predict_personal_loan():

    data = request.get_json()
    print(request.form)  # Print the form data to debug
    try:
        age = int(data['age'])
        experience = int(data['experience'])
        income = float(data['income'])
        family = int(data['family'])
        CCAvg = float(data['CCAvg'])
        mortgage = int(data['mortgage'])
        securities_acc = int(data['securities_acc'])
        cd_acc = int(data['cd_acc'])
        online = int(data['online'])
        credit_card = int(data['credit_card'])
        zip_code = int(data['zip_code'])
        graduation_level = int(data['graduation_level'])

        response = jsonify({
            'estimated_price': util.get_estimated_score(age, experience, income, family, CCAvg, mortgage, 
                                                        securities_acc, cd_acc, online, credit_card, zip_code, 
                                                        graduation_level)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error:", e)  # Log the error
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask Server For Personal Loan Prediction...")
    util.load_saved_artifacts()
    # app.run()
    app.run(host="0.0.0.0", port=5000)
