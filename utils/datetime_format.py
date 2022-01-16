from datetime import datetime, date


def str_to_datetime(datetime_str: str, _format="%Y-%m-%d %H:%M:%S"):
    """
    str转datetime
    """
    try:
        return datetime.strptime(datetime_str, _format)
    except:
        return None


def str_to_date(date_str: str, _format="%Y-%m-%d"):
    """
    str转date
    """
    try:
        return str_to_datetime(date_str, _format).date()
    except:
        return None


def datetime_to_str(_datetime: datetime, _format="%Y-%m-%d %H:%M:%S"):
    """
    datetime转str
    """
    if not isinstance(_datetime, datetime):
        return ""
    return _datetime.strftime(_format)


def date_to_str(_date: date, _format="%Y-%m-%d"):
    """
    将date对象转成str
    """
    if not isinstance(_date, date):
        return ""
    return _date.strftime(_format)
