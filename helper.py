import os


def file_size_readable(size):
    kb = round(size / 1024, 3)
    mb = round(size / (1024**2), 3)
    gb = round(size / (1024**3), 3)
    tb = round(size / (1024**4), 3)
    if kb > 1 and kb < 1000:
        return f"{kb} KB"
    elif mb > 1 and mb < 1000:
        return f"{mb} MB"
    elif gb > 1 and gb < 1000:
        return f"{gb} GB"
    elif tb > 1 and tb < 1000:
        return f"{tb} TB"
    else:
        return f"{size} bytes"


def count_files_in_directory(directory_path):
    file_count = 0
    for item in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, item)):
            file_count += 1
    return file_count


def clean_datetime(date):
    date_no_micro = date.replace(microsecond=0)
    return date_no_micro.strftime("%Y-%m-%d %H:%M:%S")
