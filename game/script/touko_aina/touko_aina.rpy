label touko_aina__router:
    $ quick_menu = True
    if touko_aina_next_step == "continue_2":
        jump gym__day_3_continued_2
    elif touko_aina_next_step == "continue_1":
        jump gym__day_3_continued_1
    elif touko_aina_next_step == "day_3":
        jump gym__day_3
    else:
        jump gym__day_1

label gym__day_1:
    $ touko_aina_next_step = "day_3"
    $ gym_available = False
    scene bg gym balls with map_fade
    "Although it was still early in the morning, I heard from the principal that some members of the basketball team come in for practice before school starts."
    "Curious to check it out, I decided to visit the basketball court."
    "I take a quick look around the premises. Doesn't seem like anyone's around."
    play sound basketball_dribble
    "Or so I thought..."
    "In the distance, I spot a lone student practicing basketball."
    "As I approach the student, it becomes obvious who it is."
    
    show touko basketball shy with moveinleft
    "Seems like Touko's getting some morning training done by herself."
    "She notices my presence and turns around."
    touko "Oh, Shinn. Good morning. What brings you here?"
    "She seems surprised..."
    shinn "Good morning, Touko. I was just checking to see if you were in for morning practice."
    touko "Ah, yes. I usually only make it in now and then, but when nationals are coming up, I try to push myself to get extra training in every day."
    shinn "I see. That's some pretty impressive determination."
    touko "Thanks. I love basketball, so I figure it's worth putting in the effort for."
    shinn "It's good that you're doing what you love. But don't forget you have other priorities too."
    touko "Oh, right, I did almost forget, actually. I have a tutoring session with you this afternoon, right?"
    shinn "That's right. Please don't forget about it."
    touko "What's today topic going to be?"
    shinn "Since it's the first session, I'll start off with some testing to get a sense of where your academics are currently."
    touko "Oh, okay."

    menu:
        thinking "Hmm... Since it's just the two of us here, maybe I should ask her some questions."
        "Ask about her relationship with Aina.":
            $ renpy.block_rollback()
            jump gym__day_1_aina
        "Ask about her academic issues.":
            $ renpy.block_rollback()
            jump gym__day_1_academic

label gym__day_1_academic:
    shinn "Since it's just us here right now, there's something I'd like to ask you."
    touko "Hmm? What is it?"
    shinn "Is there some reason why you've been struggling so much in math class?"
    touko "Well, I guess I'm mainly just doing bad because I kind of hate math."
    touko "But since I'm spending so much of my time focusing on other stuff I actually enjoy, I don't have a lot of attention left over for it."
    shinn "Ah. I see. Well, that's a pretty common problem."
    touko "Right. So, I was hoping you could help me out with that."
    thinking "Heh. Of course I'm going to \"help.\" "
    shinn "I see..."
    shinn "So, how do you usually study on your own when you're trying to catch up in math?"
    touko "Usually, I spend time together with Aina, and we do some studying together and try to help each other out."
    shinn "Spend time together?"
    touko "Yeah. Like, every weekend, we'll spend time at her house or mine to study math."
    shinn "I see..."
    touko "Usually, when exams are coming up, one of us will stay over at the other's house and we'll stay up studying."
    touko "Oh, I guess I didn't tell you this before, but me and Aina are really close friends."
    shinn "Hmm..."
    jump gym__day_1_continued_1

label gym__day_1_aina:
    "When I first met Touko, she was together with Aina. And from the way they talked, it seems like they're very close."
    "Maybe Touko has some useful information I could use against Aina? I should ask what she has to say about her."
    shinn "Since it's just us here right now, there's something I'd like to ask you."
    touko "Hm? What is it?"
    shinn "When I first met the two of you, it seemed like you and Aina were very close. What's your relationship with her?"
    touko "Hmm? Why're you asking?"
    shinn "Since I'm going to be tutoring her too, I thought'd be good to get your impression on what kind of person she is."
    shinn "I'm just trying to be better prepared."
    touko "Ah, I see. Aina, huh?"
    touko "She's a good friend of mine. We used to attend the same middle school together before we came here."
    shinn "The same school?"
    touko "Yeah. We've known each other since a while back."
    touko "Actually, she was the first friend I made back in middle school, and the two of us have been close ever since."
    shinn "I see. What do you think of Aina as a person?"
    "Touko paused for a moment, processing her thoughts."
    touko "Hmm... I guess she's a nice person. She's also always been really energetic."
    thinking "Heh. \"Energetic\"."
    touko "She's also really determined and competitive."
    shinn "I see."
    shinn "Is there a reason why she's also been struggling in math then?"
    touko "Hmm... I guess she's basically like me? We both focus on our sports a lot, so the other stuff gets sidelined."
    touko "Also, she doesn't like math either. So that too."
    shinn "I see."
    touko "Usually, I spend time together with her, and we do some studying together and try to help each other out."
    shinn "Spend time together?"
    touko "Yeah. Like, every weekend, we'll spend time at her house or mine to study math."
    shinn "I see..."
    touko "Usually, when exams are coming up, one of us will stay over at the other's house and we'll stay up studying."
    touko "Like I said before, we're pretty close."
    shinn "Hmm..."
    jump gym__day_1_continued_1

label gym__day_1_continued_1:
    thinking "Hmm... I think I see how it is."
    thinking "Since these two are such close friends, it should be easier to get the two of them together."
    touko "Erm... Shinn?"
    thinking "Maybe I could swing a threesome... Hehehe..."
    touko "Hello? Are you there?"
    "Realizing I've gotten lost daydreaming, I quickly pull myself back."
    shinn "Yeah. Sorry, I was thinking about something."
    "Touko looks at me with concern."
    touko "Are you okay?"
    shinn "Oh, I'm fine."
    shinn "I think that's it for now. Thanks for letting me know. I'll see you later."
    touko "Sure!"
    "I left her alone to her training. As I walked out of the court, my thoughts were focused on the two them."
    thinking "Hmm... this doesn't add up, does it?"
    thinking "The two of them don't seem so dumb that they'd be failing math if they get together every week to study."
    thinking "Especially if they go to the point of studying overnight together every time exams are coming up..."
    thinking "What are they really doing together?"
    thinking "Wait a minute..."
    "Some wild thoughts suddenly spring to mind"
    thinking "Could they be...?"
    "I can't help but give a sinister smile."
    thinking "Haha... If I'm right, this'll be pretty epic."
    thinking "But first, I'll need to investigate, see if I can dig up some proof."
    thinking "Hmm, how am I going to do this?"

    scene bg hallway 1 with irisin
    thinking "Shit!"
    thinking "Its 3.30 PM already. Today's lesson with Touko is supposed to be now. I wonder if she's already there."
    thinking "I should have kept better track of time and been there to wait for her."
    thinking "Let's hope she's not there yet."

    scene bg classroom with dissolve
    show touko school angry arms
    "I approach the classroom and slide open the door."
    "I was hoping to avoid this, but Touko was already there waiting for me."
    "She turns around and gives me an annoyed look."
    touko "You're late."
    shinn "Ah yes. My apologies. I wasn't looking at the time."
    touko "It's okay. Since you're here now, let's get this started so we can get it over with quickly."
    thinking "Heh. You sure seem to be in a hurry."
    shinn "Well, that'll depend on how well you understand the content we'll be covering today."
    "I take out my materials and jot down some notes on the blackboard."
    "The lesson was in session. As I walk her through the material, and explain the various methods to solve the problems in her assignments, Touko seems to be attentive."
    "Or at least, she's trying to be. Now and then, a bemused expression crosses her face."
    shinn "Err... Touko? Do you understand my explanation here?"
    touko "Y.. Yes."
    thinking "Obviously not."
    shinn "You sure?"
    touko "Yes."
    "At this point, the scheduled lesson time is over. So, I decide to give her a little test."
    shinn "Alright, Touko. Since you've gotten the explanation down, you should be able to handle this problem sheet, right?"
    touko "Er... Yes?"

    show touko school angry
    thinking "Not exactly making that sound convincing."
    "Regardless, I pass her the paper."
    shinn "Here you go then. If you don't understand any of the questions, let me know. I'll do my best to help you out with anything you're having trouble with."
    touko "Okay."
    "She sits down with the paper, and starts working her way through the questions."
    "While I watch, she seems to be pretty intently focused on her work."
    thinking "Maybe I should take the opportunity to ask her some more questions and get to know her better."
    shinn "So Touko..."
    touko "Huh?"
    "She replies, half giving me her attention while trying to focus on the sheet."
    shinn "Tell me more about yourself."
    "She pauses, trying to think of something to say."
    touko "Hmm... What do you want to know?"
    shinn "I don't know. Stuff about your life, I guess?"
    touko "My life, huh? Why do you want to know all this?"
    shinn "To get to know you better. I'm probably going to be having these sessions with you for quite a while, after all."
    touko "Hmm, let's see..."
    "She mulls it over for a bit."
    touko "Well, I come from a very strict family."
    shinn "Strict family? What do you mean?"
    touko "Well, my parents are very conservative, and they've always had a lot of rules for me to follow."
    shinn "What? Like how?"
    touko " All sorts of stuff. To begin with, they put up a lot of fuss about me joining the basketball team."
    touko "It took a whole lot of convincing to get them to let me stay on it. And if I break any of their rules, they'll want me off the team right away."
    shinn "What do they want from you then?"
    touko "Well, they want me to be more ladylike..."
    touko "They think that playing basketball will give me a bad attitude and make me too much of a tomboy."
    shinn "Hmm... Interesting..."
    touko "Eh? What's so interesting about that?"
    shinn "I mean, it's pretty uncommon these days for parents to be that restrictive with their kids."
    touko "Yeah, and it gets worse from there."
    shinn "Oh? How so?"
    touko "One of the rules they've set for me is, they don't want me getting into any kind of a relationship."
    shinn "Wow."
    touko "Yeah. If I did, they'd really crack down on me, way more than just making me quit the basketball team."
    touko "Like, they might seriously disown me."
    touko "So, I really can't afford to let anything like that happen."
    touko "They say I'll be ready for a relationship when I have their say-so, and it has to be with a partner who has their approval."
    shinn "Really? You mean like an arranged marriage or something?"
    touko "Yeah, I guess you could put it that way."
    shinn "Yikes. That's harsh."
    shinn "But hey, you're pretty popular with the girls, aren't you?"
    touko "Huh? What you mean?"
    shinn "I've heard that some of the star female athletes here get a lot of attention from other girls in this school, including yourself."
    touko "Yeah, I guess..."
    touko "Honestly, I've gotten a fair number of love letters from other girls before, definitely more than I have from boys. I guess maybe my parents had a point when they worried about me being tomboyish?"
    "Touko stares off into space, apparently lost in thought."
    shinn "Hello? Touko?"
    touko "Oh! Sorry, I guess I kind of went on for a while."
    touko "I'll keep going with the worksheet."
    shinn "Alright."
    thinking "Hmm... Let me think."
    thinking "She did say she's received more love letters from girls than boys, but that doesn't mean that she's into that herself."
    thinking "But from her reaction just now, I have a feeling I'm onto something."
    thinking "I still need more evidence to confirm though."
    thinking "But how?"
    thinking "Hmm..."
    "Time passes by while I'm thinking it over."
    touko "I'm done!"
    "Touko's sudden announcement interrupts my thoughts."
    shinn "Oh, alright, let me take a look."
    "I stand up and approach her desk."
    "I take her paper and scan through it, looking over all her answers. At a glance, I can tell hardly any of them are right."
    shinn "Well, this isn't good, Touko. It seems like you missed most of them."
    "Touko casts her eyes down in shame, unable to meet my gaze."
    shinn "This is a pretty rough start. It looks like you're going to have a whole lot of work to do to catch up in this class."
    touko "Well... I tried my best."
    shinn "But it's not getting you there. You're going to need to build more effective study habits. Didn't you say you and Aina study together?"
    touko "Erm... Yeah."
    shinn "Then how have you ended up this far behind?"
    touko "Hehe..."
    "Unable to give me a straight answer, Touko gives a nervous, self-deprecating laugh."
    shinn "It's getting late now. I'm going to give you some practice papers, try to get them done tonight and hand them back to me tomorrow, got it?"
    "Touko sulks. She clearly isn't happy with the idea of getting extra homework from me."
    shinn "..."
    shinn "Don't give me that face. I want it in by tomorrow."
    "Reluctantly, she takes the papers and packs her bags. Seems like she's pretty eager to get out of here."
    touko "Alright. Thank you for today. I'll be going then."
    shinn "Goodbye."
    "Touko slides the door open and leaves the classroom."
    shinn "..."
    thinking "I need to find out more about her. Starting tomorrow, I'll try tailing her to see what I can dig up."
    thinking "Considering the situation with her family, any kind of dirt I can get on her should make for good leverage."
    thinking "Tomorrow is going to be a long day..."

    scene bg main gate with fade
    "Classes started 30 minutes ago..."
    "But I decided to come in a bit later, since there's no work for me now anyway. Not until afternoon, at least."
    thinking "Heheh...  I'll put that time to good use tailing Touko."
    thinking "Can't wait to see what kind of dirt I'll be able to dig up on her."

    scene bg hallway 2 with dissolve
    "I enter the hallway and go up to the floor where all the 3rd year students are."
    "I know her classroom is 3-5, not far from the classroom that I use for tutoring."
    "As I approach the class, I can see Touko heading towards it from the other direction as she returns from the bathroom."
   
    show touko school happy with moveinleft
    "We spot each other at the same time."
    touko "Good morning, Shinn."
    shinn "Good morning to you too, Touko."
    "Touko seems rather surprised to run into me here."
    touko "Erm, so, what brings you here?"
    "Well, I came here to stalk her, but obviously I can't just tell her that to her face."
    "Well, better bullshit something."
    shinn "Ah... I wanted to talk to you about something."
    shinn "Do you think you can spare a bit of time now?"
    "Touko looks a bit reluctant as she thinks it over, but eventually she nods."
    touko "Err... I'm having a class right now, but a few minutes should be fine."
    
    menu:
        thinking "Okay, shit, what can I ask her to eat up time?"
        "Ask her what she thinks about Rina.":
            $ renpy.block_rollback()
            jump gym__day_1_rina
        "Ask her what she thinks about Ritsuko.":
            $ renpy.block_rollback()
            jump gym__day_1_ritsuko

