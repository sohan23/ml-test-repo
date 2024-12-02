import pytest
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from model import preprocess_data, train_model, evaluate_model

@pytest.fixture
def data():
    data = load_iris()
    X, y = data.data, data.target
    return X, y

def test_preprocess_data(data):
    X, y = data
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    assert X_train.shape[0] == y_train.shape[0]
    assert X_test.shape[0] == y_test.shape[0]
    assert X_train.shape[1] == X_test.shape[1]

def test_train_model(data):
    X, y = data
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    model = train_model(X_train, y_train)
    assert isinstance(model, LogisticRegression)
    assert model.coef_.shape[0] == len(np.unique(y))

def test_evaluate_model(data):
    X, y = data
    X_train, X_test, y_train, y_test = preprocess_data(X, y)
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    assert 0 <= accuracy <= 1
