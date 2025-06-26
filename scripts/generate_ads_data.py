import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta

fake = Faker()
np.random.seed(42)
random.seed(42)

# Settings
n_rows=60000
ctr_rate=0.05

device_types=['mobile','tablet','desktop']
ad_categories=['tech','fashion','sports','finance','music']
campaigns=[f'camp_{i:02}' for i in range(1,11)]
ads=[f"ad_{i:03}" for i in range(1,101)]
sites=[f"site_{i:02}" for i in range(1, 21)]

# Generate data

def generate_data(n):
    data = []
    start_time = pd.Timestamp("2025-01-01")

    for i in range(n):
        user_id = f"user_{random.randint(1, 10000)}"
        timestamp = start_time + timedelta(seconds=random.randint(0, 60 * 60 * 24 * 30))  # within 1 month
        device_type = random.choices(device_types, weights=[0.6, 0.3, 0.1])[0]
        ad_id = random.choice(ads)
        campaign_id = random.choice(campaigns)
        site_id = random.choice(sites)
        ad_category = random.choice(ad_categories)
        clicked = np.random.binomial(1, ctr_rate)

        data.append([user_id, timestamp, device_type, ad_id, campaign_id, site_id, ad_category, clicked])

    return pd.DataFrame(data, columns=[
        "user_id", "timestamp", "device_type", "ad_id", "campaign_id",
        "site_id", "ad_category", "clicked"
    ])
# Create and save
df = generate_data(n_rows)
df.to_csv("data/ads_data.csv", index=False)
print(f"✅ Generated {n_rows} rows and saved to data/ads_data.csv")