from ..setting.development import Development
from ..setting.option  import ReviewServiceOption
from .default import Default


class FactoryReviewService:

    @staticmethod
    def build_object(data_access,service=Development.REVIEW_SERVICE):
        if service == ReviewServiceOption.DEFAULT:
            return Default(data_access)
        raise NotImplementedError()