label gym__day_1_rina:
    "Struggling to come up with something, I spit out the first thing that comes to mind."
    shinn "So, what do you think about Rina?"
    touko "Rina? You mean the disciplinary teacher?"
    shinn "Yes."
    touko "Hmm? Why are you asking me?"
    "An explanation suddenly comes to Touko."
    touko "Oh. Don't tell me she's your type?"
    shinn "What? Hell no!"
    touko "Then why are you asking?"
    shinn "I'm asking because I'm her colleague and it's hard to work with someone you don't understand."
    touko "Hmm... I guess that makes sense."
    shinn "So?"
    touko "Well, Rina is a very strict person. Actually, I guess she's the strictest person I know in this school."
    touko "I think she's kind of unpopular with the boys here, since she tends to go a bit easier on the girls."
    shinn "Is that so?"
    touko "Yeah. When I make a mistake, she tells me firmly, but she's still nice about it. When it's with the boys though, she can be kind of aggressive."
    shinn "Yikes."
    touko "Whatever it is, I think she might see you more like a student and not a staff member because of your age."
    shinn "Hmm... Alright."
    touko "Is there anything else you wanted to ask? Otherwise, I should get going."
    shinn "Ah, no, I think that's all."
    touko "Alright, I'll be going then. See you later for tutoring!"
    shinn "See you."

    hide touko school happy with moveoutright
    "As Touko leaves I feel a sense of relief."
    "The info on Rina is probably irrelevant anyway. I'm just glad to have that over with."
    "Now, back to stalking. I want to see what she does during lunch."
    jump gym__day_1_continued_2

label gym__day_1_ritsuko:
    "Struggling to come up with something, I spit out the first thing that comes to mind."
    shinn "So, what do you think about Ritsuko?"
    touko "Ritsuko? You mean the one who's a star tennis player?"
    shinn "Yeah, that one."
    touko "Hmm... She comes from a rich family, and she's kind of well known for her whole ladylike act."
    touko "When it comes down to it though, she seems kind of useless for anything she can't get done by throwing her family's money around."
    shinn "Wow."
    touko "Yeah, I really don't have a good impression of her, sorry."
    touko "Anyway, why are you asking about this?"
    thinking "Shit, gotta come up with something..."
    "I toss out the first thing that comes to mind."
    shinn "Well, it's because Ritsuko is one of the girls I've been hired to assist."
    touko "Heh. She needs help with math?"
    touko "I figured they'd probably just chuck private tutors at her for whatever she had trouble with."
    shinn "Err..."
    touko "Sorry, my bad, I guess I shouldn't be talking like this behind her back."
    shinn "It's alright. At least I've learned something in the process."
    thinking "Not that the info on Ritsuko really matters."
    touko "Is there anything else you wanted to ask? Otherwise, I should get going."
    shinn "Ah, no, I think that's all."
    touko "Alright, I'll be going then. See you later for tutoring!"
    shinn "See you."

    hide touko school happy with moveoutright
    "As Touko leaves, I feel a sense of relief."
    "The info on Ritsuko is probably irrelevant anyway. I'm just glad to have that over with."
    "Now, back to stalking. I want to see what she does during lunch."
    jump gym__day_1_continued_2

label gym__day_1_continued_2:
    scene bg hallway 1 with irisin
    "The bell for lunch rings."
    "I already ate lunch beforehand, so I decide to take the chance to follow Touko around and see what she gets up to."
    "While the other students are leaving class and heading for the cafeteria, I spot Touko heading in the other direction."
    thinking "Hmm? Where's she going?"
    "I slowly follow along behind her, keeping out of her sight and avoiding the attention of of any of the other students nearby."
    "Touko walks further and further. The crowds of students start to thin, until almost nobody is left."
    thinking "Where is she going? I know this area. There are no classes in this part of the school, and students hardly ever come here."
    "As she walks towards the end of a dead-end hallway, she turns towards a utility closet off to the side."
    "She looks anxious, but doesn't bother to check her surroundings as she opens the door."
    "Confident that nobody is watching her, she enters the room."
    thinking "Hmm? Something strange is going on..."
    "I cautiously approach the door."
    "The door is cheaply made, and there's a wide keyhole under the knob."
    "I peer through the keyhole, hoping to get a view of whatever Touko is up to inside."
    jump touko_aina__cg_1

label touko_aina__cg_1:
    play music happy fadeout 1.0 fadein 1.0
    scene bg utility room with dissolve
    show aina school happy at right
    show touko school angry at left
    with moveinleft
    touko "Aina! Why did you call me out here during lunch?"
    aina "I miss you! We haven't been spending time together for a while now."
    "Aina begins to cry."
    "Seeing Aina's distress, Touko steps closer and gives Aina a hug."
    touko "It's okay, Aina. Once our exams and the nationals are over, we'll be able to spend all the time together we want."
    "Aina lets out a sniff, trying to hold back her tears."
    aina "You... Promise?"
    touko "Yeah, I promise."
    "Feeling relieved at her reassurance, the tension starts to leave Aina's body, and she lets Touko draw her closer into her embrace."
    
    scene touko_aina_sex_scene_1 1 with quick_fade
    "She looks at Touko with hazy eyes as she wraps her own arms around her."
    aina "Touko..."
    "Rather than relaxing into the comfort of her friend though, Aina strengthens her grip."
    "She moves forward, pressing Touko back up against a wall."
    touko "A-Aina..."
    "Their faces are almost touching."
    aina "Touko, do you know how much I've been thinking about you?"
    aina "You've been in my head all day. From the morning when I got up, through all my classes."
    aina "I've spent the whole time wanting to see you."
    touko "The whole time?"
    aina "Yeah. I can't stop thinking about all the stuff I want to do with you."
    aina "I don't want to wait, Touko. We've gotten along behind everyone's backs so far, haven't we?"
    aina "Think of everything we've gotten away with at each other's houses."
    "Aina gives Touko a seductive look."
    aina "That's what I've been thinking about all day."
    touko "..."
    aina "I want you, Touko..."
    "Touko's face is flushed. It looks as if she saw this coming."

    scene touko_aina_sex_scene_1 2
    "Aina moves her face closer, locking her mouth over Touko's."
    touko "Mmm!"
    "Touko lets out a squeak as Aina kisses her forcefully."
    "She fidgets and clenches her fingers against Aina, as if she doesn't know how to react."
    "As Aina continues to draw her into the kiss though, Touko begins to relax, opening her mouth and allowing Aina's tongue inside."
    "Aina puts her hands behind Touko's neck, drawing her head down as she works her tongue more and more forcefully through Touko's mouth."
    aina "Hmm... Mmm!"
    touko "Ah.. Nnh.."
    "They're loud enough that I can hear them even through the door."
    thinking "What the hell!? Are these two seriously getting all over each other at school?"
    "I keep watching closely through the keyhole as the sounds become even louder, their makeout session intensifying."
    
    scene touko_aina_sex_scene_1 3
    "Saliva drips from her mouth as Aina draws away from Touko for a moment."
    "She looks up at Touko's dazed face as she begins to reach under Touko's skirt."
    aina "I want more than just your mouth, Touko..."

    scene touko_aina_sex_scene_1 4 with quick_fade
    "It looks like Touko is just as into this as Aina. Her exposed pink panties are already wet, and Aina draws streaks along them as she runs her fingers over them."
    aina "Look how wet you are, Touko. You've been thinking about this too, haven't you?"
    touko "..."
    "Touko shuts her eyes, cringing with embarrassment."
    "She makes no move to stop her though, as Aina continues stroking her over her slick wet panties."
    aina "Look at you. I think you must be a bigger pervert than I am..."
    touko "..."
    aina "Hehe. And I really love you for it~"

    scene touko_aina_sex_scene_1 5
    "Aina rubs around Touko's clit."
    touko "Mmm~"
    "Touko starts to squirm, grinding herself against Aina's hand."

    scene touko_aina_sex_scene_1 6 with cum_flash
    play sound cum2
    "It looks like she can't help herself. She whimpers a little as her juices drip along Aina's fingers."
    
    scene touko_aina_sex_scene_1 7
    "With her arm wrapped around Aina's back, Touko starts to reach under Aina's skirt, beginning to stroke her back over her panties."
    "Touko works her own tongue into Aina's mouth now as she runs her fingers over the other girl's pussy."
    aina "Mmm~"
    "Aina moans eagerly under Touko's touch, urging her on."
    "Like Touko, her panties were already soaked at the first touch."
    "Aina draws back from their kiss to speak again."
    aina "Good girl, Touko. Come on, I want more."
    "Touko begins to pick up the pace, increasing the force of her fingers' movement."
    aina "Ah~"
    "Aina shivers for a moment, almost letting her own hand stop before she resumes her pressure on Touko."
    "Her juices are dripping through her panties, coating Touko's hand as she kneads her pussy."
    
    scene touko_aina_sex_scene_1 8 with quick_fade
    "This time, Touko is the one to bring her mouth to Aina's, resuming their kiss."
    "They work their tongues against each other, slurping and moaning into each other's mouths, saliva dripping from their lips as their pussy juices trickle down their legs."
    "It's a sight that could drive any man crazy with lust."
    "Unfortunately..."
    thinking "I've still got this fucking door between us! God dammit, I don't want to watch this through a shitty keyhole, I want a front row seat!"
    "But, I can't afford to risk my cover, so I stay put, trying to angle myself for the best view I can get through the keyhole."
    
    scene touko_aina_sex_scene_1 9
    "As I watch, their efforts continue to intensify. They've slipped their fingers inside each others' panties, their voices rising as they rub each other directly."
    touko "Ah! Aina!"
    aina "Touko!"
    "The two of them moan out each other's names, their voices filled with ecstasy."
    "With her free hand, Aina starts to work the buttons of Touko's top."
    
    scene touko_aina_sex_scene_1 10 with quick_fade
    "In her eagerness, she can barely slow herself down to undo the buttons rather than ripping the uniform open by force."
    "Touko shudders in anticipation, allowing Aina to take the lead once more."
    touko "Mmm, Aina~"
    "Aina works her way from the bottom up, leaving Touko's top just barely held closed until the last button comes undone."
    "Touko's top springs open, bringing her impressive breasts, bound by a pink lacy bra, into clear view."
    "I can see her hard nipples swelling against the fabric."
    aina "Ah, Touko~ I can never get enough of your breasts."
    touko "..."

    scene touko_aina_sex_scene_1 11
    "Touko's eyes are shut again. It looks like she's waiting in anticipation."
    aina "You're so beautiful, Touko. You're the best. Your boobs are just perfect."
    "Aina undoes Touko's bra, letting her breasts swing free in the air."
    "Aina grins as she runs her fingers along them."
    aina "Especially their taste~"

    scene touko_aina_sex_scene_1 12
    "She begins sucking on Touko's nipple."
    touko "Ah! Aina!"
    "Touko's body jolts as Aina's tongue makes contact."
    "Aina teases Touko's other breast with her hand as she licks and sucks."
    aina "Ahh!"
    "The sensation from her breasts is overwhelming Touko."
    aina "Mmm~"
    aina "You taste so good!"
    touko "Nnh! Aina!"
    "The sucking sound and Touko's moans are clearly audible even through the door."
    "If anyone else came by here, there's no way they wouldn't notice."
    "But the two of them picked their spot carefully, which means I have the whole show all to myself."
    "I can see Touko shuddering under the pleasure as Aina plays with both her breasts and her pussy at once."
    "The sound of her voice is also becoming increasingly desperate."

    scene touko_aina_sex_scene_1 13
    "Trying to give as good as she's getting, Touko increases the pace of her own stroking under Aina's panties."
    aina "Ah~ Touko!"
    "It looks like Aina's approaching her climax. She pulls away from Touko's breasts, unable to keep sucking as her face contorts with pleasure."
    
    scene touko_aina_sex_scene_1 14
    "Instead, she increases the pace of her fingers, trying to push Touko to the finish with her."
    
    scene touko_aina_sex_scene_1 15
    "Their eyes are locked on each other, taking in every change of expression as they urge each other on."
    "They let out little gasps and whimpers as their bodies shudder against each other."
    
    scene touko_aina_sex_scene_1 16
    "Their panties are completely soaked through, their juices dripping along their legs and down each other's fingers."
    thinking "They're both really picking up the pace now. Looks like they might be..."
    touko "Ah Aina! Aina!"
    "Touko starts moaning out her partner's name."
    touko "Ah...! I'm... I'm gonna cum!"
    thinking "Just as I thought."
    "Touko is on the very edge right now."
    aina "Mmm...! Touko! Touko!"
    aina "Me too! I'm almost there!"
    "And Aina's right there with her."
    aina "Cum with me, Aina!"
    touko "Nnh~"
    aina "Ah~"
    "The two of them keep fingering each other, bringing their pleasure to a frantic peak."
    
    scene touko_aina_sex_scene_1 17 with cum_flash
    play sound cum2
    "Almost as one, a convulsion runs through them."
    aina "Ah! Touko!"
    touko "Aina!"
    "They almost collapse, resting their weight against the wall as their legs shudder under them."
    "Their juices flood through their panties, trickling onto floor and flowing down their legs."
    "It's so much that their juices flow together, leaving a single puddle beneath them."
    "From their excitement, it seems these two must have been holding themselves back a long time."
    
    scene touko_aina_sex_scene_1 18
    "They hold onto each other, gazing at each other with hazy eyes."
    aina "Hah... I love you, Touko."
    touko "I love you too."
    aina "Then, let's do more of this again..."
    touko "Mmm... Mhm~"
    "They give each other one last kiss before they set about cleaning up. From the quickness of their work, it looks like the two of them already know where all the cleaning supplies in this utility room are stored."
    $ renpy.end_replay()
    $ persistent.touko_aina__cg_1 = True
    jump gym__day_1_continued_3

