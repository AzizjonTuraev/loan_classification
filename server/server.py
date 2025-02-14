from flask import Flask, request, jsonify
import utils
from data_checks import reformat_data_type

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Personal Loan Prediction API!"


@app.route('/get_county_names', methods=['GET'])
def get_county_names():
    response = jsonify({
        'locations': utils.get_county_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_graduation_level', methods=['GET'])
def get_graduation_level():
    response = jsonify({
        'locations': utils.get_graduation_level()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_data_columns', methods=['GET'])
def get_data_columns():
    response = jsonify({
        'locations': utils.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_personal_loan_hgb', methods=['POST'])  # 'GET', 
def predict_personal_loan_hgb():

    data = request.get_json()
    print(request.form)  # Print the form data to debug
    try:
        age, income, family, ccavg, mortgage, cd_acc, county, graduation_level = reformat_data_type(data)
        response = jsonify({
            'estimated_price': utils.get_estimated_score(age, income, family, ccavg, mortgage, 
                                                        cd_acc, county, graduation_level, 
                                                        ml_model_type="hgb")  
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error:", e)  # Log the error
        return jsonify({'error': str(e)}), 400
    

@app.route('/predict_personal_loan_lgb', methods=['POST'])
def predict_personal_loan_lgb():

    data = request.get_json()
    print(request.form)
    try:
        age, income, family, ccavg, mortgage, cd_acc, county, graduation_level = reformat_data_type(data)
        response = jsonify({
            'estimated_price': utils.get_estimated_score(age, income, family, ccavg, mortgage, 
                                                        cd_acc, county, graduation_level, 
                                                        ml_model_type="lgb")  
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 400


@app.route('/predict_personal_loan_xgb', methods=['POST'])
def predict_personal_loan_xgb():

    data = request.get_json()
    print(request.form)
    try:
        age, income, family, ccavg, mortgage, cd_acc, county, graduation_level = reformat_data_type(data)
        response = jsonify({
            'estimated_price': utils.get_estimated_score(age, income, family, ccavg, mortgage, 
                                                        cd_acc, county, graduation_level, 
                                                        ml_model_type="xgb")  
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    print("Starting Python Flask Server For Personal Loan Prediction...")
    utils.load_saved_artifacts()
    # app.run()
    app.run(host="0.0.0.0", port=5000)




