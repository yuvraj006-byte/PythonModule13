import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_pass,
    autocommit=True
)
