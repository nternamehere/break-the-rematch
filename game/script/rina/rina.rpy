label rina__router:
    if rina_next_step == "intermission":
        jump rina__intermission
    elif rina_next_step == "cg_3":
        jump rina__cg_3
    elif rina_next_step == "cg_2":
        jump rina__cg_2
    elif rina_next_step == "continue_2":
        jump staffroom_day_1__continued_2
    elif rina_next_step == "continue_1":
        jump staffroom_day_1__continued_1
    else:
        jump staffroom_day_1__start
    
label staffroom_day_1__start:
    $ rina_next_step = "continue_1"
    $ staffroom__first_visit = False
    scene bg staffroom with map_fade
    "..."
    "......"
    play sound door_open
    thinking "So, this is the staff room."
    "Back when I was a student, I was probably the only one who came in and out of here regularly for \"meetings\" with the female teachers."
    "I used to fuck some of them right in their workplace when everyone else had cleared out."
    "I wonder if I could pull the same thing off with Rina."
    "Speak of the devil..."

    show rina confident with moveinleft
    rina "Oh. Shinn. There you are."
    thinking "Huh? She actually came here looking for me?"
    shinn "Ah, Ms. Rina, good morning. Today's my first day working here. I hope you can offer me your guidance on the job."
    
    show rina vicious smile
    rina "Pfft. I wasn't expecting manners from the likes of you."
    thinking "This bitch..."
    rina "Right. Since you're already familiar with the school grounds, I'll just show you to your workplace. That's the space where you'll be doing your administrative work."
    shinn "Wait, administrative work? I didn't sign up for that. I'm just here as a tutor."
    rina "Well too bad. I discussed it with the principal, and he agreed you could handle some additional tasks while you're not working with students."
    thinking "I'm really getting the urge to kill this bitch..."
    
    show rina pissed 2
    rina "Do you have a problem with that?"
    "I give Rina the most convincing smile I've got."
    shinn "Of course not, Ms. Rina, no problem. I'll do my best."
    
    show rina vicious smile
    rina "Good. Now, since the tutoring only starts after regular classes have ended..."
    "She carries over a huge stack of paperwork, and slams it down onto my workspace."
    rina "Here's some easy administrative paperwork I need you to clear. Get it done before school lessons are over."
    thinking "Fuck!"
    "Simmering with rage, I do my best to fake an easy smile."
    shinn "Sure, Ms. Rina. I'll take care of it."
    rina "Good. Now, if there's anything else you need to know, you can come to me at my workplace and I'll sort you out."
    shinn "Okay."

    hide rina vicious smile with moveoutleft
    "Rina walks away."
    "I can't believe this. This bitch just wants to piss on me because of that encounter we had yesterday."
    "This throws a wrench into all my plans. How am I supposed to get close to any of the students while I'm shut up in here?"
    thinking "Shit. Well, there's no point agonizing over it. Better just get this stuff out of the way to get her eyes off me before I move on to the girls."
    
    scene black with fade
    "5 hours later"

    scene bg staffroom with fade
    shinn "Oh my god. It's finally over with."
    "After grueling hours of fixing simple errors, sorting out records and cross checking forms, I've finally made it through the whole stack."
    "I guess I'll check in with Rina to let her know I've gotten that out of the way."
    "As I approach her workplace, I see her heading towards the exit, looking like she's in a hurry."
    thinking "Hmm? What's wrong?"
    "Her expression grabs my attention. She seems worried and anxious. This is probably the first time I've ever seen her in such a state."

    if not gym_available and not tennis_available:
        jump staffroom_day_1__continued_1
    else:
        menu:
            thinking "Great. Just when I wanted to clear my work with her, she runs off. Now what?"
            "Now's my chance to make my move with the other girls!":
                jump map__school
            "Secretly pursue her and see what's going on.":
                jump staffroom_day_1__continued_1

label staffroom_day_1__continued_1:
    $ rina_next_step = "continue_2"
    scene black
    "I decide to be a busybody and follow her. This looks interesting, I don't want to lose track of her now."

    scene bg rooftop with dissolve
    "Using my ninja skills, I manage to chase her all the way to the rooftop without catching her attention."
    show rina pissed 2 with moveinleft
    "I hide behind the rooftop door and keep a close watch on her. She looks agitated as she takes out her phone and calls someone."
    rina "Would you stop trying to call me while I'm at work?!"
    thinking "Woah. That was pretty fierce."
    rina "I already said I wasn't going to have sex with you again! That was a one time thing, and I'm already regretting it!"
    thinking "Wait. What?"
    "I'm shocked to hear something like that out of Rina's mouth. She always puts up a front of being so straight-laced."
    
    show rina annoyed 2
    rina "Look, that only happened in the first place because I was drunk. Frankly, at this point, I have no interest in you at all. So, you can feel free to fuck off."
    thinking "Heh, looks like I've actually got some real dirt on her. And here I thought she was going to be a hard one to deal with."
    "This isn't going to be enough all by itself though. I need to do some more digging so I can properly play this to my advantage."
    rina "You know what? I'm done talking to you. I'm hanging up."
    
    hide rina with moveoutleft
    "As soon as she ends the call, she turns around and heads back towards the door."
    thinking "Oh shit, she's coming."
    "I move as quickly as I can and try to conceal myself in the corner."
    "She approaches the door and swings it open hard. She's clearly still venting her anger from the phone call as she heads back towards the staff room."
    shinn "Phew. That was a close call."
    thinking "Guess I'll head back along another route to meet up with her."

    scene bg staffroom with pixellate
    "I return to the staff room, but it seems like Rina still isn't back yet."
    thinking "She sure takes her time when she's angry."

    show rina confident with moveinright
    "Soon, Rina arrives in the staff room as well, looking composed once again."
    thinking "Wasn't she pretty wound up before? Maybe she's just putting up a front now to try and keep things under wraps."
    "I head over to her desk to let her know that the paperwork is done. As I approach, I notice that she's glued to her phone. She seems completely unaware of my presence just behind her."
    shinn "Ah... Ms. Rina. The paperwork you asked me to take care of is all finished."
    
    show rina annoyed
    "Rina turns around with a jolt, looking startled."
    rina "Oh, Shinn. So you're done."
    shinn "Er... Are you alright Ms. Rina?"
    "She immediately snaps back to her normal self."

    show rina vicious smile
    rina "What do you mean? I'm completely fine."
    rina "Since you've finished, I guess you can go now. Classes should have ended already. I'll pick up the paperwork from your workplace later on."
    shinn "Alright."

    if not gym_available and not tennis_available:
        jump staffroom_day_1__continued_2
    else:
        menu:
            thinking "Hmm... I wonder what I should do now?"
            "Now's my chance to check on the other girls!":
                jump map__school
            "Try to probe her and find out more.":
                jump staffroom_day_1__continued_2

label staffroom_day_1__continued_2:
    $ rina_next_step = "cg_2"
    scene bg staffroom
    show rina annoyed 2

    shinn "Ms. Rina, Is there anything else that I can do for you?"
    rina "Huh? Weren't you supposed to get started on tutoring our students?"
    shinn "Well, I thought maybe just for now, I might be able to do something to help you."
    "Rina is clearly put off by my suggestion."
    rina "No. Your job here is to tutor our students who are in need. The most helpful thing you can do is to do your job properly."
    shinn "Sheesh... Relax. I just wanted to help."

    show rina pissed 2
    rina "More like you're trying to butter me up. You'd better not try anything funny. I have my eye on you."
    thinking "Heh. I wonder who's watching who, Ms. Rina."
    rina "I don't have the time to talk to you right now. I have a meeting coming up, so I'll be heading out now."
    
    hide rina pissed 2 with moveoutright
    "Rina leaves the staff room in a hurry. She doesn't seem to give a second thought to leaving me behind in her workplace."
    "She probably never stopped to think that I might search through her things. Much too naïve, Rina."
    shinn "Hmm... Let's take a look."
    "As I scan her desk, I realize that she's left her phone behind on the table. A fatal mistake for her."
    shinn "Well well well... What do we have here? Looks like something pretty handy."
    shinn "Time to see what's inside."
    "To start with, I take a look through her messages and call history. I know she called someone just now, and want to get the number behind that."
    "Once I have that, I can dig up all her other calls and messages with the same guy."
    "There, that was easy enough to find."
    shinn "She's got several recent messages from the same number."
    "I open up one of the messages and take a look."
    "To my surprise, there's a picture attached of her lying naked in bed, cum leaking from her pussy. A guy sits beside her, posing with a peace sign."
    shinn "Checkmate."
    "I hide the phone away carefully. After all, there's no question she'll come running back for this soon."
    shinn "Let's wait and see what happens when she realizes she's missing this."

    scene bg hallway 1 with irisin
    "I loiter around the hallway to see if Rina's heading back to retrieve her phone."
    if tennis_available:
        "However..."
        ritsuko "Hohoho..."
        thinking "Un-oh."
        ritsuko "What do we have here?"
        thinking "Not the person I was hoping to hear from right now."
        ritsuko "What are you doing sneaking around the hallway?"
        shinn "I'm not sneaking around."
        ritsuko "Oh? I bet you're looking around scoping this place out for girls."
        thinking "This bitch..."
        shinn "Look. What do you want?"
        ritsuko "Oh hohoho~"
        ritsuko "Just making sure you don't try anything stupid while you're here."
        ritsuko "I'm watching you Shinn..."
        "Ritsuko leaves looking proud, like she's caught me out and gotten the upper hand on me."
        thinking "What a pain in the ass she is..."

    else:
        "However..."
        "From a distance, I can see Ritsuko approaching, looking distressed and defeated."
        thinking "Uh-oh"
        ritsuko "..."
        "She obviously notices me, but after giving me a glance, she turns and walks on without saying a word."
        thinking "Well, no big wonder there."
        thinking "After all, she was just raped by the guy she was expecting to enforce the rules in this school"
        thinking "Just wait till I get to her..."

    thinking "Now, where was I?"
    thinking "Oh, right. Rina still isn't back yet."
    thinking "Damn it!"
    play sound heels
    "However, after waiting a little longer, I can hear the loud, quick-paced clicking of footsteps approaching."
    "It sounds as if someone is nearly running while wearing high heels."
    thinking "That has to be her."
    "When she comes around in sight of me, she doesn't even register my presence and heads straight into the staff room."
    "From out in the hallway, I can hear the sound of her rummaging around and banging things down as she searches her desk. Unable to find it, she steps out of the staff room, her anxiety painted all over her face."
    "Scanning the hallway, she finally notices me and hurries up to speak to me."
    
    show rina pout with moveinleft
    rina "Shinn! Have you seen my phone? You were near my workplace when I left, right?"
    shinn "Your phone?"
    show rina angry

    menu:
        rina "Damn it, Shinn. Don't play dumb with me. Have you seen it or not?"
        "Lie to her.":
            $ renpy.block_rollback()
            jump staffroom_day_1__lie
        "Tell her the truth.":
            $ renpy.block_rollback()
            jump staffroom_day_1__truth

