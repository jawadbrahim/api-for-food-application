import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):
    def create_chat(self):
        raise NotImplementedError()
    def get_chat(self):
        raise NotImplementedError()
    def delete_chat(self):
        raise NotImplementedError()
    def mark_as_read(self):
        raise NotImplementedError()