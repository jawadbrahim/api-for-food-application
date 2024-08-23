from datetime import datetime, timedelta

class DateHelper:
    @staticmethod
    def get_expiration_date(minutes=60):
        exp = datetime.utcnow() + timedelta(minutes=minutes)
        return exp
