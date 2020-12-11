import asyncio
from program.logic.decode import get_values
from program.logic.load_specification import load_specification
from program.db.save_to_file import save_to_file
from bleak import BleakScanner

async def scan_specific_device(mac):
    specification = {}
    while True:
        device = await BleakScanner.find_device_by_address(mac)
        if device:
            data = device.details["props"]["ManufacturerData"][1177]
            if specification.get("version", 0) == 0:
                specification = load_specification(data[0])
            values = await get_values(specification["specification"], data)
            print(values)
            save_to_file(values["specification"])
            await asyncio.sleep(0.01)