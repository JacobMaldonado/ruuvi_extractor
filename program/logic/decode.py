import asyncio

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