label classroom__router:
    if classroom__first_visit:
        jump classroom__first_visit
    else:
        show bg classroom with map_fade
        "Under construction"
        jump map__school

label classroom__first_visit:
    scene bg hallway 2 with map_fade
    $ renpy.block_rollback()
    "Feeling satisfied, I checked over the principal's list one last time."
    shinn "Let's see... before I call it a day, is there anything else I should see?"
    "As I looked though the notes, I recongnized a familiar class name. Below it seems some notes had been written by the principal."
    shinn "Hmm? Class 3-2? Isn't this the class I was in my final year?"
    "I glanced through the notes and saw that my tutoring lessons would be held in this room."
    shinn "Wow. Looks like the principal's bringing me on a nostalgia trip."
    shinn "Might as well take a look at the old place, see what's changed."

    show bg classroom with fade
    "A sudden torrent of memories gushed through my brain as I entered the classroom. It was identical to how it had been before I left. Nothing had changed at all."
    shinn "Everything's the same. Heh. Even that crack in the floor, on the classroom's far side. Would have figured someone would have fixed that by now."
    "A dull sound, like the clicking of high-heel shoes, brought me out of my nostalgia trip. It seemed to be coming from the hallway."
    play sound heels
    "The clicking sound grew closer and closer, approaching the classroom door."
    play sound heels
    "A mature-looking, wide-hipped woman appeared in the doorway."

    show rina annoyed with moveinleft
    rina "Excuse me - who are you and what are you doing here?"
    shinn "Er..."
    "The woman entered the classroom without another word and approached."
    rina "Wait a minute... aren't you the tutor we just hired?"
    thinking "That tone of voice... I've got a bad feeling about this..."
    shinn "Yes."
    rina "Hmm... I see. Officially, the tutoring isn't supposed to start until tomorrow. As I suspect you know that, what are you doing here?"
    shinn "Me? Er. I am just taking a look at the class. Getting used to it."
    thinking "Gosh... She seems pretty nosy. But I wonder how sharp she really is?"
    rina "Get used to what? Weren't you a student here before?"
    shinn "Well, yes, but I have not been a student for quite some time. I thought looking around would give me a chance to remember the old days."
    "Rina continued to stare, her expression cold and reminiscent of Satuski's."
    thinking "Geez, these women sure are uptight..."
    shinn "Anyway, since school's out for the day, maybe I should go."
    shinn "After all, wouldn't want to run afoul of the teacher in charge of discipline, right?"

    show rina vicious smile
    rina "Indeed."
    rina "Actually, Takatsukasa briefed me about you already."
    thinking "I feared it would have been Ritsuko. What a relief."
    "Rina's gaze became one of clear disdain, and her smile only made it more obvious."
    "And yet that vicious disdain somehow made her all the more attractive to me..."
    rina "I'm still quite surprised that the principal hired a former student. You were one of our rising stars, were you not? It surprises me that we never met."
    shinn "I aim to surprise."
    "Keeping my cool, I forced myself to think. Who the hell was this woman, really?"
    thinking "I think she joined the academy after I graduated. Which explains why we haven't met."
    "I hadn't realized it, but it seemed I had been staring at Ms. Akiyama too acutely."

    show rina annoyed
    rina "Pssh! At least {i}try{/i} to be subtle."
    rina "Know that you're only a tutor here, Mr. Akatsuki. And I'll be keeping an eye on you."
    rina "If I catch you doing anything suspicious, or even hear about it, I will make sure you're ejected from the premises."

    show rina vicious smile
    rina "You know, I could start asking around about you. I'm sure many people have stories to tell about your time as a student here."
    thinking "Pesky bitch."
    rina "But I suppose it doesn't matter, really. The courses shouldn't last for more than thirty days. Maybe you can behave yourself that long."
    thinking "Seriously, she talks way too much."
    "Trying my best to look and sound polite, I softly responded to Rina."
    shinn "You shouldn't worry, Ms. Akiyama."
    shinn "I know my place here. I'm here as a formality; my presence and tutelage are essentially favors to the principal. It's nothing official."
    shinn "Admittedly, I'm also here for reasons of nostalgia. At least partly."
    shinn "But I will note that I am quite glad that you worry about my performance in these courses. It would look bad in my curriculum if I---"

    show rina angry
    rina "W-who said I was worried about you?!"
    thinking "Whoa! That was unexpected."
    shinn "Now, now. I was merely acknowledging that the only reason you would be concerned about my straightforwardness with my students is due to my teaching acumen. Unless you're suggesting something else, Ms. Akiyama?"
    "A marked change came about the woman."

    show rina pout
    rina "Hmph! Of course not! What else could it be?"
    thinking "Heh, she sure is a smooth liar."
    shinn "In that case, Ms. Akiyama, I will take my leave."
    shinn "I must make some last preperations for the courses. I will be looking forward to working with you, however..."
    rina "Fine, go ahead! Just make sure you don't do anything rash!"
    shinn "Rash, ma'am? Are you still worried about me?"
    rina "O-of course not! Now please, take your leave!"
    shinn "Yes, yes..."
    "As I was about to leave a figure suddenly emerged from the hallway and entered the room."
    thinking "Wait, what? Is that Naoko?"
    naoko "Oh, Rina. There you are."

    show rina pout at right
    show naoko smile at left
    with moveinleft
    rina "Huh? Naoko? What are you doing here?"
    naoko "I was looking for you. The documents that you asked for have been completed."
    naoko "I left the file on your desk. You said it was important, so I thought you should know immediately."
    rina "Ah. Thank you, Naoko."
    "Rina turned and looked at me."
    rina "This is Shinn. He will be assisting some of the students with their studies."
    naoko "I see. Nice to meet you, Shinn."
    thinking "Holy shit. Does she not remember me?"

    show naoko cheerful
    shinn "Nice to meet you, Naoko. I hope I'll be able to work with you as well."
    naoko "Sure! If you need anything, just ask."
    thinking "Has she forgotten what we did?"
    rina "I shall be leaving now."
    naoko "See you."

    hide rina with moveoutright
    show naoko smile at center with moveinright
    "As soon as the door shut behind Rina, Naoko whipped around to face me."

    show naoko basic
    naoko "Why did you bother to come back?!"
    shinn "Huh?"
    naoko "Don't act dumb with me, Shinn. After we had sex you just... {i}dumped{/i} me. I never heard from you again. And now you're just... here!"
    thinking "It seems she {i}hasn't{/i} forgotten after all."
    thinking "Heh. This is getting interesting."
    shinn "So what if I did?"
    naoko "You're worse than a monster, Shinn!"
    thinking "Since it has come this far, I suppose there's no more reason to put this act on."
    shinn "Then you should know why I'm back."
    naoko "What? To have sex with school girls? Did your tastes change?"
    shinn "Heh... what if they did?"
    naoko "Well, you won't succeed this time."
    thinking "Wow. Brave words. I wonder how she plans to stop me."
    shinn "Oh really? How do you plan to stop me?"
    naoko "Why, I'm going to expose you, of course."
    shinn "Oh, are you now? Do you have evidence against me? WOuld anyone believe you, even if you did?"
    naoko "Why you little..."
    "Almost before I could react she darted forward, moving to strike me in the mouth."
    shinn "Woah!"
    "I managed to catch her fist just before it hit home."
    thinking "This bitch is really asking for it now."
    shinn "What do you think you're doing?"
    naoko "LET ME GO!"
    "I shoved her fist away and she jerked back."
    naoko "You bastard!"
    thinking "If I don't teach her a lesson today, she'll being to pester me. My entire plan could be foiled by this bitch."
    shinn "For someone so vehement, I seem to recall you rather enjoying our lovemaking."
    naoko "Maybe, but that was before I knew. There was no love behind our sex - it was all a lie. A lie from a {i}fuckboy{/i} like {i}you{/i}! I {i}hate{/i} you!"
    shinn "Oh yeah?"
    "I suddenly recalled something - I had taken some pictures during our sexual adventures. Pitcures that I had never deleted."
    "I pull my phone from my pocket. Scolling through the gallery, I found the photo I was looking for and turned the phone to face Naoko."
    shinn "Remember this?"
    "It was a picture of Naoko. She was being drowned in pleasure, her naked chest splattered with a load of cum."
    naoko "You..."
    shinn "Do you remember now? Remember the time you wer begging for sex like some animal in heat?"
    naoko "Why do you still have that picture?!"
    thinking "It seems like I've found my first victim."
    shinn "Shall we take a trip down memory lane together?"
    naoko "Eh? What?"
    shinn "Don't act dumb. you know what I mean."
    naoko "You want sex?"
    thinking "She finally figured it out. Smart girl."
    shinn "Well?"
    naoko "...what if I don't comply?"
    shinn "I have pictures in my phone, and on my PC, that will instantly end your career as a teacher."
    "Naoko's expression changed immediately. She radiated defeat."
    jump naoko__sex_scene_1
