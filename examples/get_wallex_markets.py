from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    markets = client.get_markets()
    print(markets)


if __name__ == '__main__':
    main()
