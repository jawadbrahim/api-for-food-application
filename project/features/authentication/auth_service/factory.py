from ..settings.options import DefaultOptions
from ..settings.development import Development
from .default import Default



class FactoryAuthService():
    @staticmethod
    def build_object(data_access,service=Development.AUTH_SERVICE):
        if service == DefaultOptions.DEFAULT:
            return Default(data_access)
        raise NotImplementedError()