import sys
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def main(n_estimators=400, max_depth=10, dataset="heart_preprocessing.csv"):
    # Inisiasi tracking URI dan eksperimen MLflow
    mlflow.set_tracking_uri("http://127.0.0.1:5000/")
    mlflow.set_experiment("heart-disease-classification")

    # Membaca data yang sudah diproses
    df = pd.read_csv(dataset)
    X = df.drop(columns=["HeartDisease"])
    y = df["HeartDisease"]

    # Split data (gunakan 80:20 split seperti preprocessing sebelumnya)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    input_example = X_train.sample(5, random_state=42)

    with mlflow.start_run():
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("random_state", 42)

        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)

        accuracy = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            input_example=input_example
        )

if __name__ == "__main__":
    # Usage: python modelling.py <n_estimators> <max_depth> <dataset>
    n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    dataset = sys.argv[3] if len(sys.argv) > 3 else "heart_preprocessing.csv"
    main(n_estimators, max_depth, dataset)