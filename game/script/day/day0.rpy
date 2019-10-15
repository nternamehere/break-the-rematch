label day_0__start:
    play sound alarm_loop loop
    unknown "Hmm..."
    "An incessant ringing pesters my ears as I lift my head from the soft bedsheets and pillows."
    unknown "Hmm..."
    "I was having the most comfortable, enjoyable dream... but now it's gone, swept away by this annoying alarm."
    unknown "Hmm... What time is it...?"

    show bg shinn bedroom with pixellate
    "I look above the sheets, the old digital clock's red numbers seemingly staring back at me, demanding that I rise. The blurriness of sleep slowly begins to fade as I focus on the time."
    unknown "Oh... It's already 6 AM. I should get going."
    "The alarm clock continues to ring"
    unknown "Alright, alright, I'm going! Damn, this thing is loud..."
    stop sound
    play sound alarm_shutoff
    "My clock keeps ringing for some time before I muster the will to turn it off. As I rose, I noticed a blinking light on my answering machine."
    unknown "Hm? Who could this be?"
    "I approach the machine and hit the \"play message\" button."
    voicemail "Mr. Akatsuki Shinn. All the paperwork is now organized and we're ready for you to start. I need you to come in today after classes have concluded. Club activities begin at 3:45 pm, which should give you a wide window to arrive on time."
    thinking "Oh, that's great."
    thinking "Heh. Looks like I didn't need to get up so early after all. But since I'm already awake, I might as well as get prepared now."
    "I begin preparations for my first day of tutoring."

    $ renpy.music.play(audio.campus, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    show bg main gate with fade
    "Haruka Academy. I was once a student here, and my time was... exciting, to say the least. It's hard to believe that I'm back here again, working for the school rather than studying in it."
    "As I approach the school gate, I scan the inner courtyard."
    shinn "This place is awfully calm."
    thinking "Not surprising, since it's after-hours."
    thinking "Ah, but even without students around, seeing the campus again sure brings back memories."
    "Laughing under my breath, I immediately head for the Principal's office."

    show bg hallway 1 with blinds
    shinn "Well, that settles it."
    "The meeting with the Principal was quite simple. All I had to do was help a small group of students with their studies. Apparently, those on the list he gave me excelled in athletics, but were simply hopeless in arithmetic."
    "Conveniently enough, all of them are female senior students. Close to finishing their studies and beginning college and adult life."
    thinking "Heh. I guess it's natural for athletes to suck at more complex subjects."
    thinking "Speaking of, I wonder if those students have arrived yet?"
    thinking "First, I should scout this place out and get used to the schedules. They can't be too different from when I was here."
    "I look over the schedule the Principal gave me during our meeting."
    thinking "Let's see... who should I check out first..."
    jump map__school

label archery__day_0:
    $ quick_menu = True
    $ renpy.block_rollback()
    show bg range with map_fade
    "..."
    "..."
    play sound arrow
    thinking "This place feels alive, that's for sure."
    "In the two years since I graduated, the archery club seems to have grown a great deal. I remember it only having a dozen members."
    "Now the dojo is filled with students, most of whom happen to be female."
    shinn "...Oh?"
    "The continuous sound of bows being drawn and released finally draws my attention to the sole figure actually shooting."
    "The gathered students seem focused on her as well. Some are solemn, focused on her movements, whereas others are clearly watching the girl with wide-eyed admiration."
    "Curious, I step closer, trying to keep from attracting too much attention."

    show satsuki archery with dissolve
    thinking "Oh, wow."
    "I focus on the beautiful young woman. Her raven hair, tied in a traditional manner, flows over her shoulder. The pins embedded in her braid give her a certain old-fashioned air, yet the effect this has on the rest of her appearance gives off an impossible-to-ignore beauty."
    "Her expression is serious and cold, and she has eyes only for her target."
    play sound arrow
    "Without any effort at all she draws the bow and releases her shot. The arrow arcs perfectly into the center of a target 60 meters away."
    "The students immediately burst into cheers and applause."
    female_1 "As expected from Miss Katsuragi! She isn't our most valuable club member for nothing!"
    female_2 "She's so beautiful... I wish I was as good as Miss Katsuragi!"
    male "With her at our head, we'll win regionals again for sure!"
    thinking "So she's the star of the archery club. Quite popular with the students, too."
    thinking "It's no wonder why everyone idolizes her so much – she's from the prestigious Katsuragi clan."
    "I take a closer look at the girl, my eyes straying to follow the supple curves of her breasts."
    thinking "Very high class. Definitely worthy of being one of my interests."
    "Katsuragi turns, unsmiling, to look at the small audience of students who continue to cheer and praise her. She's like an idol."

    scene bg range
    show satsuki uniform cocky
    with dissolve
    "I slowly notice that Katsuragi's eyes are fixed on me. I can't read her expression, whether it projects simple curiosity or condescension."
    "The other students follow her gaze. Soon, everyone is aware of my presence."
    thinking "This might be inconvenient."
    "I fight the urge to hesitate, keeping my cool, and approach Satsuki."
    "Although she's clearly younger than I am, she really does have an aura of maturity, as if she were a woman ready for marriage."
    shinn "Good evening, Miss Katsuragi."
    satsuki "..."
    thinking "Talk about getting the cold shoulder."
    "Satsuki stands composed, glaring at me with cold eyes."
    "That's interesting. Most girls would have been startled by my sudden presence."
    "But I suppose that club members, especially their star members, have a tendency to be territorial. Perhaps it doesn't matter who I am, just that I'm here at all. A trespasser."
    shinn "My apologies, Miss Katsuragi. I'm Shinn Akatsuki. I was assigned to be your tutor."
    "She tilts her head to the side, as if perplexed, but says nothing."
    thinking "This is getting tiresome."
    shinn "Is there any chance for us to talk? That is, if you're not busy."
    "Her lips twitch, forming a concerned frown."
    satsuki "What is it you wish to discuss, Mr. Akatsuki?"
    thinking "I have to play this smoothly. Don't screw up."
    "I take a deep breath and put on my most dashing smile."
    shinn "Merely your grades in mathematics. I've come on request from the Principal."
    satsuki "I see."
    "The young woman's calm seems to resonate with everyone in the dojo - including me."
    satsuki "So you are the one our director told us about."
    shinn "I see my reputation precedes me."
    satsuki "Perhaps. I do not really see the need for such measures, but if he insists..."
    
    show satsuki uniform upset
    satsuki "I should have expected this. Club activities take up so much time..."
    shinn "Ah, but it's not out of the ordinary to take some time off to study."
    shinn "Besides, if you fail your classes you'd have to give up your club activities anyway, wouldn't you?"
    "She stares back at me. I had expected her to be startled, but instead her narrow gaze reveals annoyance."
    satsuki "Listen – we have regionals very soon. I'm putting all of my effort into them."
    shinn "Indeed, but wouldn't it be more favorable for you, your team, and the Academy if you were to excel in your academics as well?"
    "Satsuki goes silent once more, visibly pondering the very simple logic I'd laid out before her."
    thinking "Either she's dense or she's trying to play me off."
    thinking "I might have to be more forceful with her if she gets too troublesome."
    satsuki "Can you promise that my club activities will not be interrupted by our studying?"
    "I smirk back at her, trying to control myself."
    shinn "Of course not. Everything's been considered."
    
    show satsuki uniform basic
    satsuki "Very well."
    satsuki "Can I expect you to get in touch with me soon?"
    shinn "Of course. The Principal gave me your contact information. I'm looking forward to it!"
    "Continuing to smile, I bow my head as a gesture of respect."
    shinn "I shall leave you to continue your activities then, Miss Katsuragi. Have a good day."
    satsuki "Likewise, Mr. Akatsuki."
    "With a single nod, Satsuki returns her focus to the range."

    hide satsuki uniform basic with moveoutleft
    thinking "That took longer than expected..."
    "But it was quite worth it. I met the school's archery star, and she happens to be a complete babe. I mentally plan to \"check in\" with her very soon."
    thinking "Hmm... Who I should I see next?"
    $ range_available = False
    jump map__school

label tennis__day_0:
    $ quick_menu = True
    $ renpy.block_rollback()
    show bg tennis court with map_fade
    "According to my list, the next student is a member of the school's tennis club."
    thinking "There are more guys than girls in this club now, but back in my time, it was nothing but babes."
    "I snicker to myself as I remember the girls of the past – and my antics with them."
    "In the present, though, there isn't much to see. Most of the players are fooling around, not taking their training seriously. I wonder what the point of joining the club in the first place was, if not to train?"
    "Perhaps my next target isn't here after all."
    unknown "My, my. Is that you Mr. Akatsuki?"
    "I feel my heart stop, and time seems to freeze around me. That was a familiar voice, to be sure..."
    "...but more importantly, it was a familiar voice that knew who I was. I suppose it could have been one of my teachers,  but..."
    unknown "Hey! I'm talking to you, Shinn!"
    "After a moment I turn, facing the one calling to me."

    show ritsuko tennis basic with moveinright
    ritsuko "Hey, Shinn. If you're going to be coming around like this, at least try to hide the tent you're pitching for once."
    "A chill runs down my spine as I realize that it's none other than Ritsuko. I glance at the Principal's file and notice the surname..."
    thinking "Yasuhiro. Damn it! I should have realized it sooner!"
    "I'd been a fool not to catch that – it makes perfect sense that someone like her would be failing math."
    shinn "If I had realized you were going to be one of my students, I would've recommended that someone else be your tutor."
    ritsuko "Oh my, Shinn. Are you still concerned about that incident?"
    thinking "This is going to be a problem."
    shinn "Heh. I guess it makes sense. You were never good at math, though that's hardly a surprise. You certainly don't look like a particularly bright one."
    ritsuko "Oh, you're playing with fire, boy. Are you trying to provoke me?"
    "Ritsuko's eyes narrow, and she bares her teeth. Her almost-shouted words catch everyone's attention, and their gazes quickly turn towards us"
    shinn "Careful there, Ritsuko. You don't want everyone in the club to think you're an airhead, eh?"
    "I can almost hear the veins popping in her neck. But it seems her embarrassment is outpacing her rage – her face turns cherry red."
    "She closes her eyes, sighs, and looks at me again with that condescendingly smug face of hers."
    ritsuko "You should watch your back, Shinn. I know some things about you..."
    ritsuko "...Things that you did with a couple of teachers. Maybe more than a couple."
    shinn "Heh. \"Things that I did with teachers\"? Those are rumors, Ritusko. Not surprising that you don't know the difference between hearsay and facts."
    ritsuko "Oh? Rumors? I might not have physical evidence, but others' accounts don't lie."
    shinn "Hmph!"
    thinking "Even if I don't want to, it seems like I'll have to deal with this bitch if I'm going to have any hope of moving forward with my plans."
    shinn "Well, I guess we'll see about that."
    "Ritsuko's face twists, radiating pure confidence. She bleeds an arrogance that makes her look both vile and extremely seductive."
    ritsuko "Indeed, Shinn. If I ever find the evidence – which I will – you'd better be careful."
    ritsuko "An animal like you needs to learn to stay in the mud where it belongs."

    show ritsuko tennis smile
    ritsuko "I suggest you leave before you bother anyone further."
    "She gives me a mocking wink."
    shinn "Hmph! In that case, I suppose I'll let you know about the tutoring later. Or maybe I'll just let you fail!"
    "I’m so pissed that I storm off the tennis court with so much as a goodbye."
    "She'd almost caught me back when she was a first-year - I'd been having sex with one of the teachers in the second floor storeroom. I guess she heard the noise we were making and decided to investigate the storeroom herself. I managed to close the door before she could get in, but she saw my face as I jammed it shut."
    "If it weren't for that day, today's near-incident wouldn't have occurred. In fact, neither of us would have ever known each other."
    "But at least she hadn't caught me for sure. And now I'm in a position to make her regret what she almost did then, and what she's trying to do now."
    hide ritsuko tennis smile
    $ tennis_available = False
    jump map__school

label gym__day_0:
    $ quick_menu = True
    $ renpy.block_rollback()
    show bg pool with map_fade
    if not tennis_available:
        "The swimming pool isn't too far from the tennis court, but I had to take a little detour in case Ritsuko was planning something."
    shinn "Now this is more like it!"
    "It's hard to keep my voice down. I'm facing the most delicious sight so far: a number of girls in wonderfully tight, blue competitive swimsuits are strolling around or enthusiastically swimming across the pool."
    "Their busty, fit bodies were a paradise. Their figures are accentuated by the tight fabric that leaves little to the imagination."
    thinking "There's plenty of material to pick from here."
    "Or, at least, there could be. But there's only one person here who really interests me: Aina Aozaki."
    "The Principal practically fawned over her when he briefed me, as if he had a thing for her. It was a quaint idea and completely outside the realm of possibility."
    thinking "I hope she lives up to my expectations."
    unknown "Hmm? Sir? May I ask who you are?"
    shinn "Huh?"
    "A soft but confident voice echoes behind me."

    if not tennis_available:
        "Unlike that bitchy blonde's, this voice is far more dignified, and has a tone of kindness to it."
    
    show aina pool basic with moveinright
    "I turn to find myself face-to-face with a blue-haired beauty. Her stunning eyes match her hair."
    shinn "Good evening."
    thinking "Looks like I wasn't expecting too much after all."
    "What captivates me most is the confidence she seems to exude– it's soothing, but I stay on my guard."
    shinn "Hey – are you the famous Aina Aozaki?"
    "The girl smiles at me and bowed her head respectfully."
    aina "Indeed I am. With whom do I have the pleasure of speaking?"
    thinking "She seems more approachable than the others."
    "I smile at her, bowing my head in return."
    shinn "I am Shinn Akatsuki. The Principal assigned me to be your tutor."
    aina "Haah... Is this regarding my recent grades?"
    shinn "I'm afraid so, Miss Aozaki."
    
    show aina pool basic eyes
    "She winces, though the confidence doesn't leave her posture."
    aina "I can positively say that I can recover on my own. However, understanding the fact that this is our last year..."
    aina "I guess it can't really be helped. Classes are definitely more important than mere club activities. I should have remembered that."
    shinn "You are quite wise, Miss Aozaki."
    "She giggles."
    aina "Please, just call me Aina."
    shinn "Aina it is."
    aina "Did you come all this way to just find me, Mr. Akatsuki?"
    shinn "Heh. Why so formal? Just call me Shinn."
    shinn "And indeed. I always try to be as resourceful as possible."
    
    show aina pool basic
    aina "I like that."
    aina "It means we won't be wasting too much time."

    if not tennis_available:
        shinn "You're quite concerned with time. Same as Ms. Katsuragi."

        show aina pool surprise
        aina "Katsuragi? Is she going to be taking courses as well?"
        "I nodded. Aina sighed."
        aina "I suppose that makes sense."
        aina "Satsuki always does seem to pay more attention to her club activities than her actual studies."
        shinn "And how about you?"
        aina "Me? Well, I'm simply not good with math."
        aina "Even simple arithmetic makes me lose my patience."
    else:
        shinn "Sounds pretty responsible. I guess you care a lot about being efficient?"
        aina "I wish I could say that."
        aina "To be honest, I really do need the help."
        aina "I've always had a hard time with math, and now that it's this far into my last semester, I've got a lot to catch up with and not a lot of time to do it in."

    unknown "Aina? Is something happening?"
    "Another person appears from around a corner. She approaches Aina and stops beside her."
    
    show aina pool surprise at right
    show touko basketball shy at left
    with moveinleft
    "The new student is wearing a basketball uniform, which despite its looseness over her body still shows her ample and sculpted curves."
    aina "Good evening, Touko!"

    show aina pool basic
    "The student called Touko stares at me for a second, as if perplexed."
    "Aina, looking from me to her friend and back again, giggles."
    aina "Oh, this is Mr. Shinn Akatsuki. He's the tutor the principal told us about the other day."
    thinking "Seems the Principal briefed them all in advance that they were going to be getting outside help."
    touko "Pleased to meet you, Mr. Akatsuki. I believe the Principal said that you used to be a student here yourself?"
    "I nod politely."
    shinn "Yes, a couple of years ago."
    shinn "In my last year, we should actually have been attending at the same time, but I'm afraid I don't think we've ever met before."
    touko "I see. In that case, welcome back Mr. Akatsuki."
    touko "So, what brings you to our club?"
    shinn "As I was just telling Aina, I like doing work \"in advance,\" if you catch my meaning."
    "Touko nods, though I doubt if she really understood."
    touko "I see."
    touko "You're lucky to find me here, then. We're usually practicing for our next match at the gymnasium."
    shinn "Fair enough. Say – are these courses inconvenient to either of you?"
    touko "Not really."
    aina "Well, I could certainly live without them, but..."
    touko "But we don't have much choice. If we flunk, we need to recover."
    touko "It's our last year, after all."
    aina "Not to mention that the prefectural is coming soon!"
    aina "They could end up blocking our participation if we fail any more tests!"
    touko "That's why we need to take things with a cool head, Aina."
    aina "Ah! You're always so wise, Touko."
    "I notice how warmly Aina smiles towards Touko."
    thinking "Hmm... Are they good friends? Or maybe something more?"
    "Touko's eyes shift towards me. She gives a soft smile, maintaining her cool manner."
    touko "I look forward to our lessons, Mr. Akatsuki."
    "Touko returns her attention to Aina, and she gives a soft sigh. Aina, apparently noticing her, shoots her a small grin."
    aina "Mr. Akatsuki, could you please excuse us? I just remembered we had an important...thing."
    shinn "It's fine. Our lessons won't begin until tomorrow. I still have to make preparations."
    aina "Thank you!"
    "And just like that, the two attractive girls leave for places unknown."

    hide aina pool basic
    hide touko basketball shy
    with moveoutleft
    thinking "Interesting..."
    "Touko's sudden appearance interrupted my nascent conversation with Aina, but it also saved me the trouble of looking for the other girl."
    thinking "The way Touko was looking at Aina was quite suspicious..."
    shinn "Heheh..."
    "Keeping this exchange in mind, I leave for my next destination..."
    $ gym_available = False
    jump map__school

label track__day_0:
    $ quick_menu = True
    $ renpy.block_rollback()
    show bg track with map_fade
    thinking "Damn, it's hotter than I expected."
    "Only as I arrive at the track does the heat of the day really hit me."
    shinn "Still, it's a little too late for it to be like this, no?"
    "I sigh in resignation and begin looking for my next student. Unlike the others, the Principal barely told me anything about her."
    "I'd gathered that she was supposed to be rather reserved."
    thinking "Quite strange for a star athlete."
    "I have other issues to keep in mind though. Although I don't stand out as badly here as with the other clubs, I maintain my guard."
    thinking "I shouldn't have so much trouble finding a girl like this..."
    "As I walk around the track, I finally spot someone who catches my interest."
    
    show araki track basic with moveinright
    unknown "..."
    "The girl watches me as I approach, and I watch her back."
    "Her pretty blue eyes are gentle, though they also show her exhaustion."
    thinking "Ah, this must be Araki. Her demeanor is an obvious give away."
    "Smiling, I close the distance between us."
    shinn "Good evening. Are you Miss Shinjugai?"
    
    show araki track shy
    araki "..."
    "The girl hesitates a moment before responding, but then nods."
    thinking "What's with this girl?"
    "We maintain eye contact for an awkward length of time. Eventually, I decide to break the silence, trying to keep a cool and friendly appearance."
    shinn "I'll be your tutor from now on. I just wanted us to get acquainted."
    araki "I see..."
    "Her voice is soft, almost a whisper."
    thinking "Damn, she's cute."
    shinn "Are you feeling well?"

    show araki track upset
    araki "I don't... know you."
    thinking "...What?"
    shinn "Oh, don't worry. I'm just here on behalf of the Principal."
    araki "Ms. Akiyama told me about a tutor, but..."
    shinn "But what?"
    araki "...But I thought you would be older."
    thinking "Well, she's certainly a peculiar girl."
    thinking "Observant, in a strange sort of way."
    shinn "Oh? Older? As in...?"
    araki "You look like a student."
    araki "I thought you were one..."
    shinn "Heh. Well, I was a student here, after all."

    show araki track blush
    araki "Oh? You were?"
    "Araki's aura of reservation seems to lift somewhat."
    shinn "Oh yes. I graduated only a couple of years ago."
    araki "Ah... That explains it, then..."
    thinking "She's very cute indeed. It'll be fun to screw her."
    "I take a step closer."
    shinn "That's all I have to discuss for now. Once something more comes up, you'll hear from me again."
    araki "Oh... Okay..."
    araki "In that case, I'll be going then. See you soon."
    shinn "Alright. Take care."
    "With a small nod, Araki walks away."
    hide araki track basic with moveoutright
    $ track_available = False
    jump map__school

label classroom__day_0:
    $ quick_menu = True
    scene bg hallway 2 with map_fade
    $ renpy.block_rollback()
    "Feeling satisfied, I check over the Principal's list one last time."
    shinn "Let's see... before I call it a day, is there anything else I should see?"
    "As I look through the notes, I recognize a familiar class name. Below it there are some notes written by the Principal."
    thinking "Hmm? Class 3-2? Isn't this the class I was in my final year?"
    "I glance through the notes and see that my tutoring lessons are going to be held in this room."
    shinn "Wow. Looks like the Principal's bringing me on a nostalgia trip."
    shinn "Might as well take a look at the old place, see what's changed."

    show bg classroom with fade
    "A sudden torrent of memories rushes through my brain as I enter the classroom. It's identical to how it was before I left. Nothing has changed at all."
    shinn "Everything's the same. Heh. Even that crack in the floor, on the classroom's far side. I figured someone would have fixed that by now."
    "A dull sound, like the clicking of high-heeled shoes, brings me out of my nostalgia trip. It seems to be coming from the hallway."
    $ renpy.music.set_volume(.50, 0.0, channel = "sound")
    play sound heels
    "The clicking sound grows closer and closer, approaching the classroom door."
    play sound heels
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    "A mature-looking, wide-hipped woman appears in the doorway."
    
    show rina suit annoyed with moveinleft
    unknown "Excuse me – who are you and what are you doing here?"
    shinn "Er..."
    "The woman enters the classroom without another word and approaches me."
    unknown "Wait a minute... Aren't you Shinn, the tutor we just hired?"
    thinking "That tone of voice... I've got a bad feeling about this..."
    shinn "Yes."
    unknown "Hmm... I see."
    unknown "I'm Rina Akiyama, the teacher responsible for disciplinary standards here."
    rina "Officially, the tutoring isn't supposed to start until tomorrow. I suspect you know that, so what are you doing here?"
    shinn "Me? Er. I'm just taking a look at the class. Getting used to it."
    thinking "Gosh... she seems pretty nosy. But I wonder how sharp she really is?"
    rina "Get used to what? Weren't you a student here before?"
    shinn "Well, yes, but I haven't been a student for quite some time. I thought looking around would give me a chance to remember the old days."
    "Rina continues to stare, her cold expression reminiscent of Satsuki's."
    thinking "Geez, these women sure are uptight..."
    shinn "Anyway, since school's out for the day, maybe I should go."
    shinn "After all, wouldn't want to run afoul of the teacher in charge of discipline, right?"
    
    show rina suit confident
    rina "Indeed."
    rina "Actually, Miss Takatsukasa briefed me about you already."
    thinking "I was afraid it might have been Ritsuko. What a relief."
    "Rina's gaze becomes one of clear disdain, which her smile only makes more obvious."
    "And yet, that vicious disdain somehow makes her all the more attractive to me."
    rina "I'm still quite surprised that the Principal hired a recent student. You were one of our rising stars, were you not? It surprises me that we never met."
    shinn "I aim to surprise."
    "Keeping my cool, I force myself to think. Do I know anything about this woman I'm dealing with?"
    thinking "I think she joined the academy after I graduated, which explains why we haven't met."
    "Without my realizing, it seems I've been staring too closely for Ms. Akiyama's tastes."
    
    show rina suit annoyed
    rina "Pssh! At least {i}try{/i} to be subtle."
    rina "Know that you're only a tutor here, Mr. Akatsuki. And I'll be keeping an eye on you."
    rina "If I catch you doing anything suspicious, or even hear about it, I will make sure you're ejected from the premises."
    
    show rina suit confident
    rina "You know, I could start asking around about you. I'm sure many people have stories to tell about your time as a student here."
    thinking "Pesky bitch"
    rina "But I suppose it doesn't matter, really. The courses shouldn't last for more than thirty days. Maybe you can behave yourself that long."
    thinking "Seriously, she talks way too much."
    "Trying my best to seem polite, I softly respond to Rina."
    shinn "You shouldn't worry, Ms. Akiyama."
    shinn "I know my place here. I'm here on an informal basis; my presence and instruction are essentially favors to the Principal. It's nothing official."
    shinn "Admittedly, I'm also here for reasons of nostalgia, at least partly."
    shinn "But I will say that I'm quite glad to hear your worries about my performance in these courses. It would look bad for my curriculum if I--"
    
    show rina suit annoyed
    rina "W-who said I was worried about you?!"
    thinking "Whoa! That was unexpected."
    shinn "Now, now. I was just acknowledging that the only reason you would be concerned about my work with my students is due to short record of experience. Unless you're suggesting something else, Ms. Akiyama?"
    "A marked change comes about her as I pose my question."
    
    show rina suit pout
    rina "Hmph! Of course not! What else could it be?"
    thinking "Heh, real smooth there."
    shinn "In that case, Ms. Akiyama, I will take my leave."
    shinn "I must make some last preparations for the courses. I will be looking forward to working with you, however..."
    rina "Fine, go ahead! Just make sure you don't do anything rash!"
    shinn "Rash, ma'am? Are you still worried about me?"
    rina "O-of course not! Now please, take your leave!"
    shinn "Yes, yes..."
    "As I'm about to leave, a figure suddenly emerges from the hallway and enters the room."
    thinking "Wait, what? Is that Naoko?"
    naoko "Oh, Rina. There you are."
    
    show rina suit pout at right
    show naoko suit smile at left
    with moveinleft
    rina "Huh? Naoko? What are you doing here?"
    naoko "I was looking for you. The documents that you asked for have been completed."
    naoko "I left the file on your desk. You said it was important, so I thought you should know immediately."
    rina "Ah. Thank you, Naoko."
    "Rina turns and looks at me."
    rina "This is Shinn. He will be assisting some of the students with their studies."
    naoko "I see. Nice to meet you, Shinn."
    thinking "Holy shit. Does she not remember me?"
    
    show naoko suit happy
    shinn "Nice to meet you, Naoko. I hope I'll be able to work with you as well."
    naoko "Sure! If you need anything, just ask."
    thinking "Has she forgotten what we did?"
    rina "I shall be leaving now."
    naoko "See you."

    hide rina suit pout with moveoutright
    show naoko suit smile at center with moveinright
    "As soon as Rina shuts the door behind her, Naoko whips around to face me."
    
    show naoko suit angry
    naoko "Why did you bother to come back?!"
    shinn "Huh?"
    naoko "Don't act dumb with me, Shinn. After we had sex you just... dumped me. I never heard from you again. And now you're just... here!"
    thinking "Looks like she hasn't forgotten after all."
    thinking "Heh. This is getting interesting."
    shinn "So what if I did?"
    naoko "You're worse than a monster, Shinn!"
    thinking "Since it's come this far, I suppose there's no more reason to keep up the act."
    shinn "Then you should know why I'm back."
    naoko "What? To have sex with schoolgirls? Or did your tastes change?"
    shinn "Heh... what if they did?"
    naoko "Well, you won't succeed this time."
    thinking "Wow. Brave words. I wonder how she plans to stop me."
    shinn "Oh really? And what exactly would you do about it then?"
    naoko "Why, I'm going to expose you, of course."
    shinn "Oh, are you now? Do you have evidence against me? Would anyone believe you, even if you did?"
    naoko "Why you little..."
    "Almost before I can react she darts forward, moving to strike me in the mouth."
    shinn "Woah!"
    "I manage to catch her fist just before it hits home."
    thinking "This bitch is really asking for it now."
    shinn "What do you think you're doing?"
    naoko "LET ME GO!"
    "I shove her fist away and she jerks back."
    naoko "You bastard!"
    thinking "If I don't teach her a lesson today, she's bound to keep going after me. My entire plan could be foiled by this bitch."
    shinn "For how vehement you're being now, I seem to recall you rather enjoying our lovemaking."
    naoko "Maybe, but that was before I knew. There was no love behind our sex – it was all a lie. A lie from a fuckboy like you! I hate you!"
    shinn "Oh yeah?"
    "I suddenly recall something – I had taken some pictures during our sexual adventures. Pictures that I had never deleted."
    "I pull my phone from my pocket. Scrolling through the gallery, I find the object I was searching for and turn the phone to face Naoko."
    shinn "Remember this?"
    "It’s a picture of Naoko, drowning in pleasure, her naked chest splattered with a load of cum."
    naoko "You..."
    shinn "Do you remember now? Remember the time you were begging for sex like an animal in heat?"
    naoko "Why do you still have that picture?!"
    thinking "It seems I've found my first victim."
    shinn "Shall we take a trip down memory lane together?"
    naoko "Eh? What?"
    shinn "Don't act dumb. You know what I mean."
    naoko "You want sex?"
    thinking "She finally figured it out. Smart girl."
    shinn "Well?"
    naoko "...What if I don't comply?"
    shinn "I have pictures in my phone and on my PC that will instantly end your career as a teacher."
    "Naoko's expression changes immediately. Her face crumples in defeat."
    jump naoko__cg_1

label day_0__end:
    $ quick_menu = True
    scene bg main gate with fade
    stop music fadeout 1.0
    shinn "Ah. What a day!"
    thinking "Never would have expected that my first victim to be Naoko. I'm off to a great start."
    "I take out my list and begin to check through each girl's profile one last time."
    shinn "Let's see how the hit list's looking."
    
    show araki track basic with quick_fade
    thinking "There's the sporty Araki Shinjugai, with a body that's petite and tight. Utterly enticing."
    
    hide araki track basic
    show touko basketball shy
    with quick_fade
    thinking "We have the beautiful Touko Takatsukasa. Her mere gaze is quite stunning, and she packs some delicious curves in that athletic body of hers."
    
    hide touko basketball shy
    show aina pool basic
    with quick_fade
    thinking "Then there's Aina Aozaki... that bubbly, cute nature of hers is very endearing. I can't wait to turn her into an utter degenerate."
    
    hide aina pool basic
    show satsuki uniform basic
    with quick_fade
    thinking "Ah, Satsuki Katsuragi. A traditional maiden and an archery star, no less! Imagine breaking her to such a point that she no longer even cares about her exalted family name."
    
    hide satsuki uniform basic
    show ritsuko tennis basic
    with quick_fade
    thinking "And, of course, there's Ritsuko Yasuhiro."
    "I shudder at the very memory of her."
    thinking "I'll have to be careful with her, though there's no doubt I'll have to turn her into a cumdump as well. There are special methods for her type."
    
    hide ritsuko tennis basic
    show rina suit confident
    with quick_fade
    thinking "And last, Ms. Rina Akiyama. She'll be the next teacher to be my victim."
    thinking "I wasn't really planning to go after teachers this season, but after what happened with Naoko today, and considering Rina's, plump, irresistible hips, there's nothing wrong with having a token adult in the line-up."
    
    hide rina suit confident with quick_fade
    "As I turn to look back at the school, I feel a grin slide across my face."
    thinking "Now... let this breaking season commence."
    "Rubbing my hands in excitement, I begin my trip home, already planning for tomorrow."
    jump day_1__start