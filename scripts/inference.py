import joblib
import pandas as pd
import pickle
import sys

# 1. Load the new data
try: 
    df_new = pd.read_csv('/Users/juanfe/Documents/Datascience/Projects/real-time-ad-bidding-pipeline/data/new_ads_data.csv')
except FileNotFoundError:
    print("Error: File 'new_ads_data.csv' not found.")
    sys.exit(1)


# 2. Define required columns (used in training)
required_columns= [
    'user_id', 'device_type', 'ad_id', 'campaign_id', 'site_id',
       'ad_category', 'hour', 'day_of_week', 'weekend', 'time_of_day'
]

# 3. Fill in missing columns if necessary

numerical_cols=['hour', 'day_of_week', 'weekend', 'time_of_day']
for col in required_columns:
    if col not in df_new.columns:
        print(f"Warning: Column '{col}' missing. Filling with dummy values.")
        if col in numerical_cols:
            df_new[col] = 0
        else:
            df_new[col] = 'unknown'


# 4. Ensure column order 
df_new = df_new[required_columns]


#5. Load the trained pipeline 
with open("/Users/juanfe/Documents/Datascience/Projects/real-time-ad-bidding-pipeline/models/ad_click_pipeline.pkl", "rb") as f:
    model_pipeline = joblib.load(f)


# 6. Predict
predictions = model_pipeline.predict(df_new)
df_new['clicked_prediction'] = predictions

# 7. Save predictions

df_new.to_csv("/Users/juanfe/Documents/Datascience/Projects/real-time-ad-bidding-pipeline/data/predicted_ads.csv", index=False)
print("✅ Predictions saved to 'predicted_ads.csv'")