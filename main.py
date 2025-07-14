import os
import shutil
import sys
from datetime import datetime

from database_interact import (
    add_disk,
    add_folder,
    add_item,
    create_database,
    get_did,
    get_fid,
)
from helper import clean_datetime, count_files_in_directory, file_size_readable


def main():
    filepath = sys.argv[1]
    db_path = "disk_structure.db"

    if not os.path.exists(db_path):
        print(f"Database '{db_path}' does not exist. Creating it now.")
        create_database(db_path)
    else:
        print(f"Database '{db_path}' already exists.")

    date_indexed = f"{datetime.now()}"
    disk_stats = shutil.disk_usage(filepath)
    total = file_size_readable(disk_stats.total)
    used = file_size_readable(disk_stats.used)
    free = file_size_readable(disk_stats.free)

    add_disk(db_path, filepath, date_indexed, total, used, free)

    for path, dirnames, filenames in os.walk(filepath):
        for d in sorted(dirnames):
            full_dir_path = os.path.join(path, d)
            did = get_did(db_path, filepath)
            num_files = count_files_in_directory(full_dir_path)
            add_folder(db_path, d, full_dir_path, num_files, did)

        for f in [i for i in sorted(filenames) if not (i.startswith(".DSstore"))]:
            full_path = os.path.join(path, f)
            file_meta = os.stat(full_path)
            parent_directory_path = os.path.dirname(full_path)
            fid = get_fid(db_path, parent_directory_path)
            size = file_size_readable(file_meta.st_size)
            date_created = clean_datetime(datetime.fromtimestamp(file_meta.st_ctime))
            date_modified = clean_datetime(datetime.fromtimestamp(file_meta.st_mtime))
            add_item(
                db_path,
                f,
                full_path,
                size,
                date_created,
                date_modified,
                fid,
            )


if __name__ == "__main__":
    main()
