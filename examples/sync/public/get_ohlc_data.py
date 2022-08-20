from wallex.client import Client
import datetime


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.get_market_candles(
        symbol='USDTTMN',
        resolution='1',
        _from=datetime.datetime(2022, 7, 1),
        _to=datetime.datetime(2022, 7, 10)
    )
    print(data)


if __name__ == '__main__':
    main()
