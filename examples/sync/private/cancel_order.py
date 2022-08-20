from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.cancel_order(order_id='ORDER_ID')
    print(data)


if __name__ == '__main__':
    main()
