label start:
    stop music fadeout 1.0
    menu:
        "Do you want to skip the demo?"
        "Skip Demo":
            $ renpy.block_rollback()
            $ persistent.naoko__cg_1 = True
            jump day_1__start
        "Start from Beginning":
            $ renpy.block_rollback()
            jump day_0__start