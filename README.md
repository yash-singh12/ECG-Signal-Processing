# ECG Signal Processing & Analysis using Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Dataset](https://img.shields.io/badge/Dataset-MIT--BIH%20Arrhythmia-orange.svg)](https://physionet.org/content/mitdb/)

A beginner-friendly Digital Signal Processing (DSP) project that analyzes Electrocardiogram (ECG) recordings using Python. Demonstrates signal preprocessing, frequency analysis, peak detection, and evaluation against expert annotations.

---

## 📌 Features & DSP Pipeline

1. **Signal Acquisition**: Loads digitized ECG recordings (Lead MLII, $f_s = 360\text{ Hz}$) from the MIT-BIH Arrhythmia Database using `wfdb`.
2. **Preprocessing**: 4th-order zero-phase Butterworth band-pass filter ($0.5\text{--}40\text{ Hz}$) to eliminate baseline drift and high-frequency muscle noise.
3. **Frequency-Domain Analysis**: Fast Fourier Transform (FFT) to visualize noise suppression and isolate the cardiac QRS band ($5\text{--}25\text{ Hz}$).
4. **R-Peak Detection**: Robust peak extraction using `scipy.signal.find_peaks` with physiological refractory constraints and adaptive thresholding.
5. **Heart Rate & HRV Estimation**: Calculates instantaneous heart rate (BPM), R-R interval distribution, and basic Heart Rate Variability (SDNN).
6. **Evaluation**: Benchmarks detected peaks against cardiologist-verified ground truth annotations with a $\pm 50\text{ ms}$ tolerance window.

---

## 📁 Repository Structure

```text
├── ecg_processing.ipynb    # Main step-by-step Jupyter Notebook
├── mitdb/                  # MIT-BIH record files (.dat, .hea, .atr)
│   ├── 101.dat
│   ├── 101.hea
│   └── 101.atr
├── record.py               # Standalone test script
└── README.md
```

---

## 🚀 Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ecg-dsp-analysis.git
cd ecg-dsp-analysis
```

### 2. Install dependencies
```bash
pip install numpy scipy matplotlib pandas wfdb
```

### 3. Run the Notebook
Launch Jupyter or open directly in VS Code:
```bash
jupyter notebook ecg_processing.ipynb
```

---

## 📚 Tech Stack
* **Python**
* **NumPy** – Vectorized math and array operations
* **SciPy** – Butterworth digital filtering and peak finding
* **Matplotlib** – Time-domain and spectral visualizations
* **Pandas** – Summary metrics and tabular displays
* **WFDB** – Reading PhysioNet waveform and annotation formats

---

## ⚠️ Disclaimer
This project is created for **educational purposes only** and is not intended for clinical diagnosis or medical decision-making.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

