label classroom__router:
    show bg classroom with map_fade
    "Under construction"
    jump map__school

label classroom__completed_intro_check:
    if classroom__first_visit:
        if not range_available:
            if not gym_available:
                if not tennis_available:
                    if not track_available:
                        jump classroom__first_visit
                    else:
                        jump map__school
                else:
                    jump map__school
            else:
                jump map__school
        else:
            jump map__school
    else:
        jump map__school

label classroom__first_visit:
    "Feeling satisfied, I checked over the principal's list one last time."
    shinn "Let's see... before I call it a day, is there anything else I should see?"
    "As I looked though the notes, I recongnized a familiar class name. Below it seems some notes had been written by the principal."
    shinn "Hmm? Class 3-2? Isn't this the class I was in my final year?"
    "I glanced through the notes and saw that my tutoring lessons would be held in this room."
    shinn "Wow. Looks like the principal's bringing me on a nostalgia trip."
    shinn "Might as well take a look at the old place, see what's changed."

    show bg classroom with fade
    "A sudden torrent of memories gushed through my brain as I entered the classroom. It was identical to how it had been before I left. Nothing had changed at all."
