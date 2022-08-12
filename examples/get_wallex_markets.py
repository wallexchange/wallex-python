from wallex.client import Client


def main():
    client = Client(api_key='1657|kvHGB6dtGubNQ6mNhvha361kH8EjbcmV67yuq2f7')
    markets = client.get_markets()
    print(markets)


if __name__ == '__main__':
    main()
