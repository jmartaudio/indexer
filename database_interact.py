import sqlite3

try:

    def create_database(db_path):
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS Disks
                (DID INTEGER PRIMARY KEY,
                name TEXT,
                date_indexed TEXT,
                total_size TEXT,
                size_used TEXT,
                size_free TEXT)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS 'Folders' (
                'FID'   INTEGER,
                'name'  TEXT,
                'full_path' TEXT,
                'num_files' INTEGER,
                'DID'   INTEGER,
                PRIMARY KEY('FID'),
                FOREIGN KEY('DID') REFERENCES "Disks"('DID'))""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS 'Items' (
                'ID'    INTEGER,
                'name'  TEXT,
                'full_path' TEXT,
                'size'  TEXT,
                'date_created'  TEXT,
                'date_modified' TEXT,
                'FID'   INTEGER,
                PRIMARY KEY('ID'))""")

        conn.commit()
        conn.close()

except Exception as e:
    print(f"A db Error Occurred: {e}")

try:

    def add_disk(db_path, name, date_indexed, total_size, size_used, size_free):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO disks (name, date_indexed, total_size, size_used, size_free)
            VALUES (?, ?, ?, ?, ?)
        """,
            (name, date_indexed, total_size, size_used, size_free),
        )

        conn.commit()
        conn.close()

except Exception as e:
    print(f"A db Error Occurred: {e}")


try:

    def add_folder(db_path, name, full_path, num_files, did):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO folders (name, full_path, num_files, did)
            VALUES (?, ?, ?, ?)
        """,
            (name, full_path, num_files, did),
        )

        conn.commit()
        conn.close()

except Exception as e:
    print(f"A db Error Occurred: {e}")

try:

    def add_item(db_path, name, full_path, size, date_created, date_modified, fid):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO items (name, full_path, size, date_created, date_modified, fid)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (name, full_path, size, date_created, date_modified, fid),
        )

        conn.commit()
        conn.close()

except Exception as e:
    print(f"A db Error Occurred: {e}")

try:

    def get_did(db_path, filepath):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = "SELECT DID FROM disks WHERE name = ?"
        cursor.execute(query, (filepath,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

except Exception as e:
    print(f"A db Error Occurred: {e}")


try:

    def get_fid(db_path, parent_folder_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = "SELECT FID FROM folders WHERE full_path = ?"
        cursor.execute(query, (parent_folder_path,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0

except Exception as e:
    print(f"A db Error Occurred: {e}")

