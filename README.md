# Predicting Personal Loan Approval with Machine Learning 

This is  a classification task where the goal is to classify the Universal banks ' personal loan offers is accepted by customers.

The dataset comes from Kaggle [this link](https://www.kaggle.com/datasets/sriharipramod/bank-loan-classification/data)

The dataset contains the following features:
- ID : unique identifier
- Personal Loan : did the customer accept the personal load offered (1=Yes, 0=No)
- Age : customer’s age
- Experience : number of years of profession experience
- Income : annual income of the customer ($000)
- Zip code: home address zip code
- Family : family size of customer
- CCAvg : average spending on credit cards per month ($000)
- Education: education level (1) undergraduate, (2) graduate, (3) advanced/professional
- Mortgage : value of house mortgage ($000)
- Securities : does the customer have a securities account with the bank? (1=Yes, 0=No)
- CDAccount : does the customer have a certificate of deposit with the bank? (1=Yes, 0=No)
- Online : does the customer use Internet banking facilities (1=Yes, 0=No)
- CreditCard : does the customer use a credit card issued by Universal Bank? (1=Yes, 0=No)

On this project I did feature engineering: data cleaning, scaling, PCA analysis  and more.
After this, I applied bunch of ML models to classify  whether the customers will take out a loan or not. Models used:
- Logistic
- Decision Tree
- Random Forest
- Support Vector Classifier
- Bernoulli Naive Bayes Classifier
- K-Nearest Neighbours Classifier
- Ada Boost Classifier
- Gradient Boost Classifier
- Hist Gradient Boost Classifier
- XGB Classifier
- XGBRF Classifier
- Cat Boost Classifier
- ANN

I also used K-fold Cross Validation to get more robust results rather than just getting lucky from train test split.
I used GridSearchCV to find out which parameters give the best results for each classifier. The I trained the final model with the 
best parameter.

At the end, I saved the final model and put it into the deployment server using Python Flask API
