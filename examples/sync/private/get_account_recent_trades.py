from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.get_trades()
    data2 = client.get_trades(symbol='USDTTMN')
    data3 = client.get_trades(side='buy')
    data4 = client.get_trades(symbol='USDTTMN', side='buy')

    print(data)
    print(data2)
    print(data3)
    print(data4)


if __name__ == '__main__':
    main()
