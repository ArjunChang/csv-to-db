import sys
import csv
from mysql.connector import connect, Error
from helpers import get_db_table_name, format_headers
from os.path import splitext, basename
import json
import logging

logging.basicConfig(level=logging.ERROR)

with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Connect to MySQL database
conn = connect(
    host=config["DB_HOST"],
    user=config["DB_USER"],
    password=config["DB_PASSWORD"],
    database=config["DB_NAME"]
)
cursor = conn.cursor()

# Read the csv
path_to_csv = sys.argv[1]
csv_file_name = splitext(basename(path_to_csv))[0]

db_table_name = get_db_table_name(csv_file_name)
with open(path_to_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_headers = format_headers(next(csv_reader))

    insert_query = f"INSERT INTO {db_table_name} ({','.join(csv_headers)}) VALUES ({','.join(['%s'] * len(csv_headers))})"

    try:
        for row in csv_reader:
            cursor.execute(insert_query, row)

    except Error as E:
        logging.error(json.dumps({"Error": E.msg, "Table": f"{config['DB_NAME']}.{db_table_name}"}))
    
    finally:
        conn.commit()
        conn.close()





