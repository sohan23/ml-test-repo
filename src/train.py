import numpy as np
from sklearn.datasets import load_iris
from model import preprocess_data, train_model, evaluate_model

def main():
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target

    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(X, y)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Model accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
