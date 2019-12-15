label xmasST_start:
    define audio.lawrence1 = "xmasST_bgm_Merry_Christmas_Mr_Lawrence_1"
    define audio.lawrence2 = "xmasST_bgm_Merry_Christmas_Mr_Lawrence_2"

label xmasST_chapter_select:
    menu:
        "This scenario contains multiple chapters. They progress in chronological order. Finishing one chapter leads back to this choice. Which chapter would you like to start?"
        "Chapter 1 - A Christmas Transfer (2018)":
            jump xmasST_chapter_1
        "Chapter 2 - The Bipolar Express (2019)":
            jump xmasST_chapter_2

label xmasST_chapter_1:
    pause 3
    play sound sfx_knock
    sandra "Get up, you sack of lazy beans!"

    think "Is it really already time to get up again...?"

    john "Alright alright, I'm getting up."

    sandra "Get up faster! You've told me plenty of times you don't want to be the victim of Yui's wrath."

    think "And right she is."

    "This was the motivation and the reminder I needed to move my body up from the bed."

    outfit john casual
    scene bg main room day
    show john a_0 at Position(pos=(0.80, 1.5), anchor=(0.5, 1.0)), faceleft
    with dissolve
    play music xmasST_bgm_we_wish_you fadein 3
    show john at Position(pos=(0.80, 1.0), anchor=(0.5, 1.0)) with ease
    "Well, you probably know me by now. In case you don't, I wonder what you're doing here."

    "It's the day before christmas. Of course this year just had to end up having christmas on a saturday, so we would still need to attend school for today."

    "Christmas was something I looked forward to a lot each year. Especially this year, where we would be getting a few guests for once."

    "Usually christmas at home was kind of... boring, if you can call it that. It was usually just me, Holly, mom and d̉͒͝ȁḏ͕̻̱͕̻́͌̔̐̈̔̓͒͌̔̐͌̔̐̈̔̓͒͌̔̐͌̔̐̈̔̓͒͠͝͠͝͠͝unknowncharacteṟ͕̻̱͕̻̱͕̻̱͕̻̱͕̻̱͕̻̓͒̓͒̓͒̓͒̓͒̓͒͝͝͝͝͝͝{nw}"

    "Usually christmas at home was kind of... boring, if you can call it that. It was usually just me, Holly and mom."

    "So that was a thing."

    show john a_2
    sandra "Are you monologuing again?"

    john "Oh, shoot. Right. Sorry."

    scene bg main house day
    outfit john uniform
    show john a_0 at center
    with wipecircle
    "While I was rushing out of the house, naturally, that person came to see me."

    show john a_2
    show carrie a_2 at offscreenright, faceleft behind john
    show carrie at centerright with ease
    carrie "John! You're going to school 37 seconds later than usual!"

    show john a_5
    think "Wait, what?"

    carrie "Did something happen at home? Are you ok?"

    john "C- Carrie, why do you know that?"

    show carrie a_0
    carrie "I always make sure to know if something could be wrong. If anything happens, please tell me. Alright?"

    john "Uh... Sure, I guess?"

    show john a_6
    john "I just overslept, you know?"

    show carrie a_6
    carrie "You mean... You couldn't sleep because someone happened to be outside your window making noise this night?"

    show carrie a_4
    pause 1
    show john a_2
    john "...No?"

    john "What are you talking about?"

    show carrie a_3
    carrie "Phew..."

    show carrie a_0
    carrie "Nothing. I am glad that nothing is wrong then."

    show john a_6
    john "Anyways, bye, was uh... nice talking to you."

    carrie "Yes. Yes it was. Merry christmas, my love."

    show john a_5
    "That stalker still managed to make every single word she said creepy."

    show john:
        ease 1 xpos 1.3
    show carrie:
        pause 0.2
        faceright
    "I just ran pretending not to hear that last part. I really hoped she wouldn't appear in some dream of mine anytime soon."
    stop music fadeout 1
    pause 0.75

    play music xmasST_bgm_up_on_a_housetop
    accessory kiyoshi set glasses
    scene bg school entrance day
    show john a_0 at center
    show kiyoshi a_5 at offscreenright, faceleft
    with wipeleft
    show kiyoshi at offscreenright:
        ease 1 xpos 0.65
    "As I arrived at Tina Koya High, it seemed that Kiyoshi was in the same pickle as me."

    show kiyoshi at Position(pos=(0.78, 1.0), anchor=(0.5, 1.0))
    kiyoshi "Huff... J-man... huff..."

    "And he was extremely exhausted."

    show kiyoshi a_3
    kiyoshi "How... huff... is it hanging?...?"

    show john a_6
    john "You should really do some sports."

    show kiyoshi a_2
    kiyoshi "I already do!"

    show kiyoshi a_5
    "He took another, albeit long, moment to catch his breath and finally felt a bit more focussed."

    scene bg school hallway day
    show john a_0 at centerright, faceright
    show kiyoshi a_1 at center, faceright
    with wipeclock
    "As we were walking towards our classroom, Kiyoshi kept talking."

    kiyoshi "You know it well J-man. I perform cyber- and mind-sports each day."

    show kiyoshi a_5
    kiyoshi "And by Xenu do I need to get myself a bike!"

    show kiyoshi a_0
    show john a_6
    john "You haven't asked for one as a present?"

    show kiyoshi a_2
    kiyoshi "How could I when I am already requesting a model spaceship?"

    show john a_2
    john "You want a spaceship for christmas?"

    show kiyoshi a_1
    kiyoshi "Who wouldn't want a spaceship for christmas. If you've been a succesful guy during your entire year, then Santa will reward you handsomely. I cannot waste my succes on a bike."

    john "You don't seriously still believe in Santa, right?"

    kiyoshi "I have multiple theories that surround this conundrumous man."

    show kiyoshi a_0
    kiyoshi "Is he a cybernetically engineered super-human created by the government to reward those who follow the system?"

    kiyoshi "Or is he perhaps a phantom who haunts the world to feed of the goodwill of the common human once a year?"

    show kiyoshi a_4
    kiyoshi "None can truly know, J-man. None can truly know."

    show john a_6
    john "Yeah, I think you have a few more screws lose today than usual. I thought we agreed to stop believing that ten years ago."

    show gabriel a_11 at offscreenleft
    show kiyoshi a_2
    "He laughed it off, but knowing him, he probably still meant it seriously."

    hide john
    hide kiyoshi
    with dissolve
    show gabriel at left with ease
    pause 1.5
    show gabriel a_10
    pause 2

    scene bg school classroom hallway day open
    show john a_0 at center, faceright
    show kiyoshi a_1 at centerleft, faceright
    show yui a_3 at centerright, faceleft
    with sawright
    "Of course, the ever so diligent Yui was waiting for us."

    "This was the third time this week that I arrived last minute."

    show yui a_2
    show kiyoshi a_0
    show john a_2
    yui "John! Kiyoshi! Have you learned nothing?"

    show yui a_3
    john "Yeah yeah, we're sorry that we almost made it."

    show yui a_2
    yui "You wouldn't last a minute in the real world with this tardines."

    show john a_5
    show yui a_3
    "Always taking it to the extreme."

    show john a_17
    "But I had a backup plan this time."

    show john a_6
    john "I am looking forward to seeing you guys this evening. Remember to bring the duck."

    show yui a_1
    yui "Of course. And we are all really looking forward to spending christmas with yo-"

    show yui a_2
    show kiyoshi a_4
    yui "Wait, are you trying to distract me?"

    show john a_1
    john "It's usually really boring with just my family. So spending the evening with you and the other girls is sure going to be cozy."

    show yui a_0
    show john a_0
    yui "It's usually rather plain at home as well."

    show yui a_6
    yui "Wait, what were we talking about?"

    show kiyoshi a_1
    john "Oh, nothing."

    "If this were a game, this would have been a perfect score."

    john "We're just gonna go to our seats."

    yui "Uh, sure."

    hide john
    hide kiyoshi
    hide yui
    with dissolve
    show gabriel a_6 at offscreenleft
    "Yui didn't cause any ruckus. Thank god."

    show gabriel at left with ease
    pause 1
    show gabriel a_17
    pause 1.5

    scene bg classroom 2
    with wiperadial_horiz
    "While we were getting to our seats, Kiyoshi whispered to me."

    kiyoshi "You truly managed to cause the almighty Yui to lose her train of thought."

    kiyoshi "Amazing."

    john "I've been getting better at it lately, but this one was a walk in the ballpark."

    "Now just to survive another day with these boring lectures so I could get home."

    scene black with dissolve
    "Luckily for the viewer of this playthrough, they wouldn't have to endure the same monotone day as me."

    scene bg school entrance day
    show john a_1 at center, faceright
    with diamonds
    pause 1
    show john a_0 at center, faceleft
    "When school was finally over, I said my {q}see ya's{/q} to my friends. All of them had family coming over."

    "My family wasn't fortunate enough to be very connected, so my mom had the idea to invite Yuuna and her two daughters over this time."

    show gabriel a_10 at offscreenleft
    "It sounded like a good idea, so why not?"

    stop music fadeout 1.5
    pause 1
    show gabriel at centerleft with ease
    play music xmasST_bgm_oh_holy_night
    show john a_5
    "But before I could start getting home, someone stopped me just as I was about to leave the school premises."

    gabriel "Wait up."

    john "Huh? What is it?"

    "The guy looked like he was going to the same school as me from the uniform... But I had never really seen him before."

    show gabriel a_17
    gabriel "So, you think christmas is all bad, huh?"

    show john a_2
    john "What? No I do-"

    show gabriel a_15
    gabriel "You are a terrible human being. You will end up cold and alone if you continue at this rate."

    show john a_5
    john "Wh... What? Hold up, what are you talki-"

    show gabriel a_4
    gabriel "This night. You will be visited by the three spirits of christmas this very night. And I pray that you will come out a changed man."

    stop music fadeout 3
    show gabriel:
        faceleft
        ease 1 xpos -0.2
    "After that, he just left while laughing to himself."

    think "...What the hell was that about?"

    "It was bizarre to just see someone walk up and say stuff like that with no context. Did he mistake me for someone else?"

    show john a_2
    think "Well... Guess he wanted to make a point...?"

    "While trying to get that experience out of my mind, I continued home."

    play music xmasST_bgm_angels_we_have_heard fadein 1
    scene bg main livingroom day
    show holly a_2 at Position(pos=(0.25, 1.2), anchor=(0.5, 1.0)), faceright
    with wipeblinds_vert
    show john a_0 at centerright, faceleft with dissolve
    "Mom hadn't gotten home yet. But I saw Holly fiddling with some paper for what seemed like a gift on the couch."

    show john a_6
    john "Hey Holly."

    show holly a_3
    "She shot a glance my way, but apart from a quick sign of acknowledgement, I didn't get much in return."

    show john a_5
    think "Not that I expect much communication from her nowadays."

    "I had a gift or two to wrap up still myself, so I got around to that the moment I got into my room."

    scene black with wipeup
    outfit john casual
    outfit sandra casual
    accessory sandra set
    outfit yui casual
    outfit natsumi casual
    pause 1
    scene bg main kitchen night
    show sandra b_9 at Position(pos=(0.15, 1.0), anchor=(0.5, 1.0)), faceright
    show holly a_7 at Position(pos=(0.30, 1.0), anchor=(0.5, 1.0)), faceright
    show john a_0 at Position(pos=(0.43, 1.0), anchor=(0.5, 1.0)), faceright
    show yui a_0 at Position(pos=(0.57, 1.0), anchor=(0.5, 1.0)), faceleft
    show natsumi b_0 at Position(pos=(0.70, 1.0), anchor=(0.5, 1.0)), faceleft
    show yuuna a_0 at Position(pos=(0.85, 1.0), anchor=(0.5, 1.0)), faceleft
    with wipedown
    "Yuuna, Yui and Natsumi arrived later that day."

    "All of them carried presents with them themselves."

    "This year was yet another quite warm christmas evening, so they didn't even come with jackets or anything."

    "Yuuna also had a duck with her, in addition to the one my mom made, and the children were tasked with determining which one was better."

    "It ended up in a solid stalemate after both moms seemingly had bribed their own children with money to choose their own duck. Which turned out to be a fun turn of events when we all admitted to it."

    "We just had a good time in general. Played some board games, ate loads of food and commented on those cheesy christmas movies that ran at this time of the day."

    scene bg main room night
    show john a_0 at centerright, faceleft
    with sawright
    "When the time came to hit the hay, Holly housed an additional bed for Yui. Meanwhile, Yuuna and Natsumi would stay over in mom's room."

    "It turned into quite the sleepover. Luckily I was still the master of my own room."

    "I wasn't typically {q}that{/q} excited to open gifts the next morning. But as always, I quickly fell asleep, looking forward to the next morning."

    stop music fadeout 4
    scene black with HorizCenterTransition(2.0, True)
    body izuna xmasST_izuna
    body john xmasST_john
    outfit izuna uniform2
    outfit john noshirt
    pause 4
    $ izuna.name = "???"
    izuna "Hey. Wake up."

    "I was awoken by the voice of someone."

    "Was it morning already?"

    "I still felt incredibly sleepy."

    izuna "HEY!"

    play music xmasST_bgm_silent_night fadein 1
    scene bg main room dark
    show john a_4 at centerright, faceleft
    show izuna a_0 at centerleft, faceright
    with dissolve
    john "Wh- what? Who is there?"

    show john a_2
    izuna "It's me. You were supposed to be waiting for me. But you're sleeping, which is kinda rude."

    "My vision was still a bit blurry since I was tired."

    "But..."

    show john a_5
    john "Wh- who are you?"

    $ izuna.name = "Izuna"
    show izuna a_1
    john "And how the heck did you get into my room?!"

    izuna "I'm Izuna, dumbass. From school."

    show john a_2
    john "Izuna?"

    show izuna a_0
    izuna "Yes."

    show john a_6
    john "...Who?"

    show izuna a_5
    izuna "Wait, you don't know me?!"

    show john a_2
    show izuna a_8
    john "So that's why you are wearing the uniform."

    show john a_7
    john "But what are you doing in my room?!"

    show izuna a_9
    show john a_5
    izuna "We, the three spirits of christmas, were told that you are a true Scrooge McDuck. You dislike christmas, and we are here to teach you all the wonders that occur at this holy time of the ye-"

    show izuna a_10
    john "You think I dislike christmas?"

    show izuna a_4
    izuna "Well, yes. Our messenger told us."

    show izuna a_6
    john "That little purple-haired guy?"

    izuna "That's him."

    show john a_2
    john "I don't know why you guys believe that, but I do like christmas."

    show izuna a_9
    izuna "Yes, and that is why I will guide you through a journey of your own mind to make you realize that this indeed is a time of the..."

    show izuna a_5
    izuna "Wait what?"

    izuna "You like christmas?"

    show john a_5
    john "Why wouldn't I?"

    izuna "..."

    show izuna b_4
    izuna "Wait a sec."

    show izuna b_2 at faceleft
    show john a_2
    "She turned around and looked at what appeared to be notes."

    show izuna a_5 at faceright
    izuna "Is this not Calvins' Street 41?"

    show john a_0
    john "Well, yeah it is. What about it?"

    show izuna a_7
    izuna "But... Gabriel told me you hated celebrating it with your family."

    john "I don't hate it. I just think it's kind of boring with just us three."

    show john a_2
    john "Also, how do you know that?"

    show izuna a_4
    izuna "So you do hate it!"

    show izuna a_8
    izuna "Kind of."

    show izuna a_2
    izuna "Not really actually."

    show izuna a_1
    izuna "Well this sucks."

    "This started becoming very awkward."

    show john a_2
    john "Could you... you know, not be in our home illegally anymore?"

    show izuna a_7
    izuna "Ah. Right. Sorry about that."

    show izuna:
        ease 2 xpos -0.25
    "She just slowly crept out of the room and closed the door as silently as possible."

    izuna "See you at school."

    "..."

    show john a_5
    john "What the hell..."

    "With the most random and weird encounter of my life out of the way, I hopped back into bed, hoping that this wouldn't repeat itself."

    stop music fadeout 3
    scene black with HorizCenterTransition(2.0, True)
    pause 2
    $ xmasST_rayne.name = "???"
    "Once again I was awoken by someone moving me."

    xmasST_rayne "Hey, boy."

    xmasST_rayne "Wake up."

    xmasST_rayne "Wake up, boy."

    john "Hmmmm..."

    outfit xmasST_rayne dress
    scene bg main room dark
    show john a_2 at centerright, faceleft
    show xmasST_rayne c_1 at centerleft, faceright
    with dissolve
    play music xmasST_bgm_jingle_bells_calm fadein 2
    "It took a lot of energy to sit myself up in my bed again. My vision was as blurry as the last time someone woke me up."

    show john a_4
    think "Wait... Is there another person suddenly in my room?!"

    john "Wait, who is it now?"

    show john a_2
    show xmasST_rayne a_19
    xmasST_rayne "Aha. So you are alive after all!"

    "This time, some other girl was standing in my room. Someone I didn't know either."

    $ xmasST_rayne.name = "Rayne"
    john "Of course I'm alive. Who the hell are you? And how are you people getting into our home?"

    show xmasST_rayne b_7
    xmasST_rayne "I am the christmas spirit of moral compasses. Some call me Rayne. Not my real name, obviously, but that's all you need to know."

    show john a_5
    show xmasST_rayne b_6
    john "Rayne? Am I supposed to know you too?"

    show xmasST_rayne c_14
    xmasST_rayne "Haha! Nope! I have no idea who you are."

    show xmasST_rayne c_25
    xmasST_rayne "I was told you were the one who doesn't see the wonders of christmas time, you who is called John Davis."

    show xmasST_rayne c_5
    xmasST_rayne "Can I call you John?"

    john "Uhh... I would prefer it if you got out of my room to be honest."

    show xmasST_rayne a_24
    xmasST_rayne "John it is!"

    show john a_7
    show xmasST_rayne a_9
    john "Look, I already told Rachel or whatever that other girl's name was earlier that I don't dislike christmas or anything. You guys are clearly in on the ploy together and targeting the wrong person."

    show xmasST_rayne b_13
    show john a_16
    xmasST_rayne "Indeed, and she has told me."

    show xmasST_rayne b_10
    xmasST_rayne "However, as a vegan I cannot overlook that you are feasting on poor ducklings for christmas!"

    show xmasST_rayne b_4
    john "..."

    john "Are you serious?"

    show xmasST_rayne a_15
    xmasST_rayne "Dead serious!"

    show xmasST_rayne a_12:
        pause 1
        ease 1 xpos 0.5
        pause 1
        ease 1 xpos 0.3
    xmasST_rayne "You should take one of these. They will inform you of the cruelty that these ducks go through before being massacred!"

    show john a_19
    "She handed me a handwritten piece of paper that had some scribbles on it, saying {q}Ducks are for loving, not eating!{/q}."

    john "My mom buys her ducks from a friend who has an organic farm though..."

    show xmasST_rayne c_8
    xmasST_rayne "Is that so?"

    xmasST_rayne "..."

    show xmasST_rayne c_9
    xmasST_rayne "I guess you are kind of excused then. It does not make up for the massive amount of suffering you inflict upon them, however!"

    show john a_7
    john "Alright. Will you now please get out of our home before I call the police?"

    show john a_19
    show xmasST_rayne b_24 at faceleft
    xmasST_rayne "I will do my best!"

    show xmasST_rayne:
        ease 2 xpos -0.3
    xmasST_rayne "Sleep well! Think about the future of ducks!"

    john "Uh-huh..."

    "Unlike that other girl, she was out of my room in less than seconds."

    scene bg main livingroom dark with wiperight
    play sound sfx_door_close
    "I wanted to make sure she was actually leaving the house. I heard a door closing, but I went to check if she was actually gone and locked the door for good this time."

    scene bg main room dark with wipeleft
    "I could finally get some sleep. This really had deprived me of a lot of energy."

    "Only seconds passed before I dozed off again."

    stop music fadeout 4
    scene black with HorizCenterTransition(2.0, True)
    $ xmasST_kristoff.name = "???"
    outfit xmasST_kristoff santa
    pause 3
    xmasST_kristoff "Ho-ho-ho! John! Wake up!"

    think "Oh god, please no."

    play music xmasST_bgm_all_i_want_for_christmas fadein 2
    scene bg main room dark
    show xmasST_asset larger main room:
        xanchor 0.5
        xpos 0.43
    show john a_2 at centerright, faceleft
    show xmasST_kristoff b_7 at Position(pos=(0.40, 1.0), anchor=(0.5, 1.0)), faceright
    with dissolve
    "Once again, somebody was in my room."

    "Blurry vision as always, I got into a sitting position again."

    show xmasST_kristoff b_1
    xmasST_kristoff "Ho-ho-ho, there we go. You are finally awake!"

    show john a_4
    john "Wh... What the hell is going on here?!"

    $ xmasST_kristoff.name = "Santa Claus"
    "I saw some guy dressed as a Santa in front of me. But most assuredly the weirdest thing  about this was..."

    show xmasST_kristoff b_2
    xmasST_kristoff "Why the shocked look, young man? Have you never seen good old Santa before?"

    outfit izuna xmas
    john "Wh- What are..."

    show john:
        ease 0.75 xpos 0.85
    show xmasST_kristoff:
        ease 0.75 xpos 0.55
    show xmasST_asset larger main room:
        ease 0.75 xpos 0.58
    show xmasST_asset xmas harem 1 at left behind kristoff:
        zoom 1.15
        ypos 1.15
        alpha 0.0
        pause 0.5
        ease 0.5 alpha 1.0
    show izuna a_6 at Position(pos=(0.35, 1.0), anchor=(0.5, 1.0)), faceright behind kristoff:
        alpha 0.0
        pause 0.5
        ease 0.5 alpha 1.0
    john "...they doing here?"

    show xmasST_kristoff at faceleft
    show john a_2
    "He turned his head backwards."

    show xmasST_kristoff b_9
    xmasST_kristoff "Hoh?"

    "A lot of women were standing behind him in christmas clothing. Some with questionable exposure."

    show xmasST_kristoff b_7 at faceright
    xmasST_kristoff "Oh them. Do not mind them. They are simply my christmas harem."

    show john a_19
    john "What the fuck is going on here?"

    show john a_4
    show xmasST_kristoff b_5
    show izuna a_1
    john "And you! Why are you here again?!"

    show xmasST_kristoff at faceleft
    show john a_19
    izuna "Huh? What?"

    show xmasST_kristoff at faceright
    xmasST_kristoff "Ho-hoh? You know each other?"

    john "Yes we do! Apparently we are going to the same school!"

    show izuna a_4
    show xmasST_kristoff at faceleft
    izuna "Oh, hey John. Nice seeing you again."

    show xmasST_kristoff at faceright
    john "Didn't I already tell you that I have nothing against christmas?"

    xmasST_kristoff "You don't?"

    show xmasST_kristoff at faceleft
    show izuna a_5
    izuna "You don't? Oh right, you don't."

    show izuna a_4
    izuna "My bad. Santa, he is fine with you after all. Sorry, forgot to tell you."

    show xmasST_kristoff at faceright
    show john a_4
    show izuna a_1
    john "Again, why are you here?"

    show izuna a_4
    show john a_19
    show xmasST_kristoff at faceleft
    izuna "I'm a part of Santa's harem. Isn't that obvious?"

    show xmasST_kristoff at faceright
    john "...Y- Yeah, but why?"

    show izuna a_9
    show xmasST_kristoff at faceleft
    izuna "Cause Santa is hot."

    show xmasST_kristoff b_1 at faceright
    show izuna a_6
    xmasST_kristoff "So you do believe in me after all?"

    show john a_2
    john "Believe in you?"

    john "You're saying you're the actual Santa Claus?"

    xmasST_kristoff "Do I not look the part, young man?"

    show john a_19
    john "Just because you dress like him doesn't mean you are the real Santa, for your information."

    xmasST_kristoff "Ah, yes. Most say the exact same thing."

    show john a_2
    xmasST_kristoff "My existence is a conundrumous one. Many wonder who or what I truly am."

    xmasST_kristoff "Few know that I in truth am a genetically engineered super-human, created by the government to reward those who follow this system."

    show john a_16
    think "Are you for real...?"

    xmasST_kristoff "And although your tardiness is aplenty, I still do not see any truly naughty deeds on your list, young man!"

    xmasST_kristoff "Astonishing. Truly astonishing!"

    show xmasST_kristoff b_3
    show john a_2
    xmasST_kristoff "Wait, why were we paying you a visit again?"

    john "...I don't know?"

    show xmasST_kristoff at faceleft
    xmasST_kristoff "Any of you?"

    "He turned back to face his {q}harem{/q} again. All of them shook their head not knowing."

    show xmasST_kristoff b_1 at faceright
    xmasST_kristoff "Ho-ho, I apologize for waking you up in the middle of the night. I have finished my deliveries to all the nice children around the world, so as you might guess, I will be having some good days off now with the ladies."

    show xmasST_kristoff b_7
    xmasST_kristoff "That being said, an apology is warranted to you, and apologies are best offered as a gift! What do you say? Would you like to be a part of my wonderful harem?"

    show john a_15
    john "...What...?"

    xmasST_kristoff "It will be fun! What do you say?"

    think "Is this guy nuts?"

    show john a_13
    john "Dude, whatever you say. Is your plan to tie me to your back or something?"

    john "Just so you know, there are other people in this house. So scram before I wake them up."

    xmasST_kristoff "Ho-ho-ho, no need to worry young man. Just let Santa do his thing."

    "The guy continued to laugh in this manner. But all of a sudden, he snapped his fingers."

    stop music fadeout 1
    show john a_4
    morph begin magic john xmasST_willow xmas a_1
    accessory john set xmashat
    play music xmasST_bgm_sad_silent_night fadein 2
    "And in that moment, I instantaneously felt some sort of weird thing going on with me."

    morph do john
    "I could barely react before my hands and arms were becoming smaller. My head felt more and more cramped, and I could feel a sting in my chest and crotch."

    morph end john
    "It went by so fast that I had no idea what happened to me."

    show john a_6
    john "Wh- What the hell did you d- What is going on with my voice?"

    show john b_12
    john "Is that me talking?"

    show xmasST_kristoff b_1
    xmasST_kristoff "Ho ho, young lady, you look wonderful."

    show john b_0
    john "Please tell me this isn't happening..."

    show john a_21
    john "Did you just turn me into a girl, you old freak?!"

    show john a_5
    xmasST_kristoff "Why, yes. That is what you wanted was it not?"

    show john a_1
    john "No! I was being sarcastic! Do you want me to spell it out for you?!"

    show john a_6
    john "Now turn me back!"

    show john a_5
    show xmasST_kristoff b_0
    xmasST_kristoff "I'm afraid it's one wish a year for all the good kids. If you wish for something, you should be more clear, young girl."

    show john a_6
    john "Don't call me a girl!"

    show john a_5
    xmasST_kristoff "So you don't want to ride with Santa in his sleigh? All the other girls can only recommend it."

    izuna "I sure can."

    show john a_12
    john "No, I don't want to ride with you in your stupid pimp sleigh. Just turn me back already!"

    show john a_13
    xmasST_kristoff "You can wish for that next year. However, Santa really needs to return home to the northpole right now. Or was it the southpole...?"

    xmasST_kristoff "Anyhow, toodles."

    show john a_17
    show xmasST_kristoff:
        ease 4 alpha 0.0
    show izuna:
        ease 4 alpha 0.0
    show xmasST_asset xmas harem 1:
        ease 4 alpha 0.0
    "With a snap of his fingers they all disappeared."

    show john a_21
    john "No! Wait!"

    show john a_22
    john "..."

    john "Oh fuck, what now?"

    scene black with dissolve
    pause 1
    "The night suddenly became the longest night I had ever lived through."

    show john b_4 at center, faceright with dissolve:
        zoom 1.4
        ypos 1.25
    "I checked the mirror in the bathroom just to be sure this wasn't like some kind of dream. For better or for worse, it wasn't."

    show john a_11
    "Instead of my usual self, I saw a girl I had never seen before, imitating my movements as if they were my own. Because they were."

    scene bg main livingroom day
    outfit john homeworn
    accessory john set
    outfit sandra pajamas
    accessory sandra set bedhead
    outfit natsumi pajamas
    show john b_10 at offscreenleft, faceright
    show yuuna a_5 at Position(pos=(0.85, 1.0), anchor=(0.5, 1.0)), faceleft
    show sandra b_4 at Position(pos=(0.7, 1.0), anchor=(0.5, 1.0)), faceleft
    show yui a_6 at Position(pos=(0.55, 1.0), anchor=(0.5, 1.0)), faceleft
    show natsumi a_3 at Position(pos=(0.4, 1.0), anchor=(0.5, 1.0)), faceleft
    with wipecenter_vert
    show john:
        ease 1 xpos 0.3
    "When I woke up, I had one hell of a story to explain. Luckily, Yui was able to attest that something went down last night, since her and Holly were woken up by weird voices all the time."

    "And they thought I was looking at some shady videos since most of the voices were from girls."

    scene black
    outfit john uniform
    show john b_10 at center:
        zoom 1.3
        ypos 1.15
    with dissolve
    "Nonetheless, I had to hold out the year as someone new. If that guy truly was Santa Claus himself, then turning back would require that I was a good person."

    show john b_9
    "I would try that as best I could. That was for sure. I wouldn't let myself be beaten by someone like that who thinks he can just change my life without consequences."

    stop music fadeout 2
    scene black with Dissolve(1.0)
    title "Later"

    play music "<loop 61.0>" + xmasST_bgm_mr_lawrence
    scene bg lunch
    show john b_7 at center:
    with wipecircle
    "It was the first day of school after the holidays, and I was regarded as an entirely new student to take John's place who had left for another."

    "I decided that I would try and explain this to my friends."

    show john b_6
    "Else they would worry about me."

    "Mom still had her old school uniform from back when she ws in high school, so I was lucky enough to at least wear something formal until my own uniform arrived."

    hide john with wipedown
    body kiyoshi kiyoshiGB
    outfit kiyoshi casual
    accessory kiyoshi set glasses
    show kiyoshi a_9 at Position(pos=(0.78, 1.1), anchor=(0.5, 1.0)), faceleft
    show kyoko a_6 at Position(pos=(0.6, 1.1), anchor=(0.5, 1.0)), faceright
    show katrina a_4 at Position(pos=(0.4, 1.1), anchor=(0.5, 1.0)), faceright
    show john b_7 at offscreenleft, faceright behind katrina
    with wipeup
    "When lunchtime came around, I spotted Kat and Kyoko rather swiftly. But next to them was another girl I hadn't seen before. A girl that didn't have an uniform either, which likely meant she didn't go to this school or just started here like me."

    think "I wonder who that is..."

    show john:
        ease 1.5 xpos 0.35
    "I approached them, but both of my friends were too fixated on the other girl."

    show john b_10
    john "Hey..."

    show kyoko a_0 at faceleft
    show kiyoshi a_11
    show katrina a_1
    katrina "Hey John. Would you belie-"

    show katrina a_12 at faceleft
    show john b_4
    "She turned around. Had she just blurted out my name by instinct."

    show katrina a_5
    katrina "Oh. Uhh... Sorry, I mistook you for someone else."

    show john b_10
    john "Can I sit here?"

    show katrina a_4 at faceright
    show kyoko a_6
    "They both stared at each other. Kyoko shrugged."

    show katrina a_5 at faceleft
    katrina "Sure, why not."

    show john b_1:
        ease 1 ypos 1.15
    "I sat down and the new girl started talking again."

    show kiyoshi a_17
    show kyoko a_0 at faceright
    show katrina a_4 at faceright
    kiyoshi "No really. It is me."

    kyoko "That story doesn't really add up."

    katrina "We know that that weirdo isn't in school today for some reason, but so is John. They are probably doing some alien stuff."

    kiyoshi "How does one not recognize the Kiymaster? I am telling you, Santa gave me a gift!"

    show john a_17
    john "Wait. You're Kiyoshi?"

    show kiyoshi a_10
    show kyoko at faceleft
    show katrina at faceleft
    "Kiyoshi looked at me with an intense stare. Then something clicked for him."

    show kyoko at faceright
    show katrina at faceright
    show kiyoshi b_0
    kiyoshi "John?!"

    show kyoko at faceleft
    show katrina at faceleft
    show john a_1
    show kiyoshi b_7
    john "Did that guy visit you at christmas too?!"

    show katrina a_9
    show john a_0
    katrina "Hold up..."

    katrina "This girl is John now?"

    show john b_2
    john "Yes! I wanted to explain it to you slowly, but apparently this crazy Santa guy also visited Kiyoshi for christmas!"

    show kyoko b_4
    kyoko "No way. This has to be some advanced prank."

    "It was kind of hard to get them won over onto our side, but they eventually came around to accept that we involuntarily had our gender changed."

    "Or at least I thought we both had it changed involuntarily. Apparently Kiyoshi had to ditch his spaceship wish, because Santa didn't want to let him represent humanity in outer space."

    "A new bike was the third thing on his wishlist. And becoming a hot girl was second."

    scene black with dissolve
    "Christmas this year had taken a weird turn. But in the end, few things really changed."

    scene bg classroom 2
    show john b_11 at centerleft, faceright:
        ypos 1.15
    show jack a_1 at right, faceleft
    with wiperadial_vert
    "The best part was that Jack Mallory didn't know who I was, so I wasn't being bullied by the idiot any longer."

    "It turned out pretty alright in the end. I would have to wait for next christmas to turn back though."

    show john b_1
    "If I even wanted to."

    gameover "Merry Christmas v1!"

    jump xmasST_chapter_select



























    return
