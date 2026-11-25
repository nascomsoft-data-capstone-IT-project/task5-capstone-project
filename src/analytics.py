import pandas as pd

REQUIRED_COLUMNS = ["Date", "Product", "Category", "Sales", "Quantity"]


def prepare_sales_data(dataframe):
    """Validate and prepare an uploaded sales DataFrame."""
    if dataframe is None or dataframe.empty:
        raise ValueError("The uploaded CSV has no data rows. Please upload a file containing sales records.")

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in dataframe.columns]
    if missing_columns:
        missing_text = ", ".join(missing_columns)
        raise ValueError(
            f"Required column(s) missing: {missing_text}. "
            "Use the exact column names shown in the sample CSV."
        )

    data = dataframe[REQUIRED_COLUMNS].copy()
    data = data.dropna(how="all")
    if data.empty:
        raise ValueError("The file contains no usable records.")

    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
    data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
    data["Product"] = data["Product"].astype("string").str.strip()
    data["Category"] = data["Category"].astype("string").str.strip()

    invalid_mask = (
        data["Date"].isna()
        | data["Sales"].isna()
        | data["Quantity"].isna()
        | data["Product"].isna()
        | data["Category"].isna()
        | (data["Product"] == "")
        | (data["Category"] == "")
        | (data["Sales"] < 0)
        | (data["Quantity"] <= 0)
    )
    rejected_count = int(invalid_mask.sum())
    clean_data = data.loc[~invalid_mask].copy()

    if clean_data.empty:
        raise ValueError("No valid rows remain. Check dates, text fields, sales and quantities.")

    clean_data["Quantity"] = clean_data["Quantity"].astype(int)
    clean_data["Date"] = clean_data["Date"].dt.strftime("%Y-%m-%d")
    return clean_data, rejected_count


def calculate_summary(data):
    """Return simple summary values for the dashboard."""
    return {
        "total_sales": float(data["Sales"].sum()),
        "total_quantity": int(data["Quantity"].sum()),
        "number_of_records": int(len(data)),
        "average_sale": float(data["Sales"].mean()),
        "number_of_products": int(data["Product"].nunique()),
    }


def sales_by_category(data):
    """Calculate total sales for each category."""
    return data.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)


def sales_over_time(data):
    """Calculate total sales for each date."""
    dated = data.copy()
    dated["Date"] = pd.to_datetime(dated["Date"])
    return dated.groupby("Date", as_index=False)["Sales"].sum().sort_values("Date")