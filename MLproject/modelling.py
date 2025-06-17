import sys
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Membaca data yang sudah diproses
    file_path = sys.argv[3] if len(sys.argv) > 3 else "heart_preprocessing.csv"
    df = pd.read_csv(file_path)
    X = df.drop(columns=["HeartDisease"])
    y = df["HeartDisease"]

    # Split data (gunakan 80:20 split seperti preprocessing sebelumnya)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    input_example = X_train.sample(5, random_state=42)

    n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
        model.fit(X_train, y_train)

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            input_example=input_example
        )

        accuracy = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)