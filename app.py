import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from src.analytics import prepare_sales_data, calculate_summary, sales_by_category, sales_over_time

st.set_page_config(page_title="Sales Performance Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Performance Dashboard")
st.write("Upload a sales CSV file to view key performance figures, category comparisons and sales trends.")

st.sidebar.header("Upload your data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"],
    help="Your file must contain Date, Product, Category, Sales and Quantity.")
st.sidebar.info("Use sample_sales.csv in the data folder to try the dashboard.")

if uploaded_file is None:
    st.info("Please upload a CSV file using the box in the left sidebar.")
    st.subheader("Required CSV columns")
    st.write("Date, Product, Category, Sales, Quantity")
    st.stop()

try:
    raw_data = pd.read_csv(uploaded_file)
    clean_data, rejected_count = prepare_sales_data(raw_data)
except UnicodeDecodeError:
    st.error("The CSV text encoding could not be read. Save the file as UTF-8 CSV and upload it again.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("The uploaded file is empty. Please choose a CSV file with a header and data rows.")
    st.stop()
except Exception as error:
    st.error(f"The file could not be processed: {error}")
    st.stop()

summary = calculate_summary(clean_data)
st.success(f"File processed. {len(clean_data)} valid row(s) are ready.")
if rejected_count:
    st.warning(f"{rejected_count} row(s) were excluded because one or more values were missing or invalid.")

st.subheader("Key performance indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total sales", f"{summary['total_sales']:,.2f}")
col2.metric("Units sold", f"{summary['total_quantity']:,}")
col3.metric("Valid records", f"{summary['number_of_records']:,}")
col4.metric("Average sale", f"{summary['average_sale']:,.2f}")

st.divider()
left, right = st.columns(2)
with left:
    st.subheader("Sales by category")
    category_data = sales_by_category(clean_data)
    fig, ax = plt.subplots()
    ax.bar(category_data["Category"], category_data["Sales"])
    ax.set_xlabel("Category"); ax.set_ylabel("Sales"); ax.set_title("Total Sales by Category")
    ax.tick_params(axis="x", rotation=20); fig.tight_layout()
    st.pyplot(fig); plt.close(fig)

with right:
    st.subheader("Sales over time")
    time_data = sales_over_time(clean_data)
    fig, ax = plt.subplots()
    ax.plot(time_data["Date"], time_data["Sales"], marker="o")
    ax.set_xlabel("Date"); ax.set_ylabel("Sales"); ax.set_title("Daily Sales Trend")
    ax.tick_params(axis="x", rotation=35); fig.tight_layout()
    st.pyplot(fig); plt.close(fig)

st.divider()
st.subheader("Processed sales records")
st.dataframe(clean_data, use_container_width=True)
csv_output = clean_data.to_csv(index=False).encode("utf-8")
st.download_button(label="Download processed CSV", data=csv_output, file_name="processed_sales.csv", mime="text/csv")
st.caption("Note: Total sales are the sum of the Sales column in the uploaded file. The dashboard describes supplied records; it does not prove why sales changed.")