screen locations:
    add "images/map/bg-map.png"
    if day == 0:
        if range_available:
            imagebutton auto "images/map/unknown/unknown-range-%s.png" xpos 390 ypos 701 action Jump('archery__day_0')
        else:
            imagebutton idle "images/map/buttons/range-disabled.png" xpos 390 ypos 701 action None

        if classroom_available:
            imagebutton auto "images/map/unknown/unknown-classroom-%s.png" xpos 700 ypos 450 action Jump('classroom__day_0')
        else:
            imagebutton idle "images/map/unknown/unknown-classroom-disabled.png" xpos 700 ypos 450 action None

        if gym_available:
            imagebutton auto "images/map/unknown/unknown-pool-gym-%s.png" xpos 1400 ypos 525 action Jump('gym__day_0')
        else:
            imagebutton idle "images/map/buttons/pool-gym-disabled.png" xpos 1400 ypos 525 action None

        if tennis_available:
            imagebutton auto "images/map/unknown/unknown-tennis-%s.png" xpos 1250 ypos 200 action Jump('tennis__day_0')
        else:
            imagebutton idle "images/map/buttons/tennis-disabled.png" xpos 1250 ypos 200 action None

        if track_available:
            imagebutton auto "images/map/unknown/unknown-track-%s.png"  xpos 230 ypos 80 action Jump('track__day_0')
        else:
            imagebutton idle "images/map/buttons/track-disabled.png" xpos 230 ypos 80 action None

    if day >= 1:
        if staffroom_available:
            if staffroom__first_visit:
                imagebutton auto "images/map/unknown/unknown-staffroom-%s.png" xpos 700 ypos 450 action Jump('rina__router')
            else:
                imagebutton auto "images/map/buttons/staffroom-%s.png" xpos 700 ypos 450 action Jump('rina__router')
        else:
            imagebutton idle "images/map/buttons/staffroom-disabled.png" xpos 700 ypos 450 action None

        if tennis_available:
            imagebutton auto "images/map/buttons/tennis-%s.png" xpos 1250 ypos 200 action Jump('ritsuko__router')
        else:
            imagebutton idle "images/map/buttons/tennis-disabled.png" xpos 1250 ypos 200 action None

        if gym_available:
            imagebutton auto "images/map/buttons/pool-gym-%s.png" xpos 1400 ypos 525 action Jump('touko_aina__router')
        else:
            imagebutton idle "images/map/buttons/pool-gym-disabled.png" xpos 1400 ypos 525 action None

label map__school:
    $ renpy.choice_for_skipping()
    if day == 0 and not range_available and not gym_available and not tennis_available and not track_available:
        $ classroom_available = True
    if day == 1 and not staffroom_available and not tennis_available and not gym_available:
        jump day2
    if day == 2 and not staffroom_available and not tennis_available and gym_available:
        jump touko_aina__router
    if day == 2 and staffroom_available and not tennis_available and not gym_available:
        jump rina__router
    if day == 2 and not staffroom_available and tennis_available and not gym_available:
        jump ritsuko__router
    if day == 2 and not staffroom_available and not tennis_available and not gym_available:
        jump harem_end
    call screen locations with fade
