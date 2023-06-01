import pandas as pd
import numpy as np
from imblearn.pipeline import Pipeline as imbPipeline
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import pickle
warnings.filterwarnings('ignore')

pd.options.display.float_format = "{:.2f}".format


def perform_one_hot_encoding(df, column_name):
    # Perform one-hot encoding on the specified column
    dummies = pd.get_dummies(df[column_name], prefix=column_name)

    # Drop the original column and append the new dummy columns to the dataframe
    df = pd.concat([df.drop(column_name, axis=1), dummies], axis=1)

    return df


def predict(age, gender, hypertension, heart_disease, smoking_history, HbA1c_level, blood_glucose_level, bmi):
    input = dict(
        gender=gender,
        age=age,
        hypertension=hypertension,
        heart_disease=heart_disease,
        smoking_history=smoking_history,
        bmi=bmi,
        HbA1c_level=HbA1c_level,
        blood_glucose_level=blood_glucose_level,
    )

    df = pd.DataFrame(input, index=[0])

    data = df.copy()

    data = perform_one_hot_encoding(data, 'gender')

    data = perform_one_hot_encoding(data, 'smoking_history')

    with open("model.joblib", "rb") as f:
        model = pickle.load(f)

    print(model)

    print(df.head())

    y_pred = model.predict(df)

    return y_pred[0]
