screen locations:
    add "images/map/bg-map.png"
    # if range_available:
    #     if range__first_visit:
    #         imagebutton auto "images/map/unknown/unknown-range-%s.png" xpos 390 ypos 701 action Jump('range__router')
    #     else:
    #         imagebutton auto "images/map/buttons/range-%s.png" xpos 390 ypos 701 action Jump('range__router')
    # else:
    #     imagebutton idle "images/map/buttons/range-disabled.png" xpos 390 ypos 701 action None

    # if classroom_available:
    #     if classroom__first_visit:
    #         imagebutton auto "images/map/unknown/unknown-classroom-%s.png" xpos 700 ypos 450 action Jump('classroom__router')
    #     else:
    #         imagebutton auto "images/map/buttons/classroom-%s.png" xpos 700 ypos 450 action Jump('classroom__router')
    # elif classroom__first_visit and not classroom_available:
    #     imagebutton idle "images/map/unknown/unknown-classroom-disabled.png" xpos 700 ypos 450 action None
    # else:
    #     imagebutton idle "images/map/buttons/classroom-disabled.png" xpos 700 ypos 450 action None

    # if pool_gym_available:
    #     if pool_gym__first_visit:
    #         imagebutton auto "images/map/unknown/unknown-pool-gym-%s.png" xpos 1400 ypos 525 action Jump('gym__router')
    #     else:
    #         imagebutton auto "images/map/buttons/pool-gym-%s.png" xpos 1400 ypos 525 action Jump('gym__router')

    if staffroom_available:
        if staffroom__first_visit:
            imagebutton auto "images/map/unknown/unknown-staffroom-%s.png" xpos 700 ypos 450 action Jump('staffroom__router')
        else:
            imagebutton auto "images/map/buttons/staffroom-%s.png" xpos 700 ypos 450 action Jump('staffroom__router')
    else:
        imagebutton idle "images/map/buttons/staffroom-disabled.png" xpos 700 ypos 450 action None

    if tennis_available:
        if tennis__first_visit:
            imagebutton auto "images/map/unknown/unknown-tennis-%s.png" xpos 1250 ypos 200 action Jump('tennis__router')
        else:
            imagebutton auto "images/map/buttons/tennis-%s.png" xpos 1250 ypos 200 action Jump('tennis__router')
    else:
        imagebutton idle "images/map/buttons/tennis-disabled.png" xpos 1250 ypos 200 action None

    # if track_available:
    #     if track__first_visit:
    #         imagebutton auto "images/map/unknown/unknown-track-%s.png"  xpos 230 ypos 80 action Jump('track__router')
    #     else:
    #         imagebutton auto "images/map/buttons/track-%s.png"  xpos 230 ypos 80 action Jump('track__router')
    # else:
    #     imagebutton idle "images/map/buttons/track-disabled.png" xpos 230 ypos 80 action None

    if gym_available:
        if gym__first_visit:
            imagebutton auto "images/map/unknown/unknown-gym-%s.png" xpos 1400 ypos 525 action Jump('gym__router')
        else:
            imagebutton auto "images/map/buttons/gym-%s.png" xpos 1400 ypos 525 action Jump('gym__router')
    else:
        imagebutton idle "images/map/buttons/gym-disabled.png" xpos 1400 ypos 525 action None

    if pool_available:
        if pool__first_visit:
            imagebutton auto "images/map/unknown/unknown-pool-%s.png" xpos 106 ypos 449 action Jump('pool__router')
        else:
            imagebutton auto "images/map/buttons/pool-%s.png" xpos 106 ypos 449 action Jump('pool__router')
    else:
        imagebutton idle "images/map/buttons/pool-disabled.png" xpos 106 ypos 449 action None
    # if not gym_available and not pool_available and not pool_gym_available:
    #     imagebutton idle "images/map/buttons/pool-gym-disabled.png" xpos 1400 ypos 525 action None

label map__school:
    $ renpy.choice_for_skipping()
    call screen locations with fade
