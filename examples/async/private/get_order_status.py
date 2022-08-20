import asyncio
from wallex.async_client import AsyncClient


async def main():
    client = await AsyncClient.create_client(api_key='PUT YOUR API KEY HERE')
    data = await client.get_order_detail(order_id='ORDER_ID')
    print(data)


if __name__ == '__main__':
    asyncio.run(main())
