import abc

class AbstractionResponseSerializer(metaclass=abc.ABCMeta):
    def serialize_create_review(self):
        raise NotImplementedError()
    def serialzie_get_review_by_food(self):
        raise NotImplementedError()
    def serialze_get_reviews(self):
        raise NotImplementedError()
    def serialize_delete_reviews(self):
        raise NotImplementedError()