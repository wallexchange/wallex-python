import os
import pytest
from wallex.client import WallexClient


def test_init_client_with_api_key():
    WallexClient(api_key=os.environ['API_KEY'])
    print('Wallex test client create successfully')


def test_init_client_with_out_api_key():
    with pytest.raises(Exception) as e:
        print(e)
        WallexClient()


def test_init_client_with_wrong_api_key():
    with pytest.raises(Exception) as e:
        print(e)
        WallexClient(api_key='123')
