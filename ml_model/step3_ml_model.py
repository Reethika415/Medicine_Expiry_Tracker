import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix
)

# Load dataset
df = pd.read_csv('medicine_data.csv')

print('Training ML model on real medicine data...')
print(f'Dataset size: {len(df)} records')

# Feature Encoding
le_cat = LabelEncoder()
le_mem = LabelEncoder()

df['category_enc'] = le_cat.fit_transform(df['category'])
df['member_enc'] = le_mem.fit_transform(df['member'])

# Features and target
X = df[['category_enc', 'member_enc', 'price']]
y = df['status']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f'Training samples: {len(X_train)}')
print(f'Testing samples:  {len(X_test)}')

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    max_depth=5
)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print('\n' + '='*50)
print('        ML MODEL RESULTS')
print('='*50)
print(f'Model: Random Forest Classifier')
print(f'Accuracy: {accuracy*100:.2f}%')

print('\nDetailed Classification Report:')
print(classification_report(y_test, y_pred, zero_division=0))

# Feature Importance
features = ['Category', 'Family Member', 'Price']
importance = model.feature_importances_

print('\nFeature Importance:')
for f, i in zip(features, importance):
    print(f'  {f}: {i*100:.1f}%')

# Sample Predictions (FIXED — no warnings)
print('\nSample Predictions on Real Medicines:')

sample_data = [
    ['Tablet', 'Mom', 45.0],
    ['Tablet', 'Dad', 120.0],
    ['Tablet', 'Sister', 85.0]
]

for med in sample_data:
    cat_enc = le_cat.transform([med[0]])[0]
    mem_enc = le_mem.transform([med[1]])[0]

    input_df = pd.DataFrame(
        [[cat_enc, mem_enc, med[2]]],
        columns=['category_enc', 'member_enc', 'price']
    )

    pred = model.predict(input_df)[0]

    print(f'  {med[0]} / {med[1]} / Rs.{med[2]} → {pred}')
    