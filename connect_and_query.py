import os
from dotenv import load_dotenv
import psycopg2 
import pandas as pd

load_dotenv()

conn = psycopg2.connect(os.getenv("DB_CONNECTION_STRING"))

query = "select * from companies limit 5;"

data = pd.read_sql(query,conn)

print(data.head())



