from pydantic import validate_arguments

from wallex.request import AsyncRequestsApi
from wallex.schema import MarketsResponseModel, CurrenciesResponseModel, MarketOrderDetailModel, ClientSymbolInput, \
    MarketTradesModel, MarketCandlesRequestModel, MarketCandlesResponseModel, AccountFeeLevelsResponseModel, \
    AccountBalancesResponseModel, PlaceOrderRequestModel, PlaceOrderResponseModel, LastTradesResponseModel
from wallex.utils import create_list_by_symbol, create_list


class AsyncClient:
    """
    :param api_key: str = Wallex API key (required)
    :method host_is_online: bool = Returns True if Wallex API is online
    :method get_profile: dict = Returns user info
    :return: WallexClient
    """

    @validate_arguments
    def __init__(self, api_key: str, loop=None) -> None:
        self.client_user = None
        self.loop = loop
        self.consumer = AsyncRequestsApi(
            base_url='https://api.wallex.ir',
            headers={"X-API-Key": api_key},
            loop=loop
        )

    @classmethod
    async def create_client(cls, api_key: str = None, loop=None):
        self = cls(api_key, loop)

        if api_key:
            try:
                self.client_user = await self.get_profile()
                print('client user:', self.client_user['first_name'] + ' ' + self.client_user['last_name'])
            except Exception as e:
                raise Exception('can not access wallex api online server', e)

        return self

    async def get_markets(self):
        res = await self.consumer.get('/v1/markets')
        json_res = await res.json()
        symbols = json_res['result']['symbols']
        return create_list_by_symbol(symbols, MarketsResponseModel)

    async def get_currencies(self):
        res = await self.consumer.get('/v1/currencies/stats')
        json_res = await res.json()
        return create_list(json_res['result'], CurrenciesResponseModel)

    async def get_market_orders(self, symbol: str):
        params = ClientSymbolInput(symbol=symbol)
        res = await self.consumer.get('/v1/depth', params=params.dict())
        json_res = await res.json()
        return {
            'ask': create_list(json_res['result']['ask'], MarketOrderDetailModel),
            'bid': create_list(json_res['result']['bid'], MarketOrderDetailModel)
        }

    async def get_market_trades(self, symbol: str):
        params = ClientSymbolInput(symbol=symbol)
        res = await self.consumer.get('/v1/trades?', params=params.dict())
        json_res = await res.json()
        return {
            'latestTrades': create_list(json_res['result']['latestTrades'], MarketTradesModel)
        }

    async def get_market_candles(self, symbol: str, resolution: str, _from, _to):
        params = MarketCandlesRequestModel(symbol=symbol, resolution=resolution, start_time=_from, end_time=_to).dict()
        res = await self.consumer.get('/v1/udf/history?', params={
            'symbol': params['symbol'],
            'resolution': params['resolution'],
            'from': int(round(params['start_time'].timestamp())),
            'to': int(round(params['end_time'].timestamp()))
        })
        json_res = await res.json()
        checked_r = MarketCandlesResponseModel(**json_res)
        return checked_r.dict()

    async def get_profile(self):
        res = await self.consumer.get('/v1/account/profile')
        json_res = await res.json()
        return json_res['result']

    async def get_fee_levels(self):
        res = await self.consumer.get('/v1/account/fee')
        json_res = await res.json()
        return create_list_by_symbol(json_res['result'], AccountFeeLevelsResponseModel)

    # TODO: get 401 auth error when calling this method
    async def get_banking_cards(self):
        res = await self.consumer.get('/v1/account/card-numbers')
        json_res = await res.json()
        return json_res['result']

    # TODO: get 500 server error when calling this method
    async def get_banking_accounts(self):
        res = await self.consumer.get('/v1/account/ibans')
        json_res = await res.json()
        return json_res['result']

    async def get_balances(self):
        temp_balances = {}
        res = await self.consumer.get('/v1/account/balances')
        json_res = await res.json()
        balances = create_list_by_symbol(json_res['result']['balances'], AccountBalancesResponseModel)
        for balance in balances:
            temp_balances.update(balance)
        return {
            'balances': temp_balances
        }

    async def get_crypto_withdrawal_list(self):
        res = await self.consumer.get('/v1/account/crypto-withdrawal')
        json_res = await res.json()
        return json_res['result']

    async def get_crypto_deposit_list(self):
        res = await self.consumer.get('/v1/account/crypto-deposit')
        json_res = await res.json()
        return json_res['result']

    async def place_order(
            self, symbol: str, order_type: str, side: str, quantity: float, price: float, client_id: str = None
    ):
        params = PlaceOrderRequestModel(
            symbol=symbol, order_type=order_type, side=side,
            quantity=quantity, price=price, client_id=client_id
        ).dict(exclude_none=True)
        res = await self.consumer.post('/v1/account/orders', json=params)
        json_res = await res.json()
        return PlaceOrderResponseModel(**json_res['result']).dict()

    @validate_arguments
    async def get_order_detail(self, order_id: str):
        res = await self.consumer.get('/v1/account/orders/' + order_id)
        json_res = await res.json()
        return PlaceOrderResponseModel(**json_res['result']).dict()

    @validate_arguments
    async def cancel_order(self, order_id: str):
        res = await self.consumer.delete('/v1/account/orders/' + order_id)
        json_res = await res.json()
        return json_res['result']

    @validate_arguments
    async def get_open_orders(self, symbol: str = None):
        res = await self.consumer.get('/v1/account/openOrders', params={'symbol': symbol})
        json_res = await res.json()
        return json_res['result']

    @validate_arguments
    async def get_trades(self, symbol: str = None, side: str = None):
        res = await self.consumer.get('/v1/account/trades', params={'symbol': symbol, 'side': side})
        json_res = await res.json()
        last_trades = create_list(json_res['result']['AccountLatestTrades'], LastTradesResponseModel)
        return {
            'AccountLatestTrades': last_trades
        }

    async def close(self):
        return await self.consumer.close()
