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
from blueprints import (
    vertical_wallet_blueprint,
)

def layer_builder(d, w, z, offset):
    layer = cube(d[0][0],w, z).back(w*0.5).up(offset).rotate(d[0][1])
    for index in range(1, len(d)):
        back= (
            sum(tuple[0] for tuple in d[:index] if tuple[1] == 270)
            - sum(tuple[0] for tuple in d[:index] if tuple[1] == 90)
            - sum((tuple[0] ** 2 * 0.5) ** 0.5 for tuple in d[:index] if tuple[1] in (45, 135))
            + sum((tuple[0] ** 2 * 0.5) ** 0.5 for tuple in d[:index] if tuple[1] in (225, 315))
            )
        right = (
            sum(tuple[0] for tuple in d[:index] if tuple[1] == 0)
            - sum(tuple[0] for tuple in d[:index] if tuple[1] == 180)
            + sum((tuple[0] ** 2 * 0.5) ** 0.5 for tuple in d[:index] if tuple[1] in (45, 315))
            - sum((tuple[0] ** 2 * 0.5) ** 0.5 for tuple in d[:index] if tuple[1] in (135, 225))
            )
        match d[index][1]:
            case 0:
                back += w * 0.5
            case 45:
                back += w / 3
                right += w / 3
            case 90:
                right += w * 0.5
            case 135:
                back -= w / 3
                right += w / 3
            case 180:
                back -= w * 0.5
            case 225:
                back -= w / 3
                right -= w / 3
            case 270:
                right -= w * 0.5
            case 315:
                back += w / 3
                right -= w / 3
        layer += cube(d[index][0],w, z).rotate(d[index][1]).back(back).right(right).up(offset)
    return layer

def modeler():
    blueprint = vertical_wallet_blueprint()
    for index, layer in enumerate(blueprint):
        if index == 0:
            wallet = layer_builder(layer[0], w, layer[1], 0)
        else:
            wallet += layer_builder(layer[0], w, layer[1], sum(tup[1] for tup in blueprint[0:index]))
    return wallet



# wallet().save_as_scad()
pyperclip.copy(str(modeler()))