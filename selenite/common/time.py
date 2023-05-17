import datetime
import itertools
import time

DATETIME_FULL = '%Y-%m-%d %H:%M:%S'
DATETIME_SHORT = '%Y-%m-%d %H:%M'
DATETIME_DATE = '%Y-%m-%d'
DATETIME_TIME = '%H:%M:%S'
UTC_DATETIME = '%Y-%m-%dT%H:%M:%S.000Z'


def get_timestamp() -> int:
    """
    Get current timestamp in seconds since the epoch.

    Args:
        None

    Returns:
        int: The current timestamp in seconds since the epoch.

    Example:
        >>> get_timestamp()
        1630429045
    """
    return int(datetime.datetime.timestamp(datetime.datetime.now()))


def get_utc_datetime() -> datetime.datetime:
    """
    Get current UTC datetime.

    Args:
        None

    Returns:
        datetime.datetime: The current UTC datetime.

    Example:
        >>> get_utc_datetime()
        datetime.datetime(2021, 8, 31, 6, 17, 25, 123456)
    """
    return datetime.datetime.utcnow()


def format_datetime(dt: datetime.datetime, time_format: str) -> str:
    """
    Format datetime object to string using the specified format.

    Args:
        dt (datetime.datetime): The datetime object to format.
        time_format (str): The format string to use for formatting.

    Returns:
        str: The formatted datetime string.

    Example:
        >>> dt = datetime.datetime(2021, 8, 31, 6, 17, 25, 123456)
        >>> format_datetime(dt, DATETIME_FULL)
        '2021-08-31 06:17:25'
    """
    return dt.strftime(time_format)


def get_current_date() -> str:
    """
    Get current date in ISO format.

    Args:
        None

    Returns:
        str: The current date in ISO format.

    Example:
        >>> get_current_date()
        '2021-08-31'
    """
    return datetime.datetime.now().date().isoformat()


def get_current_time() -> str:
    """
    Get current time in DATETIME_FULL format.

    Args:
        None

    Returns:
        str: The current time in DATETIME_FULL format.

    Example:
        >>> get_current_time()
        '2021-08-31 06:17:25'
    """
    return datetime.datetime.now().strftime(DATETIME_FULL)


def add_days(days: int, base_time: str = None) -> str:
    """
    Add days to the specified date string in ISO format.

    Args:
        days (int): The number of days to add.
        base_time (str, optional): The base date string to add days to. Defaults to None.

    Returns:
        str: The new date string in ISO format.

    Example:
        >>> add_days(5, '2021-08-31')
        '2021-09-05'
    """
    base_time = get_current_date() if not base_time else base_time
    date = datetime.datetime.fromisoformat(base_time)
    new_date = date + datetime.timedelta(days=days)
    return new_date.date().isoformat()


def add_hours_and_days(hours: int, days: int, base_time: str = None) -> str:
    """
    Add hours and days to the specified datetime string in DATETIME_FULL format.

    Args:
        hours (int): The number of hours to add.
        days (int): The number of days to add.
        base_time (str, optional): The base datetime string to add hours and days to. Defaults to None.

    Returns:
        str: The new datetime string in DATETIME_FULL format.

    Example:
        >>> add_hours_and_days(3, 2, '2021-08-31 06:17:25')
        '2021-09-02 09:17:25'
    """
    base_time = get_current_time() if not base_time else base_time
    dt = datetime.datetime.strptime(base_time, DATETIME_FULL)
    new_dt = dt + datetime.timedelta(hours=hours, days=days)
    return new_dt.strftime(DATETIME_FULL)


def wait(seconds: float, show_with_terminal: bool = False) -> None:
    """
    Wait for the specified number of seconds.

    Args:
        seconds (float): The number of seconds to wait.
        show_with_terminal (bool, optional): Whether to show the progress with a terminal spinner. Defaults to False.

    Returns:
        None

    Example:
        >>> wait(5, True)
        Waiting 5s - [====================] 100%
        Done!
    """
    if not show_with_terminal:
        time.sleep(seconds)
    else:
        iteration = 0
        spinner = itertools.cycle(['-', '/', '|', '\\'])
        while iteration < seconds:
            progress = int(iteration / seconds * 20)
            bar = '=' * progress + '-' * (20 - progress)
            percent = (iteration / seconds) * 100
            print('\rWaiting {}s {} [{}] {:.0f}%'.format(seconds, next(spinner), bar, percent), end='')
            time.sleep(0.25)
            iteration += 0.25
        print('\rDone!')
