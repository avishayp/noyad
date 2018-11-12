
import datetime as dt
from collections import namedtuple
import bitstring
from . import log

"""
test:
$ sudo nc -l 443 | hexdump -C
00000000  02 03 e8 13 b0 95 d7 00  00 03 30 39 0a 0d        |..........09..|
0000000e

payload:

$ sudo nc -l 443 | hexdump -C
00000000  02 03 e8 13 b0 95 d7 00  0a 10 13 b0 96 22 00 13  |............."..|
00000010  b0 96 23 10 13 b0 96 24  00 13 b0 96 26 10 13 b0  |..#....$....&...|
00000020  96 27 00 13 b0 96 28 10  13 b0 96 29 00 13 b0 96  |.'....(....)....|
00000030  2a 10 13 b0 96 2b 00 13  b0 96 2d 03 31 41 0a 0d  |*....+....-.1A..|
00000040
"""


Dt = namedtuple('Dt', 'day_of_year sec_since_midnight')

def get_current_time():
    dt_now = dt.datetime.utcnow()
    date_today = dt_now.date()
    dt_midnight = dt.datetime.combine(date_today, dt.time())
    sec_since_midnight = (dt_now - dt_midnight).seconds
    day_of_tear = date_today.timetuple().tm_yday
    return Dt(day_of_tear, sec_since_midnight)


# format (10 bytes)
KP_ACK = '0x02, uint:12=DDD, uint:20=TTTTT, hex:8=PP, 0x03, uint:8=CC, 0x0A0D'

def build_ack(dt_tuple=None, ack_ok=True):
    dtt = dt_tuple or get_current_time()
    d = {
        'DDD': dtt.day_of_year,
        'TTTTT': dtt.sec_since_midnight,
        'PP': '0x00' if ack_ok else '0xFF',
        'CC': 0xFF
    }

    return bitstring.pack(KP_ACK, **d)


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
    PP   - ack (0x00), nack (0xFF)
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


"""
02AAAADDDTTTTTPXXXS₁S₁D₁D₁D₁T₁T T₁T₁T₁S₂S₂D₂D₂D₂T₂T₂T₂T₂T₂……SₓSₓDₓDₓDₓTₓTₓTₓTₓTₓ03CC0A0D
Most Significant first
 
02 - STX
AAAA – Address from 0x0000 to 0xFFFF
DDD – Date. From 0x000 to 0x16B (364). D₀D₀D₀ is current date
TTTTT – time tag in seconds from 0x00000 (00:00:00) to 0x15180 (24:00:00). T₀T₀T₀T₀T₀ is current time
P – Type. 0x0 for change of state message type. 0xF – there is no COS. The time and date will be the current (D₀D₀D₀T₀T₀T₀T₀T₀).
XXX – Number of records. From 0x000 to 0x12C (300)
SS – Status of the 4 input (“1” for open, “0” for closed). Example 0x01 -> input 1 is open.
03 – ETX
CC – Check-Sum
0A - LF
0D – CR
"""

KP_MSG_HEADER = 'hex:8, uint:16, uint:12, uint:20, hex:4, uint:12'
KP_MSG_PAYLOAD = 'hex:8, uint:12, uint:20'
KP_MSG_FOOTER = 'hex:8, uint:8, hex:16'

class KpReceive:

    def __init__(self, sock):
        self._sock = sock
        self.header = ''
        self.payload = ''
        self.footer = ''
        self.receive()

    def read(self, n):
        return self._sock.recv(n)
    
    def receive(self):
        self.header = self.read(9)
        log.info('header: %s', self.header)
        parsed = bitstring.ConstBitStream(self.header).readlist(KP_MSG_HEADER)
        size = parsed[-1]
        self.payload = self.read(size * 5)
        log.info('payload: %s', self.payload)
        self.footer = self.read(4)
        log.info('footer: %s', self.footer)

    def __str__(self):
        return (self.header + self.payload + self.footer).hex().upper()
