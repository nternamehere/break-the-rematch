label pursue_rina:
    $ rina__probe = True
    scene bg rooftop with dissolve
    "Using my ninja skills, I manage to chase her all the way to the rooftop without catching her attention."
    show rina pissed 2 with moveinleft
    "I hide behind the rooftop door and keep a close watch on her. She looks agitated as she takes out her phone and calls someone."
    rina "Would you stop trying to call me while I’m at work?!"
    thinking "Woah. That was pretty fierce."
    rina "I already said I wasn’t going to have sex with you again! That was a one time thing, and I’m already regretting it!"
    thinking "Wait. What?"
    "I’m shocked to hear something like that out of Rina’s mouth. She always puts up a front of being so straight-laced."
    show rina annoyed 2
    rina "Look, that only happened in the first place because I was drunk. Frankly, at this point, I have no interest in you at all. So, you can feel free to fuck off." 
    thinking "Heh, looks like I’ve actually got some real dirt on her. And here I thought she was going to be a hard one to deal with."
    "This isn’t going to be enough all by itself though. I need to do some more digging so I can properly play this to my advantage."
    rina "You know what? I’m done taking to you. I’m hanging up."
    hide rina with moveoutleft
    "As soon as she ends the call, she turns around and heads back towards the door."
    thinking "Oh shit, she’s coming."
    "I move as quickly as I can and try to conceal myself in the corner."
    "She approaches the door and swings it open hard. She’s clearly still venting her anger from the phone call as she heads back towards the staff room."
    shinn "Phew. That was a close call."
    thinking "Guess I’ll head back along another route to meet up with her."

    scene bg staffroom with pixellate
    "I return to the staff room, but it seems like Rina still isn’t back yet."
    thinking "She sure takes her time when she’s angry."
    show rina confident with moveinright
    "Soon, Rina arrives in the staff room as well, looking composed once again."
    thinking "Wasn’t she pretty wound up before? Maybe she’s just putting up a front now to try and keep things under wraps."
    "I head over to her desk to let her know that the paperwork is done. As I approach, I notice that she’s glued to her phone. She seems completely unaware of my presence just behind her."
    shinn "Ah... Ms. Rina. The paperwork you asked me to take care of is all finished."
    show rina annoyed
    "Rina turns around with a jolt, looking startled."
    rina "Oh, Shinn. So you’re done."
    shinn "Er... Are you alright Ms. Rina?"
    "She immediately snaps back to her normal self."
    show rina vicious smile
    rina "What do you mean? I’m completely fine."
    rina "Since you’ve finished, I guess you can go now. Classes should have ended already. I’ll pick up the paperwork from your workplace later on."
    shinn "Alright."
    if saw_touko_aina_utility and ritsuko_met_principal:
        jump rina__probe_1
    else:
        menu:
            thinking "Hmm... I wonder what I should do now?"
            "Now’s my chance to check on the other girls!":
                $ renpy.block_rollback()
                hide rina vicious smile
                jump map__school
            "Try to probe her and find out more.":
                $ renpy.block_rollback()
                jump rina__probe_1

