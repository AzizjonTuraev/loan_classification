# Predicting Loan Offer Acceptance with Machine Learning

This project focuses on a **classification task** to predict whether customers of Universal Bank will accept a personal loan offer. The goal is to classify customers into two categories:  
- **1 (Yes)**: The customer accepts the loan offer.  
- **0 (No)**: The customer does not accept the loan offer.

---

## Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/sriharipramod/bank-loan-classification/data). It contains the following features:

| Feature         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **ID**          | Unique identifier for each customer.                                        |
| **Personal Loan** | Target variable: Did the customer accept the personal loan? (1=Yes, 0=No). |
| **Age**         | Customer’s age.                                                            |
| **Experience**  | Number of years of professional experience.                                |
| **Income**      | Annual income of the customer ($000).                                      |
| **Zip Code**    | Home address zip code.                                                     |
| **Family**      | Family size of the customer.                                               |
| **CCAvg**       | Average monthly spending on credit cards ($000).                           |
| **Education**   | Education level: 1=Undergraduate, 2=Graduate, 3=Advanced/Professional.     |
| **Mortgage**    | Value of the house mortgage ($000).                                        |
| **Securities**  | Does the customer have a securities account with the bank? (1=Yes, 0=No).  |
| **CD Account**  | Does the customer have a certificate of deposit with the bank? (1=Yes, 0=No). |
| **Online**      | Does the customer use Internet banking facilities? (1=Yes, 0=No).          |
| **CreditCard**  | Does the customer use a credit card issued by Universal Bank? (1=Yes, 0=No). |

---

## Project Workflow

### 1. Feature Engineering

- **Data Cleaning**: Handled missing values, removed duplicates, and corrected inconsistencies.
- **Feature Scaling**: Applied standardization to normalize the data.
- **PCA Analysis**: Conducted Principal Component Analysis to reduce dimensionality and improve model performance.
- **Handling Imbalanced Data**: Addressed class imbalance using **SMOTE** and **undersampling** techniques.

### 2. Model Development

The following machine learning models were implemented and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Classifier (SVC)
- Bernoulli Naive Bayes Classifier
- K-Nearest Neighbours (KNN) Classifier
- AdaBoost Classifier
- Gradient Boosting Classifier
- Histogram-Based Gradient Boosting Classifier
- XGBoost Classifier
- XGBoost Random Forest (XGBRF) Classifier
- Artificial Neural Network (ANN)

### 3. Model Evaluation

- **K-Fold Cross-Validation**: Used to ensure robust results and avoid overfitting.
- **GridSearchCV**: Applied to find the best hyperparameters for each model.
- **Confusion Matrix**: Analyzed to evaluate model performance, focusing on maximizing **True Positives (TP)** and minimizing **False Negatives (FN)** and **False Positives (FP)**.

### 4. Model Selection

Based on evaluation metrics, the following models were selected for deployment:

- **XGBoost**
- **LightGBM**
- **Histogram-Based Gradient Boosting**

These models demonstrated superior performance in predicting loan acceptance while balancing precision and recall.

---

## Deployment

The final models were deployed using:

- **Flask API**: Three endpoints were created for predictions:
  1. `predict_personal_loan_hgb` (Histogram-Based Gradient Boosting)
  2. `predict_personal_loan_lgb` (LightGBM)
  3. `predict_personal_loan_xgb` (XGBoost)
- **Docker**: Containerized the application for easy deployment and portability across environments.

---

## Presenation

I prepared a short presentation (Report_presentation.pptx) summarizing the task overview, methodology, and results.


## How to Use

### 1. Build and Run the Docker Container

```bash
docker build -t loan_classification:latest -f Dockerfile .
docker run -p 5000:5000 loan_classification:latest
```

### 2. Test the API
Use Postman or any API testing tool to send requests to the endpoints. Below is an example of the required JSON input:

```json
{
  "age": 27,
  "income": 180,
  "family": 1,
  "ccavg": 6.2,
  "mortgage": 0,
  "cd_acc": 1,
  "county": "Los Angeles",
  "graduation_level": 3
}
```



