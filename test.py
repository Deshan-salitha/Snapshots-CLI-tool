import csv
import datetime
import os
import time

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

        cursor.execute("SELECT * FROM spd.snapshots")
        results = [row[0] for row in cursor]
        if not results:
            insert_query = f"INSERT INTO spd.snapshots (file_name, timespan) VALUES ('{filename}','{datetime.datetime.now()}')"
            print(insert_query)
            cursor.execute(insert_query)
            connection.commit()

        for file in results:
            if file == filename:
                print("Snapshot already added")
                return
            else:
                insert_query = f"INSERT INTO spd.snapshots (file_name, timespan) VALUES ('{filename}','{datetime.datetime.now()}')"
                # print(insert_query)
                cursor.execute(insert_query)
                connection.commit()

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            print(reader)

            for row in reader:
                columns = list(dict(row).values())
                allkeys =list(dict(row).keys())
                allkeys.pop(0)
                print(allkeys)
                keys = allkeys
                # values = ""
                # print(f"Values: {columns[0]},'{columns[1]}','{columns[2]}','{columns[3]}'")
                # for item in columns:
                # print(f"Values: {values}")
                insert_query = f"INSERT INTO spd.snapshot ({','.join(keys)}) VALUES ('{columns[1]}','{columns[2]}','{columns[3]}')"
                # print(insert_query)
                cursor.execute(insert_query, row)
                connection.commit()

            print(f"Successfully loaded {filename}")
    except csv.Error as err:
        print(f"Error reading CSV file: {err}")
    finally:
        cursor.close()


def list_snapshots(connection):
    try:
        """Lists information about imported snapshots."""

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM information_schema.TABLES WHERE table_name = 'snapshots'")
        table_exists = cursor.fetchone()

        if not table_exists:
            print("No 'snapshots' table found in database.")
            return

        cursor.execute("SELECT * FROM spd.snapshots")
        # Modify this to display relevant information
        print(cursor.rowcount)
        for row in cursor:
            print(
                f"Filename: {row[0]}, Timestamp: {row[2]}")  # Assuming filename is stored in column 2 and import time in column 3

        cursor.close()
        print(f"Successfully loaded ")
    except Exception as err:
        print(f"Error reading CSV file: {err}")


def main():
    # parser = argparse.ArgumentParser(description="Import CSV snapshots to database")
    # parser.add_argument("--database", help="Database connection URL (host:port)", required=True)
    # parser.add_argument("files", nargs='+', help="CSV snapshot files to import")
    # args = parser.parse_args()

    connection = get_connection("127.0.0.1", 3306, "root", "1234")
    # load_snapshot(connection, "data/snapshot_20230603.csv")
    list_snapshots(connection)
    connection.close()


if __name__ == "__main__":
    main()
