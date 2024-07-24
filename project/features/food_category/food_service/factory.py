from ..settings.development import Development
from ..settings.options import DefaultServiceOption
from .default import DefaultFoodService
from .mock import MockFoodService


class FactoryFoodService:
    @staticmethod
    def build_object(data_access, service=Development.Default_service):
        if service == DefaultServiceOption.DEFAULT:
            return DefaultFoodService(data_access)
        if service == DefaultServiceOption.MOCK:
            return MockFoodService(data_access)
        raise NotImplementedError()
    


