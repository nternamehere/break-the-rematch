label splashscreen:
    if not persistent.set_volumes:
        $ persistent.set_volumes = True
        $ _preferences.volumes['music'] *= .20
        $ _preferences.volumes['sfx'] *= .20
    
    $ config.keymap['game_menu'].remove('mouseup_3')
    $ config.keymap['hide_windows'].append('mouseup_3')
    $ config.keymap['hide_windows'].remove('mouseup_2')
    jump credits