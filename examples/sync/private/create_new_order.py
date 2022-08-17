from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.place_order(
        symbol='USDTTMN',
        side='buy',
        order_type='limit',
        quantity=11,
        price=25000,
        client_id='CLIENT_ID',
    )
    print(data)


if __name__ == '__main__':
    main()
