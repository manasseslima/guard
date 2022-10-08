import asyncio


async def handler(reader: asyncio.streams.StreamReader, writer: asyncio..streams.StreamWriter):
    method, url, version = tuple((await reader.readline()).decode().split(' '))



async def main():
    server = await asyncio.start_server(handler, '0.0.0.0', 8080)
    async with server:
        await server.server_forever()


if __name__ == '__main__':
    asyncio.run(run())
