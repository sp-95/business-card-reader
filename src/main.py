import ocr
import sql_interface
from sqlalchemy import create_engine
from PIL import Image

image = 'data/business_cards/002.jpg'
csvpath = 'data/bc.csv'   #  If your .csv file is in the same directory as your Python script, you only need to provide the filename. Otherwise, you need to provide the full path to the .csv file.
# engine = create_engine('postgresql+psycopg2://your_username:your_password@/cloudsql/your_connection_name/your_database')  # Create a SQLAlchemy engine

def main():
    Image.open(image).show()
    sql_interface.createcsv(image, csvpath)
    sql_interface.createdf(csvpath) #should print the df

if __name__ == "__main__":
    main()
