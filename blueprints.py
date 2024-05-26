from solid2 import (
    cylinder,
    cube
    )
import pyperclip
from config import (
    actual_x,
    actual_y,
    card_stagger,
    cash_bonus,
    cash_gap,
    gap,
    layer_height,
    main_body,
    total_y,
    w,
)
from elements import (
    slot_one_endcap,
    slot_one_endcap_with_angle,
    slot_squiggler,
    slot_switchback,
)

def four_slots_three_blocked():
    d = []
    d.extend(slot_one_endcap())
    d += [
        (actual_x + cash_bonus - w * 4 + gap, 0),
        (total_y, 270),
        (actual_x + w * 3 + gap * 3, 180),
        (actual_y * 3, 90),
        (w * 2 + gap * 2, 0),
    ]
    slot_length = actual_x
    squiggle_depth = actual_y * 2
    d.extend(slot_squiggler(slot_length, 20, squiggle_depth, 0, 270, True, False))
    d += [
        (cash_gap, 90)
    ]
    slot_length = actual_x + cash_bonus - w * 5
    squiggle_depth = actual_y * 1.5 - w - gap
    d.extend(slot_squiggler(slot_length, 21, squiggle_depth, 180, 90, True, True))
    

    return d

def four_slots_two_blocked():
    d = []
    d.extend(slot_one_endcap())
    d += [
        (actual_x + cash_bonus - w * 4 + gap, 0),
        (total_y, 270),
        (actual_x + w * 3 + gap * 3, 180),
        (actual_y * 3, 90),
        (w * 2 + gap * 2, 0),
    ]
    slot_length = actual_x
    squiggle_depth = actual_y * 2
    d.extend(slot_squiggler(slot_length, 20, squiggle_depth, 0, 270, True, False))
    d += [
        (cash_gap, 90),
        (actual_x + cash_bonus - w * 5, 180)
    ]
    return d

def four_slots_one_blocked():
    d = []
    d.extend(slot_one_endcap())
    d += [
        (actual_x + cash_bonus - w * 4 + gap, 0),
        (total_y, 270),
        (actual_x + w * 3 + gap * 3, 180),
        (actual_y * 3, 90),
        (w + gap, 0),
        (actual_y * 2, 270),
    ]
    lengths = [(actual_x + w + gap, actual_y), (actual_x, actual_y)]
    d.extend(slot_switchback(lengths, 0, 90, False))
    slot_length = actual_x
    squiggle_depth = actual_y - w - gap
    d.extend(slot_squiggler(slot_length, 20, squiggle_depth, 0, 270, True, False))
    d += [
        (cash_gap, 90),
        (actual_x + cash_bonus - w * 5, 180),
    ]
    return d

def four_slots_none_blocked():
    d = []
    d.extend(slot_one_endcap())
    d += [
        (actual_x + cash_bonus - w * 4 + gap, 0),
        (total_y, 270),
        (actual_x + w * 3 + gap * 3, 180),
        (actual_y * 3, 90),
        (w + gap, 0),
        (actual_y * 2, 270),
    ]
    lengths = [(actual_x + w + gap, actual_y), (actual_x, actual_y), (actual_x, actual_y)]
    d.extend(slot_switchback(lengths, 0, 90, True))
    d += [
        (cash_gap, 90),
        (actual_x + cash_bonus - w * 5, 180),
    ]

    
    return d

def three_slots():
    d = []
    d.extend(slot_one_endcap())
    d += [
        (actual_x + cash_bonus - w * 4 + gap, 0),
        (total_y - actual_y, 270),
    ]
    lengths = [
        (actual_x + w * 3 + gap * 3, actual_y  - (w + gap) * 0.5),
        (actual_x + w * 2 + gap * 2, w + gap), 
        (actual_x + w * 2 + gap * 2, actual_y  - (w + gap) * 0.5), 
        (actual_x + w * 2 + gap * 2, cash_gap), 
        (actual_x + cash_bonus - w * 5, actual_y)]
    d.extend(slot_switchback(lengths, 180, 90, True))

    return d

def two_slotsOLD():
    d = []
    d.extend(slot_one_endcap())
    no_slot = actual_y * 1.5 - w * 0.25 - gap
    d += [
        (w + gap, 0),
        (no_slot, 270),
        (actual_x + cash_bonus - w * 5, 0),
        (total_y - actual_y - no_slot, 270),
        (actual_x + w * 3 + gap * 3, 180),
        (actual_y * 2, 90),
        (w * 2 + gap * 2, 0),
        (actual_x, 0),
        (cash_gap - w * 0.75, 90),
        (actual_x + cash_bonus - w * 5, 180),
        (w , 90),
    ]

    return d