label gym__day_1_continued_3:
    scene bg hallway 1 with dissolve
    play music campus fadeout 1.0 fadein 1.0
    "Meanwhile, outside the door, I've been watching everything from start to finish."
    "Even just watching through that small hole, it was hot enough to get me hard and leave a bit of pre-cum leaking out."
    thinking "Damn, how come I never got to see anything like that while I was still a student here!?"
    "Feelings of jealousy well up in me. More than ever, I'm determined now to get the both of them."
    thinking "That's it, I can't wait any longer. I'm going to fuck them no matter what."
    "I let out a confident smile."
    thinking "Heh... And I think I have just the plan..."
    "As I'm piecing together the details, I hear the sound of footsteps approaching from inside the room."
    thinking "Oh shit, they're coming out! Hide!"
    "There's barely anywhere to hide nearby. I have to make a dash towards a corner in order to conceal myself."
    "As soon as someone emerges from the closet, I stick my head out a little to take a peek."
    
    show aina school happy with moveinright
    "It was Aina who'd just walked out, but Touko is nowhere to be seen."
    "Well, that makes sense. They made sure to enter separately, they must be trying to avoid being seen together."
    "As Aina walks away, I keep watching to see when Touko will come out."
    
    hide aina school happy with moveoutleft
    "After a few minutes, Touko leaves the closet as well."
    thinking "Great, now's my chance."
    "I step out from my hiding place. She's walking down the hall in the opposite direction, and doesn't see me approaching."
    
    show touko school happy arms with moveinright
    "I make my presence known..."
    shinn "Oh. Touko!"
    "As soon as she hears my voice, she freezes for a moment before turning around."
    touko "Oh, Shinn! I wasn't expecting to see you here."
    "She can't help looking suspicious, like she knows she's been caught getting up to something."
    shinn "Hmm, you okay?"
    "She quickly averts her guilty face before giving me her answer."

    show touko school concerned arms
    touko "Yeah, everything's fine."
    thinking "Heh, right, you've been having a fine time so far..."
    shinn "Well, what are you doing here during lunch time? Not many students come by here."
    touko "Err... I was just passing by."

    menu:
        shinn "I see..."
        "Ask her about her day":
            $ renpy.block_rollback()
            jump gym__day_1_day
        "Ask her about what she is doing inside the utility room":
            $ renpy.block_rollback()
            jump gym__day_1_utility

label gym__day_1_utility:
    shinn "Hey Touko. Just now I saw you coming out from the utility room. What were you doing in there?"
    "Touko's expression becomes even more nervous..."
    touko "Eh? Er..."
    $ renpy.music.set_volume(.50, 0.0, channel = "sound")
    play sound school_bell
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    "Before Touko can even reply, the school bell rings signaling the end of lunch."
    touko "Oh, I'm sorry Shinn. Lunchtime's just ended, so I've got to get back to class."
    
    hide touko school concerned arms with moveoutleft
    "Before I could give a reply, she turned around and hurried off."
    shinn "Damn it, and I was thinking I could expose her right now. Now what?"
    jump gym__day_1_continued_4

label gym__day_1_day:
    shinn "So how is your day going?"
    touko "Erm... Great, I guess?"
    "She seems reluctant to continue this line of conversation, and her tone tells me she clearly doesn't want to be here."
    shinn "Good. I hope you've completed the homework I gave you yesterday?"
    touko "Of course!"
    $ renpy.music.set_volume(.50, 0.0, channel = "sound")
    play sound school_bell
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    "However, before I could continue the conversation, the school bell signaling the end of lunch rang."
    touko "I'm sorry Shinn, but lunch is over. I have to get back to my classroom now."
    shinn "Okay. We'll talk later."

    hide touko school concerned arms with moveoutleft
    "She turns around and hurries off."
    shinn "Damn it, she ran away before I could change the subject. Now what?"
    jump gym__day_1_continued_4

label gym__day_1_continued_4:
    "I turn around to look at the door of the utility room."
    shinn "Hmm... Maybe I should take a look?"

    scene bg utility room with pixellate
    shinn "..."
    "The room is filled with a feminine smell."
    shinn "Huh, seems like they used a whole bunch of perfume to cover up the smell."
    "Looking at the place, I can't see any sign of their activities from before."
    shinn "These girls are pretty good at cleaning up. Not a trace of evidence after they're done."
    "Just to be sure, I take some time to look around the room for a more thorough search."
    shinn "Hmm... Nothing but cleaning stuff and stored equipment."
    "Just as I was about to give up searching..."
    shinn "Hmm? What's this?"
    "There seems to be something pink hidden behind a corner of shelving."
    "A bit of sunlight is shining on it from the window, but it's hard to spot at first due to its position."
    "I pick it up for a closer look."
    shinn "Hmm? Why does it feel wet?"
    "The object I grabbed was something I never expected."
    shinn "Wha- pink panties?"
    shinn "Huh?"
    "Why would this even be left behind here?"
    shinn "Wait. Could this be..."
    "The pink panties were tainted and soiled."
    "I brought it to my nose and took a whiff."
    shinn "Wow..."
    "Breathing it in almost feels like snorting drugs."
    shinn "There's no doubt that this is a high school girl's scent. And it's quite fresh."
    shinn "So, are these pink panties one of theirs?"
    shinn "Hmm... From the looks of it, it seems like one of them left her panties here in the sunlight to let them dry."
    shinn "Well... There's only one way to find out."
    "I take the panties with me and keep them in my pocket."
    shinn "Let's see who comes back to get these. If I'm on track here, they should be back for them as soon as classes are over."

    scene bg hallway 1 with pixellate
    "Classes have ended."
    "I've been waiting in this spot for over two hours now. I feel like an idiot."
    thinking "This was such a stupid idea."
    thinking "There's no guarantee that the person who left them behind will come back for them today."
    thinking "Besides, I need to be there for the tutoring sessions in just a bit."
    thinking "Maybe I should just give up and go."
    "Just as I'm about to leave, I hear footsteps heading my way."
    # SFX: *School Shoes Footsteps*
    thinking "Oh shit! Someone's coming!"
    "I run back to my hiding spot to take a look at who it is."
    show touko school happy with moveinright
    "A figure becomes visible."
    thinking "My my, what do we have here?"
    "Seems the owner of the panties was Touko after all."
    thinking "From the look of it, she seems pretty uncomfortable."
    thinking "Has she been attending afternoon classes without her panties? Wow, what a naughty girl."
    hide touko school happy with moveoutleft
    "She takes a quick look around before entering the utility room."
    thinking "There! She must have gone back to get her panties."
    thinking "Heheh. Wonder how she'll react when she sees they're nowhere to be found?"
    show touko school angry with moveinleft
    "A few minutes later, she comes back out of the room looking extremely anxious."
    hide touko school angry with moveoutright
    "She walks away slowly."
    shinn "Checkmate."
    "I feel a sense of victory welling up in me as I head towards the classroom."
    thinking "I've got the dirt on her. Now it's time for the payoff..."

    scene bg classroom with dissolve
    show touko basketball happy
    "As I slide open the door, I'm surprised as the sight of Touko waiting for me in the classroom."
    "Instead of her usual school uniform, she was dressed in her basketball team outfit."
    thinking "Heh... Afraid of being exposed?"
    touko "Good afternoon Shinn."
    shinn "Good afternoon Touko. I'm surprised to see you here in your basketball outfit."
    show touko basketball shy
    "Touko turns away, looking embarrassed."
    touko "Erm... Well, I splashed a bunch of water over my shirt while I was in the bathroom."
    thinking "Pfft... Is that the best lie you can come up with?"
    shinn "Is that so? Well, try to be more careful next time."
    touko "Yes, I will."
    show touko basketball happy
    "Touko takes the practice assignment I gave her yesterday out of her bag."
    touko "Here you go. I've completed it as promised."
    shinn "That's great. Give me a second to get my things ready and I'll give it a look over."

    menu:
        thinking "Hmm... Let's see. How should I do this?"
        "Don't expose her":
            jump gym__day_1_no_expose
        "Expose her Immediately":
            jump gym__day_1_expose
        "Wait a little longer":
            jump gym__day_1_wait_expose

label gym__day_1_no_expose:
    "Maybe it's better not to expose her."
    "After all, judging by their \"private party\" before, it seems like Aina is the one really driving this relationship."
    "Maybe it'd be easier to get to Touko through Aina rather than the other way around.."
    "I'll just go through class with her normally for now."
    shinn "Alright. Let me talk a look."
    "I scan through the work on Touko's assignment."
    shinn "Hmm..."
    touko "Well?"
    shinn "Well, there are quite a few mistakes here we'll need to go over."
    touko "Is it that bad?"
    shinn "Hmm..."
    touko "You can tell it to me straight. If you don't, I'd just worry more anyway."
    shinn "Well, it's not quite a failing grade, but you'd be in trouble if the stuff we haven't gone over yet is any weaker than this."
    touko "Oh."
    shinn "Don't worry, that's what I'm here to help with."
    shinn "So, let's get started, shall we?"
    touko "Okay."
    "I spend the rest of the session guiding her step by step through all the problems she get wrong."
    "Just like that, the session is over in no time."
    shinn "Well, I think that should be all. Think you've got it now?"
    touko "Yes. Thank you for your help, Shinn."
    shinn "No problem. It's getting pretty late now, so let's wrap it up for now."
    touko "Okay."
    "Before I start putting away my things, I hand her another sheet."
    show touko basketball shy
    "Touko gives it a wearied look."
    touko "Homework? Again?"
    shinn "Right, homework again. The only way to improve is to keep on practicing every day."
    shinn "Just like with basketball, right?"
    touko "Okay."
    "Touko reluctantly takes the paper from me."
    shinn "Alright, I'll see you tomorrow."
    touko "Yeah, see you."
    "Just as she's about to leave the class, I realize there's something I still have to ask her."
    shinn "Oh, Touko?"
    touko "Yes?"
    shinn "Would you happen to know where I'd find Aina before class in the morning?"
    touko "Yes, but why?"
    shinn "Oh, I need to catch her for a talk about her schoolwork too."
    touko "She comes in early for morning practice at the pool. You should be able to find her there."
    shinn "Alright, thank you so much."
    touko "Good bye."
    shinn "Bye."
    "Touko steps out, leaving me alone in the class."
    thinking "Heheheh... Perfect. Then Aina will be next. Swimsuit sex, here I come."
    jump map__school

label gym__day_1_wait_expose:
    shinn "Alright. Let me see how you did."
    "I take the papers from her and scan through her answers."
    shinn "Hmm... Seems like you've missed quite a few of these, I'm afraid."
    touko "Oh..."
    shinn "Don't worry Touko. Practice makes perfect, just like in basketball."
    shinn "Let's go over your mistakes for this session, and then we'll move on to a new topic."
    touko "Okay."
    "We go through the usual routine, writing down questions and formulas on the blackboard and walking her through them."
    "It doesn't take long before we reach the end of the lesson."
    shinn "Alright, let's call that a day. I think you did great."
    touko "Thank you!"
    "She packs her bag and gets ready to head home."
    "I approach her with some practice papers in hand."
    shinn "Don't forget these, Touko. I want to see your grasp of the new material."
    show touko basketball shy
    "Touko's cheery mood vanishes as she immediately falls into a sulk."
    touko "Ugh... Okay."
    shinn "Hey, don't be like that. Keep a positive attitude."
    touko "Alright."
    "She puts the papers in her bag and heads for the door. Just as she's about to open it, I call out to her."
    shinn "Oh, Touko, I think you forgot something."
    "I take the pink panties out from her pocket and flash them in front of her"
    shinn "Remember these?"
    "Touko gapes. The sudden turn in the conversation has left her dumbfounded."
    touko "That's... my..."
    shinn "That's right, these are your panties."
    "Touko's distress is written all over her body. I can see her trembling, she might scream for help at any moment."
    touko "You... Per—"
    shinn "Now, hold on a second. Before you shout, you might want to know how I got ahold of this."
    "Touko freezes. She stares back at me with a look of pure venom."
    shinn "I've been keeping an eye on you since this morning, Touko. Observing your every action and movement."
    touko "You..."
    shinn "That's right. That includes the incident in the utility room."
    touko "No... That can't be..."
    thinking "Heh. She gets it now."
    "Sensing that I have Touko trapped like a cornered animal now, I give her a sinister smile."
    shinn "Now Touko. I think it would cause some rather serious problems for you if news of this incident became public, isn't that right?"
    shinn "I think your parents would be likely to have some pretty strong opinions on the matter, wouldn't they?"
    "Touko looks defeated. She casts her gaze downwards, refusing to make eye contact with me."
    touko "What... Do... You... Want?"
    shinn "Why don't you come back over and sit down for a bit?"
    "In silence, she slowly walks back to her desk and sits down."
    jump touko_aina__cg_2

label gym__day_1_expose:
    shinn "Oh, before we get started, there's something I should probably show you."
    "I take out the pink panties from my pocket and flash them in front of her."
    show touko basketball shy
    "Touko gapes. The sudden turn in the conversation has left her dumbfounded."
    touko "That's... my..."
    shinn "That's right, these are your panties."
    "Touko's distress is written all over her body. I can see her trembling, she might scream for help at any moment."
    touko "You... Per—"
    shinn "Now, hold on a second. Before you shout, you might want to know how I got ahold of this."
    "Touko freezes. She stares back at me with a look of pure venom."
    shinn "I've been keeping an eye on you since this morning, Touko. Observing your every action and movement."
    touko "You..."
    shinn "That's right. That includes the incident in the utility room."
    touko "No... That can't be..."
    thinking "Heh. She gets it now."
    "Sensing that I have Touko trapped like a cornered animal now, I give her a sinister smile."
    shinn "Now Touko. I think it would cause some rather serious problems for you if news of this incident became public, isn't that right?"
    jump touko_aina__cg_2

