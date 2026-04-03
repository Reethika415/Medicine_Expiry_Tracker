import pandas as pd
import numpy as np
from datetime import date, timedelta
import random

# ── Step 1: Load Real Kaggle Dataset ──
print('Loading real Kaggle dataset...')
df = pd.read_csv('medicine_real_data.csv')
print(f'Total medicines in dataset: {len(df)}')
print(f'Columns: {df.columns.tolist()}')

# ── Step 2: Select Useful Columns ──
df = df[['name', 'type', 'manufacturer_name', 'price(₹)']].copy()

df.columns = ['name', 'category', 'manufacturer', 'price']

# ── Step 3: Clean the Data ──
df = df.dropna(subset=['name'])

df['category'] = df['category'].fillna('Tablet')
df['category'] = df['category'].str.strip().str.title()

valid_cats = ['Tablet', 'Syrup', 'Injection',
              'Drops', 'Ointment', 'Capsule',
              'Cream', 'Gel', 'Powder']

df['category'] = df['category'].apply(
    lambda x: x if x in valid_cats else 'Tablet'
)

df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(50.0)

# ── Step 4: Add Expiry Simulation ──
random.seed(42)
today = date.today()

def simulate_expiry(category):
    if category in ['Injection', 'Drops']:
        weights = [0.3, 0.3, 0.4]
    elif category in ['Syrup', 'Cream', 'Gel']:
        weights = [0.2, 0.2, 0.6]
    else:
        weights = [0.15, 0.15, 0.7]

    choice = random.choices(['expired', 'soon', 'safe'], weights=weights)[0]

    if choice == 'expired':
        days = random.randint(-90, -1)
    elif choice == 'soon':
        days = random.randint(1, 30)
    else:
        days = random.randint(31, 730)

    expiry = today + timedelta(days=days)
    return expiry, days

expiry_dates = []
days_list = []

for cat in df['category']:
    e, d = simulate_expiry(cat)
    expiry_dates.append(e)
    days_list.append(d)

df['expiry_date'] = expiry_dates
df['days_to_expiry'] = days_list

# ── Step 5: Add Status Column ──
def get_status(days):
    if days < 0:
        return 'Expired'
    elif days <= 30:
        return 'Expiring Soon'
    else:
        return 'Safe'

df['status'] = df['days_to_expiry'].apply(get_status)

# ── Step 6: Add Family Members ──
members = ['Self', 'Mom', 'Dad', 'Sister', 'Brother']
df['member'] = [random.choice(members) for _ in range(len(df))]

# ── Step 7: Sample 200 Records ──
df_sample = df.sample(200, random_state=42).reset_index(drop=True)

# ── Step 8: Save Processed Dataset ──
df_sample.to_csv('medicine_data.csv', index=False)

print('\nDataset processed successfully!')
print(f'Records saved: {len(df_sample)}')

print('\nStatus Distribution:')
print(df_sample['status'].value_counts())

print('\nCategory Distribution:')
print(df_sample['category'].value_counts())

print('\nSample medicine names:')
print(df_sample['name'].head(10).tolist())