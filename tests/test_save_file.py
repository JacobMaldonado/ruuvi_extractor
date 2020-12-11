import pytest
import csv
import pandas as pd
from pathlib import Path
from program.db.save_to_file import save_to_file
from enviroment import *


@pytest.mark.asyncio
async def test_save_file():
    data = {
        'DataFormat': 5, 
        'Temp': 2.45, 
        'Humidity': 62.3675, 
        'Pressure': 32296, 
        'AcelerationX': -76, 
        'AcelerationY': -64, 
        'AcelerationZ': 968, 
        'Voltaje': 34678, 
        'Motion': 82, 
        'MeasurementNumber': 5184, 
        'Mac': 248429652074041
        }

    await save_to_file(data)
    path = Path(f"{DATA_DIRECTORY_PATH}/{DATA_FILE_NAME}.csv")
    assert path.is_file()
    df = pd.read_csv(path)
    assert df.iloc[-1].to_dict() == data
    
    
