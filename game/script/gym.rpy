label gym__router:
    if gym__first_visit and day == 1:
        jump gym__first_visit
    if pool_gym__first_visit:
        jump pool_gym__first_visit
    jump map__school

label pool_gym__first_visit:
    $ renpy.block_rollback()
    show bg pool with map_fade
    if met_ritsuko:
        "The swimming pool wasn't too far from the tennis court, but I had to take a little detour in case Ritsuko was planning something."
    shinn "Now this is more like it!"
    "It was hard to keep my voice down. The most delicious sight so far faced me: a number of girls in wonderfully tight, blue competitive swimsuits strolled around or enthusiastically swam across the pool."
    "Their busty, fit bodies were a paradise; their figures, accentuated by the tight fabric, left little to the imagination."
    thinking "There's plenty of material to pick from here."
    "Or, at least, there would be. But there was only one person who {i}really{/i} interested me: Aina Aozaki."
    "The principal had been fawning over her when he briefed me, as if he had a thing for her. It was a quaint idea and completely out of the realm of possibility."
    thinking "I hope she lives up to my expectations."
    unknown "Hm? Sir? May I ask who you are?"
    shinn "Huh?"
    "A soft, confident voice echoed behind me."
    if met_ritsuko:
        "Unlike that bitchy blonde, this voice was far more dignified and had a tone of kindness to it."

    show aina basic with moveinright
    "I turned to find myself face-to-face with a blue-haired beauty. Her stunning eyes matched her hair."
    shinn "Good evening."
    thinking "Looks like I wasn't expecting too much, after all."
    "What captivated me most was the confidence that she seemed to exude - it was soothing, but I stayed on-guard."
    shinn "Hey - are you the famous Aina Aozaki?"
    "The girl smiled at me and bowed her head respectfully."
    aina "Indeed I am. With whom do I have the pleasure of speaking?"
    thinking "She seems more approachable than the others."
    "I smiled at her, bowing my head in return."
    shinn "I am Shinn Akatsuki. The principal assigned me to be your tutor."
    aina "*sigh* Is this regarding my recent grades?"
    shinn "I'm afraid so, Miss Aozaki."

    show aina eyes shut
    "She winced, though no confidence left her posture."
    aina "I can positively say that I can recover on my own. However, understanding the fact that this is our last year..."
    aina "I guess we can't really help it. Classes are definitely more important than mere club activities. I should have remembered that."
    shinn "You are quite wise, Miss Aozaki."
    "She giggled."
    aina "Please, just call me Aina."
    shinn "Aina it is."
    aina "Did you come all the way to just find me, Mr. Akatsuki?"
    shinn "*chuckle* Why so formal? Just call me Shinn."
    shinn "And indeed. I always try to be as resourceful as possible."

    show aina warm smile
    aina "I like that."
    if met_ritsuko:
        aina "It means we won't be wasting too much time."
        shinn "You're quite concerned with time. Same as Ms. Katsuragi."
        show aina surprise
        aina "Katsuragi? Is she going to be taking courses as well?"
        "I nodded. Aina sighed."
        aina "I suppose that makes sense."
        aina "Satsuki always does seem to pay more attention to her club activities than her actual studies."
        shinn "And how about you?"
        aina "Me? Well, I'm just simply not good with math."
        aina "Even simple arithmetic makes me lose my patience."
    unknown "Aina? Is something happening?"
    "Another person appeared from around a corner. She approached Aina and stopped beside her."

    show aina surprise at right
    show touko shy basketball at left
    with moveinleft
    "This new student wore a basketball uniform, which, despite its looseness over her body, still showed her ample and sculpted curves."
    aina "Good evening, Touko!"

    show aina warm smile
    if met_ritsuko:
        "The student called Touko stared at me for a second, as if perplexed, reminding me of how Satsuki had looked at me earlier."
    else:
        "The student called Touko stared at me for a second, as if perplexed."
    "Aina, looking from me to her friend and back again, giggled."
    aina "Oh, this is Mr. Shinn Akatsuki. He is the tutor the principal told us about the other day."
    thinking "Seems the principal hasn't told them anything more than that they needed tutoring."
    touko "Pleased to meet you, Mr. Akatsuki. I was just talking to Satsuki about you. I'm sure you remember her?"
    "I nodded politely."
    thinking "Satsuki... Of course"
    shinn "Yes, how could I forget?"
    "It seemed they all knew each other, which made things a little easier for me..."
    thinking "Heh, depending on the depth of their relationship, I might be able to bang all of them at the same time!"
    touko "So, Mr. Akatsuki, what brings you to our club?"
    shinn "As I was just telling Aina, I like doing work \"in advance,\" if you catch my meaning. *chuckle*"
    "Touko nodded, though I wasn't sure if she caught my meaning."
    touko "I see."
    touko "You're lucky to find me here, then. We're usually practicing for our next match at the gymnasium."
    shinn "Fair enough. Say - are these courses inconvenient to either of you?"
    touko "Not really."
    aina "Well, I could certainly live without them, but..."
    touko "But we don't have much choice. If we flunk, we need to recover."
    touko "It's our last year, after all."
    aina "Not to mention that the prefectural is coming soon!"
    aina "They could end up blocking our participation if we fail any more tests!"
    touko "That's why we need to take things with a cool head, Aina."
    aina "Ah! You're always so wise, Touko"
    "I noticed how warm Aina's smile was towards Touko."
    thinking "Hmm... Are they good friends? Or maybe something more?"
    "Touko's eyes shifted towards me. She gave a soft smile, keeping her cool manner."
    touko "I look forward to our lessons, Mr. Akatsuki."
    "Touko's attention shifted back to Aina, and she gave a soft sigh. Aina, apparently noticing her, shot her a small grin."
    aina "Mr. Akatsuki, could you please excuse us? I just remembered we had an important..."
    aina "...thing"
    shinn "That's fine. Our lessons won't begin until tomorrow. I still have to make preperations."
    aina "Thank you!"
    "And just like that, the two attractive girls left to places unknown."

    hide aina warm smile
    hide touko shy basketball
    with moveoutleft
    thinking "Interesting..."
    "It was a pleasant surprise to find two girls here at once."
    thinking "The way Touko was looking at Aina was quite suspicious..."
    shinn "*chuckle*"
    "Keeping this exchange in mind, I left for my next destination..."

    $ pool_gym__first_visit = False
    $ pool_gym_available = False
    jump map__school

