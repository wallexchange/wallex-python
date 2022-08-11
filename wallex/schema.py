import datetime
from typing import List
from pydantic import BaseModel


class ClientSymbolInput(BaseModel):
    symbol: str


class TradeDirectionModel(BaseModel):
    BUY: int
    SELL: int


class MarketStatModel(BaseModel):
    bidPrice: str = None
    askPrice: str = None
    _24h_ch: str = None
    _7d_ch: str = None
    _24h_volume: str = None
    _7d_volume: str = None
    _24h_quoteVolume: str = None
    _24h_highPrice: str = None
    _24h_lowPrice: str = None
    lastPrice: str = None
    lastQty: str = None
    lastTradeSide: str = 'BUY' or 'SELL'
    bidVolume: str = None
    askVolume: str = None
    bidCount: str = None
    askCount: str = None
    direction: TradeDirectionModel

    class Config:
        fields = {
            '24h_ch': '_24h_ch',
            '7d_ch': '_7d_ch',
            '24h_volume': '_24h_volume',
            '7d_volume': '_7d_volume',
            '24h_quoteVolume': '_24h_quoteVolume',
            '24h_highPrice': '_24h_highPrice',
            '24h_lowPrice': '_24h_lowPrice',
        }


class MarketsResponseModel(BaseModel):
    symbol: str = None
    baseAsset: str = None
    baseAssetPrecision: int = None
    quoteAsset: str = None
    quotePrecision: int = None
    faName: str = None
    faBaseAsset: str = None
    faQuoteAsset: str = None
    stepSize: int = None
    tickSize: int = None
    minQty: int = None
    minNotional: int = None
    stats: MarketStatModel
    createdAt: datetime.datetime


class CurrenciesResponseModel(BaseModel):
    key: str = None
    name: str = None
    name_en: str = None
    rank: int = None
    dominance: str = None
    volume_24h: str = None
    market_cap: str = None
    ath: str = None
    ath_change_percentage: str = None
    ath_date: datetime.datetime = None
    price: str = None
    daily_high_price: str = None
    daily_low_price: str = None
    weekly_high_price: str = None
    weekly_low_price: str = None
    percent_change_1h: str = None
    percent_change_24h: str = None
    percent_change_7d: str = None
    percent_change_14d: str = None
    percent_change_30d: str = None
    percent_change_60d: str = None
    percent_change_200d: str = None
    percent_change_1y: str = None
    price_change_24h: str = None
    price_change_7d: str = None
    price_change_14d: str = None
    price_change_30d: str = None
    price_change_60d: str = None
    price_change_200d: str = None
    price_change_1y: str = None
    max_supply: str = None
    total_supply: str = None
    circulating_supply: str = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


class MarketOrderDetailModel(BaseModel):
    price: str = None
    quantity: int = None
    sum: str = None


class MarketTradesModel(BaseModel):
    symbol: str
    quantity: str
    price: str
    sum: str
    isBuyOrder = bool
    timestamp: datetime.datetime


class MarketCandlesRequestModel(BaseModel):
    symbol: str
    resolution: str = '1' or '60' or '180' or '360' or '720' or '1D'
    start_time: datetime.datetime
    end_time: datetime.datetime


class MarketCandlesResponseModel(BaseModel):
    s: str
    t: List[datetime.datetime]
    c: List[float]
    o: List[float]
    h: List[float]
    l: List[float]
    v: List[float]


class AccountFeeLevelsResponseModel(BaseModel):
    makerFeeRate: str = None
    takerFeeRate: str = None
    recent_days_sum: int = None


class AccountBalancesResponseModel(BaseModel):
    asset: str
    faName: str
    fiat: bool
    value: str
    locked: str


class PlaceOrderRequestModel(BaseModel):
    symbol: str
    type: str = 'LIMIT' or 'MARKET'
    side: str = 'BUY' or 'SELL'
    quantity: float
    price: float
    client_id: str = None

    class Config:
        fields = {
            'type': 'order_type'
        }


class PlaceOrderResponseModel(BaseModel):
    symbol: str
    type: str
    side: str
    price: float
    origQty: float
    origSum: float = None
    executedPrice: float
    executedQty: float
    executedSum: float
    executedPercent: float
    status: str = 'NEW' or 'FILLED' or 'CANCELED'
    active: bool
    clientOrderId: str
    created_at: datetime.datetime = None


class LastTradesResponseModel(BaseModel):
    symbol: str
    quantity: float
    price: float
    sum: float
    fee: float
    feeCoefficient: float
    feeAsset: str
    isBuyer: bool
    timestamp: datetime.datetime