label staffroom_day_1__truth:
    "I take the phone out from my pocket and flash it right in front of her face."
    shinn "What, is this the one you're looking for?"

    show rina pissed 2
    rina "Yes, that's my phone. What are you even doing with it? Give it back!"
    shinn "Give it back? Not so fast."
    rina "Stop kidding around and hand it over!"
    "Time to play my hand."
    shinn "Perhaps we should have a discussion about those photos on your phone first?"
    
    show rina annoyed 2
    rina "What? What photos?"
    thinking "Playing dumb, huh?"
    "Although she's trying to feign ignorance, her face shows that she's clearly worried."
    "I go ahead and show her the photos I found inside her phone."
    shinn "Well. You still wanna play dumb with me?"
    rina "Give me back my phone!"
    shinn "Not a chance, Rina."
    rina "You..."
    shinn "Heh. To think you'd actually turn out to be such a slut."
    rina "Give it back to me or else..."
    shinn "Or else what? What are you going to do to me?"
    shinn "Keep in mind there are still students around. You wouldn't want them to find out about this, right?"
    rina "You asshole. I knew from the start that you were up to no good."
    thinking "Heh. I've got her properly cornered now."
    shinn "Good. Looks like you know where you stand here."
    "Rina was silenced."
    shinn "That's right, you have nothing on me right now."
    shinn "However..."
    "I walk up close to her and lean in, whispering into her ear."
    shinn "It looks like I've got something you want, don't I?"
    shinn "Let's settle this matter somewhere appropriate, alright?"
    jump rina__cg_1

label staffroom_day_1__lie:
    shinn "No, I don't think I've seen it."
    rina "You sure? Don't lie to me."
    shinn "I am sure. Why would I lie to you?"
    "With no reason to suspect me, she lets it drop. But her desperation to find her phone is unabated."
    rina "In that case, could you help me find it? It's very important to me."
    shinn "If it's missing, couldn't you just buy a new one?"
    rina "No, I've got some important stuff on that one."
    thinking "Heh. Some pretty important pictures."
    shinn "What kind of important stuff?"

    show rina pout
    "Rina gives a clear look of embarrassment as she thinks about what she has on that phone."
    rina "Look, don't pry so much. Will you help me out or not?"
    thinking "Even if I hadn't already seen, she's completely giving herself away. This should be fun."
    thinking "Let's see how long it takes for her to catch on."
    shinn "Sure, I'll help. Let's go through the staff room together to start."

    scene bg staffroom with fade
    "By this time, the staff room is empty apart from us. All the teachers are either on break, or out at the meeting Rina was supposed to be attending."
    "Since it's just two of us here, I relax as I pretend to look around the room, keeping my eye on Rina."
    "Rina, on the other hand, is working herself into a frenzy, sifting through boxes in the increasingly desperate hope of finding her phone."
    
    show rina angry
    rina "Damn it! Where could it be?"
    "Suddenly, Rina straightens up, an idea dawning on her."
    rina "Oh, I know. I can just use the school's line to call my phone. I didn't leave it on silent."
    "I nod at her suggestion, while I continue to pretend to search around for her phone."
    play sound phone_ringing
    thinking "Oh shit. I didn't turn it off!"
    rina "Oh, I heard it."
    thinking "Fuck! Turn it off! Turn it off!"
    "Rina follows the sound of her ringtone. I tried to stop it, but I was already too late. She catches me clearly holding the phone in my hand."
    
    show rina pissed 2
    rina "Shinn... I think you have some explaining to do."
    "Well, the game is up now, there is no point in hiding anymore."
    shinn "Well, Ms. Rina, I think YOU have some explaining to do."
    rina "Stop kidding aroun—"
    "I cut her off before she can seize the initiative."
    shinn "Kidding? I don't think those photos on your phone were any kind of a joke."
    rina "Photos?"
    shinn "You know exactly what I'm talking about."

    show rina annoyed 2
    rina "What photos?"
    "She's still playing dumb, but the worry on her face is obvious."
    "I hold up the phone in front of her, and flip through the photos I discovered."
    "Her worried expression turns to shock, and then just as quickly, to rage."
    shinn "Well. Still wanna act dumb with me?"
    rina "Give me back my phone!"
    shinn "Not a chance, Rina."
    rina "You..."
    shinn "Heh. To think you'd actually turn out to be such a slut."

    show rina pissed 2
    rina "Give it back to me or else..."
    shinn "Or else what? What are you going to do to me?"
    "Rina was silenced."
    shinn "That's right, you have nothing on me right now."
    shinn "However..."
    "I walk up close to her and lean in, whispering into her ear."
    shinn "It looks like I've got something you want, don't I?"
    shinn "Let's settle this matter somewhere appropriate, alright?"