label touko_aina__cg_2:
    play music sex fadeout 1.0 fadein 1.0
    "I walk up close, intimidating her with my presence."
    shinn "To be frank, Touko, when you told me about your friendship with Aina, this was not exactly the sort of relationship you described."
    touko "You leave her out of this!"
    "When I mention Aina, she immediately seems defensive. Seems like she wants to keep her out of this at all costs."
    shinn "Oh, how protective."
    shinn "You must really love her a lot, huh?"
    touko "..."
    shinn "Though I have to say, it takes a lot of guts to get involved in that sort of relationship, given your family circumstances."
    touko "Just leave Aina alone! She has nothing to do with this!"
    shinn "Don't worry. I won't do anything to her."
    thinking "At least for now."
    shinn "All you have to do is to listen to me and follow my instructions properly."
    touko "What do you want from me?"
    shinn "You know what I want from you."
    touko "What?"
    shinn "I heard all the action you had going on with Aina earlier. I was rock hard the whole time."
    shinn "So, I'm looking forward to having you relieve all that pressure you helped build up."
    "As Touko figures out my meaning, her face fills with revulsion."
    touko "No! There's no way in hell I'd do that sort of stuff with you!"
    shinn "What a stubborn girl. I don't think you're in any position to bargain here."
    shinn "Keep in mind what I have my hands on already."
    touko "..."
    shinn " That's right. Don't forget, carrying on relations like that at school is against the rules. As someone who's been put in charge of your education, I think it's my responsibility to teach you a lesson."
    touko "Fuck off, bastard."
    shinn "Right. Let's start off easy, shall we? Put your hands on the blackboard and lean forward with your hips out."
    touko "..."
    shinn "Come on. I don't have all day."

    scene touko_aina__cg_2 1 with fade
    "She stands up and walks over to the blackboard and does as I instructed, a look of disgust on her face."
    touko "Is that it?"
    shinn "Good."

    scene touko_aina__cg_2 2
    "I approach and stand directly behind her. I keep my eyes glued on her full and toned ass."
    shinn "Seems to me that you work your butt pretty hard for the basketball team."
    touko "Shut up!"

    scene touko_aina__cg_2 3
    shinn "Yeah, keep that up. I like to play with girls like that."
    touko "You—"

    scene touko_aina__cg_2 4
    "Before she can finish her sentence, I strip down her jersey shorts."
    touko "Kya! What— "

    scene touko_aina__cg_2 5
    "Since I already have her panties on me, her pussy and her asshole are completely exposed."
    shinn "Wow, not even wearing panties? You're a very naughty student, Touko."
    touko "Please, stop!"

    scene touko_aina__cg_2 6
    "I unzip my pants and place my erect dick right on her ass."
    shinn "I think you need to be disciplined."

    scene touko_aina__cg_2 7
    "I place my dick right up against her pussy, brushing up against her entrance."
    touko "No! Please don't! That thing is too big! It wouldn't fit!"
    shinn "Well, let's find out, shall we?"
    "I slowly thrust it in"
    touko "NOOOO!!"
    "As I thrust in, her inner walls wrap around me, clinging to my cock. She feels warm and wet inside."
    "Some of her juices leak out around me."
    shinn "No? Your pussy says otherwise."
    touko "No! Stop! Please!"
    shinn "Stop lying to yourself. You're a pervert just like me. You can't hold yourself back from doing naughty stuff even when you're at school."
    touko "That's not true!"
    "I begin to move."
    touko "No! Stop!"
    "I refuse to take heed of her pleas and push on. Her pussy tightens every time I pound her."
    thinking "At this rate..."
    "Touko is sobbing. Just like that, she's being helplessly violated by me. It seems as if she's already been emotionally broken."
    "Now all I need to do is to break her mind as well, and she'll be all mine."
    touko "Ahh! Please stop!"
    "Her screams get even louder. At this rate, someone is bound to hear her."

    scene touko_aina__cg_2 8
    "I take her pink panties and shove them into her mouth in order to muffle her."
    shinn "Shut up, bitch!"
    touko "Hmmpp..."
    "She's trying to shout for help, but with her voice muffled by her panties, nobody is going to hear her."
    "I continue to savor her pussy with my dick."

    scene touko_aina__cg_2 9
    "The sensation is breathtaking. I've never sampled an athletic girl's pussy before. It feels so different, so lively."
    "It doesn't take long before I start to feel the burning need to cum welling up in me."
    "I want to savor more of her pussy, but I can't put off the inevitability."
    shinn "I'm gonna cum!"
    touko "HMM, PFF!!"

    scene touko_aina__cg_2 10
    "Her muffled noises get even more intense, pleading with me not to do it."
    shinn "Take it, Touko!"
    shinn "Take all of my cum!"
    touko "UHMM!!!!"

    if persistent.cum == "inside":
        "Her pleas for me to stop make me even hornier. With a sudden rush of adrenaline, I pound her even harder."
        $ renpy.block_rollback()
        jump touko_aina__cg_2_inside

    elif persistent.cum == "outside":
        "Her pleas for me to stop make me even hornier. With a sudden rush of adrenaline, I pound her even harder."
        $ renpy.block_rollback()
        jump touko_aina__cg_2_outside

    else:
        menu:
            "Her pleas for me to stop make me even hornier. With a sudden rush of adrenaline, I pound her even harder."
            "Cum Outside":
                jump touko_aina__cg_2_outside
            "Cum Inside":
                jump touko_aina__cg_2_inside

label touko_aina__cg_2_inside:
    scene touko_aina__cg_2_inside 1 with cum_flash
    play sound cum2
    "Unable to resist any longer, I cum explosively inside her. It's so good, I cum enough that it gushes out from her pussy around me."
    shinn "Ahh!~"

    scene touko_aina__cg_2_inside 2 with cum_flash
    play sound cum1
    "Her legs shake and her pink panties fall as her mouth gapes open."
    "Her tongue sticks out and her eyes roll back in excitement."
    touko "AHH!"
    "She falls to the ground, unable to support her weight."
    jump touko_aina__cg_2_end

label touko_aina__cg_2_outside:
    scene touko_aina__cg_2_outside 1 with cum_flash
    play sound cum2
    "Unable to resist any longer, I take my dick out and spray it all over her back."
    shinn "Ahh!~"
    "Her legs shake and her pink panties fall as her mouth gapes open."
    "Her tongue sticks out and her eyes roll back in excitement."
    touko "AHH!"
    "She falls to the ground, unable to support her weight."

    scene touko_aina__cg_2_outside 2 with cum_flash
    play sound cum1
    "My cum is splattered everywhere, on the floor, across her back, covering her jersey."
    "Some of it is even clinging to her hair. I'm surprised it was able to shoot out over such a distance."
    jump touko_aina__cg_2_end

label touko_aina__cg_2_end:
    shinn "Heh. Look at you! What a shame that the beloved star athlete has degenerated into such a slut."
    touko "Ahh..."
    "She doesn't respond to my words. She's lost her sense of awareness."
    "I lean on Touko and whisper right into her ears."
    shinn "Listen, Touko. This isn't over yet. If you tell anyone what happened today, I'll make sure that Aina is next. You hear me?"
    touko "Ahh..."
    shinn "..."
    shinn "Now clean yourself up, bitch. And remember what I said."
    "I take one last look at her as I leave the class. Leaving her to her own demise."
    shinn "I'll look forward to even more fun tomorrow..."
    $ renpy.end_replay()
    $ persistent.touko_aina__cg_2 = True
    play music campus fadeout 1.0 fadein 1.0
    jump map__school

label gym__day_3:
    scene bg staffroom with map_fade
    $ touko_aina_next_step = "continue_1"
    "I came very early to school today just to check and ensure that everything was alright."
    "And also, to make sure that Aina doesn't suspect anything yet."
    "After all, I wasn't sure if Aina cleaned up all the mess from yesterday."
    "But thankfully, it seems everything is in the clear."
    "After everything yesterday, hopefully she'll still come in to school today."
    "I take a look at the clock and realize that school is just about to start."
    thinking "Hmm... Maybe I should pop by her class before lessons, just to give her a little surprise."

    scene bg hallway 1 with pixellate
    "I stand in the hallway outside Touko's classroom, leaning by the window, waiting for Touko to arrive."
    "However, before long, I start to realize that this might not be the greatest idea."
    "Some of the students start to take notice of my presence here. Considering that I'm not wearing my old school uniform, and don't look old enough to fit in among the faculty, I can't help standing out."
    thinking "This was a bad idea..."
    "Just as I'm about to give up and leave, a familiar person appears on the far end of the hallway."
    show touko school happy with moveinleft
    thinking "There she is."
    "Touko seems normal. In fact, she's walking along talking with some friends who I suppose are admirers of hers."
    show touko school concerned arms
    "As she gets closer, she notices me, and a look of disgust passes over her face. She passes by me without giving me another glance as she heads straight into her classroom."
    hide touko school concerned arms with moveoutright
    thinking "Heh. Ignore me all you want. Pretty soon I'll have you wrapped around my finger anyway."
    "Feeling reassured that things are still going smoothly, I head back to my workplace in the staff room."
    "As I'm on my way there, I hear someone behind me call out my name."
    unknown "Good morning, Shinn!"
    shinn "Huh?"
    show aina school happy with moveinright
    aina "It's me, Aina!"
    thinking "Oh, perfect timing."
    shinn "Good morning, Aina."
    aina "How are you?"
    shinn "I'm fine."
    aina "That's great to hear!"
    shinn "Don't forget your tutoring session with me next week."
    aina "I won't."
    hide aina school happy with moveoutleft
    "Aina walks away without the slightest inkling that my trap is already closing in on her."
    thinking "This is going to be fun."
    "Just as I'm about to walk away, a familiar figure appears."
    show satsuki uniform basic with moveinright
    shinn "Hmm? Satsuki. Is that you?"
    satsuki "Good morning Mr. Shinn."
    "Satsuki greets me in a ladylike fashion. As elegant as always."
    shinn "Ah, you're heading to class, right?"
    satsuki "Yes. My class is right there, next to Touko's."
    shinn "I see..."
    thinking "Hmm... Maybe she knows something about Touko."
    shinn "Say Satsuki..."
    satsuki "Hmm?"
    shinn "Would it be possible for you to tell me more about Touko?"
    show satsuki uniform upset
    "Satsuki gives me an uncertain look in response. It seems like she's weighing whether it's appropriate to reply."
    satsuki "..."
    thinking "Shit. She may get the wrong idea."
    shinn "Well... I don't mean that way..."
    satsuki "Well, she's certainly attractive and popular, so I can see where you're coming from."
    shinn "No no no..."
    shinn "I just mean that I want to get to know and understand her better as an instructor."
    shinn "That way, I should be able to offer her better support in math."
    show satsuki uniform basic
    "Satsuki seems somewhat relieved."
    satsuki "Oh. I see."
    satsuki "Hmm..."
    satsuki "I don't really speak with Touko much, but from what I know..."
    satsuki "She and Aina seem very close to each other. Apart from their positions in different sports clubs, it seems like the two of them are almost always together."
    satsuki "If anything, they might be too close..."
    "Satsuki stares off into space. It seems like she has something pretty serious on her mind."
    shinn "Err... Satsuki? Hello?"
    satsuki "Oh, sorry. I'm afraid I might have been getting a bit carried away with my thoughts."
    satsuki "But anyway, that is all I know. If you want to know more about Touko, you would probably be best off asking Aina."
    thinking "Well, it's not like I hadn't thought about going to her already."
    shinn "Alright then. Thanks for your help, Satsuki."
    shinn "I hope that we'll also be able to start working together soon."
    satsuki "Sure. When I have the time available in my schedule, I'll look forward to receiving your guidance."
    satsuki "If there is nothing else, I should be going now."
    hide satsuki uniform basic with moveoutleft
    "Satsuki walks off in her usual ladylike manner."
    thinking "Hmm... Seems like Aina is the key to Touko."
    thinking "Haha... Or vice versa I should say."
    jump touko_aina__cg_3
    
