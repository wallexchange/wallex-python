import asyncio
from wallex.async_client import AsyncClient


async def main():
    client = await AsyncClient.create_client(api_key='PUT YOUR API KEY HERE')
    data = await client.get_markets()
    print(data)


if __name__ == '__main__':
    main()
