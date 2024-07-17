class FoodError(Exception):
    def __init__(self, description, http_code, **kwargs):
        super().__init__(description)
        self.description = description
        self.http_code = http_code
        self.extra_data = kwargs

    def to_dict(self):
        error_info = {
            "description": self.description,
            "http_code": self.http_code
        }
        error_info.update(self.extra_data)
        return error_info