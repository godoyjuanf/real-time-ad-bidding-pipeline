# src/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Load data

df = pd.read_csv("/Users/juanfe/Documents/Datascience/Projects/real-time-ad-bidding-pipeline/data/ads_data.csv")

# Feature engineering

# Create date time fetaures
df['timestamp'] = pd.to_datetime(df['timestamp'])

df['hour']=df['timestamp'].dt.hour
df['day_of_week']=df['timestamp'].dt.day_of_week
df['weekend']=df['day_of_week'].isin([5,6]).astype(int)

# time of day
def map_time_of_day(hour):
    if 5 <=hour < 12:
        return 'morning'
    elif 12 <=hour<17:
        return 'afternoon'
    elif 17 <= hour < 21:
        return 'evening'
    else:
        return 'night'

df['time_of_day'] =df['hour'].apply(map_time_of_day)

# Drop timestamp to avoid leakage
df =df.drop(columns=['timestamp'])

# Define target and features
X = df.drop(columns=['clicked'])
y =df[['clicked']]

# Identify column types
categorical_colums = X.select_dtypes(include='object').columns.tolist()
numeric_cols = ['hour', 'day_of_week', 'weekend']

# 3. --- Preprocessing ---
preprocessor = ColumnTransformer(
    transformers=[
        ('num',StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'),categorical_colums),
    ]
)

# 4. --- Train test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=32, stratify=y
)

# 5.--- Model pipeline ---
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=32))
    ]
)

# 6. --- Train and evaluate ---
model.fit(X_train, y_train)
y_pred= model.predict(X_test)

print("Confusion matrix")
print(confusion_matrix(y_test, y_pred))

print("n\Classification Report:")
print(classification_report(y_test, y_pred))

# 7 Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "//Users/juanfe/Documents/Datascience/Projects/real-time-ad-bidding-pipeline/models/random_forest_model.pkl")