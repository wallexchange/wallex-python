import asyncio
from wallex.async_client import AsyncClient
import datetime


async def main():
    client = await AsyncClient.create_client(api_key='PUT YOUR API KEY HERE')

    data = await client.get_market_candles(
        symbol='USDTTMN',
        resolution='1',
        _from=datetime.datetime(2022, 7, 1),
        _to=datetime.datetime(2022, 7, 10)
    )

    print(data)


if __name__ == '__main__':
    asyncio.run(main())
