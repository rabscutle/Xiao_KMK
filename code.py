import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()

keyboard.modules = [encoder_handler]
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())

keyboard.col_pins = (board.D4,board.D5,board.D6,)
keyboard.row_pins = (board.D10,board.D9,board.D8,board.D7,)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

encoder_handler.divisor = 2
encoder_handler.pins = ((board.D3,board.D2,board.D1,),)

# Layer Switching
LWR     = KC.MO(1)
TLWR    = KC.LT(1, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=250)
RSE     = KC.MO(2)
TRSE    = KC.LT(2, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=250)

# Strings
MAIL    = send_string("patrick.henson@standard.com\n")
PHONE   = send_string("5555555555\n")
HIWI    = send_string("5\t9\t160\t")
T1      = send_string("\ttest\t")
T2      = send_string("\ttest\ttest\t")
T2D2    = send_string("\ttest\t01/2023\t05/2023\ttest")
T4D1    = send_string("\ttest\t01/2023\ttest\ttest\ttest\t")
T5D1    = send_string("\t01/2023\ttest\ttest\ttest\ttest\t")
WP      = send_string("")
UID     = send_string("")
CURPASS = send_string("")

# KMK Variables
XXX     = KC.NO
UPLV    = KC.TRNS

# CTRL Variables
CTA     = KC.LCTL(KC.A)
CTS     = KC.LCTL(KC.S)
CTX     = KC.LCTL(KC.X)
CTC     = KC.LCTL(KC.C)
CTV     = KC.LCTL(KC.V)
CTZ     = KC.LCTL(KC.Z)
SCCAP   = KC.LCTL(KC.PSCR)
ATAB    = KC.LALT(KC.TAB)
CAT     = KC.LCTL(KC.ALT(KC.DEL))

keyboard.keymap = [
    [   # 0.BSE - Base layer
        KC.ESC,     CTC,        CTV,
        MAIL,       PHONE,      HIWI,
        T1,         KC.LSFT,    KC.ENT,
        XXX,        TRSE,       TLWR
    ],
    [   # 1.LWR - String layer
        UPLV,       T1,         T2,
        T2D2,       T4D1,       T5D1,
        KC.SPC,     KC.TAB,     UPLV,
        XXX,        XXX,        UPLV
    ],
    [   # 1.RSE - Random stuff layer
        UPLV,       WP,         CTA,
        UPLV,       UID,        CURPASS,
        XXX,        XXX,        UPLV,
        XXX,        UPLV,       XXX
    ],
]

encoder_handler.map = (
    ((KC.LEFT, KC.TAB,KC.A),),
    ((KC.LEFT, KC.TAB,KC.A),),
    ((KC.LEFT, KC.TAB,KC.A),),
)

if __name__ == '__main__':
    #keyboard.go(hid_type=HIDModes.BLE, ble_name='BLRM')
    keyboard.go(hid_type=HIDModes.USB)

Print("done")
