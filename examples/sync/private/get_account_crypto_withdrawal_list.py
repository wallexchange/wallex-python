from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.get_crypto_withdrawal_list()
    print(data)


if __name__ == '__main__':
    main()
