import abc

class AbstractionService(metaclass=abc.ABCMeta):
     def create_review(self):
        raise NotImplementedError()
     def get_review_by_food(self):
        raise NotImplementedError()
     def get_reviews(self):
        raise NotImplementedError()
     def delete_review(self):
        raise NotImplementedError()