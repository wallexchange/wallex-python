from typing import Callable, Awaitable

from requests import Response
from aiohttp import ClientResponse


def error_handler(func: Callable[[...], Response]) -> ...:
    def wrapper(*args, **kwargs):
        response: Response = func(*args, **kwargs)
        accepted_status_codes = [200, 201, 202, 204]
        if response.status_code not in accepted_status_codes:
            raise Exception('call api error', response.json())
        return response
    return wrapper


def async_error_handler(func: Callable[[...], Awaitable[ClientResponse]]) -> ...:
    async def wrapper(*args, **kwargs):
        response: ClientResponse = await func(*args, **kwargs)
        accepted_status_codes = [200, 201, 202, 204]
        if response.status not in accepted_status_codes:
            raise Exception('call api error', await response.json())
        return response
    return wrapper


def create_list_by_symbol(dict_list: list, model) -> list:
    result = []
    for item in dict_list:
        if item != 'default':
            raw_data = dict_list[item]
            checked_r = model(**raw_data)
            temp_dict = {
                item: checked_r.dict()
            }
            result.append(temp_dict)
    return result


def create_list(dict_list: list, model) -> list:
    result = []
    for item in dict_list:
        checked_r = model(**item).dict()
        result.append(checked_r)
    return result
