# Prediksi Penyakit Jantung dengan Workflow CI/CD

Repositori ini berisi alur kerja machine learning untuk prediksi penyakit jantung dengan kemampuan continuous integration dan deployment. Proyek ini menggunakan MLflow untuk pelacakan eksperimen dan manajemen model, serta GitHub Actions untuk CI/CD.

## Gambaran Proyek

Proyek ini mengimplementasikan classifier RandomForest untuk memprediksi penyakit jantung menggunakan data kesehatan pasien. Alur kerja meliputi:

- Pra-pemrosesan data dan rekayasa fitur
- Pelatihan model menggunakan RandomForestClassifier
- Evaluasi model dan pelacakan metrik
- Continuous integration dengan GitHub Actions
- Containerisasi dengan Docker

## Dataset

Dataset (`heart_preprocessing.csv`) berisi data pasien yang sudah diproses dengan fitur-fitur berikut:
- Age (Usia)
- Sex (Jenis Kelamin)
- ChestPainType (Tipe Nyeri Dada)
- RestingBP (Tekanan Darah Istirahat)
- Cholesterol (Kolesterol)
- FastingBS (Gula Darah Puasa)
- RestingECG (ECG Istirahat)
- MaxHR (Detak Jantung Maksimum)
- ExerciseAngina (Angina akibat Olahraga)
- Oldpeak
- ST_Slope
- HeartDisease (variabel target - Penyakit Jantung)

## Struktur Proyek

```
.
├── .github/
│   └── workflows/
│       └── main.yml        # Konfigurasi workflow GitHub Actions
├── MLproject/
│   ├── conda.yaml          # Konfigurasi lingkungan conda
│   ├── MLproject           # Konfigurasi proyek MLflow
│   ├── modelling.py        # Script pelatihan model
│   └── heart_preprocessing.csv  # Dataset yang sudah diproses
├── README.md               # File ini
└── dockerhub.txt           # URL repositori Docker Hub
```

## Proyek MLflow

File MLproject mendefinisikan alur kerja untuk melatih model. Ini termasuk:

- Konfigurasi lingkungan melalui conda.yaml
- Parameter untuk classifier Random Forest:
  - `n_estimators` (default: 400)
  - `max_depth` (default: 10)
  - `dataset` (default: "heart_preprocessing.csv")

## Menjalankan Proyek

### Prasyarat

- Python 3.7+
- Conda atau Miniconda
- MLflow
- Git

### Eksekusi Lokal

1. Clone repositori ini:
   ```
   git clone <url-repositori>
   cd SMSML_Filza-Rahma-Muflihah/Workflow-CI
   ```

2. Jalankan proyek MLflow:
   ```
   cd MLproject
   mlflow run . --no-conda
   ```

   Atau dengan parameter kustom:
   ```
   mlflow run . -P n_estimators=500 -P max_depth=8 --no-conda
   ```

## CI/CD dengan GitHub Actions

Proyek ini menggunakan GitHub Actions untuk continuous integration dan deployment. Alur kerja:

1. Dipicu saat push ke repositori
2. Menyiapkan lingkungan Python
3. Menginstal dependensi
4. Menjalankan proyek MLflow
5. Membangun dan mendorong image Docker ke Docker Hub

## Docker

Model ini dikemas dalam kontainer dan tersedia di Docker Hub:
[filzarahma/heart_disease](https://hub.docker.com/r/filzarahma/heart_disease)

Untuk menarik dan menjalankan image Docker:

```bash
docker pull filzarahma/heart_disease
docker run -p 8080:8080 filzarahma/heart_disease
```

## Lisensi

[Tentukan lisensi Anda di sini]

## Kontak

[Informasi kontak Anda]