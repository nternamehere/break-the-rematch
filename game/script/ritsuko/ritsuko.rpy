label ritsuko__router:
    $ quick_menu = True
    if ritsuko_next_step == "cg_4":
        jump ritsuko__cg_4
    elif ritsuko_next_step == "day_2":
        jump tennis__day_2
    elif ritsuko_next_step == "cg_2":
        jump ritsuko__cg_2
    else:
        jump tennis__day_1

label tennis__day_1:
    $ tennis_available = False
    $ ritsuko_next_step = "cg_2"
    scene bg hallway 1 with map_fade
    "I came in to school way earlier than I needed to. Since I got such an early start this morning, I decided it was better to make an early appearance than stay around and kill time at home."
    "Not that I get credit for being early, but a little extra time to check out the students never hurts."
    "I walk towards the staff room to get some materials done for the tutoring this afternoon."
    "As I reach the entrance to the staff rom, the door suddenly swings open right in front of me."
    
    show ritsuko tennis basic with moveinright
    ritsuko "Oh?"
    "Definitely not who I was hoping to run into this early in the morning."
    ritsuko "What do we have here?"
    "Ritsuko gives me her usual disgusted-looking smirk."
    shinn "Good morning, Ritsuko. How are you doing?"
    ritsuko "How polite. Well, I'm doing just fine."
    shinn "Great. Don't forget about our session later this afternoon."
    ritsuko "Oh? Session?"
    "Ritsuko pauses for a moment."
    ritsuko "Ah! Yes, I remember now..."
    thinking "This idiot..."
    shinn "You are coming in, right?"
    ritsuko "Of course. I just hope you keep your hands to yourself."
    shinn "What?"
    ritsuko "Ho ho ho~"
    ritsuko "Oh, nothing, don't mind me. Anyway, see you later!"

    hide ritsuko tennis basic with moveoutleft
    "Ritsuko walks away."
    thinking "That little bitch. I'm seriously going to punish her."
    "But for all that she's such a snob, she can actually be pretty clever."
    "It's no wonder she almost managed to catch me back then."
    thinking "Seems like I need to go the extra mile for this girl."

    scene bg classroom with dissolve
    "I came in early this time around to prepare for the lesson."
    "I keep thinking to myself about how I'm going to deal with her."
    "But before I've managed to come up with anything, Ritsuko enters the class."

    show ritsuko school smile with moveinright
    thinking "Wow, She's early."
    "She seems to notice my look of surprise as I see her."
    ritsuko "Oh? Why so startled? Did you not expect me to turn up?"
    shinn "It's not that. It's just that I didn't expect you to be this early."
    ritsuko "Hmmph. How rude. A truly elegant lady is never late!"
    shinn "Truly elegant my ass..."
    ritsuko "What? What did you say?"
    shinn "Oh, nothing. Take a seat."
    ritsuko "Before that, I just want to confirm that you won't be getting up to anything else while we're here?"
    shinn "Huh? What else would I be doing other than teaching you math?"
    ritsuko "I mean, the sort of thing you did back then."
    shinn "What sort?"
    "Ritsuko narrows her eyes."
    ritsuko "You know. Those things you did in the storeroom."
    "I glare at Ritsuko in frustration."
    shinn "Alright, you know what? Let's clear the air."
    shinn "What sort of things did I do back then in the storeroom?"
    ritsuko "Well, You know..."
    "I get more and more pissed off the more I have to deal with her shitty attitude."
    shinn "Say it!"
    ritsuko "S- Sex?"
    thinking "No surprise that she's embarrassed to even say it."
    shinn "How do you know if it was sex?"
    "Ritsuko's face is red with embarrassment."
    ritsuko "Well, stop asking me about how I know! I just know, okay!"
    shinn "Is that so? What evidence do you have then?"
    ritsuko "..."
    shinn "Exactly. Now shut up and let's get this lesson moving. The more you put things off, the later you'll be going home."
    ritsuko "Fine..."
    "We manage to get through the lesson without any further disruption. It's a minor miracle that Ritsuko even manages to pay attention to the coursework."
    "As the sun sets, she finishes the last remaining problem set, and I decide to call it a day."
    shinn "Alright, that's enough for now."
    ritsuko "Finally. What a waste of time."
    thinking "This bitch really deserves a punch in the face."
    ritsuko "So, can I go now?"
    shinn "Not yet. Give me a minute."
    ritsuko "Hurry up, I want to go home!"
    "I walk up to her and hand over some practice questions."
    ritsuko "What? What is this? I don't have time for these."
    shinn "Too bad. Do it tonight and hand it in tomorrow."
    ritsuko "Fine. I shall take my leave then. See you tomorrow."

    hide ritsuko school smile with moveoutright
    "Ritsuko stands up and leaves the class."
    thinking "Ugh. What a horrible student..."
    thinking "I wonder how on earth she manages to make friends in school with such an arrogant attitude."
    thinking "She's probably never had a boyfriend."
    thinking "Heh. No wonder she was so embarrassed saying the word \"sex\" in front of a guy."
    thinking "You can be pretty sure that one's a virgin."
    thinking "Which means breaking her is going to be even more fun."
    "I let out a sinister laugh."
    shinn "Tomorrow should be a fun day."

    scene bg staffroom with fade
    "It's getting close to lunchtime."
    shinn "Maybe I should grab something to eat before the cafeteria is full of students."
    "I get up and leave the staff room."

    scene bg hallway 1 with dissolve
    "I head towards the cafeteria thinking about what I should get to eat."
    "As I walk, I notice Ritsuko in the distance."
    thinking "Oh, it's her. Aren't there lessons going on right now? What's she doing here?"
    "From the look of it, she seems to be sneaking around."
    thinking "What is she doing?"
    "Curious, I decide to follow her and check it out."
    "I tail her until she finally comes to a stop outside the Principal's office."
    thinking "Huh? What's she doing here?"
    thinking "Hang on a minute. Is she here to tell on me?!"
    "She knocks on the door, and I can hear a familiar voice from inside the office."
    principal "Come in."
    "Ritsuko enters the office and shuts the door behind her."
    thinking "If she's going to expose me, I'd better step in to interrupt the conversation."
    thinking "Not that that things are likely to turn out so great in that case."
    thinking "But I might not have any other options."
    "I move in close to the door to listen from the outside."
    jump ritsuko__cg_1

