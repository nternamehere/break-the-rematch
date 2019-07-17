init python:
    # Map Related Variables
    range_available = False
    classroom_available = False
    staffroom_available = True
    gym_available = True
    tennis_available = True
    track_available = False
    pool_available = True
    pool_gym_available = False

    #######################
    # Location Variables  #
    #######################

    # Range Variables
    range__first_visit = True

    # Classroom Variables
    classroom__first_visit = True

    # Staffroom Variables
    staffroom__first_visit = True

    # Gym Variables
    gym__first_visit = True

    # Pool Variables
    pool__first_visit = True

    # Pool/Gym Variables
    pool_gym__first_visit = True

    # Tennis Variables
    tennis__first_visit = True

    # Track Variables
    track__first_visit = True

    #######################
    # Character Variables #
    #######################

    # Ritsuko Variables
    met_ritsuko = False

    # Rina Variable
    rina__pursue = False
    rina__probe = False

    #######################
    #    Misc Variables   #
    #######################
    if persistent.cum is None:
        persistent.cum = "always"