label rina__probe_1:
    shinn "Ms. Rina. Is there anything else that I can do for you?"
    show rina annoyed 2
    rina "Huh? Weren’t you supposed to get started on tutoring our students?"
    shinn "Well, I thought maybe just for now, I might be able to do something to help you."
    "Rina was clearly put out by my suggestion."
    rina "No. Your job here is to tutor our students who are in need. The most helpful thing you can do is to do your job properly."
    shinn "Sheesh... Relax. I just wanted to help."
    show rina pissed 2
    rina "More like you’re trying to butter me up. You’d better not try anything funny. I have my eye on you."
    thinking "Heh. I wonder who is watching who, Ms. Rina."
    rina "I don’t have the time to talk to you right now. I have a meeting coming up, so I’ll be heading out now."
    hide rina pissed 2 with moveoutright
    "Rina leaves the staff room in a hurry. She doesn’t seem to give a second thought to leaving me behind in her workplace."
    "She probably never stopped to think that I might search through her things. Much too naïve, Rina."
    shinn "Hmm... Let’s take a look."
    "As I scan her desk, I realize that she’s left her phone behind on the table. A fatal mistake for her."
    shinn "Well well well... What do we have here? Looks like something pretty handy."
    shinn "Time to see what’s inside."
    "To start with, I take a look through her messages and call history. I know she called someone just now, and want to get the number behind that."
    "Once I have that, I can dig up all her other calls and messages with the same guy."
    "There, that was easy enough to find."
    shinn "She’s got several recent messages from the same number."
    "I open up one of the messages and take a look. To my surprise, there’s a picture attached of her lying naked in bed, cum leaking from her pussy. A guy sits beside her, posing with a peace sign."
    shinn "Checkmate."
    "I hide the phone away carefully. After all, there’s no question she’ll come running back for this soon."
    shinn "Let’s wait and see what happens when she realizes she’s missing this."

    scene bg hallway 1 with irisin
    "I loiter around the hallway to see if Rina’s heading back to retrieve her phone."
    "However..."
    if ritsuko_met_principal:
        show ritsuko sad school with moveinright
        "From a distance, I can see Ritsuko approaching, looking distressed and defeated. "
        thinking "Uh-oh"
        ritsuko "..."
        "She obviously notices me, but after giving me a glance, she turns and walks on without saying a word."
        hide ritsuko sad school with moveoutleft
        thinking "Well, no big wonder there. "
        thinking "After all, she was just raped by the guy she was expecting to enforce the rules in this school"
        thinking "Just wait till I get to her..."
    else:
        show ritsuko basic school with moveinright
        ritsuko "Hohoho..."
        thinking "Un-oh."
        ritsuko "What do we have here?"
        thinking "Not the person I was hoping to hear from right now."
        ritsuko "What are you doing sneaking around the hallway?"
        shinn "I’m not sneaking around."
        ritsuko "Oh? I bet you’re looking around scoping this place out for girls."
        thinking "This bitch..."
        shinn "Look. What do you want?"
        ritsuko "Oh hohoho~"
        ritsuko "Just making sure you don’t try anything stupid while you’re here."
        ritsuko "I’m watching you Shinn..."
        hide ritsuko basic school with moveoutright
        "Ritsuko leaves looking proud, like she’s caught me out and gotten the upper hand on me."
        thinking "What a pain in the ass she is..."
    thinking "Now, where was I?"
    thinking "Oh, right. Rina still isn’t back yet."
    thinking "Damn it!"
    play sound heels
    "However, after waiting a little longer, I can hear the loud, quick-paced clicking of footsteps approaching."
    "It sounds as if someone is nearly running while wearing high heels."
    thinking "That has to be her."
    "When she came around in sight of me, she didn’t even register my presence and headed straight into the staff room."
    "From out in the hallway, I can hear the sound of her rummaging around and banging things down as she searches her desk. Unable to find it, she steps out of the staff room, her anxiety painted all over her face."
    "Scanning the hallway, she finally notices me and hurries up to speak to me."
    show rina pout with moveinleft
    rina "Shinn! Have you seen my phone? You were near my workplace even when I left, right?"
    shinn "Your phone?"
    show rina angry
    menu:
        rina "Damn it, Shinn. Don’t play dumb with me. Have you seen it or not?"
        "Lie to her.":
            $ renpy.block_rollback()
            jump rina__lie_1
        "Tell her the truth.":
            $ renpy.block_rollback()
            jump rina__truth_1

