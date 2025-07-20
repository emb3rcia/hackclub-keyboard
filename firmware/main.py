print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
encoder_handler = EncoderHandler()


keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15)
keyboard.row_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCR, KC.SLCK, KC.PAUS],
    [KC.GRAVE, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE, KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, KC.MINUS, KC.EQUALS, KC.BSPC, KC.INS, KC.HOME, KC.PGUP],
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLS, KC.DEL, KC.END, KC.PGDN],
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENTER],
    [KC.LSFT, KC.NUBS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLSH, KC.RSFT],
    [KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.RCTL, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT],
]

keyboard.modules = [encoder_handler]
encoder_handler.map  = { KC.VOLD, KC.VOLU, KC.MUTE }

encoder_handler.pins = (board.GP27, board.GP26, board.GP22)

if __name__ == '__main__':
    keyboard.go()