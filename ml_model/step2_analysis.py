import pandas as pd

# Load processed real dataset
df = pd.read_csv('medicine_data.csv')

print('=' * 55)
print('  MEDICINE DATA ANALYSIS — REAL KAGGLE DATASET')
print('=' * 55)

# Analysis 1: Status Summary
print('\n1. Overall Medicine Status:')
status = df['status'].value_counts()
print(status)
print(f'   Total medicines analyzed: {len(df)}')

# Analysis 2: Category-wise expiry
print('\n2. Expired Medicines by Category:')
expired = df[df['status'] == 'Expired']
print(expired['category'].value_counts())

# Analysis 3: Most affected family member
print('\n3. Medicines per Family Member:')
print(df['member'].value_counts())

# Analysis 4: Average price by status
print('\n4. Average Medicine Price by Status:')
print(df.groupby('status')['price']
        .mean().round(2))

# Analysis 5: Category with shortest average shelf life
print('\n5. Average Days to Expiry by Category:')
avg_days = df.groupby('category')['days_to_expiry']\
             .mean().round(1).sort_values()
print(avg_days)

# Analysis 6: Most common medicine names
print('\n6. Top 10 Most Common Medicines:')
print(df['name'].value_counts().head(10))

# Analysis 7: Manufacturer with most medicines
print('\n7. Top 5 Manufacturers:')
if 'manufacturer' in df.columns:
    print(df['manufacturer'].value_counts().head(5))

print('\nAnalysis Complete!')
print('Copy this output into your project report!')
