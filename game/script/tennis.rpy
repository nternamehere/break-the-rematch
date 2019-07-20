label tennis__router:
    if day == 1:
        jump tennis_day_1
    if tennis__first_visit:
        jump tennis__first_visit
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
    shinn "Heh. \"Things that I did with teachers\"? These are rumors, Ritsuko. Not surprising that you don't know the difference between hearsay and facts."
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
    jump map__school

label tennis_day_1:
    scene bg hallway 1 with map_fade
    "I came in to school way earlier than I needed to. Since I got such an early start this morning, I decided it was better to make an early appearance than stay around and kill time at home."
    "Not that I get credit for being early, but a little extra time to check out the students never hurts."
    "I walk towards the staff room to get some materials done for the tutoring this afternoon."
    "As I reach the entrance to the staff room, the door suddenly swings open right in front of me."
    show ritsuko with moveinright
    ritsuko "Oh?"
    "Definitely not who I was hoping to run into this early in the morning."
    ritsuko "What do we have here?"
    "Ritsuko gives me her usual disgusted-looking smirk."
    shinn "Good morning, Ritsuko. How are you doing?"
    ritsuko "How polite. Well, I’m doing just fine."
    shinn "Great. Don’t forget about our session later this afternoon."
    show ritsuko brow
    ritsuko "Oh. Session?"
    "Ritsuko pauses for a moment."
    ritsuko "Ah! Yes, I remember now..."
    show ritsuko -brow
    thinking "This idiot..."
    shinn "You are coming in, right?"
    ritsuko "Of course. I just hope you keep your hands to yourself."
    shinn "What?"
    ritsuko "Ho ho ho~ "
    ritsuko "Oh, nothing, don’t mind me. Anyway, see you later!"
    hide ritsuko with moveoutleft
    "Ritsuko walks away."
    thinking "That little bitch. I’m seriously going to punish her."
    "But for all that she’s such a snob, she can actually be pretty clever."
    "It’s no wonder she almost managed to catch me back then."
    thinking "Seems like I need to go the extra mile for this girl."

    scene bg classroom with dissolve
    "I came in early this time around to prepare for the lesson."
    "I keep thinking to myself about how I’m going to deal with her."
    "But before I’ve managed to come up with anything, Ritsuko enters the class."
    show ritsuko with moveinright
    thinking "Wow, She’s early."
    "She seems to notice my look of surprise as I see her."
    show ritsuko brow smile
    ritsuko "Oh? Why so startled? Did you not expect me to turn up?"
    shinn "It’s not that. It’s just that I didn’t expect you to be this early."
    ritsuko "Hmmph. How rude. A truly elegant lady is never late!"
    shinn "Truly elegant my ass..."
    ritsuko "What? What did you say?"
    shinn "Oh, nothing. Take a seat."
    ritsuko "Before that, I just want to confirm that you won’t be getting up to anything else while we’re here?"
    shinn "Huh? What else would I be doing other than teaching you math?"
    ritsuko "I mean, the sort of thing you did back then."
    shinn "What sort?"
    show ritsuko -brow -smile
    "Ritsuko narrows her eyes."
    ritsuko "You know. Those things you did in the storeroom."
    "I glare at Ritsuko in frustration."
    shinn "Alright, you know what? Let’s clear the air."
    shinn "What sort of things did I do back then in the storeroom?"
    ritsuko "Well, You know..."
    "I get more and more pissed off the more I have to deal with her shitty attitude."
    shinn "Say it!"
    ritsuko "S- Sex?"
    thinking "No surprise that she’s embarrassed even to say it."
    shinn "How do you know if it was sex?"
    "Ritsuko’s face was red with embarrassment."
    ritsuko "Well, stop asking me about how I know! I just know, okay!"
    shinn "Is that so? What evidence do you have then?"
    ritsuko "..."
    shinn "Exactly. Now shut up and let’s get this lesson moving. The more you put things off, the later you’ll be going home."
    ritsuko "Fine..."
    "We manage to get through the lesson without any further disruption. It’s a minor miracle that Ritsuko even manages to pay attention to the coursework."
    "As the sun sets, she finishes the last remaining problem set, and I decide to call it a day."
    shinn "Alright, that’s enough for now."
    ritsuko "Finally. What a waste of time."
    thinking "This bitch really deserves a punch in the face."
    ritsuko "So, can I go now?"
    shinn "Not yet. Give me a minute."
    ritsuko "Hurry up, I want to go home!"
    "I walk up to her and hand over some practice questions."
    ritsuko "What? What is this? I don’t have time for these."
    shinn "Too bad. Do it tonight and hand it in tomorrow."
    ritsuko "Fine. I shall take my leave then. See you tomorrow."
    hide ritsuko
    "Ritsuko stands up and leaves the class."
    thinking "Ugh. What a horrible student..."
    thinking "I wonder how on earth she manages to make friends in school with such an arrogant attitude."
    thinking "She’s probably never had a boyfriend."
    thinking "Heh. No wonder she was so embarrassed saying the word “sex” in front of a guy."
    thinking "You can be pretty sure that one’s a virgin."
    thinking "Which means breaking her is even going to be more fun."
    "I let out a sinister laugh.  "
    shinn "Tomorrow should be a fun day."

    scene black with fade
    "It’s getting close to lunchtime."
    shinn "Maybe I should grab something to eat before the cafeteria is full of students."
    "I get up and leave the staff room."

    scene bg hallway 1 with dissolve
    "I head towards the cafeteria thinking about what I shold get to eat."
    "As I walk, I notice Ritsuko in the distance."
    thinking "Oh, it’s her. Aren’t there lessons going on right now? What’s she doing here?"
    "From the look of it, she seems to be sneaking around."
    thinking "What is she doing?"
    "Curious, I decide to follow her and check it out."
    "I tail her until she finally comes to a stop outside the Principal’s office."
    thinking "Huh? What’s she doing here?"
    thinking "Hang on a minute. Is she here to tell on me?!"
    "She knocks on the door, and I can hear a familiar voice from inside the office."
    principal "Come in."
    "Rina enters the office shuts the door behind her."
    thinking "If she’s going to expose me, I’d better step in to interrupt the conversation."
    thinking "Not that that things are likely to turn out so great in that case."
    thinking "But I might not have any other options."
    "I move in close to the door to listen from the outside."
    jump ritsuko_sex_scene_1