label touko_aina__cg_3:
    play music sex fadeout 1.0 fadein 1.0
    scene bg pool with dissolve
    "After giving the matter careful consideration..."
    "I think the best course of action is to proceed with Aina and see where things go from there."
    "I mean, I have the upper hand. What could go wrong for me?"
    "I pay a visit to the swimming pool, but no one seems to be around."
    thinking "Hmm... Weren't they supposed to have a practice session today?"
    thinking "Where have they all gone?"
    "Just then, a familiar person emerges from the girls' changing room."
    show aina pool basic with moveinright
    aina "Oh, Shinn?"
    "Target acquired."
    "Aina walks up to greet me, wearing her swimsuit."
    thinking "I have to admit, wearing a skintight swimsuit really shows off her figure."
    thinking "Considering her looks, it's no wonder she's so popular with the boys and girls in this school."
    "The more I look, the more I can feel my arousal growing. I can feel a familiar pressure building by the second."
    thinking "Shit. This isn't the time for a boner, hide it!"
    "As she arrives, I do my best to conceal the unsubtle bulge."
    aina "What brings you here?"
    shinn "I was looking for you."
    aina "Oh, what's up?"
    shinn "Is no one here for practice aside from you?"
    aina "Yeah, today's an off day. But since I have nationals coming up, I thought it'd be good to get in some extra practice."
    shinn "I see..."
    aina "So, you said you were looking for me?"
    shinn "Yes. Since we're alone here now, this should be a perfect time for it."
    aina "Huh?"
    "Since I'm going to confront her anyway, I guess there's no point hiding."
    "After all, this erection is getting pretty hard to conceal."
    "I give her a smile as I adjust my angle, leaving my boner on full display."
    "Of course, it's big enough to grab Aina's attention immediately."
    show aina pool surprise
    aina "Shinn?"
    aina "What... What are you doing?"
    shinn "Heheh... You look so hot with your swimsuit on. Can I have sex with you?"
    aina "What the fuck? Are you crazy?"
    aina "I didn't expect something like this from you, Shinn."
    shinn "Expect what? You should have seen it coming."
    "I grab her hand while teasing her."
    shinn "Come on... Let's do it."
    "Looking repulsed, Aina shoves my hands away."
    aina "Get away from me you pervert! I'm going to call for help!"
    "She turns her back on me, about to run away."
    thinking "Shit."
    shinn "I'm not so sure about that, calling for help when Touko is in trouble."
    "The moment I mention Touko's name, Aina freezes."
    shinn "That's right."
    "I slowly walk up to her and whisper right into her ear."
    shinn "I know everything..."
    "I walked around and face her. Her expression has changed to one of anxious uncertainty."
    aina "What? What did you know about her!?"
    thinking "Hmm... I wonder what I should say here?"
    shinn "I saw the two of you having a good time in the utility room yesterday."
    shinn "And after that, I went into the room to investigate."
    aina "Then what!?"
    shinn "Then I happened to see Touko's wet panties hanging out to dry."
    shinn "I took it and show it to Touko."
    shinn "Guess what I did with her?"
    "The sudden realization makes Aina sick."
    aina "You bastard! How could you!"
    "I took out my phone and show her the picture of what I did to Touko."
    shinn "Here you go. Take a look at your love, drowning in my semen."
    aina "You..."
    aina "You're not going to get away with this!"
    shinn "Well, there are two ways that this can go. One is that I expose this on the internet and around the school, and your lover Touko's career and school life are over."
    shinn "The other is that you can have sex with me right now, and I'll keep this a secret."
    aina "You..."
    shinn "So? What's it going to be? Protecting your lover by tasting this dick of mine, or ending things with Touko with the click of a button?"
    aina "..."
    "The gravity of the situation is slowly starting to sink into Aina."
    "For her, there's simply no choice between the options I offered her."
    "If she's acting for Touko's sake, there's no question that she'd choose to let me fuck her."
    "She gives me a look filled with rage."
    aina "So, if I have sex with you, you won't tell anyone."
    shinn "Tch. Of course. Who do you think I am?"
    shinn "I may be hungry for sex, but I do keep my word."
    aina "Fine..."
    aina "So... How do you want to do it...?"
    shinn "Glad you asked. Now, all I need you to do is to lay down by the side of the swimming pool."
    "Without giving any reply, Aina does as I instructed."
    "I strip down, showing off my huge erection to Aina."
    "She blushes as she catches sight of it, and through the thin fabric of her swimsuit, I can see her nipples getting hard."
    shinn "So, you like my dick, huh?"
    aina "Shut up..."
    "The latex of the swimsuit, slick and wet from her shower, turns me on like crazy."
    "Just fucking her isn't going to be enough, it makes me want to toy with her first."

    scene touko_aina__cg_3 1 with fade
    "I bend down beside her, and place my dick near the armpit opening of her swimsuit."
    "Slowly, I insert my dick into the opening, sandwiching it between the latex and her skin."
    "The size of my erection is enough that my dick reaches all the way to her nipple."

    scene touko_aina__cg_3 2
    aina "Mm..."
    "Aina doesn't say anything, but from the look on her face, this isn't a bad feeling for her."
    "I begin to rub my dick along her breast underneath the swimsuit."
    "The slick wet elastic and the softness of her breast feels so good, it's almost as if I'm having sex with a real pussy."
    aina "..."
    "As I continue to rub, her expression begins to shift from anger to embarrassment."
    "Could it be that she's actually enjoying this?"
    "Her breasts are bouncing with my thrusts, and I can see her nipples protruding sharply under the latex."
    "Each time the tip of my dick brushes her nipple, the desire to ejaculate grows inside me."
    "I start to rub harder, feeling the sensation rising up."
    shinn "Agh! Aina, I'm cumming!"
    aina "..."
    shinn "I'm gonna cum inside your swimsuit!"
    aina "Mmm..."

    scene touko_aina__cg_3 3 with cum_flash
    play sound cum2
    "As I reached the point where I couldn't hold it any longer, I ejaculate, spilling my semen across the top of her swimsuit and around the armpit opening."
    shinn "Ahh..."

    scene touko_aina__cg_3 4 with cum_flash
    play sound cum1
    shinn "That felt so good..."
    aina "...."

    scene touko_aina__cg_3 5
    "Aina examines herself, looking shocked as she realizes how much of my semen has spilled inside her suit. It's even coming out through the neck opening"
    "But apart from that, she seems to be taking the situation in stride."
    aina "So, I guess you're planning to move on to the real thing from here, huh?"
    shinn "Oh, what a surprise."
    shinn "Seems like you know your stuff after all."
    shinn "Do you do research on the internet or something?"
    shinn "Maybe look up tips and moves you can try out on your girlfriend?"
    aina "Stop talking and let's get this over with."
    shinn "Hah. And to think people at this school see you as a cheerful, pure and caring girl."
    shinn "Seems that after all you're a real slut and just keep it hidden away."
    aina "I'm not a slut. I'm just curious and got carried away with Touko before."
    shinn "Yeah, I hear excuses like that all the time."
    shinn "But from the look of it, it seems like you're starting to get pretty attached to my dick yourself."
    aina "Just shut up and finish this."
    aina "Asshole."
    thinking "Seems like she has a hard time denying that she knows a thing or two about sex."
    thinking "Considering what I saw before, it seems like she's the pushy one in her relationship with Touko."
    thinking "I guess I shouldn't be surprised."
    thinking "But if she's that horny to begin with, this should be a walk in the park for me."
    shinn "Well, alright then."

    scene touko_aina__cg_3 6
    "I move around behind Aina, where I position myself to penetrate her."
    shinn "So, I assume you've got a dildo already which you've tried out on yourself and Aina before?"
    aina "You don't need to know anything like that."
    shinn "You two must have a lot of fun times together."
    shinn "It's a shame I haven't been there to see any of it for myself."
    aina "..."

    scene touko_aina__cg_3 7
    "I take a look at her pussy before I get started."
    shinn "Look at this. It's all wet."
    shinn "Getting excited by the incoming dick, huh?"
    aina "..."
    shinn "Now, it's time for you to see which is better. A plastic dick, or a real meat rod that shoots cum out into your slutty pussy!"

    scene touko_aina__cg_3 8
    "I plunge right in, and waste no time forcing myself all the way to her deepest parts."
    aina "Kya!"
    shinn "Oh? Too much for you to take?"
    shinn "I bet a dildo doesn't feel as good as my dick now, does it?"

    scene touko_aina__cg_3 9
    aina "Shu... Shut up."
    shinn "By the end of today, I am going to make sure you won't be satisfied by anything but my dick from now on!"

    scene touko_aina__cg_3 10
    aina "Like hell I will!"
    "Since she's feeling so defiant, I decide to go even deeper, and thrust myself all the way into her womb."
    aina "Ahh~"
    "Her face started to show the pleasure of feeling my dick going in and out of her womb."
    "I can also feel her pussy getting even wetter."
    "In fact, with how wet she is now, no matter what she might say, there's no question that she's enjoying this."
    "I grab her breast to ramp up her pleasure even more."
    "The feeling of her breasts as I grab at them through her swimsuit is simply out of this world."
    "The latex of the swimsuit is slippery under my hands."
    "Not only that, the sound it makes is pretty erotic as well."
    "As I watch, Aina seems to be getting more and more aroused."
    "It shouldn't be long now before she starts to give in."
    shinn "Now tell me. Which is better. My dick or your dildo?"
    aina "Your..."
    thinking "Oh, she was about to say it..."
    shinn "What? I didn't get that."
    "It's obvious that Aina is feeling pleasure along with the embarrassment."
    "The look of anger in her face is almost gone now."
    aina "Shinn's cock..."
    shinn "Heh... Good."
    shinn "You're gonna enjoy my dick from now on, you get me?"
    aina "Y... Yes..."
    shinn "Now as a reward, you'll get to enjoy the thick milk from my balls."

    scene touko_aina__cg_3 11
    aina "What? No!"
    aina "No, not today. Today isn't safe!"
    shinn "No? But your pussy keeps squeezing me the more I move."
    shinn "You aren't being very honest with yourself, aren't you?"

    menu:
        aina "No, I am! Please!"
        "Cum Inside":
            jump touko_aina__cg_3_inside
        "Cum Outside":
            jump touko_aina__cg_3_outside

label touko_aina__cg_3_outside:
    "Since she's begging me to cum outside, I decide to humor her."
    "After all, she's already done a lot for me today."
    "Letting her decide for once isn't so bad."
    shinn "Alright, if that's how you want it..."
    "I give Aina one last pound before pulling my dick out."
    shinn "Here it comes!"

    scene touko_aina__cg_3_outside 1 with cum_flash
    play sound cum2
    "In an instant, the cum shoots out all over her body, covering her swimsuit."
    aina "Ah~"

    scene touko_aina__cg_3_outside 2 with cum_flash
    play sound cum1
    "Some of it even gets on her face."
    aina "Mm~"
    jump touko_aina__cg_3_end

label touko_aina__cg_3_inside:
    shinn "Please, do you think I care?"
    aina "No..."
    shinn "Hahaha!"
    shinn "What happened to your know-it-all attitude?"
    shinn "Got scared just because I'm gonna cum inside you?"
    aina "Please..."
    "I ignore her plea and plow ahead."
    shinn "Here it comes! Accept my milk in your womb!"
    aina "No!"

    scene touko_aina__cg_3_inside 1 with cum_flash
    play sound cum2
    "I give Aina one last pound and my milk shoots out instantly right into her womb."
    shinn "Argh!"

    scene touko_aina__cg_3_inside 2 with cum_flash
    play sound cum1
    "It's so much that the milk gushes out from her pussy."
    aina "Ah~"
    "I pull my dick out to inspect the mess I've made of her."
    jump touko_aina__cg_3_end

label touko_aina__cg_3_end:
    "She's exhausted from all the pleasure she's felt, and looks too tired to respond to anything."
    shinn "Mission accomplished."
    thinking "Well, I hope you had fun with my dick. Besides, this is just the beginning."
    thinking "There's going to be a lot more to come for you and Touko."
    shinn "I'll be going now. Go have a swim to clean yourself up or something."
    shinn "And remember, if you tell anyone about this, you know what'll happen then."
    $ renpy.end_replay()
    $ persistent.touko_aina__cg_3 = True
    play music campus fadeout 1.0 fadein 1.0
    jump map__school

label gym__day_3_continued_1:
    scene bg hallway 2 with map_fade
    $ touko_aina_next_step = "continue_2"
    "I come in early in the morning to check things out with Aina"
    "Afterall, what I did with her yesterday was kind of amazing."
    "I think today I'm gonna bring her along for a sex field trip."
    "As I walk across the hallway to my staff room, I spot the person I'm looking for."
    thinking "There she is."
    show aina school angry with moveinright
    "I walk up to her casually, as if nothing's happened between the two of us."
    "She's looking at the floor as she walks. She certainly doesn't look like she's in a good mood."
    "But who can blame her? After what I did with her yesterday, it's only natural for her to feel upset."
    shinn "Hey Aina. Good morning."
    "Just hearing my voice seems to give her a start, and she raises her head."
    "Her eyes bore into me, like in her head, I've already become a murder victim."
    show aina school angry
    aina "You..."
    shinn "I what?"
    show aina school angry arms
    aina "You have some nerve to come and talk to me like this."
    "Aina raises her voice, and some of the bystanders around us start to look our way."
    "The situation is starting to get a bit tense. I don't want things to get out of hand with everyone watching like this."
    thinking "Shit, I need to defuse this."
    shinn "Well Aina, I'm sorry, but I don't know what you're talking about."
    shinn "I'm just here as your math tutor, and that's it."
    "Aina is still looking at me like she's killing me in her mind."
    "In turn, I give her my \"if you expose me, you're dead\" look."
    "She gets the signal, and it seems she's decided to play nice for now."
    "She takes a deep breath."
    show aina school angry
    aina "Ahem. Good morning, Shinn."
    thinking "Phew..."
    shinn "Good morning, Aina."
    aina "So? What business do you have with me today?"
    "With the tension defused, the other students start to walk away, apparently deciding we're not interesting enough to bother with."
    "Since their attention is no longer on us, I walk up close to her and gently whisper in her ear."
    shinn "Meet me at the utility room during lunch. Don't be late."
    aina "What? Why would I..."
    "I interrupt her reply."
    shinn "You know what'll happen if you don't..."
    "Before she has the chance to reply, I walk away."
    hide aina school angry with moveoutleft
    thinking "Heh. Let's see if you'll show up."
    thinking "She already knows what'll happen if she doesn't."
    jump touko_aina__cg_4

