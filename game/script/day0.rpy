label day0_start:
    play sound alarm_loop loop
    unknown "Hmm..."
    "An incessant ringing pestered my ears as I lifted my head from the soft bedsheets and pillows."
    unknown "Hmm..."
    "I had been having the most comfortable, enjoyable dream... but now it was gone, swept away by this annoying alarm."
    unknown "Hm...what time is it...?"

    show bg shinn bedroom with pixellate
    "I looked above the sheets,  the old digital clock's red numbers seemingly staring back at me, demanding that I rise. The blurriness of sleep slowly began to fade as I stared at the time."
    unknown "Oh... It's already 6 AM. I should get going."
    "The alarm clock continued to ring."
    unknown "Alright, alright, I'm going! Damn, this thing is loud...."
    stop sound
    play sound alarm_shutoff
    "My clock kept ringing for some time before I mustered the will to turn it off. As I rose, I noticed a blinking light on my answering machine."
    unknown "Hm? Who could this be?"
    "I approached the machine and hit the \"play message\" button"
    voicemail "Mr. Akatsuki Shinn, all the paperwork is now organized and we're ready for you to start."
    voicemail "I need you to come in today after classes have concluded. Club activities begin at 3:45 pm, which should give you plenty of time to arrive."
    thinking "Oh, that's great."
    thinking "Heh. Looks like I didn't need to get up so early after all. But since I am already awake, I might as well get prepared now."
    "I began preparations for my first day of tutoring."
    jump school__first_visit

label school__eod_0:
    scene bg main gate with fade
    stop music fadeout 1.0
    shinn "Ah. What a day!"
    thinking "Never would have expected that my first victim would be Naoko. I'm off to a great start."
    "I took out my list and began to check through each girl's profile one last time."
    shinn "Let's see how the hit list's looking."

    show araki basic with quick_fade
    thinking "There's the sporty Araki Shinjugai, with a body that is petite and tight. Utterly enticing."

    hide araki basic
    show touko basic
    with quick_fade
    thinking "We have the beautiful Touko Takatsukasa. her mere gaze is quite stunning, and she packs some delicious curves in that athletic body of hers."

    hide touko basic
    show aina basic
    with quick_fade
    thinking "Then there's Aina... that bubbly, cute nature of hers is very endearing. I cannot wait to turn her into an utter degenerate."

    hide aina basic
    show satsuki neutral smile
    with quick_fade
    thinking "Ah, Satsuki Katsuragi. A traditional maiden and an archery star, no less! Imagine breaking her to such a point that she no longer cares about her very family name."

    hide satsuki neutral smile
    show ritsuko_tennis
    with quick_fade
    thinking "And, of course, there's Ritsuko."
    "I shuddered at the very memory of her."
    thinking "I'll have to be careful with her, though there's no doubt I'll have to turn her into a cumdump as well. There are special methods for her type."

    hide ritsuko_tennis
    show rina confident
    with quick_fade
    thinking "And last,. Ms. Rina Akiyama. She will be the next teacher to be my victim."
    thinking "I really had no plans to go after teachers this season, but after what happened with Naoko today, and considering Rina's, plumpo, irresistible hips, there's nothing wrong with having a token adult in the line-up."

    hide rina confident with quick_fade
    "As I turned to look back at the school, I felt a grin slide across my face."
    thinking "Now... let this breaking season commence."
    "Rubbing my hands in excitement, I began my trip home, already planning for tomorrow."
    jump day1_start
