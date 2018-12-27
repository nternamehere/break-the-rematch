label track__router:
    if track__first_visit:
        jump track__first_visit
    else:
        jump map__school

label track__first_visit:
    show bg track with map_fade
    shinn "{i}Damn, it's hotter than I expected.{/i}"
    shinn "Still, it's a little too late for it to be like this, no?"
    "I sighed in resignation and began looking for my next student. Unlike the others, however, the principal had barely talked about her."
    "I'd gathered that she was supposed to be rather reserved."
    shinn "{i}Quite strange for a star athlete."
    "Other issues came quickly to mind. ALthough I didn't stand out as badly here as with other clubs, I maintained my guard."
    shinn "{i}I shouldn't have so much trouble finding a girl like this...{/i}"
    "As I strode around the track, I finally spotted someone that caught my interest."

    show araki basic with moveinright
    unknown "..."
    "The girl watched me as I came closer, and I watched her back."
    "Her pretty blue eyes were gentle, though they radiated exhaustion."
    shinn "{i}Ah, this must be Araki. Her demeanor is an obvious give away.{/i}"
    "Smiling, I closed the distance between us."
    shinn "Good evening. Are you Miss Shinjugai?"
    araki "..."
    "The girl took a little while to respond, but eventually nodded."
    shinn "{i}What's with this girl?{/i}"
    "We continued to make eye contact for an awkward length of time. Eventually deciding to break the silence, I tried to act cool and friendly."
    shinn "I'll be your tutor from now on. I just wanted us to get acquainted."
    araki "I see..."
    "Her voice was soft, almost a whisper."
    shinn "{i}Damn, she's cute.{/i}"
    shinn "Are you feeling well?"
    araki "I don't... know you."
    shinn "{i}...what?{/i}"
    shinn "Oh, don't worry. I'm just here on behalf of the principal."
    araki "Ms. Akiyama had told me about a tutor, but..."
    shinn "But what?"
    araki "...but I thought you would be older."
    shinn "{i}Well, she's certainly a peculiar girl.{/i}"
    shinn "{i}Observant, in a strange sort of way.{/i}"
    shinn "Oh? Older? As in...?"
    araki "You look like a student."
    araki "I thought you were one..."
    shinn "*chuckle* Well, I {i}was{/i} a student here, after all."
    araki "Oh? You were?"
    "Araki's aura of reservation seemed to lift somewhat."
    shinn "Oh yes. I graduated only a couple of years ago."
    araki "Ah... That explains it, now..."
    shinn "{i}She's very cute indeed. It will be fun to screw her.{/i}"
    "I took a step closer."
    shinn "That's all I have to discuss for now. Once something more comes up, you'll hear from me again."
    araki "Oh... Okay..."
    araki "In this case, I will be going then. See you soon."
    shinn "Alright. Take care."
    "With a small nod, Araki walked away."

    hide araki basic with moveoutright
    $ track_available = False
    jump classroom__completed_intro_check
