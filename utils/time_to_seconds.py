def to_seconds(weeks:int=0, days:int=0, hours:int=0, minutes:int=0, seconds:int=0) -> int: 
    """Converts time in different units to seconds"""
    return int(7*24*60*60*weeks + 24*60*60*days + 60*60*hours + 60*minutes + seconds)