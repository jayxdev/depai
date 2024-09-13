import joblib
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('dependency_conflicts.csv')

# Prepare features and labels
X = data[['dependency', 'conflict']]
y = data['resolution']

# Combine dependency and conflict into a single feature
X['combined'] = X['dependency'] + ' ' + X['conflict']

# Split the dataset
_, X_test, _, y_test = train_test_split(X['combined'], y, test_size=0.2, random_state=42)

# Load the model
model = joblib.load('dependency_resolver_model.pkl')

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")