# Frameworks Assignment – CORD-19 Analysis

## Overview
This project analyzes the **CORD-19 metadata.csv** dataset using:
- Pandas (data analysis)
- Matplotlib & Seaborn (visualization)
- Streamlit (interactive app)

## Features
- Publications by year
- Top publishing journals
- Word cloud of paper titles
- Source distribution

## How to Run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Observations
- Publication counts spiked significantly in 2020.
- Journals like *medRxiv* and *bioRxiv* were leading sources.
- Keywords in titles highlight pandemic-related research focus.

## Reflection
Working with a real-world dataset required:
- Handling missing values
- Cleaning date columns
- Balancing performance with dataset size

This project reinforced practical **data science workflow** and introduced interactive data presentation via **Streamlit**.
