import argparse
import csv
import os
from datetime import datetime
import mysql.connector


def get_connection(host, port, user, pd):
    """Establishes a connection to the MySQL database."""

    try:
        connection = mysql.connector.connect(host=host,
                                             port=port,
                                             # Add your username and password here
                                             user=user,
                                             password=pd)
        print(f"Database Connect successfully!!!!!!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        exit(1)


def load_snapshot(connection, filename):
    """Loads a CSV file into a MySQL table named 'snapshots'."""

    cursor = connection.cursor()
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            # for row in next(reader):
            #     print(f"Row: {row}")
            # Modify this to match your CSV format
            columns = [row for row in next(reader)]
            print(f"Columns: {columns}")
            insert_query = f"INSERT INTO snapshots ({','.join(columns)}) VALUES ({','.join(columns)})"
            print(insert_query)

            for row in reader:
                cursor.execute(insert_query, row)
            connection.commit()
            print(f"Successfully loaded {filename}")
    except csv.Error as err:
        print(f"Error reading CSV file: {err}")
    finally:
        cursor.close()


def main():
    # parser = argparse.ArgumentParser(description="Import CSV snapshots to database")
    # parser.add_argument("--database", help="Database connection URL (host:port)", required=True)
    # parser.add_argument("files", nargs='+', help="CSV snapshot files to import")
    # args = parser.parse_args()
    #
    connection = get_connection("127.0.0.1", 3306, "root", "1234")
    load_snapshot(connection, "data/snapshot_20230101.csv")
    # for filename in args.files:
    #     load_snapshot(connection, filename)

    connection.close()


if __name__ == "__main__":
    main()
