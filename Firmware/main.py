# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.hid import HIDModes
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC

# This is the main instance of your keyboard
keyboard = KMKKeyboard()
keyboard.hid_mode = HIDModes.USB

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(MediaKeys())

# Define your pins here!
PINS = [board.D0, board.D1, board.D2, board.D3, board.D4]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.Macro(Press(KC.LGUI), Tap(KC.L), Release(KC.LGUI)), KC.Macro(Press(KC.LCTRL, KC.LSHIFT), Tap(KC.D), Release(KC.LCTRL, KC.LSHIFT)), KC.Macro(Press(KC.LCTRL, KC.LSHIFT), Tap(KC.M), Release(KC.LCTRL, KC.LSHIFT)), KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()