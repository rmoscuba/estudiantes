
import pytz

# Prueba si date es naive
def is_naive(dt):
    return not(dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None)

# Convierte de naive a local
def to_loc(dt, tz = 'UTC'):
    if is_naive(dt):
        tz = pytz.timezone(tz)
        return tz.localize(dt)
    else:
        return dt