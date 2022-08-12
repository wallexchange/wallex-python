import requests
from src.wallex.utils import error_handler


class RequestsApi:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    @error_handler
    def get(self, url, **kwargs):
        return self.session.get(self.base_url + url, **kwargs)

    @error_handler
    def post(self, url, **kwargs):
        return self.session.post(self.base_url + url, **kwargs)

    @error_handler
    def put(self, url, **kwargs):
        return self.session.put(self.base_url + url, **kwargs)

    @error_handler
    def patch(self, url, **kwargs):
        return self.session.patch(self.base_url + url, **kwargs)

    @error_handler
    def delete(self, url, **kwargs):
        return self.session.delete(self.base_url + url, **kwargs)

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination
