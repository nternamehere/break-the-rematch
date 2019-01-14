label tennis__router:
    if tennis__first_visit:
        $ renpy.block_rollback()
    else:
        jump map__school

label tennis__first_visit:
    $ renpy.block_rollback()
    show bg tennis court with map_fade
    "According to my list, the next student was a member of the school's tennis club."
    thinking "There are more guys than girls in this club, now. But back in my time, it was nothing but babes."
    "I snickered to myself as I remembered the girls of the past - and my antics with them."
    "In the present, though, there wasn't much to see. Most of the players were fooling around, not taking training seriously. I wondered what the point of joining the club in the first place was, if not to train?"
    "Perhaps my next target wasn't here at all."
    unknown "My, my. Is that you Mr. Akatsuki?"
    "I felt my heart stop, and time seemed to freeze around me. It was a familiar voice, sure..."
    "...but more importantly, it was a familiar voice that knew who I was. I supposed it could have been one of my teachers, but..."
    unknown "Hey! I'm talking to you, Shinn!"
    "After a moment I turned, facing the one calling to me."

    show ritsuko with moveinright
    ritsuko "Hey, Shinn, if you're going to be coming around like this, at least try to hide the tent you're pitching. For once."
    "A chill went down my spine as I realized that it was none other than Ritsuko. I glanced at the principal's file and noticed the surname..."
    thinking "Yasuhiro. Damn it! I should have noticed it sooner!"
    "I'd been a fool not to realize it - it made perfect sense that someone like her would be failing math."
    shinn "If I had realized you were going to be one of my students, I would've recommended someone else be your tutor."
    ritsuko "Oh my, Shinn. Are you still concerned about that incident?"
    thinking "This is going to be a problem."
    shinn "*chuckle* I guess it makes sense. you were never good at math, though that's hardly a surprise. You certainly don't look like a particularly bright one."
    ritsuko "Oh, you're playing wiht fire, {i}boy{/i}. Are you trying to provoke me?"
    "Ritusko's eyes narrowed, and she bared her teeth. Her near-shouted words caught everyone's attention, and their gazes quickly turned towards us."
    shinn "Careful there, Ritsuko. You don't want everyone in the club to think you're an airhead, eh?"
    "I could almost hear the veins popping in her neck. But it seemed the embarrassment was outpacing the rage - her face turned cherry red."
    "She closed her eyes, sighed, and looked at me again with that condescendingly smug face of hers."
    ritsuko "You should watch your back, Shinn. I know some things about you..."
    ritsuko "...things that you did with a couple of teachers. Maybe more than a couple."
    shinn "Heh. \"Things that I did with teachers\"? Theese are rumors, Ritsuko. Not surprising that you don't know the difference between hearsay and facts."
    ritsuko "Oh? Rumors? I might not have physical evidence, but others' accounts don't lie."
    shinn "Hmph!"
    thinking "Even if I don't want to, it seems I'll have to deal with this bitch if I'm to have any hope of moving forward with my plans."
    shinn "Well, I guess we'll see about that."
    "Ritsuko's face twisted, radiating pure confidence. She bled an arrogance that made her look both vile and extremely seductive."
    ritsuko "Indeed, Shinn. If I ever find the evidence - which I will - you better be careful."
    ritsuko "An animal like you needs to learn to stay in the mud, where it belongs."

    show ritsuko brow smile
    ritsuko "I suggest you leave before you bother anyone further."
    "She gave me a mocking wink."
    shinn "Hmph! In that case, I suppose I'll let you know about the tutoring later. Or maybe I'll just let you fail!"
    "I was so pissed that I stormed from the tennis court without so much as a goodbye."
    "She'd almost caught me during our first year - I'd been having sex with one of the teachers in the second floor storeroom."
    "I guess she heard the noise we were making and decided to investigate the storeroom herself. I managed to close the door before she could get in, but she saw my face as I jammed it shut."
    "If it weren't for that day, today's near-incident wouldn't have occurred. In face, neither of us would have ever known each other."
    "But at least I hadn't been caught for sure. And now I was in a position to make her regret what she'd almost done then and was trying to do now."
    $ tennis_available = False
    $ met_ritsuko = True
    $ tennis__first_visit = False
    hide ritsuko smile
    jump classroom__completed_intro_check