label ritsuko__cg_1:
    scene bg principal office with pixellate
    show ritsuko school angry at left
    show principal thinking at right
    $ renpy.music.play(audio.breakdown, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    ritsuko "Why did you call me out here all of a sudden?"
    principal "Oh, there's something I thought was important to discuss with you."
    ritsuko "What business do you have with me?"
    principal "What business? Heh..."
    principal "Do you want to take a guess? You might be a bit surprised."
    ritsuko "Surprised? If this is your idea of a joke, then I don't intend to stick around."
    principal "Leaving already? Don't be too hasty..."

    show principal smirk
    principal "I didn't know the Yasuhiro family business was so dirty."
    thinking "Dirty? This sounds like it might be going somewhere interesting."
    "I decide to take a look through the keyhole in order to follow whatever's going on."
    ritsuko "What the hell are you talking about?"
    "The Principal throws a couple of pictures onto the table in front of Ritusko."
    principal "Your father has been caught by paparazzi trying to bribe officials."
    ritsuko "W— What?"
    principal "I managed to get ahold of these since the photographer happens to be a friend of mine."
    principal "I paid my friend a good sum of money to hand these photos over to me exclusively."
    ritsuko "So? Do you think that you can hold our family to ransom?"
    principal "Ransom? Heh... What a naïve little girl."
    ritsuko "Well then. If it's not ransom you're after, then what exactly do you want?"
    principal "I am a very simple man. I have a few simple and straightforward pleasures in life."
    principal "For one thing, I take great pleasure in being the Principal of a school with so many attractive girls attending. Working here has been quite good for me."
    principal "As a single man, being able to watch girls like you all day really gets me going."
    ritsuko "..."
    principal "I want your body, Ritsuko."
    ritsuko "Hah. You must be joking, right?"

    show principal thinking
    principal "Am I joking? Haha..."
    principal "I wonder if it would be such a joke if these photos were to be released to the public."
    principal "Bribing officials is a criminal offence."
    ritsuko "You..."
    principal "Not only would your father be in hot water, the family business might be at stake too."
    ritsuko "..."

    show principal smirk
    principal "So, for the sake of your family, why not have sex with me?"
    ritsuko "..."
    principal "Come on... What's it going to be? Seeing your dad in jail or seeing my dick?"
    ritsuko "Fine! But you have to promise not to tell anyone about this."
    principal "I am a man of my word. I promise."
    "I follow along with their conversation, dumbfounded as I watch through the keyhole."
    thinking "What the fuck is going on? The Principal is actually taking advantage of her?!"
    thinking "And Ritsuko's family is caught in a scandal?!"
    thinking "Damn, and I thought I was one one-of-a-kind around here."
    thinking "If they're going to have sex, I'm definitely sticking around to watch."
    "I take a look around to make sure the place looks clear for me to hang around without getting caught."
    "As expected, this area's empty during class time. No wonder, if the Principal planned this out himself."
    principal "Right. Why don't you take your clothes off to start?"
    ritsuko "H— Here?"
    principal "Where else?"
    ritsuko "F— Fine..."

    show ritsuko naked shy
    "Ritsuko slowly undresses, revealing her lushly blooming breasts and well-rounded hips."
    principal "Phew... You look even more amazing than I expected."
    principal "Such a gem being hidden under that uniform."
    principal "I'm sure I'm not the only guy here who's been lusting after you."
    "Ritsuko flushes with embarrassment at his words."
    ritsuko "Sh— Shut up."
    "The Principal continues to stare at her, taking in the sight of her body."
    "He's not even bothering to hide his expression now, looking at her like a pervert who can't restrain himself at the sight of her."
    ritsuko "So? What do you want me to do next?"
    principal "Lie down on my desk and spread your legs."

    scene ritsuko_sex_scene_1 1 with fade
    "Ritsuko walks up to his desk and sits down. She keeps her hands covering her breasts with shyness that's quickly becoming pointless."
    "Slowly and hesitantly, she slides open her legs, exposing her pussy."
    principal "Amazing. What a beautiful pussy."
    "The Principal glances up again, and gives her an irritated look."
    principal "Come on, stop covering up those breasts! I want to see it all."
    ritsuko "..."
    principal "Do it!"

    scene ritsuko_sex_scene_1 2
    "Ritsuko flinches, then nervously moves her hands down to her sides, resting them against the desk."
    principal "That's much better."

    scene ritsuko_sex_scene_1 3
    "The Principal approaches Ritsuko and leans down to take a closer look at her pussy."
    principal "Hmm... I wonder what a high school girl's pussy tastes like."
    "The Principal sticks out his tongue..."

    scene ritsuko_sex_scene_1 4 with quick_fade
    "And slowly licks her pussy up and down."
    "Ritsuko squirms under the sensation of his tongue against her."
    ritsuko "Eee! Don't do that! It's disgusting!"
    "The Principal doesn't pay her any mind, and continues to lick at her."
    ritsuko "Mmm~ Please stop!"
    "The principal continues to lick her until her juices start to flow from between her lips."
    principal "There! That should do it."

    scene ritsuko_sex_scene_1 5 with quick_fade
    principal "Look at you. Wet, ripe, and ready to roll."
    ritsuko "W— What?"
    "The Principal removes his pants to reveal a cock that's already rock hard after licking her."
    principal "There you go. Ever seen one of these before? A real man's dick."
    principal "You're going to get to taste it for yourself."
    "The Principal moves in close, positioning his dick for insertion."
    ritsuko "Noo...!"
    principal "Are you scared? Then maybe you should blame your father!"

    scene ritsuko_sex_scene_1 6 with blood_flash
    play sound insert1
    play sound sex1_slow loop
    "Without hesitation, the principal pierces through into her pussy."
    ritsuko "Ahh! It hurts!"
    "I can see a bit of blood coming out from her pussy."
    principal "Oh? So, this is your first time?"
    principal "What a lucky day for me!"
    "The Principal begins to thrust in deeper inside her."
    ritsuko "Noo... It's too deep! Please stop!"
    principal "Stop? No way in hell I am going to stop."
    principal "I'm going to teach you how to enjoy a man's dick properly."
    ritsuko "Noo..."
    principal "Heheh... Come on. Give me a kiss..."

    scene ritsuko_sex_scene_1 7
    "The Principal sticks his tongue out, forcing Ritsuko into a sloppy French kiss."
    principal "Come on, open your mouth up. I want to taste that sweet drool straight from your mouth."
    "At first, Ritsuko tries to shut him out. But I can see her body warming up as I watch."
    "As she falls into his rhythm, she starts to stick her own tongue out, letting the Principal into her mouth."
    ritsuko "Mmm~"
    "The two of them lock together in a long kiss before the Principal draws away."
    principal "Heh... Good girl."
    "As he finishes the kiss, the Principal starts to speed up his thrusts."

    scene ritsuko_sex_scene_1 6
    ritsuko "Ah~ No!"
    principal "No? You keep saying no, but your pussy is getting wetter the more I move."
    ritsuko "That's not it!"
    principal "Come on, be honest with yourself! You like this sort of thing after all, don't you?"
    principal "Coming from the respected Yasuhiro family, you must have been sad trying to suppress your lust to keep up the image."
    ritsuko "..."
    principal "But still, a well-mannered daughter like you will do anything to protect the family."
    principal "Even this!"
    "The Principal thrusts in a little harder..."
    ritsuko "Ah~ No..."
    principal "Heh. You can blame all this on your stupid father, for being caught in the act."
    ritsuko "..."
    principal "I'm going to show you how great sex can really be for someone like you."
    principal "Let's see how arrogant and snobbish you'll be after this!"
    "I continue watching the scene unfold from outside."
    thinking "Damn, This principal reminds me of myself."
    thinking "Heh. Maybe this guy really could be me in the future?"
    "I'm rock hard here as I'm glued to the keyhole."
    "The Principal keeps pounding faster and faster."
    principal "Hey Ritsuko, you're really squeezing down on me there."
    ritsuko "..."
    principal "I guess this means you want my cum, right?"
    ritsuko "No!"
    principal "Your mouth keeps lying to me, but your body is telling the truth."
    "The motion gets even faster as the Principal approaches his limit."
    principal "Then, I'll shoot my cum out inside you, okay?"
    ritsuko "No! Take it out! Please!"
    ritsuko "Don't cum inside me!"
    principal "Take all of it Ritsuko! Take it all and get pregnant with my baby!"
    ritsuko "Nooo!"
    stop sound

    scene ritsuko_sex_scene_1 8 with cum_flash
    play sound cum1
    "With a final thrust, the Principal shoots out all of his cum in one burst."

    scene ritsuko_sex_scene_1 9 with cum_flash
    play sound cum2
    "It's so much, I can see it gushing out of her."
    ritsuko "NOO!!!"
    principal "Ah~ now that felt good."
    principal "I haven't done that in a few years now."
    principal "So that's my three years' worth of cum inside you, Ritsuko."
    ritsuko "..."
    principal "I hope you enjoyed it."
    "I can see Ritsuko starting to sob."
    principal "Don't cry. I kept my promise. I'm not going to tell anyone."
    principal "Now get dressed and get back to class."

    scene bg principal office with fade
    show ritsuko naked exposed at left
    show principal smirk at right
    "Ritsuko slowly picks up her clothes and dresses herself."

    show ritsuko school concerned
    principal "Every lunchtime, I want you to come visit me in my office."
    ritsuko "..."
    ritsuko "You said..."
    principal "I said I wouldn't tell, but I didn't say this would be a one-off."
    ritsuko "You..."
    principal "Of course, if you want this to be a one-off thing, then just for once, I'll be exposing your father to everyone."
    ritsuko "..."
    principal "That's right. Now get out of here."
    "Looking defeated, Ritsuko walks towards the door to leave the room."
    thinking "Oh crap... She's coming!"
    "As fast as I can, I run towards the nearest pillar and hide behind it."
    "I peer out from behind as Ritsuko steps out of the office and leaves the area."
    thinking "Phew. That was close..."
    "I'm still taking in everything I just saw, working out how to use it to my advantage."
    thinking "I could use this as leverage to blackmail Ritsuko myself."
    thinking "But then, too many plots going on in a narrow space might end up crashing into each other."
    thinking "Trying to keep things up with the Principal blackmailing her at the same time could be tricky."
    thinking "Unless I could convince him to coordinate with me..."
    thinking "Heh. Depending on how things go, this might turn out pretty well."
    $ renpy.end_replay()
    $ persistent.ritsuko__cg_1 = True
    jump tennis__day_1_continued_1

label tennis__day_1_continued_1:
    scene bg hallway 1 with irisout
    $ renpy.music.play(audio.campus, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    "Moments after Ritsuko leaves, I decide to see the Principal."
    thinking "Hopefully, this will work out."
    "I knock on the doors of the Principal's office."
    principal "Who's that?"
    shinn "It's me, Shinn."
    principal "Ah, Shinn! Come in."

    scene bg principal office with fade
    show principal smirk
    "The Principal greets me as I enter his office."
    principal " Hello Shinn. What can I do for you?  "
    thinking "Hmm... Maybe I should get straight to the point."
    shinn "I saw what you did with Ritsuko just now."
    "The Principal sets down the paperwork on his desk and looks me in the face."

    show principal thinking
    principal "Is that so?"
    shinn "Yes. But I have no intention of exposing you."
    principal "Then why are you telling me this?"
    shinn "I was hoping we could make a deal we would both benefit from."
    principal "Hmm... and what do you mean by that?"
    shinn "Well, I can understand why you'd want to fuck Ritsuko, what with her amazing body and all."
    shinn "To be frank, so would pretty much anyone else in your situation. Including me."
    principal "Right. And you're saying that you want in then? So what exactly do I get out of that?"
    shinn "I can mold that girl into a pet slave for you. Just like I did in the old days."
    
    show principal smirk
    principal "So, the rumors about you screwing around with the teachers back then were true."
    shinn "I wondered if you might have heard about those."
    principal "I'd definitely heard some stories. That may have had more than a bit to do with why the previous principal was removed from his position."
    principal "So, that was your work after all..."
    principal "Well, it's certainly interesting to have you confirm that for me directly."
    shinn "Well, what do you say?"
    
    show principal thinking
    principal "Hmm... a pet slave, huh? I was really just planning to use Ritsuko to carry on an affair while she's still attending here."
    principal "Making her into a sex slave is certainly outside the scope of what I'd had in mind."
    principal "Furthermore, the previous principal lost his job precisely because he got caught up in the fallout from your activities back then."
    principal "Not that I disapprove of the sentiment, but I'm not the risk-taker now that I was when I was your age."
    principal "I'm quite happy with the position I have right now, and I'd rather not put it in jeopardy "
    shinn "I can appreciate that. But I think that this is a win-win opportunity for the both of us."
    shinn "I'm not really the risk-taker I was back when I was a student here either. I intend to keep this up for a long time."
    shinn "I'll put it this way. You haven't heard about any of what I've been up to since I graduated, have you?"
    principal "If I had, I doubt that your application would have made it to my desk in the first place."
    shinn "Exactly. The goals I'm aiming for might be a bit extreme, but I know how to keep things under wraps when necessary."
    shinn "If we work together here, we can both come out ahead. I get to screw Ritsuko as intended, you get a long-term sex pet out of the deal."
    shinn "You can leave the dirty work to me and reap the rewards, all you'll have to do is make sure the administration doesn't keep too close an eye on what's going on."
    principal "Hmm..."
    shinn "We've shared this much with each other already. At this point, there's no way you'd get in trouble without me getting caught up in it too."
    principal "That's true."
    shinn "So, that being the case, do you want me to make the arrangements?"
    principal "And how do you propose to do that?"
    shinn "I'll just need some copies of those photos that you used to blackmail Ritsuko."
    principal "Hmm... But I did promise her that I wouldn't expose her any further."
    shinn "Come on... Let's be honest, is that really a promise you were intending to keep?"
    principal "Well... As long as it didn't become too much of an inconvenience, anyway."
    shinn "Besides, this is just between you and me. Nobody else would even need to know about this."
    "The Principal takes out the photos from his desk drawer and places them on the desk in front of me."
    principal "Alright, I have to hand it to you, you make an appealing offer. We have a deal."
    "I step forward and take the photos from the desk."
    shinn "Thank you. I'll be reporting to you with progress soon."
    shinn "Ritsuko should be your pet in no time."

    show principal smirk
    principal "Heh... I can't wait."
    shinn "Well then, I should be going."
    principal "Alright. See you soon."
    "I leave the Principal's office with a feeling of joy welling up in me."
    thinking "Heh... This is going to make my life so much easier now."
    thinking "Can't wait for what you've got coming to you, Ritsuko."
    if day == 2 and not staffroom_available and tennis_available and not gym_available:
        jump ritsuko__router
    else:
        jump map__school

label ritsuko__cg_2:
    $ ritsuko_next_step = "day_2"
    $ renpy.music.play(audio.sex, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    scene bg locker room with map_fade
    "I heard from her teacher that Ristuko usually has a short solo practice during lunch."
    "After eating an early lunch, I come down here to confront her."
    "I've been waiting for an opportunity like this, ever since Ritsuko threatened to expose me before."
    "Normally, there's nobody using the girls' locker room at this hour. It's a bit eerie with nobody around."
    show ritsuko tennis basic with moveinright
    "As I turn a corner, I find Ritsuko here, already dressed up for practice."
    "She turns and stares at me as I come into view."
    ritsuko "Eh? Shinn? What are you doing here!? This is a girls' locker room, you pervert! Get out!"
    shinn "I want to talk to you."
    ritsuko "No! Get out!"
    shinn "Listen here. I know what you did with the Principal this morning."
    ritsuko "Huh? How did..."
    shinn "Don't play dumb with me Ritsuko. I followed you earlier on when you met with the Principal in his office."
    "Ritsuko tries to play it cool."
    ritsuko "Oh? And so what if I did?"
    "To counter her arrogance, I flash the photos which I received from the Principal in front of her."
    shinn "I wonder if you're still interested in keeping up that act with me?"
    ritsuko "What? How did you...?"
    shinn "Why so surprised?"
    shinn "It's never too hard for like-minded people to come to an agreement. The Principal and I have struck a nice deal together."
    ritsuko "That bastard!"
    ritsuko "Give me back those photos!"
    shinn "Oh? You really want them? You know there are already loads of duplicate copies, right?"
    shinn "Even if you destroy these, there'll be more of them popping up in no time."
    ritsuko "..."
    "I take out the master key I'd received as a member of the faculty, and lock the door behind me."
    ritsuko "What... what do you want from me?"
    "At this point, she must realize the sort of trouble she's gotten herself into."
    ritsuko "What are you going to do with me!?"
    "I give her my widest smile as I approach."
    shinn "Well, how does a reenactment of your visit with the Principal sound to you?"
    ritsuko "No! Go away!"
    "I grab her hands, holding her in place. She struggles against me, trying to throw me off with all her strength."
    "Too bad, now that she doesn't think she can put an end to this by playing along, I don't have the willing compliance she gave the Principal."
    "Luckily, I still have some straightforward options at my disposal. There's a length of rope sitting within reach. I grab hold of it."
    ritsuko "Let go of me you bastard!"
    ritsuko "What do you think you're doing?! Do you know who I am?!"
    "I let her words slide over me as I proceed to bind her hands behind her back."

    scene ritsuko__cg_2 1 with fade
    "I lie her down, restrained, against a bench."
    shinn "There, that's more like it."

    scene ritsuko__cg_2 2
    ritsuko "You think you're going to get away with this!?"
    shinn "I'm not the one trying to get away here. You should worry about yourself."
    ritsuko "What?"

    scene ritsuko__cg_2 3
    "I force open her legs, revealing her beautiful black panties."
    ritsuko "Wait, what are you doing!? Stop it!"
    shinn "Stop? You must be joking. There's no turning back now."
    ritsuko "No!"
    shinn "You should have thought about this before, when you threatened to expose me."
    "I let my erect dick spring out, rubbing it along the surface of her beautiful exposed panties."
    ritsuko "Get off of me, you creep!"
    shinn "Creep? Ah, says the one who's willing to use her own body to aid in a criminal coverup."

    scene ritsuko__cg_2 4
    ritsuko "..."
    shinn "Oh? Feeling a bit self-conscious about that?"

    scene ritsuko__cg_2 5
    ritsuko "Shut up!"
    shinn "No, I don't think so. I haven't had someone resist this much for a long time now, this just makes things more interesting."
    shinn "Well then... Let's begin."
    ritsuko "No!"

    scene ritsuko__cg_2 6
    "I move open her panties to see her still-tainted pussy."
    shinn "It looks amazing even right after it's just been used, Ritsuko."
    ritsuko "No! Please don't!"

    scene ritsuko__cg_2 7
    "I place my fingers gently against her entrance."
    ritsuko "What... what are you doing?"
    "Slowly, I begin to push my fingers inside her."
    ritsuko "Ah..."
    shinn "Heh."
    "I keep pushing them in deeper, watching her reactions as she lies bound and helpless to resist."
    ritsuko "No~ It's too deep!"
    shinn "Deep? I I haven't even put it all the way in yet."
    "I keep pushing my fingers further inside her, as her walls clamp down against me."
    "From the pressure of her walls against my fingers, I can tell that she's feeling it."
    shinn "So tell me, which feels better, the Principal's tongue, or my fingers?"
    ritsuko "..."
    shinn "You don't have an answer for that? Alright then..."
    "I increase the force of my movements inside her, scraping away at her inner walls."
    ritsuko "Ah~"
    "There's no question she can feel the difference."
    shinn "See? You love it, don't you?"
    ritsuko "No..."
    shinn "Well, you might as well learn to enjoy it, because I'm going to keep fingering you until you cum."
    ritsuko "Mmmph~"
    "I keep speeding up as I feel her becoming tighter and wetter around me."
    ritsuko "Ahh~!"
    "She can't hold herself back from panting now."
    shinn "If you want to cum, there's no point holding it in, you know?"
    "I keep going faster and faster."
    "Her breathing is speeding up, and I can feel her racing pulse beneath her skin."
    "No matter how she might try to deny it, she can't hide that she's feeling it."
    shinn "I'm gonna show you who's the best. After this, your body's never going to forget me."
    "The feeling of my fingers inside her has her whole body shaking."
    ritsuko "Ah! NOO!"
    shinn "Let it all out! Squirt it out like a dirty slut!"

    scene ritsuko__cg_2 8 with cum_flash
    play sound cum1
    ritsuko "AHHHH!"
    "She bursts past her limit, her pussy juice squirting out like a fountain with my fingers still inside her."
    ritsuko "Ahh! Oh, god..."
    "Her own juices have sprayed out across her own body, covering her. She looks desperately sexy like this."
    shinn "So, looks like you like my fingers more than the Principal's tongue after all."

    scene ritsuko__cg_2 9
    shinn "I sure didn't see you cum like this with him licking you."
    "I take a close look at the state of her pussy."
    shinn "Well... Seems to me like you're well-marinated now."

    scene ritsuko__cg_2 10
    shinn "I think you're finally ready to take my dick."

    scene ritsuko__cg_2 11
    play sound sex1_slow loop
    "Without giving her a chance to protest, I slowly push my way inside."
    shinn "Ahh. Even after all that work loosening you up, it's still really tight."

    scene ritsuko__cg_2 12
    ritsuko "Ah~!"
    "As I slowly thrust my dick in, I can feel her pussy juices starting to leak out around me."
    shinn "Haha! After cumming so much, you just start leaking out the moment I put it in!"
    ritsuko "No~"
    shinn "Hahaha... What's the point in saying no now?"
    "I start moving my body up and down, pumping inside her."
    shinn "How does it feel?"
    ritsuko "No..."
    shinn "Tell me, which feels better, the Principal's dick you tasted before, or mine right now?"
    ritsuko "..."
    ritsuko "Neither."
    shinn "Neither one? I didn't see your pussy juice dripping out like this while you were taking the Principal's dick."
    ritsuko "That's... not right..."
    shinn "Are you sure? Because I can see how wet you are while I'm fucking you right now."
    ritsuko "NO!"
    shinn "Oh, how aggressive."
    shinn "Well, we'll see if you keep that up."
    "I start to put more force into my movements, slowly picking up the pace."

    scene ritsuko__cg_2 13
    ritsuko "Ah~!"
    "She's starting to let her voice out again involuntarily."
    shinn "Heh... Look at you. Not being honest with yourself at all..."
    ritsuko "..."
    "I pound against her hips even harder."
    ritsuko "Mmm~ Ah~!	"
    "She lets out an even louder moan this time."
    shinn "Yeah, keep moaning like a bitch, Ritsuko."
    shinn "This is you, Ritsuko! This is your real self! Embrace it!"
    ritsuko "Nnn~! No!"
    "As her moans start to become wilder, her inner walls squeeze down even tighter."
    shinn "Agh, you're really squeezing me hard here."
    shinn "Seems like you're really enjoying it now, huh?"
    shinn "I guess the Principal must have screwed you pretty good before."
    shinn "It seems like you're really getting the hang of it already!."
    ritsuko "..."
    "She doesn't respond, but her body is telling me how much she's enjoying it."
    "By this time, her pussy is dripping wet as it grips down on me."
    "This is really pushing me right up to the edge myself."
    shinn "I'm at my limit, Ristuko! I'm gonna shoot it out inside you!!"
    shinn "Go ahead and take my cum, Ritsuko!"
    "She doesn't say a word, but I catch the flash of fear in her eyes."

    if persistent.cum == "inside":
        shinn "Go on and take mine down and taste the difference!"
        $ renpy.block_rollback()
        jump ritsuko__cg_2_inside

    elif persistent.cum == "outside":
        shinn "Go on and take mine down and taste the difference!"
        $ renpy.block_rollback()
        jump ritsuko__cg_2_outside

    else:
        menu:
            shinn "Go on and take mine down and taste the difference!"
            "Cum Inside":
                jump ritsuko__cg_2_inside
            "Cum onto her face":
                jump ritsuko__cg_2_outside

label ritsuko__cg_2_inside:
    "I keep pounding away at Ritsuko, watching her face as I prepare to fill her with my seed."
    ritsuko "Mmm~ No, please!"
    "I pick up the pace for a final burst as I reach my climax."
    shinn "Agh! Here it comes!"

    scene ritsuko__cg_2_inside 1 with cum_flash
    stop sound
    play sound cum2
    "In one shot, I let it all out, pouring directly into her womb."
    "Fucking this stuck up rich girl has gotten me so worked up, the load is incredible. It leaks out around me while I'm still inside her."
    ritsuko "NOOOO~!"
    "Even as she screams out in protest, her body seems electrified with pleasure."

    scene ritsuko__cg_2_inside 2 with cum_flash
    play sound cum2
    "Her eyes roll up as her body shudders, her tongue hanging out as she loses control of herself."
    "As her wild shaking comes to an end, she suddenly goes limp, as if all the energy has drained out of her.."
    "I pull out my dick, revealing the mess my creampie, along with all her own pussy juice, has left."
    shinn "Heh. Well, isn't that a sight?"
    shinn "You look like you enjoyed that a hell of a lot more than the Principal's cock."
    "My work done, I untie her."
    shinn "There, you're free to go."
    "Despite all the resistance she put up before, she doesn't respond upon hearing my voice."
    thinking "Heh, looks like I broke her."
    jump ritsuko__cg_2_end

label ritsuko__cg_2_outside:
    shinn "Go ahead and take it, right on your face!."
    ritsuko "No, stop! Please!"
    "I pick up the pace for a final burst as I reach my climax."
    shinn "Agh! Here it comes!"

    scene ritsuko__cg_2_outside 1 with cum_flash
    stop sound
    play sound cum2
    "I quickly pull out and spray directly into her face."
    ritsuko "Ahh~"
    "The cum sprays out everywhere, covering her face."
    "After everything she's just been through, she smell of it all over her overwhelms her."

    scene ritsuko__cg_2_outside 2 with cum_flash
    play sound cum2
    "Her eyes roll up in her head, and she sags as all the energy seems to drain out of her, her tongue hanging from her mouth."
    shinn "Take a look at that wonderful face."
    jump ritsuko__cg_2_end

label ritsuko__cg_2_end:
    "I take out the photos."
    shinn "Of course, these are going to be staying with me."
    shinn "If you have any plans to talk about everything that just happened... keep these in mind. I'm sure you remember what'll happen to your family if these get spread around."
    "Ritsuko still gives no reply, she just stares at me."
    shinn "Well, as long as that's understood, I'll be going."
    shinn "Oh, and by the way, today's lesson is cancelled. Go ahead and take the time off to think about what you've just done."
    shinn "Bye now!"
    "I leave the room, leaving Ritsuko behind, still sitting in the mess we'd made."
    $ renpy.end_replay()
    $ persistent.ritsuko__cg_2 = True
    if day == 2 and not staffroom_available and tennis_available and not gym_available:
        jump ritsuko__router
    else:
        jump map__school

label tennis__day_2:
    $ ritsuko_next_step = "cg_4"
    scene bg classroom with map_fade
    "I've spent the whole day thinking about what I did to Ritsuko yesterday."
    "And here I am, waiting for her to show up for after-school lessons."
    thinking "Hmm... Well, it's no surprise if she hasn't showed up, considering."
    thinking "I guess that's pretty much what I should expect."
    "Nevertheless, I continue to wait."
    "But as the hours pass, and the sun starts to set, there's still no sign of her."
    thinking "Well, that's the scheduled lesson time up. No fault of mine if she doesn't make it in!"
    thinking "Might as well get going."
    "I pack up and leave the class."

    scene bg hallway 1 with pixellate
    "As I walked along the hallway, I spot Ritsuko in the distance from outside the window."
    thinking "Oh, there she is."
    "It seems she's out practicing on the tennis court."
    thinking "Well, she did skip lessons, might as well go check on her."
    "I head out to the tennis court."

label ritsuko__cg_3:
    $ renpy.music.play(audio.kinky, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    scene bg tennis court with fade
    show ritsuko tennis basic
    "As I make it within eyeshot of the court, Ritsuko instantly spots me."
    ritsuko "You! Why are you here!?"
    "In her anger, she flings a tennis ball at me."
    shinn "Ow! Hey, stop it!"
    "Even from over here, I can see her eyes watering."
    shinn "Relax, I'm not going to hurt you."
    ritsuko "Liar! All of you men are the same! You're all a bunch of uncontrollable pigs!"
    shinn "Whoa, that's a pretty bold statement. You should try to control yourself."
    ritsuko "Shut up! I don't want to hear that from you!"
    ritsuko "After all that you've done! How could you!?"
    shinn "How could I what? It's just sex. No big deal."
    ritsuko "No big deal? The Principal took my first time! The tw of you both humiliated me!"
    shinn "So?"
    ritsuko "I was supposed to share that with someone special!"
    shinn "Pfft... Do you honestly still believe in that sort of fairy tale? Why don't you grow up?"
    ritsuko "What the hell do you still want from me anyway?!"
    shinn "Well, let's see..."
    shinn "Considering what a stuck up and obnoxious bitch you are, I really just wanted to humiliate you."
    ritsuko "You..."
    ritsuko "You really are just the worst."
    shinn "Just so you know, I struck a deal with the Principal to turn you into his personal cumdump slave."
    ritsuko "You what?"
    shinn "You heard me. How else did you think I got ahold of the photos?"
    ritsuko "You're a monster..."
    shinn "Hahahaha!"
    "I can't help but laugh at hearing that."
    shinn "Monster? I've gotten that one quite a few times by now."
    shinn "Well, it's a bit funny to see you taking it so seriously."
    ritsuko "So I really was right about you after all."
    ritsuko "You're the one who was going around screwing all those female teachers and forcing them to resign! The old principal lost his job because of you!"
    shinn "Hahaha..."
    shinn "Well, not like there's any point denying it now."
    shinn "Of course, you're right. And you did almost catch me in the act back then."
    ritsuko "So, you lied to me."
    shinn "Well, what if I did? Were you planning to do something about it?"
    ritsuko "..."
    shinn "Frankly, if you had tried to expose me before, I would just have gotten an earlier start on all of this anyway."
    shinn "But, doing it this way is just as interesting."
    ritsuko "You're sick!"
    shinn "Go ahead and keep calling me names, I'm sure that'll make everything better for you."
    ritsuko "You..."
    "I take out the photos once again to show her."
    shinn "Right, you didn't forget about these, did you?"
    shinn "The moment these ended up in my hands, you know you were fated to end up as a sex slave."
    shinn "And why wait? I have an agreement to deliver on after all."
    ritsuko "Huh?"
    shinn "Take off your clothes."
    ritsuko "What? Here!?"
    shinn "Where else?"
    ritsuko "No! There's no way in hell I'm doing it out here!"
    shinn "It's here where no one's watching, or the photos where everyone can see them. Your choice."
    ritsuko "..."
    ritsuko "Fine..."
    show ritsuko naked shy
    "Ritsuko's face flushes as she slowly strips off her clothes."
    ritsuko "This is... so humiliating."
    "That blushing face has a cute sort of charm of its own."
    thinking "Damn... why did such a bitch have to end up with a cute face like this?"
    "Once she's taken off everything, she stands there awkwardly in front of me, trying to cover herself with her hands."
    "She's too embarrassed to meet my eye."
    shinn "Now, you can go ahead and put your panties back on."
    "Her eyes widen in confusion for a moment and she glances at them on the ground."
    shinn "Wear them on your head."
    ritsuko "What? No..."
    shinn "Do it. And then squat down."
    ritsuko "..."
    shinn "Or are you thinking of refusing?"
    ritsuko "F-fine..."

    scene ritsuko__cg_3_tennis 1 with pixellate
    "Ritsuko picks up the panties, and puts them on over her head. She squats down, unable to help fully exposing herself to me."
    ritsuko "This... this is disgusting!"
    "This clear view of her pussy reminds me of the good time I had with her yesterday."

    scene ritsuko__cg_3_tennis 2
    "Probably, it's doing the same for her. On getting a closer look, I can see a visible leak trickling out."
    shinn "Haha... You're getting turned on by this, aren't you?"

    scene ritsuko__cg_3_tennis 3
    ritsuko "No! I'm not!"
    shinn "Is that so? It looks like your pussy says differently."
    ritsuko "That's not it..."
    shinn "Tsk tsk..."
    shinn "Ritsuko, you ought to be more honest."
    ritsuko "Shut up! What do you want me to do next!?"
    shinn "Lift your hands up and fold them behind your head."

    scene ritsuko__cg_3_tennis 4
    "Ritsuko complies, putting her beautiful cleanly shaved armpits on full display."
    ritsuko "Li— like this?"
    shinn "Yeah, just like that."
    shinn "Heh. Your armpits look pretty nice. I bet they smell good too."
    ritsuko "You are so sick!"
    shinn "Now now, there's no need to be rude."
    shinn "Alright, so up next..."
    thinking "Now that I've got her in this position, I might as well take the opportunity to have her say something humiliating..."
    shinn "I want you to repeat after me."

    menu:
        ritsuko "Huh?"
        "I am Shinn's personal sex toy!":
            jump ritsuko__cg_3_toy
        "I want Shinn's baby-making seed inside me!":
            jump ritsuko__cg_3_baby

label ritsuko__cg_3_toy:
    scene ritsuko__cg_3_tennis 5
    shinn "Say \"I am Shinn's personal sex toy!\""
    ritsuko "No! I'm not going to do that!"
    shinn "Do it, or else..."
    "Ritsuko shudders."
    ritsuko "...Fine."
    ritsuko "I'm Shinn's personal sex toy..."
    "She mumbles it out softly, barely audible from my distance."
    shinn "What? You'll have to speak up, I can't hear you."
    "Ritsuko glares at me, angry and defeated."
    ritsuko "I'M SHINN'S PERSONAL SEX TOY!"

    scene ritsuko__cg_3_tennis 6
    ritsuko "THERE! YOU HAPPY NOW?!"
    "She shouted at the top of her lungs. If there's still anyone hanging around the school grounds, they probably heard her just now."
    shinn "Haha... Good girl."
    "I walk up to her and pick up the tennis racket by her side."
    shinn "Your wish is my command, Ritsuko."
    jump ritsuko__cg_3_continued

label ritsuko__cg_3_baby:
    scene ritsuko__cg_3_tennis 5
    shinn "Say \"I want Shinn's baby-making seed inside me!\""
    ritsuko "No! I'm not going to do that!"
    shinn "Do it or else..."
    "Ritsuko shudders."
    ritsuko "...Fine."
    ritsuko "I want Shinn's baby making seed inside me..."
    "She mumbles it out softly, barely audible from my distance."
    shinn "What? You'll have to speak up, I can't hear you."
    "Ritsuko glares at me, angry and defeated."
    ritsuko "I WANT SHINN'S BABY-MAKING SEED INSIDE ME!"

    scene ritsuko__cg_3_tennis 6
    ritsuko "THERE! YOU HAPPY NOW?!"
    "She shouted at the top of her lungs. If there's still anyone hanging around the school grounds, they probably heard her just now."
    shinn "Haha... Good girl."
    jump ritsuko__cg_3_continued

label ritsuko__cg_3_continued:
    "I walk up to her and pick up the tennis racket by her side."
    shinn "But you'll have to wait on the baby-seed. I've got something else in store for you now."

    scene ritsuko__cg_3_tennis 7
    "I take the racket, and jam the handle inside her."
    ritsuko "AH! It hurts!"
    "She cries out with shock and pain, but it looks like she came the moment I stuck it in."
    ritsuko "Take it out!"
    shinn "Take it out? You seem to be enjoying it."
    ritsuko "No, that's not true! Please, take it out!"
    shinn "Heh. You wish."
    "I move around behind her and unzip my pants."
    ritsuko "Wait, what are you doing?"
    shinn "Heh. Yesterday, I had some fun with your pussy. This time, I'll be playing with your ass."
    ritsuko "What?! No! You can't!"
    shinn "Hahaha!"

    scene ritsuko__cg_3_tennis 8
    "Ignoring her plea, I thrust my dick into her defenseless asshole."
    ritsuko "Ah! No!"
    "The moment I push myself inside her, I can see her legs starting to tremble with the pleasure."
    "It's warm and tight inside her ass, and as I slowly move inside her, she lets out a small moan."
    ritsuko "Ah~"
    shinn "See? You love it!"
    ritsuko "No! Ah~"
    shinn "Admit it, Ritsuko! You're nothing but a horny slut!"
    "I start to pound her ass harder, and her reactions become even more intense."
    ritsuko "Mmm~ Please..."
    "Her eyes are getting hazy, and it seems like she's having a hard time holding out against the pleasure."
    shinn "Just face it, you love sex! You've been nothing but a slut from the start!"
    ritsuko "..."
    shinn "No answer? You'll have one soon."

    scene ritsuko__cg_3_tennis 9
    "I push my dick inside, so suddenly and violently, her resistance snaps."
    ritsuko "Ah!"
    shinn "You are mine, Ritsuko! My sex slave! You understand?!"
    ritsuko "Ah! Feels... so good..."
    "She continues to moan, becoming even louder as I continue to plow her ass."
    ritsuko "Ahhh~! It feels so good!"
    "I can see for myself just how good it feels for her, her pussy juices are dripping down the tennis racket."
    shinn "That's right! Now you're starting to get it!"
    "As I continue to speed up, I can feel her asshole tightening around me."
    "It's squeezing me so hard now, I won't be able to last much longer."
    shinn "Hey, Ritsuko! Do you want my cum?"
    ritsuko "Ye- yes..."
    shinn "Good girl."
    "My paces reaches its peak as I can feel the urge to cum rising up in me."
    shinn "Here it comes, Ritsuko! Take it all!"
    ritsuko "Ahh! Yes!"

    scene ritsuko__cg_3_tennis 10 with cum_flash
    play sound cum2
    "I let out a thick jet of my cum, deep inside her asshole."
    ritsuko "Ahh!! I can feel your warm cum in my stomach!"

    scene ritsuko__cg_3_tennis 11 with cum_flash
    play sound cum1
    "Ritsuko's legs start to shudder uncontrollably with the overwhelming pleasure."

    scene ritsuko__cg_3_tennis 12
    "The tennis racket clatters to the ground at her feet as it's forcibly ejected by her pulsating pussy."
    ritsuko "Ah! It feels so good!"

    scene ritsuko__cg_3_tennis 13
    "After spilling out my last drop inside her, I pull out, leaving my cum dripping out from her asshole."
    ritsuko "It's too much! I can't take it anymore, I need to pee!"
    shinn "Pee? Did I give you permission?"

    menu:
        ritsuko "Ah! Please, Shinn! Let me pee!"
        "Let her go":
            jump ritsuko__cg_3_pee
        "Don't let her go":
            jump ritsuko__cg_3_no_pee

label ritsuko__cg_3_pee:
    shinn "Alright then. Since you're nothing but a dog now, go ahead."
    ritsuko "Ah~ Thank you!"

    scene ritsuko__cg_3_tennis 14
    "A yellow stream starts to trickle from her urethra, quickly turning into a forceful spray splashing against the pavement of the court."
    ritsuko "Ah! It feels so good! I want more sex!"
    shinn "You want more? Good. There's plenty more coming."
    shinn "Let's bring you to my house for a good baby-making session."
    ritsuko "Yes!"
    jump ritsuko__cg_3_house

label ritsuko__cg_3_no_pee:
    shinn "I don't think so. You're not allowe to pee without my permission."
    ritsuko "But Shinn! I need to pee! I can't hold it!"
    shinn "You hold it until I say you're allowed to go. Your place is to follow my instructions."
    ritsuko "No... I can't hold much longer."
    "A sudden jet of urine squirts from her urethra."
    ritsuko "Ah! I'm sorry Shinn!"
    shinn "What the..."

    scene ritsuko__cg_3_tennis 14
    "The last of her control broken, the jet becomes a continuous forceful stream as Ritsuko relieves herself on the pavement."
    ritsuko "Ah! Peeing suddenly feel so good!"
    shinn "Look at you. In just a day, you've gone from being a noble and elegant lady to an uncontrollable sex-starved pet."
    shinn "Seems like I'm going to have to punish you to teach you some manners."
    ritsuko "Ah, yes! Please, I need to be punished!"
    shinn "Good. Let's bring you to my house to teach you a proper lesson."
    ritsuko "Yes!"
    jump ritsuko__cg_3_house 

label ritsuko__cg_3_house:
    scene bg shinn bedroom with fade
    show ritsuko tennis horny
    "It's evening by the time I make it back home with Ritsuko after our session on the tennis court, but Ritsuko's lust hasn't begun to cool."
    ritsuko "Ah, Shinn~"
    ritsuko "Are you going to give me the lesson here in your room?"
    "I give her a contemptuous glance."
    shinn "You're here for more than just a lesson. I'm really going to pound you, Ritsuko."
    "Ritsuko perks up with excitement on hearing that."
    ritsuko "Let's get started then!"
    show ritsuko naked exposed
    "Ritsuko strips herself naked in front of me, without even waiting for my instruction."
    ritsuko "You like my body, right?"
    "It's not like I can deny that."
    "The body she's honed with her hard tennis practice is simply out of this world."
    "Or maybe she's just naturally gifted with that figure?"
    "As I focus my attention on her incredible body, I can't help but feel a twinge of regret over having to hand her over to the Principal."
    "Well, it can't be helped since I made a deal. But before I turn her over to him, I'm going to take the chance to have my fun."
    
    scene ritsuko__cg_3_house 1
    "Once again, Ritsuko moves without instruction, lying down on my bed facing me."
    ritsuko "Come on~"
    shinn "Heh. Did I ask you to lie down and strip for me?"
    shinn "You were supposed to listen to orders!"
    "Within a moment, I fling my own clothes to the floor and leap on top of her."
    shinn "I'm going to pound you hard till you remember to do what you're told!"

    scene ritsuko__cg_3_house 2
    "I slam my dick all the way into her pussy in one thrust, and she screams out in pleasure."

    scene ritsuko__cg_3_house 3
    ritsuko "Ah~ Shinn!"
    "I continue to pound away at her as she pants and wails under me."
    ritsuko "Yes! Shinn~ More~!"

    scene ritsuko__cg_3_house 4
    "Already, she's a far cry from the resistant girl she was earlier this afternoon."
    shinn "Remember this pleasure! Remember this feeling! ‘Cause this is what you're made for, and what you're gonna do for the rest of your life!"
    ritsuko "Yes! Yes Master~!"
    "She doesn't show even a trace of hesitation anymore."

    scene ritsuko__cg_3_house 5
    "Pounding her on and on, I keep on going without rest like a frenzied wild animal."
    "I plan for the two of us to keep fucking like rabbits all through the night."
    "I'm going to keep this up until there's nothing left in her but the desire to receive."
    ritsuko "Ah, Shinn! I want your cum in me so much! Please, give it to me!"
    shinn "Haha! You want to have my cum, eh!?"
    ritsuko "Yes, please!"
    shinn "As you wish!"
    "My whole body is pressed down against hers as I slam my hips against her."
    "The movement is so forceful, the bed is heaving against the wall."
    "I hope the bed will actually be able to last out the night."
    "With each thrust, I angle to reach as deep inside her as I can."
    "When I cum, she's going to feel me cum right into her womb."
    ritsuko "Ah! Shinn! Your dick's so deep inside me! I love it!"
    ritsuko "I can feel the tip inside my womb! It feels so good!"
    shinn "Yeah, go on and take it!"
    "Her pussy was already dripping wet from the moment of my first thrust, making my movements inside her perfectly smooth."
    "She still has traces of sweat on her from her workout on the tennis court before."
    "When I see her armpits right up near my face, I can't help but want to have a taste."
    shinn "Ritsuko, lift your arms for me."

    scene ritsuko__cg_3_house 6
    ritsuko "Ah? Hah... Okay..."
    "She lifts them up, giving me a perfect closeup view of her beautiful smooth armpits."
    "They're slick with sweat and steamy hot. I don't bother to hold myself back."

    scene ritsuko__cg_3_house 7
    "I reach my tongue out, and start to lick."
    ritsuko "Kya~! Shinn!"
    ritsuko "That's dirty~!"
    "I ignore her and continue to lick away."
    "The taste of a sporty girl's sweaty armpit is amazing."
    "It might not be for everyone, but to me, the taste and feel of this is simply irresistible."
    "Even without the rest, I could enjoy this by itself."
    "But there's no need to have it on its own. Far from it, as I lick her, I speed up my thrusts even more."

    scene ritsuko__cg_3_house 8
    ritsuko "Ah! Shinn! Kiss me!"
    ritsuko "Please, stop licking my armpit and give me a kiss!."

    scene ritsuko__cg_3_house 9
    "For this, I'll oblige her. I pull back, and thrust my tongue into her mouth for a deep kiss."
    "She braces her tongue against mine and tangles around it in her mouth."

    scene ritsuko__cg_3_house 10
    "Ritsuko can't help herself, slurping lewdly and sucking down my saliva as I invade her mouth."
    ritsuko "Mmm~ Shinn..."
    "The kiss only adds to the intensity as I pound into her."
    "Ritsuko keeps sucking desperately, unable to pull herself away."
    ritsuko "Mmm~!"
    "I keep on going, fucking her while locked in this kiss."
    "But it can't go on forever. I can feel myself getting close to bursting."

    if persistent.cum == "inside":
        "I'm about to reach my climax, locked hard against her like this."
        $ renpy.block_rollback()
        jump ritsuko__cg_3_inside

    elif persistent.cum == "outside":
        "I'm about to reach my climax, locked hard against her like this."
        $ renpy.block_rollback()
        jump ritsuko__cg_3_outside

    else:
        menu:
            "I'm about to reach my climax, locked hard against her like this."
            "Cum inside her":
                jump ritsuko__cg_3_inside
            "Cum onto her face":
                jump ritsuko__cg_3_outside

label ritsuko__cg_3_outside:
    scene ritsuko__cg_3_house 11
    shinn "Ah! I'm at my limit!"
    ritsuko "Yes! Shinn! Do it! Cum inside me!"

    scene ritsuko__cg_3_house 12
    thinking "It's really tempting..."
    thinking "But I want to see that face of hers smeared all over with my cum."
    ritsuko "Hurry up Shinn! Do it!"
    thinking "Should I?"
    thinking "Screw it, this one's to remind her who's in charge. I'm teaching her a lesson here."
    shinn "Here it comes!"

    scene ritsuko__cg_3_house_outside 1 with cum_flash
    play sound cum2
    "I pull out just in time and spray out a gush of my cum across her face."
    ritsuko "Ah~ Shinn's cum is all over me!"

    scene ritsuko__cg_3_house_outside 2 with cum_flash
    play sound cum1
    "I take a moment to admire my handiwork splattered across her slutty face"
    shinn "Heheh... Look at you."
    "Despite how much I just came, the sight of her face smeared with my cum still keeps my hard."
    "But, it looks like Ritsuko's feeling a bit unsatisfied."
    ritsuko "Unh... Shinn didn't cum inside..."
    shinn "Don't worry, Ritsuko. I still have plenty of training left to give you."
    shinn "Besides, the night is still young. We're gonna be keeping this up until morning."
    "My reassurance seems to completely revive her mood."
    ritsuko "Really?"
    shinn "Heh. Of course."
    "I position my rock hard dick against her entrance again."
    shinn "Alright, let's begin!"
    jump ritsuko__cg_3_end

label ritsuko__cg_3_inside:
    scene ritsuko__cg_3_house 11
    shinn "Ah! I'm at my limit!"
    ritsuko "Yes! Shinn! Do it! Cum inside me!"
    thinking "Not sure I want to take responsibility for what might happen.., "
    thinking "But who cares? That's a choice I can make one way or another later on."

    scene ritsuko__cg_3_house 12
    ritsuko "Hurry up Shinn! Do it!"
    shinn "Here it comes!"
    "I slam my dick into her one final time, piercing all the way inside her."

    scene ritsuko__cg_3_house_inside 1 with cum_flash
    play sound cum2
    "The gush of cum completely fills her up, overflowing and dripping out in seconds while I'm still seated inside her."
    ritsuko "Ah! Shinn's cum! It's inside me!"
    ritsuko "I'm so full of Shinn's cum!"

    scene ritsuko__cg_3_house_inside 2 with cum_flash
    play sound cum1
    "It's just too much for her to keep it all inside. It's leaking out all over now."
    shinn "There might be a lot of it inside you now, but there's a whole lot more left where that came from."
    "The thought of that gets Ritsuko excited all over again."
    ritsuko "Ah~ All of Shinn's cum inside me!"
    "Despite how much I just came, the sight of her freshly creampied pussy gets me hard again."
    shinn "Look at you. Mind completely broken, just the way I like."
    "I stare straight into Ritsuko's hazy eyes."
    shinn "I hope you don't think we're done already, Ritsuko."
    shinn "The night is still young. We're gonna be keeping this up until morning."
    ritsuko "Ah, yes! More! Give me more!"
    shinn "Good girl. That's the spirit."
    "I position my rock-hard dick against her entrance again."
    shinn "Alright, let's keep going!"
    jump ritsuko__cg_3_end

label ritsuko__cg_3_end:
    ritsuko "Yes Master!"
    $ renpy.end_replay()
    $ persistent.ritsuko__cg_3 = True
    if day == 2 and not staffroom_available and tennis_available and not gym_available:
        jump ritsuko__router
    else:
        jump map__school

label ritsuko__cg_4:
    $ renpy.music.play(audio.kinky, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    scene ritsuko__cg_4 1 with map_fade
    "The last few days with Ritsuko have been pretty busy."
    "I've been training her pretty much nonstop. I think she's completely lost track by now of how long it's been."
    "Looking at her now, her complete transformation from a snobbish rich girl to a sex-crazed bitch is pretty incredible."
    "At this point, she'll completely submit to the pleasure of anything I do to her."
    "So, I guess she's finally ready to bring back to the Principal as promised.."
    "I've gotten her properly giftwrapped, with a sexy pink sling bikini and a dog collar. After all, an occasion like this is worth putting some effort into presentation."
    
    scene ritsuko__cg_4 2
    "Her erect nipples stand out against the thin fabric of the bikini, showing off just how ready she is for action."
    shinn "So, I have the gift you've been waiting for."
    principal "Ah, Shinn. I was wondering when you'd be getting back to me."
    ritsuko "Hi! ~"
    principal "Oh, what do we have here?"
    ritsuko "It's me! Slutty Ritsuko!"
    principal "Well, this is certainly quite a change from last time."
    shinn "Yes. I hope I didn't keep you waiting too long, but I made sure to be quite thorough with her."
    shinn "She's had all the training she needs to be a completely loyal bitch."
    shinn "Just as promised, instead of a resistant schoolgirl for a few months, she'll be a committed sex slave for life."
    ritsuko "Teehee~"
    ritsuko "I can't wait to suck on your fat cock!"
    principal "Oh, very nice."
    principal "It definitely looks you trained her well. I really have to give you credit for coming through on this one."
    shinn "Thank you, Principal."
    principal "Now then, shall we have some fun with her?"
    shinn "We?"
    principal "Of course. You worked hard to make her like this. Why not enjoy her together?"
    principal "After all, you deserve it."
    thinking "Well, it'd be a new way to have fun with her after everything I've already done training her."
    shinn "If you're offering then..."
    principal "Do you want to have a taste of my dick, Ritsuko?"

    scene ritsuko__cg_4 3
    ritsuko "Yes! ~"
    principal "Good girl. Come here."
    "The Principal unzips his pants, exposing his steamy erect dick to Ritsuko."
    ritsuko "Ah! Dick!"

    scene ritsuko__cg_4 4
    "Rather than waiting for her to make a move, the Principal grabs holdof Ritsuko and hoists her into air, holding her entire weight suspended."

    scene ritsuko__cg_4 5
    ritsuko "Kya~!"

    scene ritsuko__cg_4 6
    "Holding her legs hiked up, the Principal positions his dick at the entrance of Ritsuko's pussy."
    ritsuko "Ah~ Principal's dick! I can feel it!"
    "She squirms a bit in his grip, trying to push herself down and bury his length inside her."
    ritsuko "Please put it in! I want your dick so bad!"
    principal "Good girl. In that case, go ahead and take it!"
    "The Principal slowly lowers her weight, impaling Ritsuko on his cock."
    ritsuko "Ah~! It's so big! I love it!"
    "The Principal lowers her all the way down, embedding himself completely inside her."
    ritsuko "Principal! Your dick is kissing my womb! It's driving me crazy!"

    scene ritsuko__cg_4 7
    "Ritsuko cranes her neck back and reaches out her tongue, inviting him in for a kiss."
    ritsuko "Principal~! Give me a kiss too~"
    principal "Here you go."

    scene ritsuko__cg_4 8
    "The Principal locks lips with her, docking his tongue into her mouth."
    "They tangle their tongues together so intensely that drool starts leaking out."
    ritsuko "Hmm~ Principal's saliva is so tasty."
    principal "Hahaha..."
    "Looks like he's pretty pleased with the effect my training has had on her."
    principal "Shinn! What can I say? You're really one of a kind!"
    shinn "Uhh... Thank you?"
    principal "Thank you? Come on, what are you waiting for?"
    principal "Come on and get your thanks over here!"
    principal "Her ass is out in the cold over here, she needs someone to warm it up for her!"
    ritsuko "Yeah! Hurry up Shinn! I want your dick inside my asshole!"
    shinn "..."
    thinking "These people are really on fire today..."
    "I approach Ritsuko from behind and unzip my pants."
    "Seeing Ritsuko acting like such a slut in front of the Principal has already gotten me plenty hard."
    thinking "Alright then, time to work out this tension on her."

    scene ritsuko__cg_4 9
    "I move myself into position, and thrust deep into her asshole."

    scene ritsuko__cg_4 10
    ritsuko "Ah! Two dicks inside me! It feels so good!"
    ritsuko "Hnnh~ Hah.... Aaaahh~!"

    scene ritsuko__cg_4 11
    "Ritsuko's body quivers in the Principal's grip as a jet of her pussy juices spills to the floor."
    ritsuko "Haahhh~ I came with two dicks in me."
    principal "Hahaha!"
    principal "I haven't even started moving again and you've already cum!"
    principal "What a hungry slut!"
    ritsuko "Please Principal, move your fat cock inside me!"
    principal "Alright then, you don't have to ask twice."

    scene ritsuko__cg_4 12
    "The Principal starts bouncing Ritsuko up and down on his cock, and I quickly follow suit, thrusting into her in time with him."
    "The pace is pretty slow to start with as we work out a rhythm, but Ritsuko's obviously still feeling it."
    ritsuko "Ah! Yes~! Dicks! Dicks!"
    "I've been preparing her for this for some time. Right now, she can't keep anything on her mind but the dicks she's taking inside her."
    shinn "Heheh... You really do love dick now, don't you?"
    ritsuko "Yes! I love dicks and I want to taste them all!"
    principal "Hahaha! You'll get plenty to taste today!"
    ritsuko "Yes! Thank you Principal! I can't wait to take in all your cum inside me!"
    ritsuko "I really want to taste it!"
    "The Principal gradually increases his speed, and I follow suit, keeping pace with him."
    thinking "God damn, for guy his age, the guy's got a hell of a lot of energy. Pounding her while holding her weight up like this is no joke."
    "As we speed up, Ritsuko pants and moans out her pleasure, taking it all like the slut she is."
    "On my end, it's actually getting a bit tough to keep this up, even though the Principal's the one taking most of her weight."
    "I'm just glad the guy doesn't seem to go out on the prowl now himself, otherwise I'd have a serious rival on my hands."
    "As we keep drilling her, her pussy juice leaks out more and more, even dripping down all the way to the floor."
    "Of course, this doesn't go unnoticed by the Principal."
    principal "Ah! What a dirty girl, making a mess all over my office floor!"
    principal "I can't have that sort of thing in here, I'm gonna have to punish you for that!"
    "The Principal starts to move his hips faster and faster."
    ritsuko "Kya~!"
    principal "You like that, don't you?"
    ritsuko "Yes! Harder! Please!"
    principal "Heh. Are you happy now, being such cock-worshipping slut?"
    ritsuko "Yes! I'm so happy! I love it!"
    principal "Good girl. I can tell you do from how your pussy's squeezing me. You really want me to cum, huh?"

    if persistent.cum == "inside":
        ritsuko "Yes! I want your thick baby-milk!"
        $ renpy.block_rollback()
        jump ritsuko__cg_4_inside

    elif persistent.cum == "outside":
        ritsuko "Yes! I want your thick baby-milk!"
        $ renpy.block_rollback()
        jump ritsuko__cg_4_outside

    else:
        menu:
            ritsuko "Yes! I want your thick baby-milk!"
            "Cum Inside her":
                jump ritsuko__cg_4_inside
            "Cum Outside":
                jump ritsuko__cg_4_outside

label ritsuko__cg_4_outside:
    principal "Ugh... I can't hold on much longer."
    "Looks like the Principal is reaching his limit."
    "Good timing, since I'm almost over the edge too."
    shinn "Ugh... Same here."
    ritsuko "Please cum! Please!"
    ritsuko "Please cum on your slutty cumdump bitch!"
    principal "Alright Shinn, let's cum together on her and give her that baby-milk she wants!"
    ritsuko "Yes~!"
    principal "Here it comes!"

    scene ritsuko__cg_4_outside 1 with cum_flash
    play sound cum2
    "The Principal and I pound her hard together one last time before the two of us pull out in unison."
    "We both let out jets of cum across her body, leaving every part of her streaked and spattered with our jizz."

    scene ritsuko__cg_4_outside 2 with cum_flash
    play sound cum1
    ritsuko "Ah! Cum! It's all over me!"
    ritsuko "I love the taste and smell and the feel! I love all of it!"
    "The shower of cum over her sends a shockwave through her whole body."
    ritsuko "Ah~ Cum~!"
    "From the look of it, her lust for cum has been pounded into her for life."
    principal "Hey, why don't you do a slutty peace sign?"
    principal "I wanna see it."
    ritsuko "Okay!"

    scene ritsuko__cg_4_outside 3
    "She lifts up her hands for a double peace sign in front of her face."
    ritsuko "Peace~!"
    principal "Oh, you'r making me hard all over again."
    shinn "Heh. It's too bad she doesn't have a proper creampie to complete the look."
    principal "Don't worry. We have all day."
    principal "We can keep on creampieing her all day until she gets pregnant."
    ritsuko "Yes! Please make me your cumdump until I'm pregnant!"
    jump ritsuko__cg_4_end

label ritsuko__cg_4_inside:
    principal "Ugh... I can't hold on much longer."
    "Looks like the Principal is reaching his limit."
    "Good timing, since I'm almost over the edge too."
    shinn "Ugh... Same here."
    ritsuko "Please cum! Please!"
    ritsuko "Please cum on your slutty cumdump bitch!"
    principal "I'm gonna make you pregnant!"
    ritsuko "Yes! I want Principal's baby! I want it!"
    principal "Here it comes!"
    principal "Take it, Ritsuko! Take my cum and get pregnant!"

    scene ritsuko__cg_4_inside 1 with cum_flash
    play sound cum2
    "The Principal and I pound her hard one last time before we both explode together."
    "The bursts of cum fill her, leaving drips of cum trickling out of her pussy and asshole."

    scene ritsuko__cg_4_inside 2 with cum_flash
    play sound cum1
    "There's so much, some of it is even dripping onto the floor."
    ritsuko "AAHH~! It's inside me!"
    ritsuko "The Principal's thick baby seed is inside me!"
    ritsuko "My egg's gonna be fertilized by the Principal's sperm!"
    principal "Hahahaha!"
    principal "Hey, why don't you do a slutty peace sign?"
    principal "I wanna see it."
    ritsuko "Okay!"

    scene ritsuko__cg_4_inside 3
    "She lifts up her hands for a double peace sign in front of her face."
    ritsuko "Peace~!"
    principal "Oh, you'r making me hard all over again."
    principal "I'm gonna fuck you hard every day to make sure you get properly pregant"
    ritsuko "Yes, darling~!"
    principal "Shinn, let's take turns for today."
    shinn "Heh. Sure, sounds like fun."
    jump ritsuko__cg_4_end

label ritsuko__cg_4_end:
    $ renpy.end_replay()
    $ persistent.ritsuko__cg_4 = True
    $ tennis_available = False
    scene black
    "END OF RITSUKO ARC"
    $ renpy.music.play(audio.campus, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    jump map__school