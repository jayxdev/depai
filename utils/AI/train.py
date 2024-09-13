import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv('dependency_conflicts.csv')

# Prepare features and labels
X = data[['dependency', 'conflict']]
y = data['resolution']

# Combine dependency and conflict into a single feature
X['combined'] = X['dependency'] + ' ' + X['conflict']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X['combined'], y, test_size=0.2, random_state=42)

# Create a pipeline with CountVectorizer and DecisionTreeClassifier
pipeline = Pipeline([
	('vectorizer', CountVectorizer()),
	('classifier', DecisionTreeClassifier())
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, 'dependency_resolver_model.pkl')