def two_slots_angle(arm_len):
    # current_length = w
    # goal_length = (actual_x + w * 2 + gap * 2.5) * 0.5
    # current_height = layer_height
    # while current_length < goal_length:
    #     blueprint.append([two_slots(current_length), layer_height])
    #     current_length += w * 0.5
    #     current_height += layer_height
    d = []
    d.extend(slot_one_endcap())
    no_slot = actual_y * 1.5 - w * 0.25 - gap
    d += [
        (w + gap, 0),
        (no_slot, 270),
        (actual_x + cash_bonus - w * 5, 0),

        (total_y - actual_y * 2 - no_slot - (w + gap) * 0.5, 270),
        (arm_len, 180),
        (w + gap, 270),
        (arm_len, 0),
        (actual_y - (w + gap) * 0.5, 270),

        (actual_x + w * 3 + gap * 3, 180),



        (actual_y - (w + gap) * 0.5, 90),
        (arm_len, 0), 
        (w + gap, 90),
        (arm_len, 180),
        (actual_y - (w + gap) * 0.5, 90),



        
        (w * 2 + gap * 2, 0),
        (actual_x, 0),
        (cash_gap - w * 0.75, 90),
        (actual_x + cash_bonus - w * 5, 180),
        (w , 90),
    ]

    return d

def two_slots():
    d = []
    d.extend(slot_one_endcap())
    no_slot = actual_y * 1.5 - w * 0.25 - gap
    d += [
        (w + gap, 0),
        (no_slot, 270),
        (actual_x + cash_bonus - w * 5, 0),
        (total_y - actual_y - no_slot, 270),
    ]
    lengths = [
        (actual_x + w * 3 + gap * 3, actual_y  - (w + gap) * 0.5),
        (actual_x + w * 2 + gap * 2, w + gap), 
        (actual_x + w * 2 + gap * 2, actual_y  - (w + gap) * 0.5), 
        (actual_x + w * 2 + gap * 2, cash_gap - w * 0.75), 
        (actual_x + cash_bonus - w * 5, actual_y)]
    d.extend(slot_switchback(lengths, 180, 90, True))
    d += [
        (w , 90),
    ]

    return d

def one_slot_angle_builder(blueprint):
    b = cash_bonus - w * 7
    current_length = w
    goal_length = (cash_gap ** 2 + b ** 2) ** 0.5
    current_height = layer_height
    while current_length < goal_length:
        blueprint.append([one_slot(current_length), layer_height * 2])
        current_length += w * 0.5
        current_height += layer_height * 2
    return blueprint

def one_slot(angle_length=0):
    d = []
    if angle_length == 0:
        d.extend(slot_one_endcap())
    else:
        d.extend(slot_one_endcap_with_angle(angle_length))
    no_slot = actual_y * 1.5 - w * 0.25 - gap
    d += [
        (w + gap, 0),
        (no_slot, 270),
        (actual_x + cash_bonus - w * 5, 0),
        (total_y - actual_y * 2 - no_slot, 270),
        (actual_x + w * 3 + gap * 3, 180),
        (actual_y, 90),
        (w * 2 + gap * 2, 0),
        (actual_x, 0),
        (cash_gap - w * 0.75, 90),
        (actual_x + cash_bonus - w * 5, 180),
        (w , 90),
    ]
    return d

def zero_slots():
    d = [
        (actual_x + cash_bonus - w * 4, 0),
        (cash_gap, 270),
        (actual_x + w * 3, 180),
        ((cash_gap ** 2 + (cash_bonus - w * 7) ** 2) ** 0.5 + w * 2, 135),
        (actual_y * 1.5, 90),
        (w * 2, 0),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 270),
        (w + gap, 0),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 90),
        (w + gap, 0),
        (w * 3 - gap, 270),
        (w + gap,180),
        (w, 270),
    ]
    return d

def vertical_wallet_blueprint():
    blueprint = []
    blueprint.extend([
        (four_slots_three_blocked(), card_stagger),
        (four_slots_one_blocked(), card_stagger),
        (four_slots_none_blocked(), main_body),
        (three_slots(), card_stagger * 0.5),
        (two_slots(), card_stagger * 0.5),
        (one_slot(), card_stagger - 6.120000000000004),
    ])
    one_slot_angle_builder(blueprint)
    blueprint.extend([
        (zero_slots(), card_stagger),
    ])
    return blueprint