label rina__cg_1:
    scene bg utility room with fade
    show rina pissed 2 with moveinleft
    play music happy fadeout 1.0 fadein 1.0
    "I bring Rina to the utility room."
    "This place is nice and secluded, and I know well from experience that nobody ever visits here at this time of day."
    "Rina follows along in quiet frustration. Before we enter, I scan the hallway to make sure that nobody sees us heading in together, then close the door behind us."
    play sound door_close
    shinn "Well, now that we're here..."
    "She immediately cuts in."
    rina "You better not try anything funny, you sicko."
    shinn "Woah. Relax, Ms. Rina. All I wanted to do is give you some training."

    show rina annoyed 2
    rina "What? Train me?"
    shinn "Yes. Train you and discipline you."

    show rina angry
    rina "Don't fuck around with me, Shinn."
    shinn "Well, Ms. Rina, considering your position as a disciplinary teacher, I'm afraid it's simply unacceptable for you to behave in such a manner while you're off campus."
    shinn "Therefore, I feel that it's my responsibility to teach you to conduct yourself in a more appropriate manner."
    rina "Who the fuck do you think you are?"
    thinking "This bitch is awfully slow on the uptake."
    shinn "*Sigh*. Come on, Rina. We've discussed this already, haven't we?"
    "I take out her phone again to show her where she stands."
    shinn "I don't think it would go well for you if these photos were spread all around the school would it?"
    
    show rina pout
    rina "..."
    shinn "Good. Then let's get started."
    shinn "Strip yourself naked "
    "Rina is stunned. But with no way to resist, she removes her clothes in disgust."
    
    show rina naked
    "Once she's fully naked, I look her over from top to bottom with satisfaction. Her huge, shapely ass, her incredible tits and luscious hips..."
    "Just the sight of her is getting me rock hard."
    shinn "That's good. Now squat down."
    rina "..."
    shinn "Come on... Be a good girl."

    scene rina_masturbation_1 1 with dissolve
    "She squats down in front of me, leaving her pussy fully exposed to my view."
    "She gives me a look of disgust."
    "Is she disgusted with me, or with herself for playing along with her own humiliation?"
    rina "What do you want now!?"

    scene rina_masturbation_1 2
    "I take out a vibrating dildo and flash it in front of Rina."
    shinn "Do you know what this is?"
    "Rina looks at it with embarrassment."
    rina "Wh— What are you planning to do with this?"
    shinn "Oh, I'm not really planning to do anything with it."
    shinn "Instead, why don't you try inserting it yourself?"
    rina "What? Are you crazy?"
    shinn "Hahahaha...."
    shinn "I just want to see you pleasuring yourself. Is there anything wrong with that?"
    shinn "Remember, you don't have a choice here."
    rina "..."
    "Rina takes the dildo from my hand."
    rina "Fine! I'll do it!"
    "Rina slowly inserts the dildo into herself bit by bit."

    scene rina_masturbation_1 3 with quick_fade
    play sound insert1
    "As she does so, she accidently lets out a little moan, already starting to feel pleasure from the insertion."
    rina "Mmm..."
    shinn "See? I knew that you'd enjoy this..."
    rina "N— No. I'm not."

    scene rina_masturbation_1 4
    "The dildo fully seated inside her now. I can see drips of her pussy juice leaking around it."
    shinn "You're already wet just from putting it in."
    rina "..."
    "I take a remote control from my pocket, and show it off in front of Rina."
    shinn "So, can you guess what this is a remote control for?"
    rina "No... Please don't..."
    shinn "What are you begging me for? You're going to enjoy this."

    scene rina_masturbation_1 5
    "I turn the switch on the remote to \"on,\" and the dildo begins buzzing inside her."
    rina "No! Please stop!"
    "Her reaction makes clear, the vibrations are already having an effect on her."
    rina "No..."
    "From the look of it, she's trying her best to suppress the pleasure."
    shinn "Are you starting to enjoy yourself yet, Rina?"
    rina "No! Just get this over with!"
    "Seems like she's still looking to resist."
    shinn "Well, that's fine, don't worry."
    shinn "After all, this is still just the lowest setting."
    shinn "I slowly turn up the intensity a little..."
    rina "Mmm..."
    "She lets out another moan before she manages to regain control of her voice."
    "Even though she's holding her voice back, her body isn't hiding it at all."
    "Her pussy is twitching around the dildo, as little droplets of her juice fall between her legs."
    thinking "Looks like she's already on her way to losing it."
    "I grin as I call her attention to the state she's in."
    shinn "Look at you! See how much you're leaking just playing around with a dildo in front of me?"
    shinn "Admit it, you're a slut."
    rina "No! That's not true!"
    shinn "Yeah... That's what every girl says before they reveal their true colors."
    shinn "Tell you what. If you're not having enough fun already, why don't I increase the intensity some more?"
    rina "No!"
    "Ignoring her plea, I shift the level higher again."
    rina "Mmmm!"
    "She lets her voice out involuntarily again with the new increase in intensity."
    shinn "Does that feel any better now?"
    rina "..."
    "She doesn't say anything this time. Instead, she looks desperately focused on trying to hold her voice in."
    "There's a tremor in her thighs, and her juices are dripping freely now."
    "Her expression looks almost pained with her efforts to control herself."
    "At this point, it's pretty clear that she won't be able to hold out."
    shinn "So, are you feeling good now Rina? You think you're going to cum?"
    rina "..."
    "She doesn't give me an answer this time. She probably wants to deny it, but she doesn't trust her voice not to betray her."
    shinn "Well, if you don't have anything to say..."
    shinn "Let's turn it up to max!"
    "I increase it to the highest intensity."
    "The dildo is buzzing loudly now, sending flecks of her pussy juices flying as they drip down over it."
    rina "No... Please..."
    "From her expression, I can see she's going to lose it any moment now."
    rina "I can't..."
    shinn "Can't what? You know you can just cum. You don't have to fight against yourself."
    rina "No..."
    rina "I can't hold it... I need to cum..."
    shinn "Go on then. Cum like a bitch."
    rina "..."
    shinn "This is fun. Let' see how long you can last..."
    "Even though she struggles her hardest against herself, she only holds out for seconds longer."
    rina "Ahh~"

    scene rina_masturbation_1 6 with cum_flash
    play sound cum3
    "She comes violently, a jet of her juices gushing from her pussy."

    scene rina_masturbation_1 7 with cum_flash
    "The force of her orgasm expels the dildo from her body, sending it clattering to the ground beneath her spasming pussy."
    "Her whole body is shuddering with the pleasure. Her hips are shaking and her eyes have gone hazy."
    shinn "Heh. You love it, don't you? Look how much you're enjoying yourself."
    rina "..."
    shinn "Now then..."
    
    scene rina_blowjob_1 1 with quick_fade
    "I unzip my pants to reveal my huge dick."
    shinn "Would you like to taste a real cock instead?"
    "Rina looks at it dumbfounded. Seems like she never expected a young guy like me to be packing something like this."
    rina "..."
    shinn "What? Embarrassed to see a real dick? I'm pretty sure you've seen a few of these before."
    rina "No..."
    shinn "What a blatant lie. Or is it just because mine is the biggest you've ever seen before?"
    rina "Shut... Up..."
    thinking "Heh. Seems like those guys in the photos have nothing on me."
    shinn "Let's cut the crap, shall we? I want you to give me a blowjob."
    rina "..."
    "Rina's mind is already cloudy from her last orgasm, and she moves now without hesistating."
    "Now, rather than disgust, her face seems to show fascination as she approaches my huge cock."
    
    scene rina_blowjob_1 2 with quick_fade
    play sound oral1
    "She begins to take a little sniff at my dick and licks lightly at the tip."
    shinn "Ah, that's it. Good."
    rina "..."
    "Her look of focus increases further as my pre-cum starts to leak out."
    shinn "So, how does it taste?"
    rina "..."
    "I can see that she's starting to enjoy it."
    shinn "It's not that bad, is it?"
    rina "..."
    "She doesn't respond to my question."
    "Instead, she just keeps her mouth glued to my cock."
    "She licks at it as if she were licking ice cream."
    shinn "Come on. Do more!"

    scene rina_blowjob_1 3
    play sound oral2
    "I urge her to take my dick all the way into her mouth."
    shinn "Deep throat it!"
    "She complies slowly trying to take my whole cock inside her throat."
    "As she gets a good taste of my dick, I can see that her switch is starting to flip."
    "The expression in her eyes is beginning to shift from focus and curiosity, to enthusiasm."
    "She pauses for a moment to enjoy the savory taste of my dick."
    rina "Mmm..."
    "She picks up her movement again slowly and steadily. She keeps up the suction in her mouth constantly, as if she's a cum-sucking machine. Seems like she's a real expert at this sort of thing after all."
    shinn "Ah. That's good. Rina. Suck it more."
    "The temptation to cum under the force of her efforts is building."
    "It seems like she's enjoying it too. The more my pleasure builds, the harder she works, sucking faster and more forcefully at my cock."
    "It's not just my imagination, I can hear the sound building as the intensity of her blowjob increases"
    thinking "Damn. She really is enjoying this."
    thinking "I don't think I can keep up..."
    thinking "Ugh. At this rate..."
    shinn "Rina, I'm gonna cum."
    rina "Mmm..."
    "She looks at me with that hazy look, signaling that she's ready to take it all."
    "Unable to hold on any longer, I let it all out in an instant. Her mouth is filled with an explosion of my cum."
    
    scene rina_blowjob_1 4 with cum_flash
    play sound cum2
    shinn "Ah!"
    rina "UHMM!!!!!!"
    "The rush is so sudden and forceful, some of it bursts from her nose. What a pitiful sight."
    
    scene rina_blowjob_1 5 with cum_flash
    play sound cum1
    "I pull out from her mouth. It's so completely filled with my cum, I can barely see her teeth."
    shinn "Swallow all the cum. Do it!"
    rina "..."
    shinn "Do it. Go on and savor the taste."

    scene rina_blowjob_1 6 with quick_fade
    "She closes her mouth and tries to gulp it down. It's too much for her to take in at once, but she still tries her best."
    "It's clear that right now, she's still reveling in what she just did."
    rina " Mmm..."

    scene rina_blowjob_1 7 with quick_fade
    "When she opens her mouth once again, there's not a trace of it left. She's completely swallowed it all."
    rina "Ah..."
    shinn "Heh. Good girl."
    shinn "See? I knew you'd enjoy this."
    rina "..."
    "As she tries to recover her senses, she lets out a soft and submissive voice."
    "She looks at me as if she's pleading for mercy."
    rina "Give... it... back..."
    shinn "What? Give you back what?"
    rina "My... Phone"
    thinking "Ha! What an idiot."
    shinn "Are you stupid? You think you've earned it back just like that?"
    rina "W— What?"
    "Rina looks at me, shocked, as if I've just betrayed her."
    shinn "We've only just gotten started, Rina. There's still more to come for someone like you."
    shinn "Your discipline lesson isn't over yet."
    rina "You... Mothe—"
    shinn "Woah. Hold your language, Rina. You shouldn't be so rude to your colleagues."
    rina "..."
    shinn "Tell you what. I think we can have some more fun together."
    shinn "So why don't you meet me naked at the rooftop in the evening later? If you come, I promise I'll give you back your phone."
    rina "I don't believe you!"
    shinn "Well. Whether you decide to believe me or not is entirely up to you."
    shinn "But for now, I'll be keeping this with me."
    shinn "And I don't think it would be a good idea for you not to come."
    shinn "Especially given what the consequences of that would be."
    rina "..."
    shinn "Well, think about it."
    "I left the room to make some preparations of my own."
    thinking "Heh. I'm going to have some real fun later on."
    $ renpy.end_replay()
    $ persistent.rina__cg_1 = True
    $ staffroom_available = False
    play music campus fadeout 1.0 fadein 1.0
    jump map__school

