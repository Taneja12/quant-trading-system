# Nifty 50 Quantitative Trading System

This repository contains a complete pipeline for a quantitative trading strategy on Nifty 50, systematically covering data acquisition, cleaning, feature engineering, strategy logic, ML-based trade filtering, and outlier analysis.

## Overview

The project implements a regime-based trading strategy using EMA crossovers and Volatility filters, enhanced by Machine Learning models (XGBoost & LSTM) to filter out false signals.

## Project Structure



```text
klypto/
├── data/                   # Raw and processed datasets
│   ├── nifty_spot_raw.csv  # Primary source data
│   └── ...                 # Intermediate CSVs
├── notebooks/              # Jupyter notebooks (Run in order 01-08)
├── src/                    # Helper Python modules
├── results/                # Output files (metrics, trade logs)
├── models/                 # Saved ML models (.pkl files)
├── plots/                  # Generated charts and graphs
├── requirement.txt         # Project dependencies
└── README.md               # Project documentation
```

## How to Run

### 1. Environment Setup

It is recommended to use a virtual environment.

```bash
# Create virtual environment (Windows)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

### 2. Install Dependencies

Install the required packages from the text file.

```bash
pip install -r requirement.txt
```

### 3. Execution

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebooks in the following **exact order** to generate the results:

1.  `01_data_acquisition.ipynb`
2.  `02_data_cleaning.ipynb`
3.  `03_data_merging.ipynb`
4.  `04_features_engineering.ipynb`
5.  `05_regime_detection.ipynb`
6.  `06_strategy_logic.ipynb`
7.  `07_ml_enhancement.ipynb`
8.  `08_outlier_analysis.ipynb`

## Output & Performance

### 1. Baseline Strategy Performance
*Metrics derived from `06_strategy_logic.ipynb`*

| Metric | Value |
| :--- | :--- |
| **Total Return** | -1.77% |
| **Sharpe Ratio** | -1.38 |
| **Max Drawdown** | -2.94% |
| **Win Rate** | 40.00% |
| **Total Trades** | 30 |

The improved strategy (EMA 20/50) shows significantly better stats than the original (EMA 5/15), though still negative.

### 2. Machine Learning Enhancement
*Comparison from `07_ml_enhancement.ipynb`*

We applied XGBoost and LSTM models to filter trade signals, aiming to remove false positives.

| Model | Total Return | Improvement |
| :--- | :--- | :--- |
| **Baseline** | 0.53% | - |
| **XGBoost Filtered** | 0.08% | 🔻 Decline |
| **LSTM Filtered** | 0.0% | Neutral |

**Key Insight:** The ML models in this specific test run were conservative.

### 3. Outlier Analysis
*From `08_outlier_analysis.ipynb`*
- **Total Trades Analyzed**: ~5596 candles/points
- **Identified Outliers**: 53 events (0.95%)
