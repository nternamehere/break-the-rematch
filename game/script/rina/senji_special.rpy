label senji_special_1:
    if not _in_replay:
        jump touko_special_1
    
    play music sex fadeout 1.0 fadein 1.0
    scene senji_cg_1_blow 1 with fade
    ""
    $ renpy.end_replay()