label rina__cg_2:
    $ rina_next_step = "cg_3"
    scene bg rooftop with map_fade
    "It's evening, and the sun has already started to set. I'm still waiting for Rina to show up."
    thinking "Where is she?"
    show rina overcoat with moveinleft
    "Just then, the door creaks open, and a familiar figure emerges behind it. Looks like she's decided to show after all."
    shinn "There you are. What took you so long?"
    rina "Shut up, you piece of shit. You don't need to know."
    "Taking a look at her, it seems like the hold-up might have something to do with how she's dressed. She's wearing a brown trenchcoat which hangs all the way to the floor."
    "She must have walked through the school in that to get here."
    shinn "Heh. Must be pretty embarrassing for you walking around school with nothing but that coat on, huh?"
    rina "Shut the fuck up."
    shinn "Well. I guess it doesn't matter right now. Unbutton it, I want to see that naked body of yours."
    show rina naked
    "Flushed with shame and seeming even shyer than before, she strips herself down in front of me once again."
    shinn "Oh, looking pretty sexy there..."
    rina "..."
    shinn "Ha, I didn't expect you'd go to the trouble of dressing yourself up for me."
    rina "..."
    shinn "I guess you're really looking forward to what I have in store for you."
    rina "Shut up!"
    shinn "So tell me Rina, how do you feel, exposing yourself in the open like this?"
    rina "..."
    "She doesn't reply, and tries to cover herself with her hands while refusing to meet my eye."
    shinn "Good. I like you this way."
    "I made my own preparations before I came here as well. This bag contains a supply of sex toys I can use to train her all night long."
    "Hopefully, by the end of the day, I'll have made her putty in my hands. Just like I used to do in the old days."
    shinn "Now. Get in the doggy position."
    rina "W.. Wh—"
    shinn "You heard me. In the doggy position."
    "Rina freezes in hesitation."
    shinn "Do you want your phone back or not?"
    "She glares at me with hatred before she complies, getting down on her hands and knees."
    
    scene rina_rooftop_1 1 with fade
    shinn "Good girl."
    "Once she's assumed the postion, I walk up to her and lean over, looking her in the face."
    "From my bag, I retrieve a set of pink anal beads, and hold it up in front of her."
    shinn "We had some fun with your pussy before. So now, let's have fun with your ass."
    rina "Wait, what?"
    shinn "You heard me."
    rina "No way..."
    "Having informed her of my intentions, I move around behind her to inspect her ass more closely."
    "Taking a close look at it, it seems to be completely unused."
    shinn "Hmm... Any guys ever play with your ass before?"
    rina "What are you on about!?"
    shinn "I'm saying, judging by the look of it, it seems untouched. Looks like I'm going to be the first."
    rina "Don't you dare..."
    shinn "Hahaha!"
    "I start to stroke and touch around her back hole."
    rina "Wait, what are you doing?!"
    shinn "Wow, you seem pretty soft back here."
    shinn "Here, let me try out the inside."
    "As I insert my finger, her body immediately reacts."

    scene rina_rooftop_1 2
    rina "No! What are you doing!? Stop!"
    shinn "Wow. Your ass really is soft inside."
    rina "It hurts! Please!"
    shinn "It hurts, huh? Well, let's see if we can turn that pain to pleasure."
    "I twist my finger around and angle it inside her to target her weak spots."
    rina "Ah~ No~"
    "Rina lets out a little moan."
    shinn "Feeling it already, huh? Looks like your body is built for this."
    rina "Stop it!"
    shinn "A man never puts down what he's doing halfway through!"
    "I increase the pressure a bit more, pushing her to climax from her ass."
    rina "Ah~"
    shinn "What's the matter? Just give in to the pleasure."
    "It's clear that Rina is trying to hold back the feeling as much as she can."
    "So, I increase the intensity on my end to compensate."
    rina "Mm!"
    "At this point, I can see the juices slowly starting to leak from her pussy."
    shinn "See!? You're getting this wet already. Just let go, Rina."
    shinn "Indulge in the pleasure! Let it all out!"
    rina "..."
    "She's still being stubborn. So, I decide to work my way further into her ass."
    rina "Ah~"
    "She feels my fingers plunging all the way in."
    rina "No~"
    "I ramp up the intensity in a bid to make her climax."
    shinn "Time to turn it up!"
    rina "Ah~"
    rina "I can't..."
    shinn "You can't? Then let it out. You'll feel better that way."
    "Her legs have started to tremble, and her juices have started dripping down her thighs."
    "It's only a matter of time now."
    rina "Ah~"
    rina "I can't hold it!"
    "Her pussy twitches as her juices start gushing out."

    scene rina_rooftop_1 3 with cum_flash
    play sound cum3
    "Looks like she finally submitted to the pleasure from her ass."
    "I remove my fingers from her anus."

    scene rina_rooftop_1 4
    "Surprise surprise, her hole is twitching like mad."
    shinn "Good girl, Rina."
    shinn "I told you you'd enjoy it."
    rina "..."
    "Her expression is vacant and hazy from her climax. All the better for me."
    shinn "Well, let's get on to the next play, shall we?"
    "I pick up the set of anal beads I showed off to Rina before."
    
    scene rina_rooftop_1 5
    shinn "Remember these? I think you've gotten enough of a warm-up now."
    rina "..."
    "Rina doesn't respond, but I see a hint of curiosity on her face."
    shinn "Let's get you lubed up first."
    "I run my fingers along her pussy, coating them in her juice, before inserting them back into her ass."
    rina "Ah~"
    "I rub around inside her hole again for a bit to make sure she's ready."

    scene rina_rooftop_1 6
    "Her insides feel loose and steamy hot from her last orgasm."
    "Now that she's ready, I position the first bead at the entrance of her anus."

    scene rina_rooftop_1 7
    "She can feel the tip of the sex toy pushing up against her."
    rina "Ah~ No!"
    "I slowly push the first bead inside."
    rina "Mmm~"
    "She lets out a little moan, but I don't give her a response this time. Her asshole seems soft and pliant, easy to tease."
    "Without further ado, I switch on the anal bead. The sudden vibration sends a shock of pleasure through her body."
    rina "AHH!"
    "She lets out a wild scream. Sounds like unrestrained pleasure to me."
    shinn "Enjoying it so far?"
    "Her face shows a look of shock. Compared to my finger before, the stimulation from the vibrating bead is far more vigorous."
    rina "No! Please take it out! It's disgusting!"
    shinn "Pfft... Relax,Rina, we're just getting started here."
    "Despite her protestations, I can see more juice leaking from her twitching pussy. She's definitely feeling it."
    shinn "Why lie to yourself Rina? You're enjoying this."
    rina "NO!"
    shinn "Come on. Be honest with yourself. You see how wet you've gotten? Why not come to terms with the slut you are?"
    rina "NO! Please stop!"
    shinn "Heh. Like hell I'm going to stop now."
    "I push my head in close and start to lick her clit. I can feel her body shivering in excitement against me."
    
    scene rina_rooftop_1 8
    rina "Ah~ No..."
    shinn "See? You like it after all."
    "Using my index and middle finger, I begin to penetrate her pulsing wet pussy. She's so soaking wet inside, it feels like dipping my fingers into a warm pool. She lets out a moan as she feels my fingers thrust inside her."
    
    scene rina_rooftop_1 9
    rina "Ah~"
    "It was soft, but I could hear it clearly."
    shinn "I'm gonna make you cum, Rina"
    "I start to work my fingers around inside her, stimulating the walls of her vagina."
    rina "Ah~ No! Stop!"
    "I can tell it's getting to her. Her pussy is streaming with her juices, and her legs have started to quiver again. It seems like she's getting close."
    "Her reactions spur me on, and I start to move my hand even more aggressively."
    rina "NO! PLEASE STOP!"
    "Her legs buck as a sudden splash gushes from her pussy. Her eyes roll back as she shudders with more pleasure than she can take."
    "The convulsions of her orgasm force the beads out from her ass all at once."
    
    scene rina_rooftop_1 10 with cum_flash
    play sound cum3
    "The string of anal beads falls to the ground, still vibrating."
    rina "AAAHH!"
    "Her legs are shuddering, and her pussy is pulsing wildly, clamping down on my fingers."
    "I guess that means she wants more. I unzip my pants to reveal the cock she'd sucked before."
    shinn "Look at it. You like it right?"
    rina "..."
    "Her asshole was twitching. I guess she wants it there."
    shinn "Looks like you want to have some more fun with your ass."
    rina "Wait... No..."

    scene rina_rooftop_2 1
    "Rina looked back with a worried face."
    shinn "No what?"
    rina "Please don't stick it into my ass..."
    shinn "Heh. Why not?"
    rina "It's dirty..."
    shinn "Dirty? Nah, it's okay."
    shinn "I'll clean it up for you with my dick."

    scene rina_rooftop_2 2
    "I set the tip of my cock against her ass."
    rina "No! Please..."
    shinn "Here it comes!"
    "I slowly thrust inside her slippery asshole."
    rina "Mmm~"
    "Once again, Rina lets a little moan slip out."
    "The more we continue, the more her real self is starting to show through."
    "I continue thrusting into her as I feel the walls of her rectum squeezing against me."
    shinn "Man. I didn't think your ass would be this tight."
    shinn "It's almost like I'm fucking a real pussy back here."
    rina "No~"
    "I can feel her clamping down on me with every thrust."
    shinn "Heh... Seems like you really want me to cum."
    rina "No~ That's not true! Please take it out!"
    rina "It's disgusting!"
    shinn "Ah! Disgusting?!"
    shinn "Why are you so concerned with what's disgusting?"
    shinn "Look at yourself! Look at how dirty you are!"
    shinn "Out here getting fucked in the ass on the roof of the school."
    shinn "What does that make you? You're nothing but a pig whore!"
    rina "..."
    "The more I mock and shame her, the harder I can feel her clamping down on my dick."
    rina "You're... too... rough..."
    shinn "Too rough?"
    shinn "I don't think so..."
    "I start to rail her ass even harder. She's feeling the pleasure and pain blending together."
    rina "Ahh~"
    shinn "That's right. A whore like you loves it like this."
    "With every insult and bit of dirty talk, I can feel her squeezing down more against me."
    shinn "You really do want me to cum, huh?"
    rina "No..."
    shinn "Stop lying to yourself."
    "I slam my dick into her even harder..."
    rina "..."
    "Rina is left speechless for a moment by the intensity of the feeling."
    "I'm getting close to cumming. But, not without letting the little slut know first."
    shinn "Time for an anal creampie!"
    rina "Mmm~"

    scene rina_rooftop_2 3 with cum_flash
    play sound cum2
    "I shoot my cum out into her ass."
    rina "Ahh~! Cum!"
    rina "Its flowing into my stomach! I can feel it!"
    "Her entire body is trembling again. I get the impression this is going to be a routine thing for her."
    "In fact, I'm going to make sure of that myself..."
    shinn "That's right. Feel that hot cum inside your stomach."
    shinn "You dirty whore."

    scene rina_rooftop_2 4 with cum_flash
    play sound cum1
    "I take out my dick, letting the jizz I'd shot inside her flow free."
    shinn "Wow. That's a lot."
    shinn "Heheh... I wasn't expecting your ass to squeeze out so much."
    rina "..."
    "I took a look at her eyes. She looks drunk with lust."
    thinking "Seems like she's already half broken..."
    thinking "Time for the final step."
    shinn "Done already? I'm not done yet."
    "My cock is still rock hard."
    shinn "See what I've got ready for you, Rina?"
    rina "..."
    "She looks at my cock with a dreamy expression."
    shinn "If you want my cock, go ahead and beg for it."
    rina "..."
    "For a moment, a look of shock penetrates her haze of lust."
    shinn "Don't play dumb with me. I know you want my cock now. If you want it, show me and beg for it."
    rina "..."
    "I can tell she wants it, but she still resists saying it."
    "I keep pushing her for an answer, trying to force her the rest of the way."
    shinn "Don't want it? Fine. We can end this right now and I can give you your phone back. But, you'll never see my cock again."
    rina "..."
    shinn "So? What's it going to be?"
    rina "Shinn... cock..."
    "Her voice is barely a whisper. I can just make out her words, but I want to hear her loud and clear."
    shinn "What? You've gotta say it louder, I couldn't hear you."

    scene rina_rooftop_2 5
    "I apply a little more pressure, placing the tip of my cock at the entrance of her pussy."
    thinking "I can tell she's about to give in."
    shinn "Come on... Say the magic words."
    "Feeling the sensation of my cock against her pussy, her control is starting to give way."
    "The more I rub up against her, the more impossible it becomes for her to restrain herself."
    "Her desire for my cock is overriding everything else in her mind."
    thinking "Anytime now..."
    "Just as I predicted, she can't hold herself back any longer."
    rina "I WANT SHINN'S BIG FAT COCK IN MY SLUTTY PUSSY!"
    "Just what I was waiting for."
    shinn "That's what I wanted to hear."

    scene rina_rooftop_2 6
    "I push inside her without hesitation."
    rina "Ah! Shinn!"
    "The inside of her pussy is amazing. It's so tight, I can feel it squeezing down on me, even soaked from all her orgasms so far."
    "I start to pound her hard, her body reacting to every thrust."
    rina "Yes! More! More!"
    thinking "Looks like I've really done a number on her. I bet she doesn't even know who she is right now."
    rina "Harder, Shinn! HARDER!"
    shinn "You've got it!"
    "I thrust even harder, causing her to tighten around me."
    "I can feel her squeezing down more and more as I pound her insides."
    shinn "Fuck, Rina! Your pussy feels so good!"
    rina "Yes! Love it more, fuck me harder!"
    "It's getting hard to hold myself back now."
    shinn "It's too much, I'm going to cum!"
    rina "YES! SHINN, CUM INSIDE ME! FILL ME UP WITH YOUR THICK BABY MILK!"

    if persistent.cum == "inside":
        thinking "Ugh. Hearing her talk dirty like that, I can't take any more!"
        $ renpy.block_rollback()
        jump rina__cg_2_inside

    elif persistent.cum == "outside":
        thinking "Ugh. Hearing her talk dirty like that, I can't take any more!"
        $ renpy.block_rollback()
        jump rina__cg_2_outside

    else:
        menu:
            thinking "Ugh. Hearing her talk dirty like that, I can't take any more!"
            "Cum Inside":
                $ renpy.block_rollback()
                jump rina__cg_2_inside
            "Cum Outside":
                $ renpy.block_rollback()
                jump rina__cg_2_outside