label gym__first_visit:
    $ gym__first_visit = False
    scene bg gym balls with map_fade
    "Although it was still early in the morning, I heard from the principal that some members of the basketball team come in for practice before school starts."
    "Curious to check it out, I decided to visit the basketball court."
    "I take a quick look around the premises. Doesn’t seem like anyone’s around."
    play sound basketball_dribble
    "Or so I thought..."
    "In the distance, I spot a lone student practicing basketball."
    "As I approach the student, it becomes obvious who it is."
    
    show touko shy basketball with moveinleft
    "Seems like Touko’s getting some morning training done by herself."
    "She notices my presence and turns around."
    touko "Oh, Shinn. Good Morning. What brings you here?"
    "She seems surprised..."
    shinn "Good Morning, Touko. I was just checking to see if you were in for morning practice."
    touko "Ah, yes. I usually only make it in now and then, but when nationals are coming up, I try to push myself to get extra training in every day."
    shinn "I see. That’s some pretty impressive determination."
    touko "Thanks. I love basketball, so I figure it’s worth putting in the effort for."
    shinn "It’s good that you’re doing what you love. But don’t forget you have other priorities too."
    touko "Oh, right, I did almost forget, actually. I have a tutoring session with you this afternoon, right?"
    shinn "That’s right. Please don’t forget about it."
    touko "What’s today topic going to be?"
    shinn "Since it’s the first session, I’ll start off with some testing to get a sense of where your academics are currently."
    touko "Oh, okay."
    menu:
        thinking "Hmm... Since it’s just the two of us here, maybe I should ask her some questions."
        "Ask about her relationship with Aina.":
            $ renpy.block_rollback()
            jump ask_about_aina
        "Ask about her academic issues.":
            $ renpy.block_rollback()
            jump ask_about_academics
