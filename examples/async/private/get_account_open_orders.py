import asyncio
from wallex.async_client import AsyncClient


async def main():
    client = await AsyncClient.create_client(api_key='PUT YOUR API KEY HERE')

    data = await client.get_open_orders()
    data2 = await client.get_open_orders(symbol='USDTTMN')

    print(data)
    print(data2)


if __name__ == '__main__':
    asyncio.run(main())