label rina__cg_2_outside:
    scene rina_rooftop_2 9 with cum_flash
    play sound cum2
    "I ignore her plea and pull out quickly. The cum sprays out across her butt covering her entire back."
    rina "Ah! Shinn's cum is everywhere!"
    jump rina__cg_2_end

label rina__cg_2_inside:
    scene rina_rooftop_2 7 with cum_flash
    play sound cum2
    "I fulfill her wish and let out everything I've got into her womb."
    "It's so much that it fills all the way to the brim, trickles of cum leaking out from around my dick."
    rina "Ah! Shinn's baby seeds are inside me!"
    thinking "Eh. Pretty likely she'll get pregnant from this after all."

    scene rina_rooftop_2 8 with cum_flash
    play sound cum1
    "As soon as I'm done, I pull my dick out, sending the cum gushing out from her like a waterfall."

    scene rina_rooftop_2 9
    jump rina__cg_2_end

label rina__cg_2_end:
    "She can no longer hold herself in position, and collapses to the ground, a shaking mess."
    "I take a look over her, completely broken, paralyzed with pleasure. Seems to me like this lesson was a success."
    rina "Ughh~ Se... Sex..."
    "She's mumbling something incoherent. Maybe she wants more. I stand up and plant my foot on her ass."
    shinn "You are mine now, Rina. Understand? I want you to call me Master from now on."
    rina "Ah~ Yes Master!"
    $ renpy.end_replay()
    $ persistent.rina__cg_2 = True
    jump map__school

