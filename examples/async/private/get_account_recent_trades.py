import asyncio
from wallex.async_client import AsyncClient


async def main():
    client = await AsyncClient.create_client(api_key='PUT YOUR API KEY HERE')

    data = await client.get_trades()
    data2 = await client.get_trades(symbol='USDTTMN')
    data3 = await client.get_trades(side='buy')
    data4 = await client.get_trades(symbol='USDTTMN', side='buy')

    print(data)
    print(data2)
    print(data3)
    print(data4)


if __name__ == '__main__':
    asyncio.run(main())