label touko_aina__cg_4:
    play music sex fadeout 1.0 fadein 1.0
    scene bg utility room with pixellate
    "I came ahead of time to make preparations for what I'll be doing with Aina today."
    "I expect a bit of resistance from her, but not too much."
    "When you consider what I already did with her yesterday..."
    shinn "Heheheh."
    shinn "Can't wait to get a taste of that sexy swimmer's body again."
    "Time continues to pass as I wait for her arrival."
    shinn "Ugh, It's getting late. Is she even coming?"
    shinn "If she isn't coming, I am going to find her it'll be a whole lot more trouble for that bitch."
    shinn "I'll give her 5 more minutes."
    "I stare at my phone as I wait, counting down five minutes by the clock."
    shinn "Well, looks like she's not coming. Guess that's it."
    shinn "Time to go find her."
    show aina school angry with moveinright
    "But before I could leave the room to start my search, Aina opens up the door."
    shinn "Tsk. You sure took your time."
    show aina school angry
    aina "..."
    aina "Fuck off, Shinn."
    shinn "Woah. Watch your attitude young girl."
    aina "Cut the crap. What do you want with me now?"
    shinn "Ah. Good question, Aina."
    shinn "You see... When you and Touko were enjoying a fun and sexy time in  here..."
    shinn "I was left out all by my lonesome, having a sad look through that little keyhole."
    aina "So?"
    shinn "I was thinking that you could reenact with me the same thing you did with Touko."
    shinn "I'm sure this will satisfy the craving I built up watching that juicy yuri scene."
    aina "You're a sick fuck."
    shinn "Hahaha... Watch your language there."
    shinn "You don't want to offend me, do you?"
    aina "..."
    show aina school angry
    aina "I am sick and tired of your games."
    shinn "Games? Heh, what games?"
    aina "Whether I say yes or no, you're going to do it anyway, so why bother to even ask me?"
    shinn "Smart girl, Aina. Probably the smartest I've come across so far."
    show aina school angry arms
    aina "..."
    shinn "You see, it's very simple."
    shinn "Ever since I saw you, I knew I couldn't let you go without having sex with you."
    shinn "Your body is too irresistible. There's nothing that could make me give up on that."
    shinn "So, it doesn't really matter what you try to come up with to get in my way. I'm just going to keep at it one way or another."
    shinn "If it comes to that, there are all kinds of ways I can make your life difficult if I don't get what I want."
    shinn "But, if you go along with this now, I'll delete the dirt I have on Touko and forget about things with the two of you."
    shinn "After that, it'll be over between you and me."
    thinking "Well, if you're not addicted to my cock by then, that is."

    scene touko_aina__cg_4 1 with fade
    "I corner her against the walls."
    shinn "So why don't we stop the chatting and get down to business?"

    scene touko_aina__cg_4 2
    "Cornered like this, Aina seems unable to think straight."
    "Maybe she's decided that her best option is to go along with things as I said, or maybe she just doesn't have the nerve to resist, but her body seems to loosen up."
    
    scene touko_aina__cg_4 3
    "I decide to take a chance, and reach slowly reach out my hand to feel her pussy."
    aina "Mmm~"
    aina "Don't... don't move too fast, okay?"
    shinn "Too fast? Heh..."
    shinn "Alright then. What do you want me to do?"
    aina "..."
    aina "A... Kiss..."
    shinn "A kiss? From me, huh? Not Touko?"
    aina "..."
    shinn "What changed your mind?"
    shinn "Did you realize after you got a taste of my cock before that you were missing out on the good stuff?"
    aina "Shut... Up..."
    shinn "I expected better from you, Aina."

    scene touko_aina__cg_4 4
    "Despite my words, Aina continues to stare at me, as if she'expecting something."
    shinn "You really want that kiss, huh?"
    shinn "Okay then."
    "I lean my face forward, extending my tongue."
    "She opens up her mouth to let me in, and begins to interlock her tongue with mine."
    "Unlike those forced kisses from before, this one is a surreal experience."
    "She begins to work her tongue against mine, and I can feel her saliva dripping into my mouth."
    "The excess saliva starts to trickle out from our mouths, even dripping from out chins."
    "During all of this, I've continued to gently stroke my fingers over her pussy..."
    "It's almost an exact repeat of the scene with Touko from before. Except for the part where Touko didn't have a dick."
    "Speaking of dick, the feeling of our kiss, and of her smooth pussy against my hands, has gotten me completely hard."
    "In fact, I'm so hard now that the pre-cum has already started leaking out, and Aina hasn't even touched me yet."
    "I stop the kiss for a moment to examine the wet spot growing against the bulge in my pants."

    scene touko_aina__cg_4 6
    "As I pull back, Aina takes notice of it as well, and begins to stroke the tip."
    "Without my instruction, she takes the initiative and unzips my pants."

    scene touko_aina__cg_4 7
    "My dick immediately springs free, catching her by surprise."
    shinn "Whoa, looks like you know what you're doing after all."
    shinn "Just like I thought, I had you pegged as the really horny one between you and Touko."
    shinn "Tell me, do you watch porn every day to pick up tips?"
    aina "I started watching lesbian porn after I got together with Touko... but I've watched straight porn a few times too."
    shinn "I bet you got curious after seeing a man's dick on the internet."
    shinn "You must have wanted try tasting it for yourself, right?"
    aina "..."
    "She doesn't answer, but with this girl, I can tell that it's true."
    "My dick is quivering while we speak."
    shinn "My dick is hungry for some attention. Why don't you try out some of your techniques from the internet on me?"
    aina "..."

    scene touko_aina__cg_4 8
    "Aina begins to stroke my dick slowly."
    aina "Its... warm..."
    shinn "Heh. You like it, don't you?"
    shinn "Come on, stroke it harder, pleasure me if you can."
    shinn "In return, I'll make you feel good with my fingers."
    "Aina doesn't reply, but from her expression, I can see I've got the go ahead."

    scene touko_aina__cg_4 9
    "I shift her underwear to the side and begin to insert my finger as she strokes."
    aina "Ah~"
    "I begin to finger her gently. I can't be bothered to go soft like this all the time, but I feel like showing her a bit of consideration."
    "In retun, she strokes my dick at a matching pace."

    scene touko_aina__cg_4 10
    "Our movements are perfectly synchronized so that the two of us can cum at the same time."
    "She's staring straight at my face as she jerks me off, and I can feel the hot, steamy air of her breath against my skin."
    "She's getting more into this by the moment."
    "Her expression right now looks so different compared to yesterday."
    "Far from being repulsed, it looks like she's started embracing this."
    "The more I look at her, the sexier she seems."
    "Just watching her builds up my tension, making my dick even harder."
    "And of course, her stroking is out of this world as well."
    shinn "Ah... Aina, you're so good at this."
    aina "You... too..."
    "Hearing my voice seems to get her even more excited."
    "She starts to stroke even faster..."
    "And I start to finger faster."

    scene touko_aina__cg_4 11
    aina "Ah~ Shinn..."
    aina "I can't..."
    shinn "Let it out, Aina."
    shinn "Unh~"
    "I can feel something rising up in me, about to erupt."
    shinn "Ugh, I can't take it! I'm gonna cum soon!"
    shinn "Hey Aina, come on! Let's cum together!"
    "She speeds up her hand as she approaches her climax, while I speed up my fingers."
    aina "Ah~!"
    aina "I- I'm cumming!"
    "At that moment, a flood of her juices gush from her pussy."
    aina "Ah~ It feels so good!"
    "As she cums, she violently jerks at my penis."
    shinn "Agh, me too!"

    scene touko_aina__cg_4 12 with cum_flash
    play sound cum2
    "The sight of her, and the sudden movement, force me over the edge as well."
    shinn "Ahh~"
    "The feeling is incredible. It's enough that the two of us nearly black out."
    "The two of us lean against each other, panting as we try to regain our senses."
    "The area around us is a mess. Her skirt is covered with my cum, while my hand and her panties are drenched with her pussy juice."

    scene touko_aina__cg_4 13 with cum_flash
    play sound cum1
    "From the look on Aina's face, it seems like she's still hungry for more."
    shinn "Not enough, eh?"
    shinn "Seems like you're ready to move on to the main course."
    aina "Yeah..."
    shinn "Alright then. Since you're being a good girl today, I'll give you a treat."

    scene touko_aina__cg_4 14
    "I lift up one of her legs, exposing her soaking wet panties."
    aina "What are you doing?"
    shinn "Oh, you'll see."
    "I shift her underwear out of the way to get a clear view of her pussy hole."

    scene touko_aina__cg_4 15
    "Without giving any warning, I slam my dick straight into her pussy."
    aina "Oww~"
    shinn "You love it. Don't you?"
    "It looks like the sudden thrust sent a shock of pain through her."
    "But that doesn't stop her from enjoying my dick."
    aina "Yes..."
    "I fall into my usual forceful pattern as I penetrate her."

    scene touko_aina__cg_4 16
    "I thrust deep inside her, all the way to her womb. And damn, but she sure shows that she's feeling it."
    aina "Ah~ Harder!"
    "I pick up the pace as the raw pleasure shows itself on her face."
    aina "Yes~!"
    "She holds onto me tightly, like she can't bear to let go or let this end."
    "She's completely drowned in the act now. There's nothing on her mind but my cock."
    "I think she's well and truly addicted now, but just to be sure..."
    shinn "So tell me Aina, what do you love the most?"
    shinn "My dick? Or Touko's pussy?"
    aina "Your dick!"
    aina "Your dick is the best!"
    shinn "Heh. That's what I thought!"
    shinn "Since you're being such an obedient and good girl today, I'm going to pump my full load of cum inside you."
    shinn "Make sure you savior the taste, okay?"
    aina "Yes..."
    shinn "Just a yes? That's not right. From now on, you call me Master."
    shinn "Understood?"
    aina "..."
    shinn "Come on..."
    shinn "With me as your master, I can give you the love and pleasure Touko can't, every single day."
    aina "Yes, master."
    shinn "Good girl. Now, what about Touko?"
    "Without taking a moment to think, she responds."
    aina "Touko? What about her?"
    "Seems like she's finally snapped."
    aina "Why should I think about Touko? She doesn't have a dick and can't make me feel like this."
    aina "Dicks are the best after all, especially yours!"
    shinn "Hahaha..."
    shinn "That's what I want to hear."

    scene touko_aina__cg_4 17
    "As she said that, I could feel her pussy clamping down on me even tighter."
    "Seems like her desire for my cum is getting stronger by the minute."
    "At the same time, it feels like my balls are almost desperate to shot it out."
    shinn "Heh. You really want my cum, huh Aina?"
    aina "Yes~"
    shinn "Well then, how about this? From now on, you can be my sex slave, and I'll give you loads of my cum every single day."
    shinn "What do you say?"
    aina "Yes..."
    aina "Yes Master!"
    shinn "Good. Now before you get your treat, there's something I want you to promise me."
    aina "Ah, hurry up Master, tell me! I can't wait for your cum!"
    shinn "Help me make Touko my sex slave too."
    aina "Geez, aren't I enough?"
    shinn "Oh, are you jealous? Don't worry, you're still my favorite pet."
    shinn "Now, will you do it?"
    aina "Yes Master! I'll do whatever you say!"
    shinn "Good. Now here's the reward you've been waiting for!"

    menu:
        aina "Yes! It's coming!"
        "Cum Inside":
            jump touko_aina__cg_4_inside
        "Cum Outside":
            jump touko_aina__cg_4_outside

label touko_aina__cg_4_outside:
    "Her pussy is squeezing me like mad."
    "I've reached the point where I can't hold out any longer."
    aina "Hurry up, Master!"
    shinn "It's coming!"

    scene touko_aina__cg_4_outside 1 with cum_flash
    play sound cum2
    "I pound her womb one final time, then just as I'm about to explode, I pull it out and spray my cum all over body."
    aina "Ah~! Shinn's cum~"
    aina "It smells so good!"
    "The room is filled with the smell of my cum."
    "Aina has really milked me dry with this. It'll be a while before I'm ready to go again."

    scene touko_aina__cg_4_outside 2 with cum_flash
    play sound cum1
    "But her body, and face are completely covered with my jizz, and Aina seems fully sated."
    "She's blissed out, basking in the feel, smell, and taste of my cum, which overpowers her senses."
    "It looks like she doesn't even know what's going on around her anymore."
    jump touko_aina__cg_4_end

label touko_aina__cg_4_inside:
    "Her pussy is squeezing me like mad."
    "I've reached the point where I can't hold out any longer."
    aina "Hurry up, Master!"
    shinn "It's coming!"

    scene touko_aina__cg_4_inside 1 with cum_flash
    play sound cum2
    "In an instant, I spray everything that's left inside my balls straight into her womb."

    scene touko_aina__cg_4_inside 2 with cum_flash
    play sound cum1
    "Aina convulses as she feels the boiling heat of my cum flooding her insides."
    aina "Ah~! Shinn's cum!"
    aina "It feels so good inside me!"
    aina "I can't take it all!"
    "Seems like she's gotten so into this, she's lost all awareness of what's going on around her."
    jump touko_aina__cg_4_end

label touko_aina__cg_4_end:
    aina "Ah~ Shinn's cum. I love it!"
    aina "Men are the best after all!"
    shinn "Heh. That's right."
    shinn "Now, if you do as I said, I'll give you a bigger treat next time. Alright?"
    aina "Yes Master!"
    shinn "Good."
    shinn "Today, Touko will have another tutoring session, I want you to attend it."
    shinn "From there, it'll be up to you to convince her. You got that?"
    aina "Yes master!"
    shinn "Alright. See you later."
    $ renpy.end_replay()
    $ persistent.touko_aina__cg_4 = True
    play music campus fadeout 1.0 fadein 1.0
    jump map__school

label gym__day_3_continued_2:
    scene bg hallway 1 with map_fade
    show aina naked happy
    "The tutoring session was supposed to start at 3.30pm, but I'm running a little bit late."
    "You can chalk that up to the work I've had to go to to get Aina properly ready."
    "She's waiting in the wings to get things started now, wearing nothing but a dog collar."
    thinking "Yeah, this is definitely a good look for her."
    "I take my time to look her body up and down as I approach."
    shinn "So? You ready?"
    aina "Yes!"
    shinn "Alright. Keep quiet for now keep youself out of the way until I need you."
    shinn "I'll call you in when I'm ready."
    aina "Got it!"
    jump touko_aina__cg_5