label rina__cg_3:
    scene rina_dog_1 1 with map_fade
    $ rina_next_step = "intermission"
    "A day has passed since our training session on the rooftop."
    "I thought I could parade her around to show all the students here how much she loves cock now."
    "And what better time than in the morning when everyone is coming in to school?"
    "She's excited, to say the least. After all, she's completely turned into a sex-crazed bitch by now."
    "I pull the dog leash as I hurry her along beside me."
    "She crawls along like an obedient dog."
    "It doesn't take long for the other students to notice it..."
    female_1 "Wait, what the hell!"
    female_2 "Is that Ms. Rina?"
    male_1 "What the hell is going on?"
    male_2 "Is this for real?"
    "The students in the hallway instantly freeze when they see Rina in such a state."
    "They can't believe their eyes."
    "I can hear whispers spreading through the crowd as they watch her."
    "I can even make out some of their conversations..."
    male_1 "Wow. To think we'd see a disciplinary teacher do something like this..."
    male_2 "I know right? This looks like something straight out of a porn scene."
    "That's right. Well, it's possible I got the idea from something like that to begin with."
    "Some of them are openly commenting on her figure."
    male_3 "I knew she was hot and had big tits, but I didn't expect her to have a figure like that."
    male_4 "Yeah, her boobs are amazing. Makes me want to suck on ‘em."
    shinn "Look around you, Ms Rina. Everyone is looking at you."
    shinn "They love your body and how slutty you've become. Everyone is lusting after you now."
    rina "Ah, everyone is looking at me!"

    scene rina_dog_1 2
    "Rina lets out a whine as the whole crowd's attention is focused on her."
    shinn "How does it feel, letting your students see what a slutty bitch you are?"
    rina "Ahhh..."
    rina "Ah! I'm too excited, I can't take it! I'm gonna cum!"
    "While Rina is working herself up to the point of orgasm, I take a moment to take in the crowd watching us."

    scene rina_dog_1 3
    "It seems a group of boys has started to gather around us."
    "Just from the excitement of being watched, Rina cums in front of everyone, her pussy juices dripping onto the floor of the school hallway."
    shinn "Wow. You came just like that?"
    rina "Ah, my pussy is so wet right now. I want cocks inside me!"
    shinn "You are really a dirty whore, aren't you?"
    rina "Yes. Rina is a whore who loves cock!"
    shinn "Heheh..."
    shinn "Is there anything you want to say to your beloved students?"
    rina "Y.. Yes..."
    rina "Everyone! Ms. Rina here! I love big cocks!"
    rina "I love the taste and smell of men's cum. If you have any, please give it to me!"
    "I burst into laughter."
    shinn "Hahahaha... Alright guys. You heard her. She wants your cum."
    male_1_2 "..."
    male_3 "Oi, is this for real?"
    shinn "What do you think?"
    male_4 "She looks so sexy..."
    shinn "Then what are you waiting for?"
    male_4 "Will we get in trouble?"
    shinn "Don't worry. Nothing is going to happen to anyone."
    shinn "She's a willing participant after all."
    shinn "Besides, it's a once in a lifetime opportunity to do it with a woman with a figure like that, don't you think?"
    "While the guys are busy lusting after Rina, a group of female students butts in."
    female_2 "This is disgusting."
    female_1 "You know that I looked up to you Ms. Rina?"
    male_4 "Oi, get lost, girls. This has nothing to do with you."
    male_3 "Yeah! Go away before this happens to you!"
    female_1 "..."
    shinn "You heard them. Get lost!"
    "As the girls in the hallway slowly walk away in horror, the male students move in closer towards to Rina."
    "Rina takes a look at the boys who're now surrounding her."
    rina "Ah, boys! Give me cum!"
    shinn "You heard her. Do it guys!"

    scene rina_dog_1 4
    "The boys start to unzip their pants and flash their hardened dicks in front of Rina."
    rina "Ah, cocks!"

    scene rina_dog_1 5
    rina "I can smell it! It smells so good!"
    rina "Please! I want more. I want your cum!"
    male_1 "Wow. You are really a slut."
    male_2 "You asked for it!"

    scene rina_dog_1 6
    "The boys start to jerk off in front her."
    "Staring at Rina's luscious body, the virgin boys are unable to hold out for long."
    "After all, they've probably never seen a naked woman in real life before."
    male_2 "Ms Rina, your body is so hot!"
    male_3 "Yeah, I can't hold out much longer!"
    rina "Its okay. Just let it all out on me. I'll savor it all."
    "The boys are at their limit now."
    male_2 "Agh! She's just too much! I'm cumming!"
    male_1 "Argh! I'm cumming!"
    male_3 "Me too!"
    male_4 "Take it all, Ms Rina!"
    rina "Yes! Give it to me! Give it all to me!"

    scene rina_dog_1 7 with cum_flash
    play sound cum2
    "Almost at once, the boys ejaculate, shooting their cum out onto Rina."
    "Her entire body is covered with their semen."
    rina "Ah! Cum! It feels so good!"
    shinn "Look at you, Rina. Aren't you happy getting showered with these boys' cum?"
    rina "Yes! I'm happy!"

    scene rina_dog_1 8
    "I take a quick look at the boys. Clearly, they're not done yet."
    "Even after ejaculating, their dicks are still rock hard."
    "They're staring at Rina, giving off a predatory vibe."
    "Meanwhile, Rina is still far from sated."

    scene rina_dog_1 9
    rina "I want more~"
    shinn "Heh. Alright."
    shinn "Hey guys, do you want have sex with Rina?"
    male_1 "We can?"
    male_2 "Seriously?"
    shinn "Of course."
    male_4 "Hell yeah! This is a dream come true!"
    shinn "Alright. Let's bring this slut to an empty classroom to get started."
    shinn "Also, I take it this is you guys first time, right?"
    male_students "..."
    thinking "Not a single reply. It has to be, poor guys."
    shinn "It's alright. I'm gonna teach you how to pleasure her."
    shinn "You guys can all enjoy popping your cherries on this slut."
    shinn "Follow me."

    scene bg classroom with fade
    show rina naked
    "I gathered all the boys hanging around in the hallway, and brought them here."
    "It's an unused classroom with tables and chairs lying around."
    "I brought Rina to the front of the class so that everyone could see her clearly."
    shinn "Alright boys. I know you can't wait to get a real piece of the action."
    shinn "But first, I'd like to show you how to tame a bitch like her."
    "I take off my pants and lie down on the floor."
    shinn "Rina. Come here."
    rina "Yes Master."
    shinn "Use my cock, Rina."
    rina "Yes, Master."

    scene rina__cg_3_gangbang 1 with dissolve
    "Rina crawls over and wastes no time in lowering herself onto my dick in cowgirl position."
    "Rina faces the whole room full of boys head on."

    scene rina__cg_3_gangbang 2
    "As she looks on, she can see the bulges straining at all of their pants."
    rina "Don't be shy, boys. Let me see your huge throbbing cocks."
    shinn "Heh. You heard her. Let her see ‘em."
    male_3 "O— Okay..."

    scene rina__cg_3_gangbang 3
    "The boys slowly comply and unzip their pants."
    rina "Ah. There we go."

    scene rina__cg_3_gangbang 4
    "The view further excites Rina as she starts to bounce her hips up and down on her own."

    scene rina__cg_3_gangbang 5
    shinn "Yeah, that's the spirit."

    scene rina__cg_3_gangbang 6
    "Rina lifts up her shoulders to show off her beautiful armpits."
    "They're clean-shaven, according to my taste."
    male_2 "Wow, her armpits look amazing..."
    male_1 "Yeah..."

    scene rina__cg_3_gangbang 7
    "Eventually, some of the boys start to jerk off watching the scene I've provided for them."

    scene rina__cg_3_gangbang 8
    "As for me, I lie here and let Rina slam her hips against me, letting off a slapping sound throughout the room."
    rina "Ah! Dick! Dick! It feels so good inside me!"
    "She's obviously enjoying this."
    "I let her plunge down to penetrate herself on me all the way to her womb, her pussy juice dripping out over me."
    "The wet and slippery sound as she brings herself down on me over and over again is incredibly erotic. So much so that I can't hold on for much longer."
    "I'm gonna cum, Rina!"
    rina "Yes, cum! Give it to me! Give me all of your cum!"
    "The boys are reaching their limits too."
    male_1 "Me too. This... this is too good!"
    shinn "Let's all cum together and give Rina a wonderful experience, shall we?"
    male_2 "Hell yeah!"
    rina "Ah~"
    "Her pussy clamps down on me, like she's trying to squeeze the cum from me."
    shinn "Here it comes!"
    rina "Ahh~"

    scene rina__cg_3_gangbang 9 with cum_flash
    play sound cum2
    "In an instant, I shoot right into her womb."

    scene rina__cg_3_gangbang 10 with cum_flash
    play sound cum1
    "There's so much, it's impossible for her to contain it all, leaving my creampie spilling from her pussy."

    scene rina__cg_3_gangbang 11 with cum_flash
    play sound cum3
    "At the same time, all the boys come together, shooting out over her body."
    "They cover her hair, her armpits, her belly and her hips."

    scene rina__cg_3_gangbang 12 with cum_flash
    play sound cum2
    "Everywhere I can see, her body is covered in cum."
    "It was enough for the smell of it to fill the whole room."

    scene rina__cg_3_gangbang 13
    rina "Ah! Cum! There's so much! I love it!"
    "Rina's mind is addled all over again. And it seems she isn't ready to stop here."
    rina "More~ I want more!"
    "With just a glance around the room, I can see that all the boys are staring straight at her creampied pussy."
    "Clearly, the boys aren't about to stop here either."
    shinn "Heheh..."
    shinn "I see you boys still want more."
    rina "But Master, I want more too~"
    shinn "Of course you do. But let me think how the boys should give it to you."
    "It takes just a moment to come up with an idea I'm sure Rina will love."
    shinn "Alright guys."
    shinn "Why don't you each take turns cumming in her mouth?"
    shinn "She'll drink it all down."
    rina "Ah! Master! I get to drink all the boys' cum?"
    shinn "Yeah, they'll be your own personal cum buffet. You like that idea, don't you?"
    rina "Yes Master! I love it!"
    "Rina widens her mouth, licking her lips in anticipation."
    rina "Come on, boys, what are you waiting for? Who's first?"
    male_1 "Me! I'll go first!"
    male_2 "Me next!"
    "With Rina's erotic face spurring them on, the boys quickly line themselves up."

    scene rina__cg_3_gangbang 14
    "The first boy wastes no time inserting himself into her mouth."
    male_1 "Oh my god, her mouth is heaven!"
    rina "Mmm~ Tastes so good!"
    "The boys in line stand transfixed, watching what's unfolding in front of them."
    "They watch the boy in front with envy and anticipation, jerking themselves off while waiting their turns."
    "Meanwhile, Rina deepthroats the boy hard, doing her best to suck out the contents of his balls."
    "She wraps her tongue around his dick, giving off a slurping sound that's audible throughout the room."
    "Though I can't see it from my place on the floor, her face must be  quite a sight to see."
    "As the sucking becomes more and more intense, the boy starts to reach his limit."
    male_1 "Agh, I can't take any more. I'm gonna cum!"
    "The realization that the boy is about to cum in her mouth gets Rina even more excited."
    "And that excitement makes her go even faster."
    "With the boy at the very edge, she pulls away for just a moment to speak."
    rina "It's okay. You can cum inside me. I'll drink it all!"
    male_1 "Argh! Here it comes!"

    scene rina__cg_3_gangbang 15 with cum_flash
    play sound cum2
    "The cum shoots out of his dick directly into Rina's throat as she takes it all down."

    scene rina__cg_3_gangbang 16 with cum_flash
    play sound cum1
    rina "Hmm~ Cum!"
    "The mere taste of cum gets her so excited that she can't think about anything else."
    "The boy pulls back as soon as she's taken everything he had."
    "Her eyes have rolled back and her tongue lolls out of her mouth while she pants like a dog."
    rina "Ah~ cum! More! More!"
    shinn "Alright, who's next?"
    male_2 "Me!"
    shinn "Alright. Go on then!"

    scene rina__cg_3_gangbang 17
    "The cycle repeats again and again. As time goes by, I lose count of the number of boys who've used her mouth."

    scene rina__cg_3_gangbang 26
    "She's taken in so much cum that it's left her stomach swollen."
    rina "Ah... So much..."
    shinn "Look at you, you look like you're pregnant."
    rina "..."

    scene rina__cg_3_gangbang 32
    "She's unable to respond, so full she can barely make herself speak."
    shinn "I think could go without any more food for a few days now."
    shinn "Hahaha..."
    male_1 "We want to taste the real stuff, Shinn!"
    male_2 "Yeah! Give us the real stuff!"
    "The boys are staring at Rina. Even after several ejaculations, they still haven't calmed down."
    "It seems the bunch of them won't be satisfied without a taste of Rina's pussy."
    "The pussy that's still clamped down on my dick as she sits on top of me."
    shinn "Alright, relax, guys."
    shinn "Go ahead and use her however you want. You can use her pussy, her ass, however you like it."
    male_3 "R— Really?"
    shinn "Yeah? Isn't this what you guys wanted?"
    male_1 "Fuck yeah!"
    male_2 "Let's do it!"
    "As the boys get themselves ready, Rina looks thrilled."
    rina "Yes~ More~"

    scene rina__cg_3_gangbang 33
    shinn "It's going to be a long day for you, Rina."
    $ renpy.end_replay()
    $ persistent.rina__cg_3 = True
    jump map__school

