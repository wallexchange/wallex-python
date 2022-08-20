from pydantic import validate_arguments
from wallex.request import RequestsApi
from wallex.schema import MarketsResponseModel, CurrenciesResponseModel, MarketOrderDetailModel, ClientSymbolInput, \
    MarketTradesModel, MarketCandlesRequestModel, MarketCandlesResponseModel, AccountFeeLevelsResponseModel, \
    AccountBalancesResponseModel, PlaceOrderRequestModel, PlaceOrderResponseModel, LastTradesResponseModel
from wallex.utils import create_list_by_symbol, create_list

from wallex._base_client import _Base


class Client(_Base):
    """
    :param api_key: str = Wallex API key (required)
    :method host_is_online: bool = Returns True if Wallex API is online
    :method get_profile: dict = Returns user info
    :return: WallexClient
    """

    @validate_arguments
    def __init__(self, api_key: str) -> None:
        self._consumer = RequestsApi(
            base_url='https://api.wallex.ir',
            headers={"X-API-Key": api_key}
        )

        try:
            self.client_user = self.get_profile()
            print('client user:', self.client_user['first_name'] + ' ' + self.client_user['last_name'])
        except Exception as e:
            raise Exception('can not access wallex api online server', e)

    def get_markets(self):
        res = self._consumer.get('/v1/markets')
        symbols = res.json()['result']['symbols']
        return create_list_by_symbol(symbols, MarketsResponseModel)

    def get_currencies(self):
        res = self._consumer.get('/v1/currencies/stats')
        return create_list(res.json()['result'], CurrenciesResponseModel)

    def get_market_orders(self, symbol: str):
        params = ClientSymbolInput(symbol=symbol)
        res = self._consumer.get('/v1/depth?', params=params.dict())
        return {
            'ask': create_list(res.json()['result']['ask'], MarketOrderDetailModel),
            'bid': create_list(res.json()['result']['bid'], MarketOrderDetailModel)
        }

    def get_market_trades(self, symbol: str):
        params = ClientSymbolInput(symbol=symbol)
        res = self._consumer.get('/v1/trades?', params=params.dict())
        return {
            'latestTrades': create_list(res.json()['result']['latestTrades'], MarketTradesModel)
        }

    def get_market_candles(self, symbol: str, resolution: str, _from, _to):
        params = MarketCandlesRequestModel(symbol=symbol, resolution=resolution, start_time=_from, end_time=_to).dict()
        res = self._consumer.get('/v1/udf/history?', params={
            'symbol': params['symbol'],
            'resolution': params['resolution'],
            'from': int(round(params['start_time'].timestamp())),
            'to': int(round(params['end_time'].timestamp()))
        })
        checked_r = MarketCandlesResponseModel(**res.json())
        return checked_r.dict()

    def get_profile(self):
        res = self._consumer.get('/v1/account/profile')
        return res.json()['result']

    def get_fee_levels(self):
        res = self._consumer.get('/v1/account/fee')
        return create_list_by_symbol(res.json()['result'], AccountFeeLevelsResponseModel)

    # TODO: get 401 auth error when calling this method
    def get_banking_cards(self):
        res = self._consumer.get('/v1/account/card-numbers')
        return res.json()['result']

    # TODO: get 500 server error when calling this method
    def get_banking_accounts(self):
        res = self._consumer.get('/v1/account/ibans')
        return res.json()['result']

    def get_balances(self):
        temp_balances = {}
        res = self._consumer.get('/v1/account/balances')
        balances = create_list_by_symbol(res.json()['result']['balances'], AccountBalancesResponseModel)
        for balance in balances:
            temp_balances.update(balance)
        return {
            'balances': temp_balances
        }

    def get_crypto_withdrawal_list(self):
        res = self._consumer.get('/v1/account/crypto-withdrawal')
        return res.json()['result']

    def get_crypto_deposit_list(self):
        res = self._consumer.get('/v1/account/crypto-deposit')
        return res.json()['result']

    def place_order(self,
                    symbol: str, order_type: str, side: str,
                    quantity: float, price: float = None, client_id: str = None):
        params = PlaceOrderRequestModel(symbol=symbol, order_type=order_type, side=side,
                                        quantity=quantity, price=price, client_id=client_id
                                        ).dict(exclude_none=True)
        res = self._consumer.post('/v1/account/orders', json=params)
        return PlaceOrderResponseModel(**res.json()['result']).dict()

    def order_market(self, symbol: str, side: str, quantity: float, client_id: str = None):
        return self.place_order(
            symbol=symbol, order_type=self.ORDER_TYPE_MARKET, side=side, quantity=quantity, client_id=client_id
        )

    def order_limit(self, symbol: str, side: str, quantity: float, price: float, client_id: str = None):
        return self.place_order(
            symbol=symbol, order_type=self.ORDER_TYPE_LIMIT, side=side,
            quantity=quantity, price=price, client_id=client_id
        )

    def order_market_buy(self, symbol: str, quantity: float, client_id: str = None):
        return self.order_market(
            symbol=symbol, side=self.ORDER_SIDE_BUY, quantity=quantity, client_id=client_id
        )

    def order_market_sell(self, symbol: str, quantity: float, client_id: str = None):
        return self.order_market(
            symbol=symbol, side=self.ORDER_SIDE_SELL, quantity=quantity, client_id=client_id
        )

    def order_limit_buy(self, symbol: str, quantity: float, price: float, client_id: str = None):
        return self.order_limit(
            symbol=symbol, side=self.ORDER_SIDE_BUY, quantity=quantity, price=price, client_id=client_id
        )

    def order_limit_sell(self, symbol: str, quantity: float, price: float, client_id: str = None):
        return self.order_limit(
            symbol=symbol, side=self.ORDER_SIDE_SELL, quantity=quantity, price=price, client_id=client_id
        )

    @validate_arguments
    def get_order_detail(self, order_id: str):
        res = self._consumer.get('/v1/account/orders/' + order_id)
        return PlaceOrderResponseModel(**res.json()['result']).dict()

    @validate_arguments
    def cancel_order(self, order_id: str):
        res = self._consumer.delete('/v1/account/orders/' + order_id)
        return res.json()['result']

    @validate_arguments
    def get_open_orders(self, symbol: str = None):
        res = self._consumer.get('/v1/account/openOrders', params={'symbol': symbol})
        return res.json()['result']

    @validate_arguments
    def get_trades(self, symbol: str = None, side: str = None):
        res = self._consumer.get('/v1/account/trades', params={'symbol': symbol, 'side': side})
        last_trades = create_list(res.json()['result']['AccountLatestTrades'], LastTradesResponseModel)
        return {
            'AccountLatestTrades': last_trades
        }
