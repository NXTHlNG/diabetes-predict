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

# Import Neccessary libraries

# Import Visualization libraries

# Import Model

# Import Sampler libraries

# Set the decimal format
pd.options.display.float_format = "{:.2f}".format


df = pd.read_csv("diabetes_prediction_dataset.csv")

print(df.head())

duplicate_rows_data = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_data.shape)

df = df.drop_duplicates()

print(df.isnull().sum())

df = df[df['gender'] != 'Other']

df.describe().style.format("{:.2f}")

# df.to_csv("diabetes_.csv")


def recategorize_smoking(smoking_status):
    if smoking_status in ['never', 'No Info']:
        return 'non-smoker'
    elif smoking_status == 'current':
        return 'current'
    elif smoking_status in ['ever', 'former', 'not current']:
        return 'past_smoker'


df['smoking_history'] = df['smoking_history'].apply(recategorize_smoking)


print(df['smoking_history'].value_counts())

data = df.copy()


def perform_one_hot_encoding(df, column_name):
    # Perform one-hot encoding on the specified column
    dummies = pd.get_dummies(df[column_name], prefix=column_name)

    # Drop the original column and append the new dummy columns to the dataframe
    df = pd.concat([df.drop(column_name, axis=1), dummies], axis=1)

    return df


data = perform_one_hot_encoding(data, 'gender')

data = perform_one_hot_encoding(data, 'smoking_history')



# Split data into features and target variable
X = df.drop('diabetes', axis=1)
y = df['diabetes']


# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



with open("model.joblib", "rb") as f:
    model = pickle.load(f)
    
print(model)

print(X_test.head())

y_pred = model.predict(X_test)

print("Model Accuracy: ", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Plot confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()