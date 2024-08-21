import os
from dotenv import load_dotenv
import psycopg2 

load_dotenv()

conn = psycopg2.connect(os.getenv("DB_CONNECTION_STRING"))
print(conn.status)

