
import datetime as dt
from collections import namedtuple
import bitstring

Dt = namedtuple('Dt', 'day_of_year sec_since_midnight')

def get_current_time():
    dt_now = dt.datetime.utcnow()
    date_today = dt_now.date()
    dt_midnight = dt.datetime.combine(date_today, dt.time())
    sec_since_midnight = (dt_now - dt_midnight).seconds
    day_of_tear = date_today.timetuple().tm_yday
    return Dt(day_of_tear, sec_since_midnight)

# format,  zero-padded to length of 20 hex (10 bytes)
kp_format = '0x02, uint:12=DDD, uint:20=TTTTT, hex:4=P, 0x03, uint:8=CC, 0x0A0D, pad:4'

def build_ack(dt_tuple=None, ack_ok=True):
    dtt = dt_tuple or get_current_time()
    d = {
        'DDD': dtt.day_of_year,
        'TTTTT': dtt.sec_since_midnight,
        'P': '0x0' if ack_ok else '0xF',
        'CC': 0xFF
    }

    return bitstring.pack(kp_format, **d)


def set_cc(ack, pos=13*4):
    cc = ack[:pos].int % 255
    bs = bitstring.pack('uint:8', cc)
    ack.overwrite(bs, pos)


class KpResponse:

    """
    02 | DDD | TTTTT | P | 03 | CC | 0A0D

    02  - STX
    DDD – Date (day of year). From 0x000 to 0x16B (364)
    TTTTT   – time tag in seconds from 0x00000 (00:00:00) to 0x15180 (24:00:00)
    P   - ack (0x0), nack (0xF)
    03  – ETX
    CC  – Check-Sum
    0A  - LF
    0D  – CR
    """

    def __init__(self):
        self.res = build_ack()
        set_cc(self.res)

    def raw(self):
        return self.res.bytes

    def __str__(self):
        return self.res.hex.upper()