label rina__lie_1:
    shinn "No, I don’t think I’ve seen it."
    rina "You sure? Don’t lie to me."
    shinn "I am sure. Why would I lie to you?"
    "With no reason to suspect me, she let it drop. But her desperation to find her phone is unabated."
    rina "In that case, could you help me find it? It’s very important to me."
    shinn "If it’s missing, couldn’t you just buy a new one?"
    rina "No, I’ve got some important stuff on that one."
    thinking "Heh. Some pretty important pictures."
    shinn "What kind of important stuff?"
    show rina pout
    "Rina gave a clear look of embarrassment as she thought about what she had on that phone."
    rina "Look, don’t pry so much. Will you help me out or not?"
    thinking "Even if I hadn’t already seen, she’s completely giving herself away. This should be fun."
    thinking "Let’s see how long it takes for her to catch on."
    shinn "Sure, I’ll help. Let’s go through the staff room together to start."

    scene bg staffroom with fade
    "By this time, the staff room is empty apart from us. All the teachers are either on break, or out at the meeting Rina was supposed to be attending."
    "Since it’s just two of us here, I relax as I pretend to look around the room, keeping my eye on Rina."
    "Rina, on the other hand, is working herself into a frenzy, sifting through boxes in the increasingly desperate hope of finding her phone."
    show rina angry
    rina "Damn it! Where could it be?"
    "Suddenly, Rina straightens up, an idea dawning on her."
    rina "Oh, I know. I can just use the school’s line to call my phone. I didn’t leave it on silent."
    "I nod at her suggestion, while I continue to pretend to search around for her phone."
    play sound phone_ringing
    thinking "Oh shit. I didn’t turn it off!"
    rina "Oh, I heard it."
    thinking "Fuck! Turn it off! Turn it off!"
    "Rina followed the sound of her ringtone. I tried to stop it, but I was already too late. She catches me clearly holding the phone in my hand."
    show rina pissed 2
    rina "Shinn... I think you have some explaining to do."
    "Well, the game is up now, there is no point in hiding anymore."
    shinn "Well. Ms. Rina. I think YOU have some explaining to do."
    rina "Stop kidding aroun—"
    "I cut her off before she can seize the initiative."
    shinn "Kidding? I don’t think those photos on your phone were any kind of a joke."
    rina "Photos?"
    shinn "You know exactly what I’m talking about."
    show rina annoyed 2
    rina "What photos?"
    "She’s still playing dumb, but the worry on her face is obvious."
    "I hold up the phone in front of her, and flip through the photos I discovered."
    "Her worried expression turns to shock, and then just as quickly, to rage."
    shinn "Well. Still wanna act dumb with me?"
    rina "Give me back my phone!"
    shinn "Not a chance, Rina."
    rina "You..."
    shinn "Heh. To think you’d actually turn out to be such a slut."
    show rina pissed 2
    rina "Give it back to me or else..."
    shinn "Or else what? What are you going to do to me?"
    "Rina was silenced."
    shinn "That’s right, you have nothing on me right now."
    shinn "However, ..."
    "I walk up close to her and lean in, whispering into her ear."
    shinn "It looks like I’ve got something you want, don’t I?"
    shinn "Let’s settle this matter somewhere appropriate, alright?"
    jump rina_blowjob_scene_1

label rina__truth_1:
    "I took out the phone from my pocket and flash it right in front of her face."
    shinn "What, is this the one you’re looking for?"
    show rina pissed 2
    rina "Yes, that’s my phone. What are you even doing with it? Give it back!"
    shinn "Give it back? Not so fast."
    rina "Stop kidding around and hand it over!"
    "Time to play my hand."
    shinn "Perhaps we should have a discussion about those photos on your phone first?"
    show rina annoyed 2
    rina "What? What photos?"
    thinking "Playing dumb, huh?"
    "Although she’s trying to feign ignorance, her face shows that she’s clearly worried."
    "I go ahead and show her the photos I found inside her phone. Well. You still wanna play dumb with me?"
    rina "Give me back my phone!"
    shinn "Not a chance, Rina."
    rina "You..."
    shinn "Heh. To think you’d actually turn out to be such a slut."
    rina "Give it back to me or else..."
    shinn "Or else what? What are you going to do to me?"
    shinn "Keep in mind there are still students around. You wouldn’t want them to find out about this, right?"
    rina "You asshole. I knew from the start that you were up to no good."
    thinking "Heh. I’ve got her properly cornered now."
    shinn "Good. Looks like you know where you stand here."
    "Rina was silenced."
    shinn "That’s right, you have nothing on me right now."
    shinn "However, ..."
    "I walk up close to her and lean in, whispering into her ear."
    shinn "It looks like I’ve got something you want, don’t I?"
    shinn "Let’s settle this matter somewhere appropriate, alright?"
    jump rina_blowjob_scene_1
