init python:
    # Map Related Variables
    range_available = True
    classroom_available = False
    gym_available = True
    tennis_available = True
    track_available = True

    #######################
    # Location Variables  #
    #######################

    # Range Variables
    range__first_visit = True

    # Classroom Variables
    classroom__first_visit = True

    # Gym Variables
    gym__first_visit = True

    # Tennis Variables
    tennis__first_visit = True

    # Track Variables
    track__first_visit = True

    #######################
    # Character Variables #
    #######################

    # Ritsuko Variables
    met_ritsuko = False

    #######################
    #    Misc Variables   #
    #######################
    if persistent.cum is None:
        persistent.cum = "always"
