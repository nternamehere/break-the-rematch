label day_1__start:
    $ quick_menu = True
    $ day = 1
    $ tennis_available = True
    $ staffroom_available = True
    $ gym_available = True
    
    show bg shinn bedroom with fade
    "I woke up without the aid of my alarm clock today. I couldn't keep myself in bed. I'm already restless with anticipation."
    "Today, I finally get to put my plans for those girls into action."
    thinking "Alright. Time to brighten up and get going..."
    "I begin preparations for my first day of tutoring."

    show bg main gate with fade
    $ renpy.music.play(campus, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    shinn "Wow. Quite a crowd we've got here."
    "Even this early in the morning, there's already a huge rush of students heading in to school."
    "I smile a bit as memories of my own past here come to mind."
    thinking "This really brings back the good old days. Yeah, I had some good times here."
    thinking "Well, no time like the present though."
    "Without further ado, I begin my operations."
    thinking "Alright. Where should I go first?"
    jump map__school