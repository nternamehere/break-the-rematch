label start:
    stop music fadeout 1.0
    menu:
        "Do you want to skip the demo?"
        "Skip Demo":
            $ renpy.block_rollback()
            $ persistent.naoko__sex_scene_1 = True
            jump day1_start
        "Start from Beginning":
            $ renpy.block_rollback()
            jump day0_start