label rina__intermission:
    scene black with map_fade
    "???"
    "Since I first started letting other students fuck Rina..."
    "It's been months, I guess. I'm not sure quite how long."
    "Rina herself has certainly lost all track of time."
    "After all, what does time matter to a meat toilet?"
    "But even if I've lost track of the days, that doesn't mean things have gotten dull."
    jump rina__cg_4

label rina__cg_4:
    "The room is filled with naked and hungry schoolboys."

    scene rina__cg_4_gangbang 2 with fade
    "In the middle of the class, strung up and suspended with ropes, is Rina."
    "I tied her up there myself, in this pose which shows off free and easy access to her pussy."
    "I've spent quite a while getting her ready for this sort of play."
    "The drugs I've been giving her should increase her libido even compared to before. And maybe also make her lactate as a side effect..."
    "This whole setup looks the scene of a BDSM porno."
    "The students here aren't just any boys. They're all thugs from the school who had serious beef with Rina from before. As a disciplinary teacher, she'd picked up quite a few of them."
    "So, I thought I'd make a pastime of inviting them to use her. These events have just gotten bigger over time as more and more of them have gotten involved."
    "Rina has completely accepted her fate. You can't even call her resigned to it. Since the very start, she's been living like she was born for this."
    "Once a strong-minded person and a respected authority figure, she's come to embrace being a public meat toilet."
    "It's quite a thing to see how just one chance encounter can turn someone's whole life around."
    "I sit at the front of the class, watching Rina while she stares back at all the boys surrounding her."

    scene rina__cg_4_gangbang 3
    rina "Ah... So many... I... want them all..."
    "Her eyes are hazy. Surrounded by cock, she can no longer think about anything else."

    scene rina__cg_4_gangbang 4
    "Overcome with anticipation, her pussy is leaking while her body quivers against ropes."
    "Some of the guys are getting impatient..."
    thug_1 "Oi, Shinn! When can we start!?"
    shinn "Go ahead. Fuck her till you're all dry."
    thug_1 "All right!"
    thug_2 "Let's do it."
    "Everyone clusters in around Rina, fanning her lust even more."
    rina "Ah~ it's starting!"
    "Before we start the feast, I thought I'd give Rina a little surprise."
    shinn "Hang on guys. Let's loosen her up a little first."
    "One of the boys has a lit candle ready, and approaches Rina from the back."
    rina "Ah~ What's this?"
    "Rina has never experienced this type of foreplay before, but she can't help but anticipate pleasure."
    thug_3 "Take this!"

    scene rina__cg_4_gangbang 5
    "The student drips the hot melted wax onto Rina's sensitive breasts."
    "The wax is hot enough to inflict pain, but in her current state, Rina immediately embraces it as pleasure."
    rina "Ah!~ It hurts~"
    "The sensation causes her pussy to twitch a little, with more of her juices trickling out."
    thug_4 "It's not over yet!"

    scene rina__cg_4_gangbang 6
    "Another student uses a whip to lash at Rina's thighs. Again, Rina takes the pain as pleasure."
    rina "Ah! MORE! MORE!"
    "At this point, driven by her pleasure, a spring of milk starts to flow from her breasts."

    scene rina__cg_4_gangbang 7
    "The student with the whip picks up the pace, leaving marks on her legs with each lash."
    rina "GIVE IT TO ME! GIVE IT TO ME!"
    "The combined pleasure of the whip and the hot wax is enough to drive her over the edge."
    rina "Yes! I'M CUMMING! I'M CUMMING! AHHHH~~!"

    scene rina__cg_4_gangbang 8 with cum_flash
    play sound cum2
    "The pleasure causes a gush of juice from her twitching pussy, and a sudden spurt of milk from her breasts."
    rina "Ah~"

    scene rina__cg_4_gangbang 10
    thug_1 "Woah! Check it out, she's squirting milk!"

    scene rina__cg_4_gangbang 11
    "Seems like that side effect is for real after all."

    scene rina__cg_4_gangbang 12
    "As the milk continues to drip from her breasts, one student decides to have a taste."
    thug_2 "Let me try it~"

    scene rina__cg_4_gangbang 13
    "The student bites down on Rina's nipple as he begins to suck."
    rina "Ah~ Not my breast!"
    "He takes his time sucking at her lactating breast."

    scene rina__cg_4_gangbang 14
    "When he finally pulls away, he licks his lips."
    thug_2 "Mmm.... So Rina's breast milk is sweet."
    "It seems the school gang boss has gotten impatient sitting back and watching one of his underlings breastfeed."
    thug_boss "Move away guys! This is a waste of time!"
    "Seems he can't wait any longer to enjoy her pussy."

    scene rina__cg_4_gangbang 15
    "The gang boss pushes his way through the crowd and immediately thrusts his dick straight inside her, not giving her even a moment to prepare."
    "Rina immediately goes wild."
    rina "Ah!!! COCK!"

    scene rina__cg_4_gangbang 16
    "The boys at her side start jumping in, grabbing at her hands and urging her to jerk them off."
    thug_1 "Come on Rina! Use your hands too!"
    rina "Ah~ Okay~"

    scene rina__cg_4_gangbang 17
    "She eagerly goes along with it, vigorously stroking off the boys at her sides."
    "The rest of the boys stand around watching the action, jerking themselves off while waiting for their own turns with her pussy."

    scene rina__cg_4_gangbang 18
    thug_boss "Damn! Her pussy is still this tight even after she's been used this many times!"
    thug_1 "Eh? Are you kidding me? Her pussy is tight even after everything we've put into her!?"
    thug_2 "Hey, lemme check!"
    thug_boss "Heh, wait your turn. Everyone gets to use her eventually."
    thug_1 "Yeah. We can all use her to the fullest!"
    "Amid all this conversation, Rina's desire for cocks has reached its peak. She's panting with her tongue out like a dog, demanding more."
    thug_1 "Haha! Look at her! She's like a fucking dog!"
    thug_2 "What a slut!"
    "She rocks her hips up and down with as much force as she can while jerking the boys off even faster."
    rina "More! Give it to me! Shoot it all! I want it all!"
    thug_1 "Ahaha! She's gone mad!"
    "Her hips are moving unstoppably, like a machine. With such forceful movement and her tight pussy, the boss can't last long inside her."
    thug_boss "Alright, since you asked for it!"
    "The boss starts pounding her even harder, bouncing her up and down on top of him. Rina moans out load, urging him on."
    rina "I LOVE IT! GIVE IT TO ME! GIVE ME MORE!!"
    thug_boss "Here you go!"

    scene rina__cg_4_gangbang 19 with cum_flash
    play sound cum2
    "The boss cums inside her, the pleasure for both of them reaching a peak."

    scene rina__cg_4_gangbang 20 with cum_flash
    play sound cum1
    "Rina cums along with him, shuddering against him, another spurt of milk splashing from her breasts."

    scene rina__cg_4_gangbang 21
    rina "MORE! I WANT MORE!"

    scene rina__cg_4_gangbang 27 with cum_flash
    play sound cum3
    "The boys jerking off around her quickly begin to empty their loads as well, splashing their cum across her body, leaving her covered."
    rina "Ugh~ So much cum! ~"
    "Her eyes have rolled back with satisfaction. But, it's clear she's still ready for more."
    "Her pussy is twitching as the boss's cum starts to leak out."
    shinn "Good job there."
    thug_boss "Eh, thanks. If it weren't for you, we'd never have had the chance to enjoy all this."
    shinn "No problem, man."
    "All the guys waiting around her are getting eager to jump in. Looks like they can't wait for their own turn at her pussy. Even after cumming once, all of them are still rock-hard."
    "Getting impatient, some of them start trying to force their way to the front."
    thug_4 "My turn!"
    thug_5 "Hey!"
    principal "Hang on."
    "A familiar voice emerges from the back."
    thinking "Wait a minute. That voice..."
    "Everyone is shocked as they realize who it is walking to the front of the classroom."
    thug_2 "No way..."
    thug_1 "It's the Principal!"
    thug_boss "Shit! Are we all screwed?"
    principal "No worries, guys. I'm just here to join in the fun."
    "Of course, this is no surprise to me. I invited the Principal along myself when I found out how eager he was to have a taste of Rina."
    principal "Sorry I'm late, Shinn."
    shinn "No problem."
    principal "Looks like you guys have already gotten her basted and ready."
    shinn "Well, not a bad time for you to jump in then, is it?"
    principal "Certainly."
    "Realizing what's going on, Rina perks up in excitement, recognizing her boss."
    rina "Ah~ The Principal is here! Are you here to have fun with me?!"
    principal "Yes, of course."
    rina "Ah~ I can't wait! I'm sorry for being such a slutty teacher inside your school."
    principal "Heh. Don't apologize. I'm here to reward you for your work."
    "The Principal unzips his pants and positions himself."
    principal "Time to taste this slutty bitch's pussy!"

    scene rina__cg_4_gangbang 22
    "The Principal violently thrusts in and begins pounding away at her."
    rina "Ah! Principal! Your dick is amazing! I love it!!"

    scene rina__cg_4_gangbang 23
    principal "Ooh! Looks like her pussy is still tight after all this!"
    rina "Give it to me, Principal! Shoot everything inside me! I want the taste of your cum so badly! Please!"
    principal "Not yet. I want to savor this pussy for a while."
    "The Principal starts moving even faster, sending Rina into a frenzy."
    rina "Yes! More! More!"
    "He keeps hammering away at her until he's finally ready to unload."
    principal "Alright, get ready. Make sure you enjoy every single drop of my cum!"
    rina "Yes! The Principal is cumming inside me! I love it! Do it!"

    scene rina__cg_4_gangbang 24 with cum_flash
    play sound cum2
    "With a sudden gush, the Principal cums inside her. Rina shudders, dazed with pleasure."

    scene rina__cg_4_gangbang 25 with cum_flash
    play sound cum1
    "The Principal pulls out, letting the flood of cum drip fom her pussy."
    principal "There. All done."

    scene rina__cg_4_gangbang 26
    "The schoolboys look on in awe at how much he came inside her. And incredible display for a man of his age."
    "Satisfied, the Principal zips up his pants."
    shinn "That's all?"
    principal "I'll be back for more later."
    shinn "Alright then. Come back whenever you feel like it, she'll be here all day."
    "As the Principal leaves, the clamor starts up again as the boys fight for a place at the front of the line."
    "I offer some reassurance to calm them down."
    shinn "Don't worry guys, there's plenty of time today for everyone to fuck her!"

    scene rina__cg_4_gangbang 29
    "After a few hours, Rina is thoroughly fucked, but still far from finshed."
    "The marks left on her tights counting the rounds are been through today are now too numerous to track."
    "She's exhausted, but still eager, happy to be able to fuck her fill. Seems like she's been enjoying it more than the boys."
    rina "Yes... More... Give me more!"
    shinn "Heh. Good girl."
    "As the others start to filter out of the classroom, thoroughly spent, I walk up to her to look her over in her current state."
    rina "Ah~ Shinn~"
    shinn "Heh..."
    shinn "Did you enjoy yourself today?"
    rina "Yes! I love it!"
    shinn "Then let's end the day with my cock, shall we?"
    "Rina's sudden rush of enthusiasm wipes away all the signs of her exhaustion."
    rina "Yes! Nothing beats Shinn's big fat cock!"
    shinn "Good girl. Looks like you're still loyal to me after everything."

    scene rina__cg_4_gangbang 30
    "I strip off my pants and expose my cock in front of her. The sight of it makes Rina tremble."
    rina "Ah! Shinn!~"
    shinn "As a reward for your loyalty, I'm going to let you taste it."
    rina "Yes!"

    scene rina__cg_4_gangbang 31
    "Lubed up with all the cum that's been spilled inside her, I slide it in easily."
    rina "Ah! Shinn's cock! It's in!"
    "She squeezes down tight around me in her excitement. Even after all the boys who've used her, her body is still eager."
    shinn "Ugh. It really is tight. You're a one-of-a-kind slut, aren't you?"
    "As my hips pound against her ass, I can feel my balls getting ready to release my load."
    rina "Ah! Shinn! HARDER! HARDER!"
    "I speed up, pounding even harder against her womb."

    if persistent.cum == "inside":
        rina "YES! MORE!"
        $ renpy.block_rollback()
        jump rina__cg_4_inside

    elif persistent.cum == "outside":
        rina "YES! MORE!"
        $ renpy.block_rollback()
        jump rina__cg_4_outside

    else:
        menu:
            rina "YES! MORE!"
            "Cum Inside":
                jump rina__cg_4_inside
            "Cum Outside":
                jump rina__cg_4_outside

