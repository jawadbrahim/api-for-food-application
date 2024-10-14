from ..setting.development import Development
from ..setting.option import ServiceOption
from .default import Default


class FactoryService():

    def build_object(data_access,service=Development.CHAT_SERVICE):
        if service == ServiceOption.DEFAULT:
            return Default(data_access)
        
        raise NotImplementedError()