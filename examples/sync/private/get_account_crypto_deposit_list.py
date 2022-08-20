from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.get_crypto_deposit_list()
    print(data)


if __name__ == '__main__':
    main()
