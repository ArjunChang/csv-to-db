import csv
from mysql.connector import connect
from helpers import is_header, validate_row
import json
import logging
from argparse import ArgumentParser

# Initiate a Logger
logger = logging.getLogger()


# Parser to fetch the table and the path to the csv file
parser = ArgumentParser()
parser.add_argument('--type', help='Type of Product')
parser.add_argument('--file', help='Path to csv file')
args = parser.parse_args()

table_name = args.type
csv_file = args.file

# Load the configurations
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

# Get the metadata of the specified table
metadata_file = open(f"metadata/{table_name}.json", "r")
metadata = json.load(metadata_file)
attributes = [attr for attr in metadata['attributes']]
number_of_attributes = len(attributes)

# Read the csv
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    insert_query = f"INSERT INTO {table_name} {tuple(attributes)} VALUES ({','.join(['%s'] * number_of_attributes)})".replace('\'', '')

    try:
        rows = []
        # Parse 1st row
        row = next(csv_reader, None)

        # Ignore first row if header, else insert the data into the database
        if not is_header(row):
            if validate_row(row, metadata["attributes"], number_of_attributes):
                rows.append(row)

        # Validate every row before sending data to the database
        for row in csv_reader:
            if validate_row(row, metadata["attributes"], number_of_attributes):
                rows.append(row)

        # Batch insert all data
        cursor.executemany(insert_query, rows)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    except BaseException as E:
        logger.error(E.msg)





