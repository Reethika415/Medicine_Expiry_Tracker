import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv('medicine_data.csv')

# Create charts folder
os.makedirs('charts', exist_ok=True)

print('Generating charts...')

# ── Chart 1: Status Pie Chart ──
plt.figure(figsize=(6,6))
df['status'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Medicine Status Distribution')
plt.ylabel('')
plt.savefig('charts/chart1_status_pie.png')
plt.close()
print('Chart 1 saved')

# ── Chart 2: Category Bar Chart ──
plt.figure(figsize=(8,5))
df['category'].value_counts().plot(kind='bar')
plt.title('Medicines by Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=30)
plt.savefig('charts/chart2_category_bar.png')
plt.close()
print('Chart 2 saved')

# ── Chart 3: Family Member Bar Chart ──
plt.figure(figsize=(8,5))
df['member'].value_counts().plot(kind='barh')
plt.title('Medicines per Family Member')
plt.xlabel('Count')
plt.ylabel('Member')
plt.savefig('charts/chart3_member_bar.png')
plt.close()
print('Chart 3 saved')

# ── Chart 4: Status by Category ──
pivot = df.groupby(['category', 'status']).size().unstack(fill_value=0)

pivot.plot(kind='bar', stacked=True)
plt.title('Status by Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=30)
plt.savefig('charts/chart4_status_by_category.png')
plt.close()
print('Chart 4 saved')

print('\nAll charts generated successfully!')