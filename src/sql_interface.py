#data will be small, so using DataFrames gives more flexibility than .csv as-is.
import pandas as pd
from sqlalchemy import create_engine
import csv
import ocr

# Define your data as a list of lists
data = [
    ['company', 'name', 'phone', 'email'],
    ['Microsoft', 'Bill', '1234567890', 'bill@microsoft.com'],
]

def createcsv(image, csvpath):
    extracted_data = ocr.ocr_extract(image)
    data.append(extracted_data)
    with open(csvpath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Read the .csv file into a pandas DataFrame
def createdf(csvpath):
    df = pd.read_csv(csvpath)
    print(df)
    return df

# Create a SQLAlchemy engine
# engine = create_engine('postgresql+psycopg2://your_username:your_password@/cloudsql/your_connection_name/your_database')

# Write the DataFrame to your SQL table
def postsql(engine, df):
    df.to_sql('your_table', con=engine, if_exists='append', index=False)

# Read the data from your SQL table into a new DataFrame
def getsql(engine):
    df_new = pd.read_sql('SELECT * FROM your_table', con=engine)
    return df_new
