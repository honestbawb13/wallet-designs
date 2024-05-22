from solid2 import cube
import pyperclip

extrude_width = 0.5
card_z = 87
card_x = 54
card_y = 0.8
tolerance = 0.1
cash_bonus = 8
cash_gap = card_y * 3 + tolerance
line_x = card_x + tolerance + extrude_width * 2
open_y = card_y + tolerance

def large_slot(layer_z):
    s = cube(line_x + cash_bonus, extrude_width, layer_z)
    s += cube(extrude_width + cash_bonus, extrude_width, layer_z)
    return s

def four_slots_two_blocked(layer_z):
    layer = cube(line_x, extrude_width, layer_z)
    layer += cube(extrude_width, cash_gap, layer_z).forward(extrude_width).right(line_x - extrude_width)
    layer += large_slot(layer_z).forward(cash_gap + extrude_width)

    return layer

def wallet():
    stagger = 12
    bottom_layer = four_slots_two_blocked(stagger)
    return bottom_layer

# wallet().save_as_scad()
# print(wallet())
pyperclip.copy(str(wallet()))