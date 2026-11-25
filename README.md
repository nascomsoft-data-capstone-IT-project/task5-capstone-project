# Sales Performance Dashboard – Capstone Task 5

## Project overview
This project is an interactive Streamlit dashboard that allows a user to upload a sales CSV file and view summary statistics, charts, and processed records.

## Business problem
A nontechnical operations manager needs to review sales information without editing or running Python analysis code manually.

## Input data and required columns
The app accepts CSV files containing:
- `Date`
- `Product`
- `Category`
- `Sales`
- `Quantity`

A sample file is available at `data/sample_sales.csv`. The sample data is for demonstration and is not a real company's confidential sales data.

## Data validation policy
- The file must contain all five required columns.
- Dates must be recognizable dates.
- Sales and Quantity must be numeric.
- Sales cannot be negative.
- Quantity must be greater than zero.
- Rows with invalid or missing required values are excluded and counted.
- The uploaded source file is not overwritten.

## Tools and dependencies
- Python 3
- Streamlit
- pandas
- matplotlib

## Project structure

```text
task5_interactive_dashboard/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   └── analytics.py
├── data/
│   └── sample_sales.csv
└── tests/
    └── test_checklist.md

## Contributor

-Daniel Asham Isaac – Project Lead, Streamlit Dashboard (`app.py`), GitHub Organization Setup & Integration

-Glory Pius – team Member

