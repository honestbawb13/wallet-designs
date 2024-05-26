#=============================================
# Adjust these
#=============================================
w = 0.8  # extrude_width
card_x = 54
card_y = 0.6
aprox_card_z = 85
gap = 0.05
cash_bonus = 9.4
layer_height = 0.12
aprox_total_z = 112
aprox_card_stagger = 12
aprox_card_protrusion = aprox_card_stagger * 0.5
#=============================================
# computed variables
#=============================================
total_z = round(aprox_total_z / layer_height) * layer_height
card_stagger = round(aprox_card_stagger / layer_height) * layer_height
card_protrusion = round(aprox_card_protrusion / layer_height) * layer_height
card_z = round(aprox_card_z / layer_height) * layer_height
actual_y = card_y + gap + w
actual_x = card_x + gap + w + 6
cash_gap = actual_y * 3
total_y = actual_y * 7.5
total_x = card_x + cash_bonus + w + gap * 2
floor_height = 0.25 + layer_height * 2
main_body = card_z - card_protrusion * 2 - card_stagger * 2
#=============================================
#=============================================