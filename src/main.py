from fastapi import FastAPI
from PIL import Image
from sqlalchemy import create_engine

from . import sql_interface

image = "data/business_cards/002.jpg"
csvpath = "data/bc.csv"  #  If your .csv file is in the same directory as your Python script, you only need to provide the filename. Otherwise, you need to provide the full path to the .csv file.
# engine = create_engine('postgresql+psycopg2://your_username:your_password@/cloudsql/your_connection_name/your_database')  # Create a SQLAlchemy engine

app = FastAPI()


@app.get("/")
async def root():
    return {"health": "OK"}


def main():
    Image.open(image).show()
    sql_interface.createcsv(image, csvpath)
    sql_interface.createdf(csvpath)  # should print the df


@app.get("/ocr")
async def ocr():
    return main()


if __name__ == "__main__":
    main()