label tennis_day_1_continued:
    scene bg hallway 1 with irisout
    "Moments after Ritsuko left, I decided to see the principal."
    thinking "Hopefully, this will work out."
    "I knocked on the doors of the principal office."
    principal "Who’s that?"
    shinn "Its me. Shinn."
    principal "Ah Shinn! Come in."

    scene bg principal office with fade
    "I entered the principal office and was greeted by the principal."
    principal " Hello Shinn. What can I do for you?    "
    thinking "Hmm... Maybe I should get straight to the point..."
    shinn "I saw what you did to Ritsuko just now."
    "The principal stops whatever he is doing and look at me in the face."
    principal "Is that so?"
    shinn "Yes. But I am not going to expose you or anything."
    principal "Then why are you telling me this?"
    shinn "I wanted to make a deal, so that both of us could benefit."
    principal "Hmm... What do you mean by this?"
    shinn "I know the principal wants to do Ritsuko a lot given her amazing body."
    shinn "And to be frank, so is everybody else including me."
    principal "Exactly, and why do I want to share this girl with you?"
    shinn "I can effectively train her to be your pet slave just like back in the old days."
    principal "So, the rumors about you screwing around our teachers back then is true..."
    shinn "I believe you had heard about my adventure back then."
    principal "There were rumors from what I heard, which is why I was being replaced by the previous principal here."
    principal "I just didn’t know its true until you tell me."
    principal "So, it is you after all..."
    shinn "Well. What do you say?"
    principal "Hmm... Pet slave, huh? I only intend to use Ritsuko as some sort of a secret love affair."
    principal "I never thought I could get him to become my sex slave."
    shinn "I could do just that for you."
    principal "And how do you propose you could do just that?"
    shinn "I just need copies of those photos that you used to blackmail Ritsuko."
    principal "Hmm... But I promise her not to expose any further."
    shinn "Come on... Let’s be honest, do you really think you were going to keep that promise?"
    principal "Well... Not really..."
    shinn "Besides, its just you and me. Nobody else will know about this."
    "The principal took out the photos from his desk drawer and placed it on her desk."
    principal "We have a deal."
    "I approached the desk to grab the photos."
    shinn "Thank you and I will let you know the progress soon."
    shinn "She is going to be your pet in no time."
    principal "Heh... Can’t wait."
    shinn "Well then, I shall get going."
    principal "Okay. See you soon."
    "I left the principal office with joy."
    thinking "Heh... This is going to make my life so much easier now."
    thinking "Can’t wait to fuck a rich girl with well-developed body."
    $ tennis_available = False
    jump map__school