"""
Scan/Discovery
--------------
Example showing how to scan for BLE devices.
Updated on 2019-03-25 by hbldh <henrik.blidh@nedomkull.com>
"""

import asyncio
import platform
from bleak import BleakScanner

specification = {
    "DataFormat": {
        "bytes":1
        },
    "Temp": {
        "bytes":2,
        "increment": 0.005,
        "signed": True
        },
    "Humidity": {
        "bytes":2,
        "increment": 0.0025
        },
    "Pressure": {
        "bytes":2
        },
    "AcelerationX": {
        "bytes":2,
        "increment": 1,
        "signed":True
        },
    "AcelerationY": {
        "bytes":2,
        "increment": 1,
        "signed":True
        },
    "AcelerationZ": {
        "bytes":2,  
        "increment": 1,
        "signed":True
        },
    "Voltaje": {
        "bytes":2,
        "increment": 1
        },
    "Motion": {
        "bytes":1
        },
    "MeasurementNumber": {
        "bytes":2
        },
    "Mac": {
        "bytes":6,
        "increment": 1
        }
}

address = (
    "E1:F2:09:29:DE:39"  # <--- Change to your device's address here if you are using Windows or Linux
    if platform.system() != "Darwin"
    else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"  # <--- Change to your device's address here if you are using macOS
)

async def run():
    try:
        while True:
            device = await BleakScanner.find_device_by_address(address)
            if device:
                data = device.details["props"]["ManufacturerData"][1177]
                values = await get_values(specification, data)
                print(values)
                await asyncio.sleep(0.01)
    except KeyboardInterrupt:
        pass
    

async def get_values(specification, data):
    
    byteData = [number.to_bytes(1, byteorder="big") for number in data]

    values = {}
    for data_name, data_description in specification.items():

        signed = data_description.get("signed", False)
        data_bytes = data_description.get("bytes", 1)
        data_increment = data_description.get("increment", 1)
        data_start_value = data_description.get("start", 0)

        if data_bytes > len(byteData):
            raise ValueError("Specification has more bytes than readed data")

        values[data_name] = int.from_bytes(
                b''.join(byteData[:data_bytes]),
                byteorder='big',
                signed=signed
            ) * data_increment + data_start_value
        byteData = byteData[data_bytes:]
    return values





if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())