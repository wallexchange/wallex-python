from wallex.client import Client


def main():
    client = Client(api_key='PUT YOUR API KEY HERE')
    data = client.get_banking_cards()
    print(data)


if __name__ == '__main__':
    main()