label touko_aina__cg_5:
    play music breakdown fadeout 1.0 fadein 1.0
    scene bg classroom with dissolve
    show touko school angry
    "I slide the door opened to find Touko already waiting for me."
    "She tenses up the moment I come into the room."
    "Well, that can't be helped considering what I've already done with her."
    "I keep my eyes locked on her as I head over to my seat at the teacher's desk."
    "By the time I get all my things out, Touko is already looking seriously unnerved."
    shinn "What's wrong, Touko? You seem nervous."
    touko "..."
    show touko school angry arms
    touko "You're not going to do anything with me again today, right?"
    shinn "Well... we'll see about that."
    touko "Please..."
    "Her voice is a soft, pleading whisper."
    touko "Please leave me and Aina alone. We were already having a hard enough time being together through everything."
    touko "Why are you doing this to us?"
    "As she pleads with me, I can see her eyes starting to fill up with tears."
    thinking "Uh-oh. Here come the waterworks I guess."
    touko "I'm begging you to let us go, please."
    shinn "Heh. What exactly am I supposed to get in return for letting you off?"
    touko "..."
    touko "I could give you money."
    shinn "Money? I'm already fine on that front. What I want is sex. And you don't want to give that to me, so where does that leave us?"
    touko "Then use me! Use my body! Just leave Aina alone! As long Aina stays safe and we can be together, I'll put up with anything!"
    shinn "You sure?"
    touko "Yes, I'm sure! Please!"
    shinn "Well you see, about that..."
    "This seems like the perfect time to call on her."
    shinn "Aina! Come in!"
    aina "Yes Master!"
    touko "M... Master...?"
    show aina naked happy at left
    show touko school angry arms at right
    with moveinleft
    "The door slides open to reveal Aina, naked and hungry for sex."
    aina "Aina, reporting for service!"
    "Touko turns around and stands up with a jolt as she looks at Aina with a mixture of horror and confusion."
    show touko school angry at right
    touko "No..."
    touko "This can't be..."
    "The sudden revelation has an overwhelming impact on her. I can see Touko's heart sinking as she stares at Aina, taking in what this means."
    touko "..."
    shinn "Hahahahaha!"
    shinn "Sorry Touko, I'm afraid it's already too late for that!"
    shinn "You can offer anything for her that you want, but all your precious girlfriend cares about now is my cock!"
    touko "..."
    touko "Aina.... Why?"
    aina "Why? Because I love Master's cock!"
    aina "It's big and feels the best!"
    aina "When Master fucked me, it felt better than anything. So there's no way you could ever take his place, Touko."
    touko "...."
    touko "No way... This is a joke, right?"
    shinn "A joke? Maybe for me. But this is definitely real. You should get used to where you stand here."
    shinn "Give it up, Touko! It's over for you."
    shinn "If you love Aina and want to be with her that much, go ahead and join her! The two of you can service me together."
    shinn "There's always room for more in my harem!"
    "Aina slowly walks up to Touko"
    show aina naked happy arms at left
    aina "Come on, Touko. Why not join me? We can have fun together all the time with Master's cock!"
    aina "Don't you want to be really satisfied?"
    "Touko looks completely lost. Her expression is blank and unchanging, but I can tell she's breaking down."
    touko "I..."
    "Aina cuts in, doing her best to persuade her for me."
    aina "If you really love me, we should stick together! Stay with me, and we can keep having fun all we want!"
    "Touko looks Aina in the eye."
    touko "Is... Is this what you really want? Do you love doing this?"
    aina "Of course! Why would you even need to ask?"
    "Aina was so emphatic, Touko's reslve was starting to waver. No matter how far this might have been from what she expected, Aina was utterly sincere."
    "I walk up to stand alongside them and apply a little more pressure to Touko."
    shinn "Look at her, Touko. Have you ever seen Aina this happy before?"
    "Touko looks over Aina again, examining her blissful expression."
    "There's no question, she's never seen Aina looking like this before."
    touko "No..."
    "Finally seeming resigned, Touko asks one more time."
    touko "Aina, is this really what you want?"
    aina "Yes, it is!"
    shinn "Come on, Touko. What are you waiting for!?"
    "Touk seems to have finally come to terms with the fact that she's powerless to stop this. She stands in silent agony as the situation sinks in."
    "She unbuttons her clothes and skirt, undoes her black lace bra, and pulls down her panties."
    show touko naked at right
    "Her luscious breasts and the pussy I enjoyed so much yesterday are now fully exposed."
    shinn "Oh? Good girl."
    aina "Yeah! Touko is part of the family now!"
    "It's a wonderful sight having these two beautiful and well-developed girls on display like this. I join in too, and strip down along with them."
    "My dick flicks out, standing to attention as I pull my pants down. Touko is flushed with embarrassment, while Aina is enthralled."
    aina "Wow, Master's big cock!"
    "Seeing the contrasting reactions of the two in front of me, it's impossible for me to resist. And why should I?"
    shinn "Both, of you kneel down and suck my dick."
    aina "Yes Master!"
    shinn "You heard me. You too, Touko."
    "At this point, Touko has given up on fighting back. She's accepted this as reality, and follows suit along with Aina, even as her face shows that she's still repulsed by all of this."
    
    scene touko_aina__cg_5_blowjob 1 with fade
    "The two of them kneel down in front of me side by side. With the two of them on the ground like this, the tip of my dick nearly reaches out to touch their foreheads."
    "Touko, who's never seen a dick up close before, is clearly intimidated at the sight of it."
    thinking "Looks like she's wondering if it's even possible for her to take it in her mouth."
    shinn "Well ladies, what are we waiting for?"

    scene touko_aina__cg_5_blowjob 2
    "Aina knows what to do, and makes the first move, licking my cock along the side. Seems like she's trying to lead Touko by example."

    scene touko_aina__cg_5_blowjob 3
    "Touko takes a look at Aina's skillful tongue work, and does her best to follow suit."

    scene touko_aina__cg_5_blowjob 4
    "Aina continues to lick while keeping a watch over Touko. She works her tongue down the length of my shaft, even taking my balls into her mouth."

    scene touko_aina__cg_5_blowjob 5
    shinn "Ahhh... Touko, this feels great."

    scene touko_aina__cg_5_blowjob 6
    "As Touko begins to pick up a feel for what she's doing, she takes a bold step and takes my cock into her mouth, filling up her throat as far as she can while Aina continues to suck off my balls."
    touko "Enngh... It's salty."

    scene touko_aina__cg_5_blowjob 7
    "Touko makes a sour face as she finally gets her first taste of a real dick in her life. Hardly surprising in her case."
    "But, she should be used to it pretty soon."
    shinn "Aww, yeah... You guys are doing great."

    scene touko_aina__cg_5_blowjob 8
    "They keep sucking and licking together, trading off on my cock and balls between them. It feels amazing."
    aina "Mmm..."
    "Aina's clearly enjoying this. Seems like her lesson this afternoon really sunk in."

    scene touko_aina__cg_5_blowjob 9
    "Her sucking feels like it's trying to pull my cum straight out of me. Considering how much time she's probably spent licking Touko's pussy, it seems she's probably picked up a thing or two."
    shinn "Ugh... I'm gonna cum..."
    "Touko understood what was coming, but she didn't want to think about it, and kept on at her regular pace."
    "Meanwhile, Aina picks up the intensity in anticipation of what's coming,"
    aina "Ah, Master is going to cum! Please shoot out your thick juicy cum for us!"
    shinn "Ugh! Stick your tongues out!"

    scene touko_aina__cg_5_blowjob 10
    "They both hold their tongues out for me, like they're waiting for the taste of my cum."
    "Without their mouths to stimulate me, I take over with my hand, forcefully jerking myself off to the finish."
    shinn "Here it comes!"

    scene touko_aina__cg_5_blowjob 11 with cum_flash
    play sound cum2
    "I aim between their faces as I shoot out my cum. It sprays out all over them, across their faces, their bodies, a little even landing in their mouths."
    
    scene touko_aina__cg_5_blowjob 12 with cum_flash
    play sound cum1
    aina "Ah~ Master's cum! It's all over me! I love it!"
    "No wonder that Aina is enjoying it. But Touko seems a little surprised at the taste."
    touko "So... this is what cum is like..."
    touko "It tastes... salty, huh."
    aina "Master's cum tastes great! Isn't that right, Touko?"
    touko "..."

    scene touko_aina__cg_5_blowjob 13
    "Both of them really seem to get into the taste and smell of my cum. Although Touko still seems a bit reserved, it looks like she's adapting to this pretty fast."
    shinn "Heh. It's not over yet."

    scene touko_aina__cg_5_ride 1 with fade
    "I strip off the rest of my clothes, and lie down on the classroom floor."
    shinn "Alright. Touko, I want you to ride my dick."
    touko "W... What?"
    shinn "You heard me. Go ahead. ."
    "Touko still seems a bit reluctant."
    touko "..."
    "But Aina doesn't have much patience for Touko's resistance."
    aina "Come on Touko, listen to Master's orders. Be a good girl, and we'll both be rewarded with lots of his cum."
    shinn "Come on, Touko,Take a cue from Aina. She's being such a good girl trying to convince you."
    "Touko slowly gets into place and positions herself for insertion."
    shinn "Well, what are you waiting for? Hurry up and put it in."

    scene touko_aina__cg_5_ride 2
    "The size is a bit much for her to handle, but Touko works up her resolve and finally brings herself down onto it."
    "She takes my dick inside her, bit by bit, the pleasure starting to show on her face."
    touko "Ah~"
    "Finally, she manages to sink down all the way onto me, my dick fully inserted inside her."
    "At this depth, I can feel the head of my cock rubbing up against her womb."

    scene touko_aina__cg_5_ride 3
    touko "Ah~! It's so deep inside me!"
    aina "Isn't it amazing?"
    touko "I guess..."
    "My cock is throbbing for more action, so I push Touko to get started."
    shinn "Come on and move Touko. My cock isn't going to milk itself."
    "Touko starts to move up and down. She's riding my cock slowly, but for an amateur like her, it's a good start."
    shinn "That's more like it."
    touko "Mmm~"
    "This must be reminding her of the pleasure she already got a taste of last time."
    shinn "You missed that feeling, didn't you?"
    shinn "I know you fell in love with my cock the moment you tasted it."
    touko "..."
    shinn "It happened to Aina too. Just one round with my cock was enough to get her completely hooked."
    shinn "Just a little bit of training was all it took to bring out the animal in her. Her true, uncontrollable lust for sex."
    shinn "You've got the same thing inside you, Touko. You can be just like Aina, with the same thirst for cocks and cum."
    touko "..."
    shinn "So now, I'm going to bring out the animal inside you, and show you who you really are."
    "I begin thrusting myself up from the floor, slamming my cock deep inside her. It's a lot of effort, forcing her whole body weight up with every single stroke, but for Touko's sake, I'm going to put out everything I've got."
    touko "Ahh~ Too fast~"
    shinn "Heh... Not fast enough."
    "While all this was going on, Aina was watching from the sidelines."
    aina "Hmmph..."
    "Looks like she's pretty jealous that Touko's getting to have all the fun."
    aina "No fair~ Aina wants to play with Master too!"
    "Well, considering her good work, it'd be a shame to leave her out."
    shinn "Alright Aina, why don't you sit on my face so I can lick your pussy?"
    aina "Okay~"

    scene touko_aina__cg_5_ride 4
    "Aina hurries over and gets on top of me without hesitation."
    "She faces Aina as she rests her cushion-like ass against my face."

    scene touko_aina__cg_5_ride 5
    "Seems like all the time she's spent training her body for swimming has really paid off."
    thinking "Damn... If her ass was this soft, I should have tried this before."

    scene touko_aina__cg_5_ride 6
    "I stick out my tongue, running it over her pussy."
    aina "Ahh... Master's tongue is licking my pussy! You're sucking out all the juice from my pussy!"
    aina "Amazing! It feels so good!"

    scene touko_aina__cg_5_ride 7
    "Unable to resist the feeling of my tongue, Aina rocks her hips against me, grinding herself against my face."
    "Her butt feels so soft against me, I can't help but let her go at it."
    "It's like having a plush, warm pillow squashed against my face."
    "It's a special kind of bliss all on its own."
    "Meanwhile, Touko is rocking her hips against me as well like there's no tomorrow."
    "Seems like she's really getting into it now."
    "Their bodies are heating up as they get more and more wild and horny."
    "Even like this, the two of them still love each other, and they look at each other with hazy eyes as they bounce against me."
    "Seems like they're flashing back to all the dirty stuff they've done together."
    "It almost feels like their hearts and minds are being connected through me right now."
    
    scene touko_aina__cg_5_ride 8
    "They reach out for each others' hands, holding on tight, not needing to hide anything now."
    "Touko is the first one to speak out."
    touko "Aina, I love you!"
    "Aina follows suit"
    aina "I love you too, Touko!"

    scene touko_aina__cg_5_ride 9
    "Aina leans forward, moving her face in close and opening her mouth, inviting Touko in for a kiss."
    "As Touko follows her lead, the two of them lock mouths in an energetic and passionate kiss."
    touko "Mmm~"
    aina "Mmm~"

    scene touko_aina__cg_5_ride 10
    "The two of them let their saliva run into each other's mouths, drip down each other's faces, even dripping onto me underneath them."
    "Of course, I don't mind. I'm getting the most out of their love of anyone after all."
    "Touko pulls back first, and gazes at Aina with hearts in her eyes."
    touko "Whatever you do, Aina, I'll always be with you."
    aina "I feel the same way. I'm glad we can stay together like this."

    scene touko_aina__cg_5_ride 11
    "Looks like Touko doesn't care about the circumstances anymore. As long as Aina is with her, she's happy."
    "She's finally accepted the fact that the only way she can stay together with Aina is to give in and become my sex slave."
    "She's finally realized just how amazing my dick really is, and why Aina loves it so much."
    "She lets out an even louder moan as she grinds herself against me."
    touko "Ahh~"

    scene touko_aina__cg_5_ride 12
    "As she senses Touko enjoying herself more and more..."
    aina "Touko, Master's dick is amazing isn't it?"
    touko "Yeah..."
    aina "This is what we're meant for, Touko. Being Master's cumdump is the best!"
    aina "So let's do our best and give Master lots of love, okay?"
    touko "Ahh~"
    touko "Okay..."
    touko "Let's cum together and give him our love."
    "Aina gives her a bright smile back."
    aina "Hmm! Let's do that."
    thinking "Wait a minute..."
    thinking "How the hell did this turn into a lovey-dovey situation?"
    thinking "Pffft... Whatever. As long as it keeps going well for me, I'm fine with it."

    scene touko_aina__cg_5_ride 13
    "Both of them start to rock faster."
    "Their pussies are getting tighter, and it's getting harder and harder to get my tongue inside of Aina."
    touko "Ah~! Aina, I'm cumming~"
    aina "Me too! Let's cum together with Master!"
    touko "Yes! Let's all cum together!"
    touko "Ah~ Ah~ Ah~!"
    aina "Ah~ Ah! I'm cumming!"
    "A sudden squirt of juices gushes from their pussies as the two of them cum together."
    touko_aina "Ahh~"
    "I taste Aina's sweet pussy juice as it runs into my mouth and trickles out along my jaw."

    scene touko_aina__cg_5_ride 14 with cum_flash
    play sound cum2
    "Unable to resist the taste of the sweet high school girl on top of my, I finally cum, hard, into Touko's pussy."
    "My cum mixes together with Touko's own juices as they splash out."

    scene touko_aina__cg_5_ride 15 with cum_flash
    play sound cum1
    touko "Ah~ Master's cum!"
    "The whole space around us is a mess. My cum and their juices are mixed together in a puddle on the floor."
    "That was a hell of a good time. But for all I enjoyed myself, it was nothing compared to the number it did on Touko."
    "Just like Aina, she's completely mine now."
    "The two of them stand up and pull me to my feet."

    scene bg classroom with dissolve
    show touko naked at right
    show aina naked happy arms at left
    touko "Master~"
    shinn "Heh. Good girl. Looks like you get your purpose in life now."
    aina "Yeah, we get to have fun with master now! I'm so proud of you, Touko."
    aina "We're going to be together forever!"
    touko "Yes~"
    "I hand over a dog collar to Touko."
    shinn "Wear this, Touko. You can be just like Aina now."
    show touko naked collar
    "Touko wastes no time putting it on."
    aina "It's a perfect fit! And it looks just like mine!"
    touko "It does!"
    shinn "Alright, enough chatting. I have a mission for the both of you."
    aina "Master is giving us a mission? What is it?"
    thinking "Heheh. They have no idea."
    shinn "Well... Let me bring you to the gymnasium first, and you'll find out soon."
    touko_aina "Okay!"
    $ renpy.end_replay()
    $ persistent.touko_aina__cg_5 = True
    jump touko_aina__cg_6

