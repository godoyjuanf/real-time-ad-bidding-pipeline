import pandas as pd
import random
import numpy as np

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

n_samples = 10

data = {
    'user_id': [f"user_{i}" for i in range(n_samples)],
    'ad_id': [f"ad_{random.randint(1, 5)}" for _ in range(n_samples)],
    'campaign_id': [f"cmp_{random.randint(1, 3)}" for _ in range(n_samples)],
    'site_id': [f"site_{random.randint(1, 3)}" for _ in range(n_samples)],
    'device_type': [random.choice(['mobile', 'desktop', 'tablet']) for _ in range(n_samples)],
    'ad_category': [random.choice(['sports', 'tech', 'fashion']) for _ in range(n_samples)],
    'time_of_day': [random.choice(['morning', 'afternoon', 'evening', 'night']) for _ in range(n_samples)],
    'day_of_week': [random.randint(0, 6) for _ in range(n_samples)],
    'weekend': [random.randint(0, 1) for _ in range(n_samples)],
    'hour': [random.randint(0, 23) for _ in range(n_samples)]

}

df_new = pd.DataFrame(data)
df_new.to_csv("/Users/juanfe/Documents/Datascience/Projects/real-time-ad-bidding-pipeline/data/new_ads_data.csv", index=False)

print("✅ Sample new_ads_data.csv generated.")