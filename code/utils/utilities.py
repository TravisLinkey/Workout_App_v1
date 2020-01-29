from datetime import datetime, date

class Utilities:
    @classmethod
    def fix_date(cls, obj):
        date_format = '%Y-%m-%dT%H:%M:%S.000Z'

        if isinstance(obj, (datetime, date)):
            new_date = obj.strftime(date_format)
            return new_date
        raise TypeError('Object is no good')
