label staffroom__router:
    if rina__finale:
        jump rina_finale
    if rina__students:
        jump rina_dog_scene_1
    if rina__rooftop_sex:
        jump rina_rooftop_scene_1
    if rina__probe:
        jump rina__probe_1
    if rina__pursue:
        jump pursue_rina
    if staffroom__first_visit:
        jump staffroom__first_visit
    else:
        show bg classroom with map_fade
        "Under construction"
        jump map__school

label staffroom__first_visit:
    scene black with map_fade
    $ renpy.block_rollback()
    $ staffroom__first_visit = False
    $ rina__pursue = True
    "..."
    "......"
    thinking "So, this is the staff room."
    "Back when I was a student, I was probably the only one who came in and out of here regularly for “meetings” with the female teachers."
    "I used to fuck some of them right in their workplace when everyone else had cleared out."
    "I wonder if I could pull the same thing off with Rina."
    "Speak of the devil..."
    rina "Oh. Shinn. There you are."
    thinking "Huh? She actually came here looking for me?"
    shinn "Ah, Ms. Rina, good morning. Today’s my first day working here. I hope you can offer me your guidance on the job."
    rina "Pfft. I wasn’t expecting manners from the likes of you."
    thinking "This bitch..."
    rina "Right. Since you’re already familiar with the school grounds, I’ll just show you to your workplace. That’s the space where you’ll be doing your administrative work."
    shinn "Wait, administrative work? I didn’t sign up for that. I’m just here as a tutor."
    rina "Well too bad. I discussed it with the principal, and he agreed you could handle some additional tasks while you’re not working with students."
    thinking "I’m really getting the urge to kill this bitch..."
    rina "Do you have a problem with that? "
    "I give Rina the most convincing smile I’ve got."
    shinn "Of course not, Ms. Rina, no problem. I’ll do my best."
    rina "Good. Now, since the tutoring only starts after regular classes have ended..."
    "She carries over a huge stack of paperwork, and slams it down onto my workspace."
    rina "Here’s some easy administrative paperwork I need you to clear. Get it done before school lessons are over."
    thinking "Fuck!"
    "Simmering with rage, I do my best to fake an easy smile."
    shinn "Sure, Ms. Rina. I’ll take care of it."
    rina "Good. Now, if there’s anything else you need to know, you can come to me at my workplace and I’ll sort you out."
    shinn "Okay."
    "Rina walks away."
    "I can’t believe this. This bitch just wants to piss on me because of that encounter we had yesterday."
    "This throws a wrench into all my plans. How am I supposed to get close to any of the students while I’m shut up in here?"
    thinking "Shit. Well, there’s no point agonizing over it. Better just get this stuff out of the way to get her eyes off me before I move on to the girls."

    scene black with fade
    "5 Hours later"

    scene black with fade
    shinn "Oh my god. It’s finally over with."
    "After grueling hours of fixing simple errors, sorting out records and cross checking forms, I’ve finally made it through the whole stack."
    "I guess I’ll check in with Rina to let her know I’ve gotten that out of the way."
    "As I approach her workplace, I see her heading towards the exit, looking like she’s in a hurry."
    thinking "Hmm? What’s wrong?"
    "Her expression grabs my attention. She seems worried and anxious. This is probably the first time I’ve ever seen her in such a state."
    menu:
        thinking "Great. Just when I wanted to clear my work with her, she runs off. Now what?"
        "Now’s my chance to make my move with the other girls!":
            $ renpy.block_rollback()
            jump map__school
        "Secretly pursue her and see what’s going on.":
            $ renpy.block_rollback()
            jump pursue_rina
