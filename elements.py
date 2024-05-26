from config import (
    actual_y,
    gap,
    w
)

def slot_one_endcap():

    endcap = [
        (actual_y * .75 - w * 0.5 - gap * 0.5, 90),
        (w + gap, 180),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 270),
        (w * 2, 180),
        (actual_y * 1.5, 90),
        (w * 2, 0),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 270),
        (w + gap, 0),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 90)
    ]
    return endcap

def slot_one_endcap_with_angle(angle_length=4):
    endcap = []
    endcap += [
        (actual_y * .75 - w * 0.5 - gap * 0.5, 90),
        (w + gap, 180),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 270),
    ]

    endcap += [
        (angle_length, 315),
        (w * 2, 180),
        (angle_length, 135),

    ]
    endcap += [
        (actual_y * 1.5, 90),
        (w * 2, 0),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 270),
        (w + gap, 0),
        (actual_y * .75 - w * 0.5 - gap * 0.5, 90)
    ]
    return endcap

def slot_squiggler(slot_length, squiggle_count, squiggle_depth, x_angle, y_angle, x_first, trim):
    anti_x_angle = 180 if x_angle == 0 else 0
    anti_y_angle = 270 if y_angle == 90 else 90
    slot = []
    for index in range(0,squiggle_count):
        if x_first:
            slot.append((slot_length/squiggle_count, x_angle))
            if index % 2 == 0:
                slot.append((squiggle_depth, y_angle))
            else:
                slot.append((squiggle_depth, anti_y_angle))
        else:
            if index % 2 == 0:
                slot.append((squiggle_depth, y_angle))
            else:
                slot.append((squiggle_depth, anti_y_angle))
            slot.append((slot_length/squiggle_count, anti_x_angle))
    if trim:
        slot.pop()
    return slot

def slot_switchback(lengths, first_angle, second_angle, trim):
    match first_angle:
        case 0:
            anti_first_angle = 180
        case 90:
            anti_first_angle = 270
        case 180:
            anti_first_angle = 0
        case 270:
            anti_first_angle = 90
    d = []
    for index, length in enumerate(lengths):
        if index % 2 == 0:
            d.extend([(length[0], first_angle), (length[1], second_angle)])
        else:
            d.extend([(length[0], anti_first_angle), (length[1], second_angle)])
    if trim:
        d.pop()
    return d