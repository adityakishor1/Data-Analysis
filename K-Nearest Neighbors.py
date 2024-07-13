from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the dataset
dataset = pd.read_csv("Iris.csv")

# Extract features and target variable
X = dataset.iloc[:, :-1].values  # Assuming the last column is the target variable
y = dataset.iloc[:, -1].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

# Initialize and train the classifier
classifier = KNeighborsClassifier(n_neighbors=8, p=3, metric='euclidean')
classifier.fit(X_train, y_train)

# Predict the test results
y_pred = classifier.predict(X_test)

# Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('Confusion matrix is as follows\n', cm)

# Print accuracy metrics
print('Accuracy Metrics') 
print(classification_report(y_test, y_pred)) 
print("Correct predictions:", accuracy_score(y_test, y_pred)) 
print("Wrong predictions:", 1 - accuracy_score(y_test, y_pred))
