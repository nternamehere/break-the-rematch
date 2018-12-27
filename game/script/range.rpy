label range__router:
    if range__first_visit:
        jump range__first_visit
    else:
        jump map__school

label range__first_visit:
    show bg range with map_fade

    "..."
    "..."
    shinn "{i}This place feels alive, that's for sure{/i}"
    "In the two years since I graduated, the archery club seemed to have grown a good deal. I remembered it only having a dozen members."
    "Now the dojo was filled with students, most of whom happened to be female."
    shinn "...oh?"
    "The continuous sound of a bow being drawn and released finally drew my attention to the sole figure actually shooting."
    "The gathered students seemed focused on her as well. Some were solemn, focused on her movements, whereas others, their eyes wide, clearly admired the girl."
    "Curiously, I stepped closer, trying to keep from attracting too much attention."

    show satsuki archery with dissolve
    shinn "{i}Oh, wow.{/i}"
    "I focused on the beautiful young woman. Her dark raven hair, tied in a traditional manner, flowed over her shoulder. The pins embedded in her braid gave her a certain old-fashioned air, yet the effect this played with the rest of her appearance released an impossible-to-ignore beauty."
    "Her expression was serious and cold, and she had eyes only for her target."
    "Without any effort at all she drew the bow and released her shot. The arrow arced perfectly into the center of a target 60 meters away."
    "The students immediately burst into cheers and applause."
    female_1 "As expected from Miss Katsuragi! She isn't our most valuable club member for nothing!"
    female_2 "She's so beautiful... I wish I was as good as Miss Katsuragi!"
    male "With her at our head, we'll win regionals again for sure!"
    shinn "{i}So she's the start of the archery club. Quite popular with the students, too.{/i}"
    shinn "{i}It's no question why everyone idolizes her so much - she's from the prestigious Katsuragi clan.{/i}"
    "I took a closer look at the girl, my eyes straying to follow the supple curves of her breasts."
    shinn "{i}Very high class. She's worthy to be one of my interests.{/i}"
    "Katsuragi turned, unsmiling, to look at the small audience of students, who continued to cheer and praise her. She was like an idol."

    scene bg range
    show satsuki cocky
    with dissolve
    "I slowly noticed that Katsuragi's eyes were fixed on me. I couldn't read her expression, whether it radiated simple curiosity or condescension."
    "The other students followered her gaze. Soon, everyone was aware of my presence."
    shinn "{i}This might be inconvenient.{/i}"
    "I fought the urge to hesitate, keeping my cool, and approached Satsuki."
    "Although she was clearly younger than me, she really did have an aura of maturity. As if she were a woman ready for marriage."
    shinn "Good evening, Miss Katsuragi."
    satsuki "..."
    shinn "{i}Talk about a cold shoulder.{/i}"
    "Satsuki stood composed, glaring at me with cold eyes."
    "That was interesting. Most girls would have been startled by my sudden presence."
    "But I supposed that club members, especially their star members, had a tendency to be territorial. Perhaps it didn't matter who I was, just taht I was there at all. A tresspasser."
    shinn "My apologies, Miss Katsuragi, I'm Shinn Akatsuki. I was assigned to be your tutor."
    "She tilted her head to the side, as if perplexed, but said nothing."
    shinn "{i}This is becoming tiresome.{/i}"
    shinn "Is there a chance for us to talk? That is, if you're not busy."
    "Her lips twitched, forming a concerned forwn."
    satsuki "What is it you wish to discuss, Mr. Akatsuki?"
    shinn "{i}I have to play this smoothly. Don't screw up.{/i}"
    "I took a deep breath and put on my most dashing smile."
    shinn "Merely your grades in mathematics. I've come on request from the principal."
    satsuki "I see."
    "The young woman's calmness seemed to resonate with everyone in the dojo - including me."
    satsuki "So you are the one our director told us about."
    shinn "I see my reputation precedes me."
    satsuki "Perhaps. I don not really see the need for such measures, but if he insists..."

    show satsuki defeated
    satsuki "I should have expected this. Club activities take up so much time..."
    shinn "Ah, but it's not out of the ordinary to take some time off for studying."
    shinn "Besides, if you fail your classes, you'd have to give up your club activities anyway, no?"
    "She stared back at me. I had expected her to be startled, but instead her narrow gaze revealed annoyance."
    satsuki "Listen - we have regionals very soon. I'm putting all of my effort into them."
    shinn "Indeed, but wouldn't it be more favorable for you, your team, and the Academy if you were to excel in your academics as well?"
    "Satsuki was silent once more, visibly pondering the very simple logic I had laid out before her."
    shinn "{i}She's either dense or trying to play me off.{/i}"
    shinn "{i}I might have to be more forceful with her if she gets too troublesome.{/i}"
    satsuki "Can you promise that my club activities will not be interrupted by our studying?"
    "I smirked back at her, trying to control myself."
    shinn "Of course not. Everything's been considered."

    show satsuki neutral smile
    satsuki "Very well."
    satsuki "Can I expect you to get in touch with me soon?"
    shinn "Of course, the principal gave me your contact information. I'm looking forward to it!"
    "Continuing to smile, I bowed my head as a gesture of respect."
    shinn "I shall leave you to continue your activities then, Miss Katsuragi. Have a good day."
    satsuki "Likewise, Mr. Atkatsuki."
    "With a single nod, Satsuki returned her focus to the range."
    hide satsuki neutral smile
    shinn "{i}That took longer than expected...{/i}"
    "But it was quite worth it. I'd met the school's archery start, and she happened to be a complete babe. I mentally planned to \"check in\" with her very soon."
    shinn "{i}Hmm... Who should I see next?{/i}"
    $ range_available = False
    $ range__first_visit = False
    jump classroom__completed_intro_check