label rina__cg_4_inside:
    scene rina__cg_4_gangbang_inside 1 with cum_flash
    play sound cum2
    "Going all out at the end, I finally reach my limit. In an instant, I let everything out!"
    shinn "Ahh!"

    scene rina__cg_4_gangbang_inside 2 with cum_flash
    play sound cum1
    "My cum pours out inside her pussy, enough that some of it splashes to the floor beneath her."
    rina "AH! SHINN! I'M SO HAPPY!"
    jump rina__cg_4_end

label rina__cg_4_outside:
    scene rina__cg_4_gangbang_outside 1 with cum_flash
    play sound cum2
    "Going all out at the end, I finally reach my limit. In an instant, I pull out, spraying my cum across her body like a fountain."

    scene rina__cg_4_gangbang_outside 2 with cum_flash
    play sound cum1
    rina "Ah!! Shinn's cum! It's everywhere!"
    jump rina__cg_4_end

label rina__cg_4_end:
    "My balls are empty. She's sucked me dry of cum, like some kind of vampire."
    rina "Ah~ Shinn's cock is still the best!"
    "She seems broken again, completely unaware of what's going on around her."
    "Looking at her right now, I think I can say I'm properly satisfied with my job training her."
    "Looks like my job is done here. As far as what'll happen to her from now on, I can't be bothered."
    "It's not like I have any plans to take responsibility. Hell, I don't think anyone would want to take responsibility for her now."
    shinn "Good luck, Rina. Have fun with all the boys' cocks in school."
    rina "Yes~ I will!"
    $ renpy.end_replay()
    $ persistent.rina__cg_4 = True
    $ staffroom_available = False
    "END OF RINA ARC"
    jump map__school
    # -RINA ARC ENDED-
