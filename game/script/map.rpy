screen locations:
    imagemap:
        ground "images/map/map_locked.png"
        hover "images/map/map_hover.png"
        idle "images/map/map.png"

        if range_available:
            hotspot (224, 75, 470, 60) clicked Jump("range__router")
        if classroom_available:
            hotspot (990, 317, 333, 55) clicked Jump("classroom__router")
        if gym_available:
            hotspot (153, 474, 155, 72) clicked Jump("gym__router")
        if tennis_available:
            hotspot (279, 891, 404, 58) clicked Jump("tennis__router")
        if track_available:
            hotspot (1152, 831, 174, 55) clicked Jump("track__router")

label map__school:
    $ renpy.choice_for_skipping()
    call screen locations with fade
