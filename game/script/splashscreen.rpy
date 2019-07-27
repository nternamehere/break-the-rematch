label splashscreen:
    if not persistent.set_volumes:
        $ persistent.set_volumes = True
        $ _preferences.volumes['music'] *= .20
    
    return