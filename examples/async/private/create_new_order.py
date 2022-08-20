import asyncio
from wallex.async_client import AsyncClient


async def main():
    client = await AsyncClient.create_client(api_key='PUT YOUR API KEY HERE')
    data = await client.place_order(
        symbol='USDTTMN',
        side='buy',
        order_type='limit',
        quantity=11,
        price=25000,
        client_id='CLIENT_ID',
    )
    print(data)


if __name__ == '__main__':
    asyncio.run(main())
