import csv
from pathlib import Path
from enviroment import *

async def save_to_file(data):

    path = Path(f"{DATA_DIRECTORY_PATH}")
    path.mkdir(parents=True, exist_ok=True)
    path = Path(f"{DATA_DIRECTORY_PATH}/{DATA_FILE_NAME}.csv")

    if path.is_file():
        with path.open(mode="a") as f:
            writer = csv.DictWriter(f, [*data])
            writer.writerow(data)
    else:
        with path.open(mode="w") as f:
            writer = csv.DictWriter(f, [*data])
            writer.writeheader()
            writer.writerow(data)
