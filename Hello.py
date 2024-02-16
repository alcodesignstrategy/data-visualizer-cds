import streamlit as st
import pandas as pd
from io import BytesIO

# Function to convert DataFrame to CSV (as bytes) for download
def convert_df_to_csv(df):
    output = BytesIO()
    df.to_csv(output, index=False)  # Without the index
    output.seek(0)
    return output.getvalue()

st.title('CSV and Excel Transposer')

# Update the uploader to accept CSV and XLSX files
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Determine the file type and read the file accordingly
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    
    # Check if the DataFrame is not empty
    if not df.empty:
        st.write("Uploaded Data:")
        st.dataframe(df)

        # Transposing the first row correctly
        # Convert the first row to a DataFrame where each column-value pair becomes a row
        transposed_df = pd.DataFrame(df.iloc[0]).reset_index()
        transposed_df.columns = ['Original Column', 'Transposed Value']  # Rename columns to match your requirement

        st.write("Transposed Data (First Row):")
        st.dataframe(transposed_df)

        # Convert transposed DataFrame to CSV
        csv = convert_df_to_csv(transposed_df)

        # Create a download button for the transposed CSV
        st.download_button(
            label="Download transposed CSV",
            data=csv,
            file_name='transposed_data.csv',
            mime='text/csv',
        )
    else:
        st.write("The uploaded file is empty or not properly formatted.")

print("Hello World")