init python:
    # Map Related Variables
    range_available = True
    classroom_available = False
    staffroom_available = False
    gym_available = True
    tennis_available = True
    track_available = True
    pool_available = False
    pool_gym_available = False
    day = 0

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
    # Touko Variables
    saw_touko_aina_utility = False
    touko_aina_next_step = ""
    no_expose_touko = False

    # Ritsuko Variables
    met_ritsuko = False
    ritsuko_met_principal = False
    ritsuko_next_step = ""

    # Rina Variable
    rina__pursue = False
    rina__probe = False
    rina_next_step = ""

    #######################
    #    Misc Variables   #
    #######################
    if persistent.cum is None:
        persistent.cum = "always"
