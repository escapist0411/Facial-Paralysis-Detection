# Neural Shield AI - Facial Paralysis Diagnostics

A highly accurate, deep-learning-powered clinical platform designed to diagnose and assess the severity of facial paralysis. The application utilizes a customized CNN for medical classification alongside an internal U-Net architecture for high-fidelity facial segmentation and a MediaPipe pipeline for asymmetry extraction. 

The entire front-end is wrapped in a highly professional, dark-themed Streamlit portal tailored for clinicians and medical researchers.

## ✨ Core Features
- **Classification AI**: Automatically diagnoses Normal vs. Paralysis from uploaded patient photos using a custom CNN.
- **Asymmetry Scoring**: Detects 468 precise facial landmarks via MediaPipe and calculates a geometric asymmetry score.
- **Severity Inference**: Dynamically scores the severity (Normal, Mild, Moderate, Severe) based on diagnostic confidence and geometric deviation.
- **Medical Segmentation**: Highlights key facial regions via a fully trained U-Net segmentation network.
- **PDF Report Generation**: Automatically compiles the diagnostic findings, original photo, and segmentation overlays into a downloadable clinical PDF report.
- **Clinical Dashboard**: A premium UI offering a patient queue, live-updating metrics, and a secure contact desk.

## 📁 Project Structure
```
Facial-Paralysis-Detection/
├── dataset/             # Raw classification images (Normal / Paralysis)
├── models/              # Saved model weights (.keras files)
├── reports/             # Output directory for generated PDF clinical reports
├── src/                 # Backend AI Logic
│   ├── predict.py       # Core prediction & inference engine
│   ├── train_model.py   # Training script for the diagnostic CNN
│   ├── train_unet.py    # Training script for the U-Net segmentation model
│   ├── config.py        # Project pathings and class names
│   └── unet_segmenter.py# U-Net post-processing functions
├── tools/               # Utility scripts (e.g. generate_masks.py)
├── web/                 # Streamlit Frontend Web App
│   ├── Home.py          # Main landing dashboard
│   ├── theme.py         # Global CSS logic & Splash Screen animation
│   └── pages/           # Individual portal tabs (Upload, Reports, Contact Us)
```

## 🚀 Installation & Setup

1. **Clone the repository and set up a Python 3.11 virtual environment:**
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

2. **Install exact dependencies:**
*(Note: These dependencies have been heavily optimized for macOS Apple Silicon to avoid native metal/JAX clashes)*
```bash
pip install -r requirements.txt
```

## 🧠 Training the Models

If you do not have the `.keras` files inside the `models/` folder, you must train them from your dataset:

**1. Train Diagnostic Model:**
```bash
PYTHONPATH=. python src/train_model.py
```
**2. Train Segmentation U-Net Model:**
First, autogenerate your ground truth face masks from your raw images:
```bash
PYTHONPATH=. python tools/generate_masks.py
```
Then, train the actual U-Net model:
```bash
PYTHONPATH=. python src/train_unet.py
```

## 💻 Running the Web Portal

To start the Neural Shield interactive clinician dashboard:
```bash
streamlit run web/Home.py
```
The application will securely launch on `http://localhost:8501`.