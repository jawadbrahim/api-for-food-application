import abc

class AbstractionRequestValidator(metaclass=abc.ABCMeta):
    def validate_create_review(self):
        raise NotImplementedError()