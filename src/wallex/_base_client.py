from abc import ABC, abstractmethod


class _Base(ABC):
    ORDER_TYPE_LIMIT = 'LIMIT'
    ORDER_TYPE_MARKET = 'MARKET'

    ORDER_SIDE_BUY = 'BUY'
    ORDER_SIDE_SELL = 'SELL'

    @abstractmethod
    def get_markets(self):
        raise NotImplementedError

    @abstractmethod
    def get_currencies(self):
        raise NotImplementedError

    @abstractmethod
    def get_market_orders(self, symbol: str):
        raise NotImplementedError

    @abstractmethod
    def get_market_trades(self, symbol: str):
        raise NotImplementedError

    @abstractmethod
    def get_market_candles(self, symbol: str, resolution: str, _from, _to):
        raise NotImplementedError

    @abstractmethod
    def get_profile(self):
        raise NotImplementedError

    @abstractmethod
    def get_fee_levels(self):
        raise NotImplementedError

    @abstractmethod
    def get_banking_cards(self):
        raise NotImplementedError

    @abstractmethod
    def get_banking_accounts(self):
        raise NotImplementedError

    @abstractmethod
    def get_balances(self):
        raise NotImplementedError

    @abstractmethod
    def get_crypto_withdrawal_list(self):
        raise NotImplementedError

    @abstractmethod
    def get_crypto_deposit_list(self):
        raise NotImplementedError

    @abstractmethod
    def place_order(
            self, symbol: str, order_type: str, side: str, quantity: float, price: float, client_id: str = None
    ):
        raise NotImplementedError

    @abstractmethod
    def get_order_detail(self, order_id: str):
        raise NotImplementedError

    @abstractmethod
    def cancel_order(self, order_id: str):
        raise NotImplementedError

    @abstractmethod
    def get_open_orders(self, symbol: str = None):
        raise NotImplementedError

    @abstractmethod
    def get_trades(self, symbol: str = None, side: str = None):
        raise NotImplementedError

    @abstractmethod
    def order_market(self, symbol: str, side: str, quantity: float, client_id: str = None):
        raise NotImplementedError

    @abstractmethod
    def order_limit(self, symbol: str, side: str, quantity: float, price: float, client_id: str = None):
        raise NotImplementedError

    @abstractmethod
    def order_market_buy(self, symbol: str, quantity: float, client_id: str = None):
        raise NotImplementedError

    @abstractmethod
    def order_market_sell(self, symbol: str, quantity: float, client_id: str = None):
        raise NotImplementedError

    @abstractmethod
    def order_limit_buy(self, symbol: str, quantity: float, price: float, client_id: str = None):
        raise NotImplementedError

    @abstractmethod
    def order_limit_sell(self, symbol: str, quantity: float, price: float, client_id: str = None):
        raise NotImplementedError
