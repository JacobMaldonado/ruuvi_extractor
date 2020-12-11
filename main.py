import asyncio
import platform
# Imports
from program.logic.scanner import scan_specific_device


if __name__ == "__main__":

    address = (
        "E1:F2:09:29:DE:39"  # <--- Change to your device's address here if you are using Windows or Linux
        if platform.system() != "Darwin"
        else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"  # <--- Change to your device's address here if you are using macOS
    )
    loop = asyncio.get_event_loop()
    loop.create_task(scan_specific_device(address))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
        loop.close()