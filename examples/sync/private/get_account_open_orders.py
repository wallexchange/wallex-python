from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.get_open_orders()
    data2 = client.get_open_orders(symbol='USDTTMN')
    print(data)
    print(data2)


if __name__ == '__main__':
    main()