label touko_aina__cg_6:
    play music gang fadeout 1.0 fadein 1.0
    scene bg gym with pixellate
    "It was a long and exciting walk. Since the two of them were following along behind me naked, we were flirting with the risk of getting caught the entire time."
    "Of course, at this hour, everyone has usually already gone home, but I have to count myself lucky that we didn't run into any last-minute surprises."
    "Of course, there are some people I already knew were still here today."
    "As we reach the entrance of the hall, I can already hear the chatter of a large number of boys' voices inside."
    shinn "Ah, looks like they've made it..."
    show touko naked collar at right
    show aina naked happy arms at left
    with moveinleft
    "I open the door, and show the girls the crowd I've assembled for them."
    "When the boys inside catch sight of Touko and Auna's faces, they immediately go wild."
    male_1 "Seriously? Aina and Touko? Fuck YES!"
    male_2 "Alright! I can't believe we're seriously gonna do this!"
    male_3 "Yes!! This is a dream come true!"
    "There's no way I can keep count of them all, but from the look of it, almost everybody showed up."
    "The guys here are all members of the school's sports clubs; baseball, football and so on."
    "Right now, the hall is filled with at least a hundred boys, almost the entire male athlete population of the school."
    "These guys have always had their eyes on the choicest girls in the school's sports clubs."
    "After having spent day after day watching these girls practice, their ability to control their hormones has already been taxed to the limit."
    "And in terms of stamina, these boys should be able to last all day."
    "The whole bunch of them have already gotten themselves ready ahead of time. They've been standing around in their underwear waiting for us."
    "To properly kick things off, I step forward to introduce the girls to the crowd."
    shinn "Gentlemen, welcome to tonight's fuck fest! I know you've been looking forward to this!"
    shinn "I've brought with me a couple of girls you've had your eyes on for a long time! You all know know them, and you all want them!"
    shinn "Let' give a warm welcome to the bright and cheerful Aina, and the tomboyish and sexy Touko!"
    "When they hear the girls' names, the crowd goes wild."
    male_1 "FUCK YEAH!"
    male_2 "ALRIGHT!"
    male_3 "WOOOOOOOO!!"
    "As the crowd gets a bit crazy, Touko and Aina start to draw back, looking unnerved."
    shinn "Getting a bit scared?"
    aina "Master... Why are all these people here?"
    shinn "Don't worry, love. These people are just here to have fun with you."
    touko "Really?"
    shinn "Yeah, I'm sure you'll love it."
    shinn "After all, they all came here to enjoy and appreciate your bodies just like I do."
    touko "Okay~"
    "Just hearing that from me is enough to alleviate the girls' worries, and I can see them start to relax."
    shinn "Come on, girls. Let's go."
    "As I lead them to the center of the crowd, the boys look on with hungry eyes. Some of them are actually drooling."
    "Down to the last one, I can see the obvious bulges protruding at the fronts of their underwear."
    shinn "Look at them all, Aina, Touko. You see how much they all love your lustful bodies?"
    "Aina gazes around at the crowd wth excitement, paying particular attention to the cocks that are going to be used on her soon."
    aina "Wow, there's so many!"
    "Touko, on the other hand, was overwhelmed by the sheer number of people lusting after her and Aina."
    touko "Wow..."
    "As Aina and Touko start to come to grips with the situation they've gotten involved with, I can see their bodies are starting to react."
    "Naked as they are, I can watch their pussies getting wet before my eyes."
    shinn "Heh. You girls are leaking already. Can't wait, eh?"
    touko_aina "Master~"
    "As they watch the girls chatting in front of them, the boys start to grow restless."
    male_1 "Oi, Shinn! When can we start? We can't wait anymore longer!"
    male_2 "Yeah! I want to fuck them now!"
    shinn "Calm down, you thirsty bastards."
    shinn "Now girls, remember, you're here to enjoy the wonders of men's dicks."
    shinn "Let them use whichever parts of your bodies they want, and they'll reward you with your favorite cum."
    aina "Okay~!"

    scene touko_aina__cg_6_group 1 with fade
    "I unhook the leashes from their collars and step away. Immediately, all the boys jump in."
    male_1 "Aina!"
    male_2 "Holy shit, check Touko out!"
    "All of the boys take off their underwear and look for whatever parts they can find free to take their pleasure from Aina and Touko."
    "As usual, Aina is the more daring and the more eager. As soon as the boys approach, Aina begins to embrace their attentions without any sign of hesitation."
    
    scene touko_aina__cg_6_group 2
    "One of the boys pushes her down and lifts up her legs, plowing her pussy against the floor. Aina immediately moans out in pleasure."
    aina "Ah~!"

    scene touko_aina__cg_6_group 3
    male_11 "Fuck, it's amazing! Her pussy's so tight and wet. Shinn must really have trained her for this!"
    "The boy gradually picks up the pace as he pounds her, forcing his dick all the way up against her womb."
    aina "Ah~! More, more~!"

    scene touko_aina__cg_6_group 4
    "Getting impatient watching Aina being fucked, more boys start to jump in for a piece of the action."
    male_1 "Ugh, Aina, please rub my dick!"

    scene touko_aina__cg_6_group 5
    aina "Sure!"

    scene touko_aina__cg_6_group 6
    "Aina happily complies and begins to stroke the boy's dick with her hand."
    male_2 "Aina! Me too!"
    "Aina takes the second boy's cock in her other hand, and starts jerking him off as well."

    scene touko_aina__cg_6_group 7
    aina "Ahh~ You boys' cocks are so hard and thick~!"

    scene touko_aina__cg_6_group 8
    male_3 "Oh, fuck, I can't wait anymore when she talks slutty like that!"

    scene touko_aina__cg_6_group 9
    "Upon hearing her, one of the boys kneels down close to Aina, and thrusts into her mouth."

    scene touko_aina__cg_6_group 10
    male_3 "Go on Aina! Take my sweaty cock in your mouth!"
    aina "Mmmph~!"

    scene touko_aina__cg_6_group 11
    "In no time, Aina was taking on boys' cocks in every way she could."
    male_3 "Aina's mouth-pussy is so good! It feels like my dick is melting inside her mouth!"
    male_4 "Unh! It's not just her mouth, her pussy is so tight, it's driving me crazy!"
    male_2 "Even her hands are amazing! It feels incredible. I can't believe Aina is such a slut!"
    male_3 "Nngh, it's like she's milking my cock with her tongue!"
    aina "Mmm~"
    aina "Hmm... Please give me more of your juicy cock!"
    male_3 "Sure thing!"
    "Not to miss out on the action, Touko quickly follows after Aina."
    "As she lay down, she was immediately pressed to the floor by a guy from the basketball team."
    male_5 "Yes! Touko's pussy! I've been dreaming about getting to do this since day one!"
    male_5 "I watch you practice every day, just looking makes me want to fuck you so bad!."
    male_5 "I always masturbate to you as soon as I get home!"
    "Seeing how much the boy loves her lusty body, Touko offers him her warm reassurance."
    touko "Its okay! Now you can enjoy my real slutty pussy as much as you want!"
    male_5 "Ah, I can't wait!"
    "The boy slowly lines up his dick with Touko's pussy, and starts to thrust into her."
    male_5 "Ah! Touko's pussy! It's like I've been waiting my whole life for this! It's so tight and wet, it's just incredible!"
    "Another of the boys quickly jumps in for a request."
    male_6 "Ah, Touko! Please rub my dick with your hand!"
    touko "Hm? Ah, sure..."

    scene touko_aina__cg_6_group 12
    "Touko uses her hand to slowly stroke his dick, and soon another boy is clamoring to get at her other hand.."
    male_7 "Me too, Touko! Please!"
    touko "Okay~"

    scene touko_aina__cg_6_group 13
    "Touko slowly strokes away at both of the boys' dicks."
    touko "Ah~ So big..."
    male_6 "Fuck, Touko's hands are so soft! It feels so good!"
    male_7 "Yeah!"
    male_8 "Heh... Look at you two. I didn't know the two of you were such dirty girls."
    male_9 "Yeah. Holy shit, I'm so glad I came. This is a once in a lifetime opportunity!"
    male_4 "Hey, why don't we all try to cum together and blow their minds in one go?"
    male_1 "Yeah! Let's do that!"

    scene touko_aina__cg_6_group 14
    "The boys start to pick up the pace, their movements becoming even more aggressive."
    "Aina and Touko start stroking the boys' dicks even faster to keep up, anticipating the incoming cum shower."
    touko "Mmm... Your dicks all feel so good! Please give me all of your cum!"
    touko "Shower me with your hot and tasty cum!"
    male_5 "Yeah! You're gonna get all of it! Make sure take down every single drop!"
    touko "Ahh~!"
    "Meanwhile, the boys fucking Aina are also reaching their limits."
    male_1 "Aina! I can't take it any more! I'm gonna cum!"
    aina "Mmmph!"
    male_4 "Me too! Go on and take it Aina!"
    aina "Ahh~! Yes, I want it! Come on and give me every drop of your seed!"
    touko "Please~!"

    scene touko_aina__cg_6_group 15 with cum_flash
    play sound cum2
    "Almost in unison, the boys cum, shooting out inside and over Aina and Touko's bodies from every angle."

    scene touko_aina__cg_6_group 16 with cum_flash
    play sound cum1
    "The bunch of them together leave the girls completely drenched with their cum."
    "Looks like some of it even got into their mouths."

    scene touko_aina__cg_6_group 17
    "The taste, the smell, and the sticky feeling all over their skin seems to drive the girls crazy."

    scene touko_aina__cg_6_group 18 with cum_flash
    play sound cum2
    "These girls are already absolutely addicted to cum. It's like a drug to them now."

    scene touko_aina__cg_6_group 19
    aina "Ah... There's so much cum and it smells so good! I'm going crazy!"
    touko "Mmm~ Tastes so good!"
    aina "Please give us more!"
    male_1 "Heh, no worries. There's plenty more to come."
    male_2 "This is far from over, ladies, so make sure you're ready for it all!"

    scene touko_aina__cg_6_group 20
    touko_aina "Sure! ~"
    "I stand back and watch as the boys form a train on them."
    "The boys keep on going, one group after another."
    "By now I think we're up to around... round fifteen?"

    scene touko_aina__cg_6_used 1 with fade
    "The girls' pussies are overflowing with cum, and there are tally marks scrawled across their thighs keeping track of how many times they've been used."
    male_11 "Wow. So Aina's taken it in the pussy 45 times now!"
    male_12 "Heh, then Touko's ahead. 60 times!"
    male_11 "And from the look on their faces, both of them still want more!"
    "Traces of the boys' pubic hair are clinging to the girls around their mouths and hips."
    "The boys must have been going at it pretty hard."
    "Aina and Touko look pretty worn out, but at the same time, it looks like they're still thoughly enjoying themselves."
    "By now, it looks like Touko doesn't have the slightest regret following after Aina."
    "She couldn't be happier to be doing this together with her."
    "Touko crawls towards Aina, with cum still leaking from her pussy."
    male_8 "Hey, where are you going?"
    "Touko makes her way across the floor to Aina, and stops in front of her."
    aina "Hmm? Touko?"
    "Touko pulls Aina into a passionate kiss."
    aina "Mmph!?"
    touko "Aina, I love you."
    touko "Thank you for everything."
    touko "You helped show me the real me. I want to keep doing this forever with you."
    "Aina smiles back at Touko,"
    aina "Me too. I love you, Touko."
    aina "So, let's stay as cumdump sex slaves together forever, okay?"
    touko "Okay!"
    male_2 "Aw, look at them. They're having a lovey-dovey moment in the middle of all this."
    male_1 "Well, isn't that cute?"
    "Not paying attention to the boys' words, Aina and Touko continue kissing each other, tangling their tongues in each other's mouths."
    aina "Mmm..."
    touko "Mmm..."
    "The sudden plunge into full on lesbian action catches the boys off guard."
    "As they take in the sight in front of them, the boys' enthusiasm ramps up even further."
    male_3 "Hey, what's this?"
    male_4 "They just started kissing each other."
    male_2 "Fuck, it's making me hard all over again!"
    male_1 "Hey, why don't we make their love even more fulfilling with our cum?"
    male_6 "Fuck yeah, let's do it! I've still got another round in me for that!"
    "The boys gather and begin to jerk off around Aina and Touko."

    scene touko_aina__cg_6_used 2
    "A couple of enterprising boys take up position behind the two of them, mounting them doggy style."

    scene touko_aina__cg_6_used 5
    "With the boys around them egging them on, Aina and Touko's kiss becomes even more lustful, drawing in the crowd even more."

    scene touko_aina__cg_6_used 7
    "The two of them are completely lost in the moment, kissing each other as they're getting fucked from behind."

    scene touko_aina__cg_6_used 10
    "The boys around them are jerking off frantically, preparing to shower them with their cum."
    aina "Mmm~"
    touko "Mmph~!"
    "Even over the sound of the boys around them, I can hear the two of them moaning into each other's mouths as they're railed by the boys behind them."
    "It looks as if the guys are about to reach their limits."
    male_1 "Oh fuck, she's squeezing so hard, I can't hold it!"
    male_2 "Me too! I'm gonna cum!"

    scene touko_aina__cg_6_used 9
    "The boys pound into the girls even harder as they approach their finish."
    male_1 "Here it comes!"

    scene touko_aina__cg_6_used 11 with cum_flash
    play sound cum2
    "Together at once, both the boys shoot their cum out deep into Aina and Touko's wombs."

    scene touko_aina__cg_6_used 12 with cum_flash
    play sound cum1
    male_1_2 "UGH!"

    scene touko_aina__cg_6_used 13 with cum_flash
    play sound cum2
    aina "Ah~!"
    touko "Mmm~!"
    "The boys pull out, leaving a flood of cum gushing out of Touko and Aina's pussies."
    male_3 "MY TURN!"
    "But that doesn't stop the rest of the boys. There are still plenty of boys lining up behind who're far from spent, waiting their turns for the two."
    male_4 "Yeah! Go on and take my cum, Aina! Get pregnant!"
    aina "Ah~! You guys..."
    "Aina and Touko look like they're in heaven right now. Their eyes are rolling back in their heads, overwhelmed by the pleasure."
    aina "Ahh! That felt so good!"
    touko "I love it!"
    male_5 "Ah, me too! Aina, please take my cum!"
    "Some of the boys are too impatient to wait. They take aim at Aina and Touko's bodies as they jerk off around them, showering the two with their cum."
    aina "Ah, so much cum! I love it!"
    "The two of them are completely drenched, so much that the smell of cum overpowers the entire gym."
    "The boys keep up a train on them, providing the girls with a buffet of their cum."
    
    scene touko_aina__cg_6_used 14 with cum_flash
    play sound cum2
    "By now, Aina and Touko's stomachs are bulging with the tremendous amount of cum they've taken inside them."
    "The two of them look like they're pregnant. Although, considering everything they've been through tonight, it wouldn't be at all surprising if they really are now."
    "As the latest round of boys releases their load, they start to show signs of exhaustion."
    "This might be the end of the session, it seems like the boys may finally be tapped out."
    "I move in to check on Aina and Touko."
    shinn "So, how are my girls doing?"
    aina "Ah, Master, you're here! I love it! I want more dicks inside! I want to keep this up all the time!"
    touko "Me too!"
    "I give them a smile."
    shinn "That's good. Do you want to take a rest before you keep going?"
    aina "Ah! No, Master, I want more! I don't need to rest!"
    touko "Yes! I don't want to stop tasting cock, Master ~!"
    "Heh, seems like they're still having fun after all. Good."
    shinn "Hmm... What about the boys? Can you guys continue?"
    male_1 "Are you kidding me? I've still got some left in me."
    male_2 "I'm not dried up yet! I'm not going anywhere until they've taken down the last drop!"
    male_3 "We'll keep this up even if it means we're here all night!"
    shinn "Alright, let's keep this going all night then!"

    scene black with fade
    "One thing is for sure; these girls have found their true destiny."
    $ renpy.end_replay()
    $ persistent.touko_aina__cg_6 = True
    $ gym_available = False
    "END OF TOUKO AND AINA ARC"
    play music campus fadeout 1.0 fadein 1.0
    jump map__school

# *touko_aina Arc End*