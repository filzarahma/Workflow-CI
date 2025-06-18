# Heart Disease Prediction with CI/CD Workflow

This repository contains a machine learning workflow for heart disease prediction with continuous integration and deployment capabilities. The project uses MLflow for experiment tracking and model management, and GitHub Actions for CI/CD.

## Project Overview

This project implements a RandomForest classifier to predict heart disease using patient health data. The workflow includes:

- Data preprocessing and feature engineering
- Model training using RandomForestClassifier
- Model evaluation and metrics tracking
- Continuous integration with GitHub Actions
- Containerization with Docker

## Dataset

The dataset (`heart_preprocessing.csv`) contains preprocessed patient data with the following features:
- Age
- Sex
- ChestPainType
- RestingBP
- Cholesterol
- FastingBS
- RestingECG
- MaxHR
- ExerciseAngina
- Oldpeak
- ST_Slope
- HeartDisease (target variable)

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions workflow configuration
├── MLproject/
│   ├── conda.yaml          # Conda environment configuration
│   ├── MLproject           # MLflow project configuration
│   ├── modelling.py        # Model training script
│   └── heart_preprocessing.csv  # Preprocessed dataset
├── README.md               # This file
└── dockerhub.txt           # Docker Hub repository URL
```

## MLflow Project

The MLproject file defines the workflow for training the model. It includes:

- Environment configuration via conda.yaml
- Parameters for the Random Forest classifier:
  - `n_estimators` (default: 400)
  - `max_depth` (default: 10)
  - `dataset` (default: "heart_preprocessing.csv")

## Running the Project

### Prerequisites

- Python 3.7+
- Conda or Miniconda
- MLflow
- Git

### Local Execution

1. Clone this repository:
   ```
   git clone <repository-url>
   cd SMSML_Filza-Rahma-Muflihah/Workflow-CI
   ```

2. Run the MLflow project:
   ```
   cd MLproject
   mlflow run . --no-conda
   ```

   Or with custom parameters:
   ```
   mlflow run . -P n_estimators=500 -P max_depth=8 --no-conda
   ```

## CI/CD with GitHub Actions

This project uses GitHub Actions for continuous integration and deployment. The workflow:

1. Triggers on push to the repository
2. Sets up the Python environment
3. Installs dependencies
4. Runs the MLflow project
5. Builds and pushes a Docker image to Docker Hub

## Docker

The model is containerized and available on Docker Hub:
[filzarahma/heart_disease](https://hub.docker.com/r/filzarahma/heart_disease)

To pull and run the Docker image:

```bash
docker pull filzarahma/heart_disease
docker run -p 8080:8080 filzarahma/heart_disease
```

## License

[Specify your license here]

## Contact

[Your contact information]