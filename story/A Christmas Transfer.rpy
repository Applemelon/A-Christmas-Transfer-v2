label xmasST_start:
    define audio.lawrence1 = "xmasST_bgm_Merry_Christmas_Mr_Lawrence_1"
    define audio.lawrence2 = "xmasST_bgm_Merry_Christmas_Mr_Lawrence_2"

label xmasST_chapter_select:
    scene black
    show xmasST_asset deco
    with dissolve

    play music xmasST_bgm_jingle_bells_calm
    $ gui.textbox_yalign = 1.0
    menu:
        "This scenario contains multiple chapters. They progress in chronological order. Finishing one chapter leads back to this choice. Which chapter would you like to start?"
        "Chapter 1 - A Christmas Transfer (2018)":
            hide xmasST_asset deco with dissolve
            jump xmasST_chapter_1
        "Chapter 2 - The Bipolar Express (2019)":
            hide xmasST_asset deco with dissolve
            jump xmasST_chapter_2

label xmasST_chapter_1:
    stop music fadeout 2
    resetstate
    pause 4
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

label xmasST_chapter_2:
    stop music fadeout 2
    resetstate
    pause 4
    body john xmasST_willow
    body kiyoshi kiyoshiGB
    outfit john casual
    accessory john set xmashat
    accessory kiyoshi set glasses
    play music xmasST_bgm_angels_we_have_heard fadein 1.5
    show john b_6 at center with dissolve
    john "{i}Sigh...{/i}"

    show john b_9
    "It's been a year now since the incident of last christmas happened."
    "As one might assume, I was stuck like this for the entire duration."
    "We graduated high-school, even I under current conditions."
    "But instead of having the name {q}John{/q} in my exam, it now said {q}Willow{/q}."

    outfit xmasST_kristoff santa
    $ xmasST_kristoff.name = "Santa"
    show john b_4
    show xmasST_kristoff b_1 at centerright:
        alpha 0.0
    "One might think that something like {q}Jane{/q} would fit better as my supposed girl name, but my mom said it was too obvious a name."

    body kiyoshi xmasST_kiyoshiGB
    outfit kiyoshi casual_b
    show john b_11:
        ease 0.75 xpos 0.25
    pause 0.5
    show xmasST_kristoff:
        ease 0.5 alpha 1.0
    "That aside, I at least wanted to meet that old guy again who did this to me."

    show kiyoshi b_10 behind john:
        center
        xpos 0.4
    with dissolve
    "And I wasn't alone on this. Kiyoshi wanted too."
    "If not because of what the guy did to him, then out of pure curiosity."
    "After all, I wasn't the only one who was visited by this jerk."
    "Our goal was simple. While we ended up not really having anything against being the opposite gender, since few things really change, being able to change back at will would be the best compromise."

    accessory john set
    outfit katrina casual
    scene bg katrina livingroom night
    show john b_4:
        center
        faceleft
        xpos 0.65
    show kiyoshi a_10:
        center
        faceleft
        xpos 0.8
    show katrina a_4 at centerleft, faceright
    with dissolve
    "So even if we had to suffer through countless hours of Kat forcing us to do the act of being girls..."

    show katrina a_12
    katrina "Let me see your girl face."

    show john b_17
    show katrina a_4
    john "...Our what?"

    show katrina a_12
    show john b_8
    show kiyoshi a_7
    katrina "You got a girl face?"

    show katrina b_1
    katrina "UwU!"

    show katrina a_12
    katrina "That's a girl face. Now let me see your girl face."

    show katrina a_4
    show john a_7
    john "Uh... u... wu?"

    show kiyoshi b_13
    katrina "Bullshit, you didn't convince me."

    show katrina a_12
    katrina "Now let me see your real girl face!"

    show katrina a_4
    show john a_12
    john "Oh for god's sake-"

    show john a_19
    show kiyoshi b_15:
        ease 0.25 xpos 0.85
    john "UwU!"

    show john a_6
    show katrina a_1
    john "Happy?!"
    "Yeah, she was way too hung up on terrible references to take her seriously."

    outfit kiyoshi casual
    accessory kiyoshi set glasses, xmashat
    outfit john xmas
    accessory john set xmashat
    outfit yui casual
    outfit sandra casual
    outfit natsumi casual_b
    scene bg main livingroom night
    show john b_2 at centerright, faceleft
    show kiyoshi b_11 at right, faceleft
    show yui a_13 at centerleft, faceright
    show sandra b_1 at center, faceright
    show yuuna a_1 at left, faceright
    show natsumi a_2:
        center
        faceright
        xpos 0.2
        ypos 1.075
    with wipeleft
    "Eventually, the 24th of December rolled around again."
    "I managed to bring Kiyoshi for this year's christmas, even if Natsumi and Yuuna had no idea who this was."

    show yui a_11
    show john b_4
    yui "Isn't it a bit much with those christmas clothes...?"

    show john b_1
    john "Might as well use it now that I have it."

    outfit john homeworn
    outfit kiyoshi underwear
    accessory john set
    accessory kiyoshi set
    play music xmasST_bgm_silent_night fadeout 1.5
    scene bg main room night
    show john b_4 at centerright, faceleft
    show kiyoshi b_1 at center, faceright
    with wipecircle
    "Well, he was here because he had a plan."
    "He knew that I especially wanted to meet this Santa look-alike again, so he proposed simply waiting for him during this night."
    kiyoshi "W-girl, don't worry about it. He showed up last year, right?"

    show john b_7
    show kiyoshi b_3
    john "Well, yeah, it's just... You know, we don't have guarantees that he's gonna come this christmas again."

    show kiyoshi b_6
    kiyoshi "He knows you have another wish. No Santa in this world would refuse giving one to someone who has done nothing bad this entire year."

    show kiyoshi b_7
    kiyoshi "You haven't done anything bad this year, right?"

    show john a_7
    john "Of course not. I'm not some scumbag."

    show john b_2
    john "I guess you're right. I'm worrying too much."

    show kiyoshi b_3
    kiyoshi "See? Now let's wish for a spaceship for real this time."

    show john b_10
    think "He is still set on getting that spaceship...?"

    scene black with Dissolve(2.0)
    john "Good night. Wake me up if you hear anyone."
    kiyoshi "You can count on me."

    stop music fadeout 2
    pause 5
    scene bg main room day
    show john a_0:
        centerright
        faceright
        ypos 2.0
    show kiyoshi c_25:
        center
        faceright
        ypos 2.0
    with dissolve
    pause 1.5
    play sound xmasST_sfx_rooster
    pause 2
    show john:
        ease 1.5 ypos 1.5
    pause 2
    $ gui.textbox_yalign = 0.03
    john "Huh...?"

    show john b_6
    john "...Wait, is it already...?"

    pause 1.5
    play music xmasST_bgm_we_wish_you
    show john b_12:
        faceleft
        ease 0.25 ypos 1.2
    with hpunch
    $ gui.textbox_yalign = 1.0
    john "Oh god, it's morning!"
    john "Kiyoshi! Wake up!"

    show kiyoshi:
        ease 2.5 ypos 1.35
    kiyoshi "...Hunh...?"
    john "Dude, get up!"

    show kiyoshi c_16
    kiyoshi "{i}Yaawn...{/i}"

    show john b_15
    show kiyoshi b_17
    kiyoshi "What's going o-"

    show kiyoshi b_8:
        faceleft
        ease 0.25 ypos 1.1
    with hpunch
    kiyoshi "Ah! It's morning!"
    john "Of course it is! He didn't come after all!"

    show kiyoshi b_8
    kiyoshi "Uh- Uhh... Alright, so maybe-"

    show kiyoshi b_15 at faceright
    kiyoshi "Maybe he is having a nice morning coffee with your mom!"
    john "He isn't coming, you idiot."
    kiyoshi "Then maybe! Maybe we can just... Ask someone where he is!"

    show john a_6
    john "If it were that simple then we would have done that a long time ago-"

    show john b_12
    show kiyoshi b_0
    john "Oh shit, we should have done that a long time ago!"

    outfit john coat
    outfit kiyoshi casual
    accessory kiyoshi set glasses
    scene bg shrine day
    show john b_3 at center, faceright
    show kiyoshi b_3 at centerleft, faceright
    with wipeclock
    "With that, we set off for Setsuna's after celebrating christmas day at home. Even if my memories were a bit foggy from last year's christmas night, I still remembered one name in particular."
    "Setsuna sometimes talked about a friend of hers called Izuna, who apparently went to the same school as us. So if we could find her, I bet we could find this Santa guy."

    show john b_7 at faceleft
    john "You know, I've been wondering..."

    show kiyoshi b_0
    kiyoshi "Hm?"
    john "Aren't you cold in those clothes?"

    show kiyoshi b_7
    kiyoshi "I don't have warmer clothes than this."

    show john b_4 at faceright
    john "Oh. Right. Sorry."

    scene bg shrine interior day
    show john b_1:
        centerleft
        faceright
        alpha 0.0
        pause 1.0
        ease 0.5 alpha 1.0
    show kiyoshi b_3:
        left
        faceright
        alpha 0.0
        pause 1.5
        ease 0.5 alpha 1.0
    show setsuna a_9:
        right
        faceright
        ypos 1.15
        transform_anchor True
        rotate -60
    with diamonds
    "And we did arrive, but..."

    show kiyoshi b_7
    show john b_17
    setsuna "ZZzzzz..."

    show john b_6 at faceleft
    john "Uh... Maybe we should just come back later?"

    show nemuri a_3:
        offscreenright
        faceleft
        ease 0.75 right
    show john b_4 at faceright
    show kiyoshi a_11
    nemuri "Is someone here?"

    show nemuri a_0
    nemuri "Ah, visitors. Can I help you?"
    john "Actually, we just wanted to talk to Setsuna here, but we'll come back later when she isn't... Sleeping at 2 o'clock in the livingroom...?"
    nemuri "Please excuse her, she decided to stay up way too late yesterday..."

    show nemuri a_1:
        ease 0.15 xpos 0.8
        pause 0.1
        ease 0.2 xpos 0.85
    show setsuna a_8
    show kiyoshi b_2
    show john b_8
    with hpunch
    play sound sfx_whack
    nemuri "Dear, you have visitors!"
    "He slapped her right on her head with a stick he was carrying."

    show setsuna:
        parallel:
            faceleft
            pause 0.25
            faceright
            pause 0.25
            faceleft
            pause 0.25
            faceright
        parallel:
            ease 0.75 ypos 1.0 xpos 0.65 rotate 0
    setsuna "Wha- What?!"

    show nemuri at offscreenright, faceright with ease
    nemuri "Tend to your guests, would you?"

    show setsuna a_7 at faceleft
    pause 1.5
    setsuna "Oh!"

    show kiyoshi b_11
    setsuna "Jo- I mean, Willow! And... You!"

    show setsuna a_6
    setsuna "I'm sorry, have we met before?"
    john "Oh, you see..."

    play music xmasST_bgm_holiday_weasel fadeout 2.5
    scene black with wipeblinds_horiz
    pause 0.5
    outfit john casual
    scene bg shrine interior dusk
    show setsuna b_0:
        right
        faceleft
        ypos 1.15
    show john b_1:
        centerright
        faceright
        ypos 1.15
        xpos 0.575
    show kiyoshi b_5:
        center
        faceright
        ypos 1.15
        xpos 0.45
    with wipeblinds_horiz
    setsuna "I see."
    setsuna "So Izuna was much more than I thought."

    show setsuna b_3
    setsuna "I expected her to be out of the ordinary, but to be a part of... Santa's harem...?"
    setsuna "Why do I even believe you? That sounds so stupid."

    show john b_4
    john "Don't look at me, I think it's a ridiculous thought too."

    show setsuna a_2
    setsuna "I'll give her a call and ask her if she can help you guys out. Give me one sec."

    show setsuna a_1
    show john b_1
    "She took out her phone that she kept in her miko dress and dialed a number."

    play sound xmasST_sfx_dialing
    show setsuna b_2
    setsuna "Heh, it can take a little while, she's really bad at picking up her phone."

    play sound xmasST_sfx_pick_up
    show setsuna b_0
    "But we did eventually reach her after a few seconds."
    izuna "Hello?"

    show setsuna b_1
    setsuna "Hey Izuna. It's Setsuna."
    izuna "Oh, hey! How's my favorite girl?"
    setsuna "I'm great, thank you. I've got two people here who would like to talk to you, something about wanting to meet with Santa or something..."
    izuna "R- Really?!"
    izuna "Are they at your place right now?!"

    show setsuna b_0
    show kiyoshi b_17
    setsuna "Uh, yeah."

    show john b_11
    izuna "Give me ten seconds!"

    play sound xmasST_sfx_hang_up
    show setsuna b_6
    "And with that, she hung up."
    john "...Uh?"
    setsuna "...That's odd."

    stop music fadeout 3
    play sound xmasST_sfx_airplane
    show john b_10
    show kiyoshi b_2
    show setsuna a_7
    "Not long after though, we heard a really loud noise right outside."

    show john b_16
    show kiyoshi b_16
    john "What the hell is that?!"

    play sound xmasST_sfx_crash
    "The sound was promptly abrupted with an extremely noisy crashing sound."

    show kiyoshi b_15 at faceleft behind john
    show john b_8 at faceleft
    show setsuna b_8
    setsuna "Did someone just crash outside?"

    scene bg shrine dusk
    body izuna xmasST_izuna
    outfit izuna xmas
    show xmasST_asset crashed plane:
        center
        xpos 0.1
        ypos 1.5
        faceleft
        zoom 1.5
    show izuna a_6 at left
    show john b_0:
        faceleft
        center
        xpos 0.6
        alpha 0.0
        pause 0.75
        ease 0.5 alpha 1.0
    show kiyoshi a_15:
        faceleft
        center
        xpos 0.75
        alpha 0.0
        pause 0.9
        ease 0.5 alpha 1.0
    show setsuna a_8:
        faceleft
        center
        xpos 0.9
        alpha 0.0
        pause 1.05
        ease 0.5 alpha 1.0
    with sawleft
    izuna "Whew, that was a close one."

    show izuna a_4:
        pause 1
        ease 0.5 xpos 0.4
    izuna "Oh! Hey Setsuna, thanks for telling me!"
    kiyoshi "What the-"
    kiyoshi "Is that a plane?"

    play music xmasST_bgm_dvorak_polka fadein 1
    scene bg shrine interior dusk
    show izuna a_6:
        centerleft
        faceright
        ypos 1.15
    show kiyoshi b_5:
        center
        faceleft
        ypos 1.15
    show john b_1:
        centerright
        faceleft
        ypos 1.15
    show setsuna b_0:
        right
        faceleft
        ypos 1.15
    with cubeclouds
    "We explained what we wanted to her, and she was cheerfully listening to every bit of it."

    show john b_7
    "If I had to know better, I'd even think she was enjoying herself a bit {i}too{/i} much listening to our request."
    "As if she hadn't talked with anyone in years."

    show izuna a_9
    izuna "Okay, got it."

    show izuna a_7
    izuna "But aw man, I can't believe that you are that Kiyoshi guy though."
    izuna "Santa really did a good job on you. You look way cuter now."

    show kiyoshi a_1
    kiyoshi "I wholeheartedly agree. His request of joining his harem is something I could not accept though, unfortunately."

    show kiyoshi b_18
    kiyoshi "After all, what I strive for is a harem of my own."

    show kiyoshi b_0 at faceright
    john "You want a harem of guys around you now?"

    show kiyoshi a_23
    kiyoshi "Obviously not. Girls are still my interest, after all."

    show john b_2
    john "Pff, good luck finding such a large amount of lesbians."

    show john b_7 at faceright
    setsuna "Could you guys not talk about those sorts of topics while in the shrine, please?"
    john "Sorry."

    show john at faceleft
    show kiyoshi a_0 at faceleft
    izuna "Anywho, I just crashed the plane that Santa gave me this year, so I can't really give you a lift in that one..."

    show izuna a_5
    izuna "Boy was it hard to control..."

    show izuna a_0
    show john b_17
    john "He gave you a freaking airpla- Argh, whatever."

    show john b_7
    john "Does the guy really live at the north pole?"

    show izuna a_4
    izuna "He sure does. And I think I know another way to get there!"
    izuna "But we have to leave today still, it's the last chance at going there."
    john "Yes please."

    scene bg main livingroom night
    show john b_2 at center, faceleft
    show kiyoshi b_3 at centerright, faceleft
    show izuna a_7 at right, faceleft
    show sandra b_4 at centerleft, faceright
    show holly b_8 at left, faceright
    with sawleft
    "We went home to quickly notify our parents about our absence."

    scene bg kiyoshi livingroom night
    show kiyoshi b_14 at center, faceright
    show john b_9 at centerleft, faceright
    show izuna a_5 at left, faceright
    show maurice a_3 at centerright, faceleft
    with sawright
    "Or in Kiyoshi's case, his guardian."

    play music xmasST_bgm_oh_christmas_tree fadein 1.5 fadeout 1
    scene xmasST_bg trainstation 1
    show izuna a_8 at centerleft, faceleft
    show john b_4 at center, faceleft
    show kiyoshi b_11 at centerright, faceleft
    with wiperadial_horiz
    "Eventually, she led us to the trainstation of the city."

    show izuna a_1 at faceright
    izuna "Huff... Guys, you need to hurry, I think we could be late!"

    show izuna a_7
    john "Are we just taking a train?"
    john "Surely it can't be that easy."
    izuna "Of course we are."
    kiyoshi "I didn't expect for us to pay for a train ticket, I barely have enough money saved up for myself."
    john "Yes, that too."

    show izuna a_5
    izuna "Urgh, you guys, don't you think I have everything planned?"
    john "No."
    kiyoshi "Definitely not."

    show izuna a_9
    izuna "Well, prepare to be amazed then."

    show izuna a_6 at faceleft
    "She turned around and started looking at the walls in front of us."

    show izuna:
        ease 0.5 left
    "She then started walking towards it, looking at various sections of the wall conspicuously."

    show izuna a_4:
        ease 0.75 xpos 0.2
    "Then, as if readying up for a run, she got into position..."

    show izuna:
        ease 0.25 xpos 0.05
    pause 0.2
    play sound sfx_whack
    show izuna a_7 at anim_fall_over_right with hpunch
    izuna "Ow!"

    hide izuna
    show john b_17
    show kiyoshi b_17
    john "Uh..."

    show izuna a_5 at left, faceright with easeinbottom
    izuna "That was a fluke!"
    izuna "I always get them mixed! It's over here instead!"

    show john b_7
    show izuna a_8 at faceleft
    "Preparing for yet another run at the wall, she now aimed for another spot."

    show izuna:
        ease 0.5 offscreenleft
    play sound xmasST_sfx_enter
    show kiyoshi b_2
    show john b_12
    "And sure enough, she went right through."
    kiyoshi "Wha- A cloaking device?!"
    kiyoshi "Those exist on earth?!"

    show izuna a_4:
        transform_anchor True
        faceright
        xpos -0.3
        ypos 1.1
        rotate 20
        ease 0.5 xpos 0.15
    izuna "You coming or what?"
    john "Uh- Yeah, sure..."

    scene xmasST_bg trainstation 2
    show izuna a_10:
        center
        faceright
    show john b_10:
        right
        faceleft
        xpos 0.9
        pause 0.5
        ease 0.5 xpos 0.7
    show kiyoshi b_0:
        right
        faceleft
        xpos 1.1
        pause 0.75
        ease 0.5 xpos 0.85
    with wipeclock
    "As if entering a completely different world, we were now suddenly outside again."
    "Now, a very traditional looking train with low resolution was waiting for us."

    show izuna a_6
    john "So that's the train we'll be taking?"
    izuna "Yep."

    show xmasST_misha a_5 at left, faceright with dissolve
    show izuna a_7
    xmasST_misha "Ey! You there. Are little girls taking train to pole tonight?"

    show izuna at faceleft
    show xmasST_misha a_7
    izuna "Oh, Miss Conductor. Yes, we're getting on!"
    xmasST_misha "...Santa girl, you taking little girls to pole tonight? Sure about it?"

    show izuna a_9
    izuna "Of course. I know what I'm doing."

    show izuna a_6
    xmasST_misha "...Very well. Go on board."

    show xmasST_misha a_3
    xmasST_misha "Welcome to Bipolar Express. We leave now."

    scene black with wipedown
    pause 0.5
    scene xmasST_bg wagon 2
    show izuna a_6 at centerright, faceright
    show xmasST_misha a_7 at right, faceleft
    show john b_7 at center, faceright
    show kiyoshi b_11 at centerleft, faceright
    with wipeup
    xmasST_misha "I am Misha. Conductor. I am from Russia, so use Russia accent for me."
    xmasST_misha "There are not many people going to pole tonight. It is day after christmas, not big surprise."
    xmasST_misha "There is no smoking, loitering or eating in my train. Else I will throw you off to wolves. Kapiche?"

    show john b_17
    john "Uh, yeah."

    show john b_7
    xmasST_misha "Enjoy trip. I will start train. Goodbye."

    show xmasST_misha at offscreenright, faceright with ease
    pause 0.75
    show izuna at faceleft
    izuna "Isn't she just great?"
    kiyoshi "I felt like I was being interrogated."
    izuna "Exactly!"
    john "...Alright. So do we just wait until we arrive now?"
    izuna "Yup."
    john "...That's convenient."

    scene black with wiperadial_horiz
    pause 1
    scene xmasST_bg wagon 2
    show izuna a_6:
        centerleft
        faceright
        ypos 1.15
    show kiyoshi b_5:
        center
        faceright
        ypos 1.15
    show john b_1:
        centerright
        faceright
        ypos 1.15
    with wiperadial_vert
    john "So... I've been meaning to ask..."

    show john at faceleft
    john "Why is it called the {q}Bipolar Express{/q}?"

    show izuna a_4
    izuna "That's because..."

    show izuna a_9
    izuna "..."

    show izuna a_8
    izuna "Because it has a bipolar disorder."

    show john b_7
    john "...Are you sure?"
    izuna "...Yes?"

    show john at faceright
    john "{i}Sigh...{/i} Alright."

    show john b_11
    show kiyoshi b_10
    show izuna a_1
    xmasST_misha "Passengers, attach your seatbelts."
    "I already had mine strapped on as I wasn't going anywhere, but shortly after the announcement over the speakers, the train started to slow down."

    show john at faceleft
    kiyoshi "The train is stopping?"
    john "It would seem so."

    show john at faceright
    "Eventually it came to a complete stop."
    xmasST_misha "...You wait in seats until I am done fixing problem. We going soon again."

    show izuna a_8
    show john at faceleft
    show kiyoshi at faceleft
    izuna "Mmhh, it's rare for the trains to be late from what I've heard."

    show izuna a_6
    izuna "I'm sure everything will be alright."
    "She said that, but..."

    scene xmasST_bg wagon 2
    show izuna a_0:
        centerleft
        faceright
        ypos 1.15
        xpos 0.45
    show kiyoshi b_13:
        left
        faceleft
    show john b_7:
        centerright
        faceright
        ypos 1.15
    with wipecircle
    "A few minutes quickly became 20 minutes..."

    scene xmasST_bg wagon 2
    show izuna a_2:
        centerright
        faceright
        ypos 1.15
    show kiyoshi b_16:
        centerleft
        faceleft
    show john b_10:
        left
        faceright
    with wipecircle
    "20 minutes quickly became 40..."

    scene xmasST_bg wagon 2
    show izuna a_5:
        centerleft
        faceleft
        ypos 1.15
    show kiyoshi b_12:
        centerright
        faceleft
    show john b_11:
        right
        faceleft
    with wipecircle
    "And eventually, even 40 minutes became 1 hour and 30 minutes..."

    show izuna at faceright
    john "Hey, Izuna, how long is this really going to take?"

    show izuna a_2
    izuna "Sigh... I don't know."
    john "Is it okay if we go check what's actually wrong?"
    izuna "Yeah, yeah, I'll just wait here then..."
    think "Talk about a downer."

    scene xmasST_bg wagon 1
    show xmasST_misha a_5 at centerright, faceright
    show john b_8 at centerleft, faceright
    show kiyoshi b_10 at left, faceright
    with wipeblinds_horiz
    "The wagon right next to ours was the main control center for this train, which looked way too advanced for the task it was supposed to perform."
    "We found Misha, quite frustrated in here."
    john "Uhm, hey..."

    show xmasST_misha a_4 at faceleft
    xmasST_misha "What do little girls want? I am fixing problem. Go away."
    john "Is there anything we could help with to fix the problem maybe?"
    kiyoshi "I know a few things about trains personally."

    show xmasST_misha a_7
    xmasST_misha "Ugh, little girls care too much. But yes. Could need little help."
    xmasST_misha "I have lost important key to important box for getting snow off rails. I have searched all over control center, but find nothing."
    xmasST_misha "Maybe somebody stole key from control center. Maybe. So need somebody to check all cabins."

    show xmasST_misha a_2
    xmasST_misha "Tall girl with anorexia stay, want to push her into airlock to check if key in there."

    show kiyoshi a_2
    kiyoshi "You want to shove me into what-now?!"

    show xmasST_misha a_4
    xmasST_misha "No complaining. Weak girl, go look for key and ask other passengers if they know where key is."

    show john b_2
    john "Okay, I'll do that."

    play sound xmasST_sfx_new_room
    show john a_1 at offscreenleft with ease
    show kiyoshi at faceleft
    kiyoshi "No, wait, W-girl! Don't leave me here with her!"

    play music xmasST_bgm_holiday_weasel fadeout 1 fadein 1.5
    $ gui.textbox_yalign = 0.03
    scene xmasST_bg wagon 2
    with wipecircle
    "As you enter the cabin you previously were in, you can feel something changing."
    "All of a sudden, this has turned into a point-and-click adventure with you in first person."

label xmasST_tutorial_1:
    show screen item_search_tutorial_1 with dissolve
    "With this newborn resolve and change of perspective, you get the urge to click on Izuna to talk with her."
    "I said, we will now click on Izuna."
    "..."
    "Click on her."
    "If you don't want to click on her out of consideration, then click in the general vicinity of her."
    "Okay now listen here you little shit, you click on her whether you like it or not, the next one is going to be a loop that you can't stop looping in so enjoy your endless torture and misaligned textboxes."

label xmasST_tutorial_screw_you:
    "CLICK ON HER."
    jump xmasST_tutorial_screw_you

label xmasST_tutorial_2:
    scene xmasST_bg wagon 2
    show xmasST_asset overlay1
    show izuna a_6 at centerleft, faceright
    show john b_1 at centerright, faceleft
    with dissolve
    izuna "Oh John, did everything turn out alright?"
    john "Sadly not, she needs some sort of key. Do you know where I could find it or how it looks?"
    show izuna a_0
    izuna "A key? Nope, sorry."
    show izuna a_6
    izuna "But do you want to know what I {i}did{/i} find?"

    scene xmasST_bg wagon 2
    show izuna a_6 at left, faceright
    show xmasST_asset overlay2:
        zoom 1.15
        yalign 0.6
        xalign 0.4
    show screen item_search_tutorial_2
    with dissolve
    izuna "Tadah!"
    izuna "I managed to find a coin and made it balance on the seat!"
    izuna "How neat is that?"
    john "..."
    john "I'll take it."
    show izuna a_2
    izuna "Aww..."

label xmasST_tutorial_take_it:
    "I took the coin."
    jump xmasST_tutorial_take_it

label xmasST_tutorial_3:
    hide xmasST_asset overlay2 with dissolve
    $ coin = True
    if coin == True:
        show xmasST_asset coin:
            center
            xpos 0.95
            ypos 1.0
        with dissolve
    "You added the coin to your inventory."
    show izuna a_6
    izuna "Oh yeah, John, make sure you go look in the cabins behind us too, right?"
    john "But there is a wall. There only are two cabins."
    izuna "That's just another magic wall. You can walk right through it."
    john "...Right, I'll keep that in mind."
    $ xmasST_rng_bool = False
    $ xmasST_natsumi_game_completed = False
    $ xmasST_natsumi_spoken = False
    $ tea = False
    $ xmasST_rayne_spoken = False
    $ xmasST_rayne_coin = False
    $ xmasST_bear_move = False
    $ key = False
    $ stick = False
    $ kiyoshi_ = False
    $ kiyoshi_activated = False
    $ kiyoshi_activated_talked = False
    jump xmasST_wagon_2




label xmasST_wagon_1:
    scene xmasST_bg wagon 1
    show screen item_search_wagon_1
    if coin == True:
        show xmasST_asset coin as coin:
            center
            xpos 0.95
            ypos 1.0
    if tea == True:
        show xmasST_asset teacup as teacup:
            center
            xpos 0.885
            ypos 1.0
    if stick == True:
        show xmasST_asset stick inv as stick:
            center
            xpos 0.825
            ypos 1.0
    if key == True:
        show xmasST_asset key as key:
            center
            xpos 0.78
            ypos 1.0
    with wipecircle

    menu:
        "Where would you like to go?"
        "Cabin 2":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_1
            with wipecircle
            jump xmasST_wagon_2_sleep


label xmasST_wagon_2_sleep:
    $ xmasST_rng = renpy.random.randint(0, 2)
    if xmasST_rng == 0:
        $ xmasST_rng_bool = True
        scene xmasST_bg wagon 2
        show izuna a_10:
            transform_anchor True
            rotate 90
            left
            faceleft
            ypos 0.9
            xpos 0.0
        if coin == True:
            show xmasST_asset coin as coin:
                center
                xpos 0.95
                ypos 1.0
        if tea == True:
            show xmasST_asset teacup as teacup:
                center
                xpos 0.885
                ypos 1.0
        if stick == True:
            show xmasST_asset stick inv as stick:
                center
                xpos 0.825
                ypos 1.0
        if key == True:
            show xmasST_asset key as key:
                center
                xpos 0.78
                ypos 1.0
        with wipecircle
        menu:
            "Where would you like to go?"
            "Cabin 1":
                play sound xmasST_sfx_new_room
                scene black
                hide screen item_search_wagon_2
                with wipecircle
                jump xmasST_wagon_1
            "Cabin 3":
                play sound xmasST_sfx_new_room
                scene black
                hide screen item_search_wagon_2
                with wipecircle
                jump xmasST_wagon_3
    else:
        jump xmasST_wagon_2

label xmasST_wagon_2:
    if xmasST_rng_bool:
        jump xmasST_wagon_2_sleep
    scene xmasST_bg wagon 2
    show screen item_search_wagon_2
    if coin == True:
        show xmasST_asset coin as coin:
            center
            xpos 0.95
            ypos 1.0
    if tea == True:
        show xmasST_asset teacup as teacup:
            center
            xpos 0.885
            ypos 1.0
    if stick == True:
        show xmasST_asset stick inv as stick:
            center
            xpos 0.825
            ypos 1.0
    if key == True:
        show xmasST_asset key as key:
            center
            xpos 0.78
            ypos 1.0
    with wipecircle

    menu:
        "Where would you like to go?"
        "Cabin 1":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_2
            with wipecircle
            jump xmasST_wagon_1
        "Cabin 3":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_2
            with wipecircle
            jump xmasST_wagon_3


label xmasST_wagon_3:
    scene xmasST_bg wagon 3
    if coin == True:
        show xmasST_asset coin as coin:
            center
            xpos 0.95
            ypos 1.0
    if tea == True:
        show xmasST_asset teacup as teacup:
            center
            xpos 0.885
            ypos 1.0
    if stick == True:
        show xmasST_asset stick inv as stick:
            center
            xpos 0.825
            ypos 1.0
    if key == True:
        show xmasST_asset key as key:
            center
            xpos 0.78
            ypos 1.0
    show screen item_search_wagon_3
    with wipecircle

    menu:
        "Where would you like to go?"
        "Cabin 2":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_3
            with wipecircle
            jump xmasST_wagon_2_sleep
        "Cabin 4":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_3
            with wipecircle
            jump xmasST_wagon_4

label xmasST_wagon_4:
    scene xmasST_bg wagon 4
    if coin == True:
        show xmasST_asset coin as coin:
            center
            xpos 0.95
            ypos 1.0
    if tea == True:
        show xmasST_asset teacup as teacup:
            center
            xpos 0.885
            ypos 1.0
    if stick == True:
        show xmasST_asset stick inv as stick:
            center
            xpos 0.825
            ypos 1.0
    if key == True:
        show xmasST_asset key as key:
            center
            xpos 0.78
            ypos 1.0
    show screen item_search_wagon_4
    with wipecircle

    menu:
        "Where would you like to go?"
        "Cabin 3":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_4
            with wipecircle
            jump xmasST_wagon_3
        "Cabin 5":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_4
            with wipecircle
            jump xmasST_wagon_5

label xmasST_wagon_5:
    scene xmasST_bg wagon 5
    if coin == True:
        show xmasST_asset coin as coin:
            center
            xpos 0.95
            ypos 1.0
    if tea == True:
        show xmasST_asset teacup as teacup:
            center
            xpos 0.885
            ypos 1.0
    if stick == True:
        show xmasST_asset stick inv as stick:
            center
            xpos 0.825
            ypos 1.0
    if key == True:
        show xmasST_asset key as key:
            center
            xpos 0.78
            ypos 1.0
    if xmasST_bear_move == False:
        show screen item_search_wagon_5_1
    else:
        show screen item_search_wagon_5_2
    with wipecircle

    menu:
        "Where would you like to go?"
        "Cabin 4":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_5_1
            hide screen item_search_wagon_5_2
            with wipecircle
            jump xmasST_wagon_4
        "Cabin 6":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_5_1
            hide screen item_search_wagon_5_2
            with wipecircle
            jump xmasST_wagon_6

label xmasST_wagon_6:
    scene xmasST_bg wagon 6
    if coin == True:
        show xmasST_asset coin as coin:
            center
            xpos 0.95
            ypos 1.0
    if tea == True:
        show xmasST_asset teacup as teacup:
            center
            xpos 0.885
            ypos 1.0
    if stick == True:
        show xmasST_asset stick inv as stick:
            center
            xpos 0.825
            ypos 1.0
    if key == True:
        show xmasST_asset key as key:
            center
            xpos 0.78
            ypos 1.0
    if stick == False:
        show screen item_search_wagon_6
    with wipecircle

    menu:
        "Where would you like to go?"
        "Cabin 5":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_6
            with wipecircle
            jump xmasST_wagon_5

label xmasST_wagon_trapdoor:
    scene xmasST_bg wagon trapdoor
    if coin == True:
        show xmasST_asset coin as coin:
            center
            xpos 0.95
            ypos 1.0
    if tea == True:
        show xmasST_asset teacup as teacup:
            center
            xpos 0.885
            ypos 1.0
    if stick == True:
        show xmasST_asset stick inv as stick:
            center
            xpos 0.825
            ypos 1.0
    if key == True:
        show xmasST_asset key as key:
            center
            xpos 0.78
            ypos 1.0
    if key == False:
        show screen item_search_wagon_trapdoor
    with wipecircle
    menu:
        "Where would you like to go?"
        "Cabin 5":
            play sound xmasST_sfx_new_room
            scene black
            hide screen item_search_wagon_trapdoor
            with wipecircle
            jump xmasST_wagon_5

label xmasST_izuna:
    show xmasST_bg wagon 2
    show xmasST_asset overlay1:
        xalign 0.5
    show izuna a_6 at centerleft, faceright
    show john a_1 at centerright, faceleft
    with dissolve
    izuna "Anything new?"
    john "Nope. We're not moving yet."
    izuna "I see. Be sure to tell me if we're starting to churn towards the north pole again, I'm really starting to starve, you know."
    jump xmasST_wagon_2

label xmasST_misha:
    if key == True:
        jump xmasST_chapter_2_finale
    show xmasST_bg wagon 1
    show xmasST_asset overlay1:
        xalign 0.5
    show john b_7 at centerright, faceleft
    show xmasST_misha a_3 at centerleft, faceright
    with dissolve
    xmasST_misha "You have my key?"
    john "Not yet. Do you have any other idea of where it could be?"
    xmasST_misha "Hmm..."
    xmasST_misha "Perhaps you should ask Bear in cabin 5. He is train mechanic. Best guess."
    john "Alright, I'll ask him."
    jump xmasST_wagon_1

label xmasST_kiyoshi:
    show xmasST_bg wagon 1
    show xmasST_asset overlay1:
        xalign 0.5
    show john b_1 at centerright, faceleft
    show kiyoshi a_10 at centerleft, faceright
    with dissolve
    if key == True:
        kiyoshi "C'mon W-girl, give her that thing so I don't have to listen to her anymore. I like women, but not like this."
        jump xmasST_wagon_1
    else:
        if kiyoshi_activated == False:
            john "Everything alright there?"
            kiyoshi "If I am alright? She just stuck me up into the air vents. Everything is going {i}just fine{/i}."
            john "Is that a no?"
            show kiyoshi b_13
            kiyoshi "I am not one for sarcasm, but even I can crack one in this situation."
            kiyoshi "Just hurry up and find that stupid key so we can go look for my spaceship."
            jump xmasST_wagon_1
        else:
            if kiyoshi_activated_talked == False:
                $ kiyoshi_ = True
                $ kiyoshi_activated_talked = True
                john "Hey Kiyoshi, you're tall, right?"
                kiyoshi "I sure am."
                john "I think I found the right key, but I can't reach it. Want to come with?"
                show kiyoshi b_18
                kiyoshi "You found it?! Thank goodness!"
                show kiyoshi b_13
                kiyoshi "Having to listen one more word to this crazy communist will make my head explode in even bits."
                show kiyoshi b_18
                kiyoshi "Lead the way, W-girl."
                jump xmasST_wagon_1
            else:
                kiyoshi "Lead the way, W-girl."
                jump xmasST_wagon_1

label xmasST_natsumi:
    outfit natsumi formal
    show xmasST_bg wagon 3
    show xmasST_asset overlay1:
        xalign 0.5
    show john b_17 at centerright, faceleft
    show natsumi a_9 at centerleft, faceright
    with dissolve
    if xmasST_natsumi_game_completed == False:
        if xmasST_natsumi_spoken == False:
            $ xmasST_natsumi_spoken = True
            john "Natsumi? What are you doing here?"
            natsumi "Heya John. Or Willow."
            natsumi "I am visiting my friend."
            john "Your friend?"
            natsumi "Yup."
            john "What sort of friend do you have exactly? How did you even get on the train?"
            show natsumi a_0
            natsumi "Haven't you heard of my tea parties? I told mommy about them but she never takes me seriously."
            natsumi "My friend is a nice Ice Witch who lives in a forest nearby. But this train is soooo slow."
            show natsumi a_9
            natsumi "Hey John. Or Willow. Do you want to play a game?"
            show john b_11
            john "I'm really in a hurry right now."
            natsumi "Let's say you win a cup of my tea if you win!"
            show natsumi a_8
            natsumi "My tea is very delicious, I bet it would warm up anyone who tried it!"
            show natsumi a_9
        else:
            natsumi "Hey John. Or Willow. Do you want to play?"
        menu:
            "Do you want to play Natsumi's game?"
            "Let's try":
                jump xmasST_natsumi_game_1
            "Not right now":
                natsumi "Okay. See you later."
                jump xmasST_wagon_3
    else:
        natsumi "Hey John. Or Willow. Good luck doing what you're doing!"
        john "Thanks."
        jump xmasST_wagon_3

label xmasST_natsumi_game_1:
    natsumi "Alright! You just have to answer all the questions right!"
    natsumi "Ready?"
    menu:
        natsumi "What is the name of the town we live in?"
        "Tina Koya":
            jump xmasST_natsumi_wrong
        "San Fransokyo":
            jump xmasST_natsumi_game_2
        "Izunaville":
            jump xmasST_natsumi_wrong

label xmasST_natsumi_game_2:
    show natsumi a_8
    natsumi "Yey!"
    show natsumi a_9
    natsumi "Okay, next question!"
    menu:
        natsumi "What is Sadie-Lynn's last name? No google!"
        "Kobayashi":
            jump xmasST_natsumi_game_3
        "Grandales":
            jump xmasST_natsumi_wrong
        "Otani":
            jump xmasST_natsumi_wrong

label xmasST_natsumi_game_3:
    show natsumi a_8
    natsumi "Yey! You got that right too!"
    show natsumi a_9
    john "Who even is that? That was a pure guess."
    natsumi "That's not important. Final question!"
    menu:
        natsumi "How many students are officially known to be in the Student Council of Tina Koya High?"
        "Two":
            jump xmasST_natsumi_wrong
        "Three":
            jump xmasST_natsumi_game_4
        "Four":
            jump xmasST_natsumi_wrong

label xmasST_natsumi_game_4:
    $ xmasST_natsumi_game_completed = True
    show natsumi a_8
    natsumi "You did it!"
    show natsumi a_9
    natsumi "You really earned this tea. Congratulations!"
    $ tea = True
    show xmasST_asset teacup:
        center
        xpos 0.885
        ypos 1.0
    with dissolve
    "You added tea to your inventory."
    natsumi "You can enjoy it yourself or give it to someone else. Good luck doing what you're doing!"
    jump xmasST_wagon_3

label xmasST_natsumi_wrong:
    show natsumi a_5
    natsumi "That's not right at all."
    natsumi "You're a big stinky, you don't even know that."
    show natsumi a_0
    natsumi "Go practice and try my super duper quiz again!"
    jump xmasST_wagon_3

label xmasST_rayne:
    outfit xmasST_rayne dress
    show xmasST_bg wagon 4
    show xmasST_asset overlay1:
        xalign 0.5
    show john b_6 at centerright, faceleft
    show xmasST_rayne a_17 at centerleft, faceright
    with dissolve
    if xmasST_rayne_coin == False:
        if xmasST_rayne_spoken == False:
            $ xmasST_rayne_spoken = True
            xmasST_rayne "Oh! Oho! If it isn't the one whose name I cannot remember!"
            john "Oh, it's just {i}you{/i}."
            show xmasST_rayne c_13
            xmasST_rayne "Did you perhaps learn anything since last we met about animals and their worth in life?"
            john "Are you just the dedicated vegan of this place?"
            xmasST_rayne "Naturally!"
            show xmasST_rayne a_5
            xmasST_rayne "Could there be a possibility that you know why the train has stopped?"
            john "The conductor needs a key to get into some sort of box, until then we won't be moving."
            xmasST_rayne "Ah. What a shame."
            show xmasST_rayne b_4
            xmasST_rayne "I always knew that vehicles running on fossil fuel are grossly inadequate."
            show xmasST_rayne c_13
            xmasST_rayne "No matter. For a donation towards the P.E.T.A. foundation, which is short for Pet Every Tiger Around, I {i}could{/i} grant you a bit of information."
            john "Aren't you just as stuck as I am here?"
            xmasST_rayne "Let's just say it's not for personal profit."
            if coin == True:
                menu:
                    "Give her a coin?"
                    "Yes":
                        $ coin = False
                        $ xmasST_rayne_coin = True
                        show xmasST_rayne b_24
                        "Rayne has taken your coin."
                        xmasST_rayne "Thank you very much!"
                        show xmasST_rayne b_19
                        xmasST_rayne "In the very back of the train you will find something useful. Telling you will make you aware, but you might need it."
                        john "How do you know that?"
                        show xmasST_rayne c_14
                        xmasST_rayne "Let's just call it convenient magic!"
                        jump xmasST_wagon_4
                    "No":
                        xmasST_rayne "Ah well. You will likely succeed either way. Good luck!"
                        jump xmasST_wagon_4

            else:
                john "I don't have any money on me."
                xmasST_rayne "What a shame. Nonetheless, I am sure you will succeed either way. Good luck!"
                jump xmasST_wagon_4
        else:
            xmasST_rayne "How about it? Would you like to donate for information?"
            if coin == True:
                menu:
                    "Give her a coin?"
                    "Yes":
                        $ coin = False
                        show xmasST_rayne b_24
                        "Rayne has taken your coin."
                        xmasST_rayne "Thank you very much!"
                        show xmasST_rayne b_19
                        xmasST_rayne "In the very back of the train you will find something useful. Telling you will make you aware, but you might need it."
                        john "How do you know that?"
                        show xmasST_rayne c_14
                        xmasST_rayne "Let's just call it convenient magic!"
                        jump xmasST_wagon_4
                    "No":
                        xmasST_rayne "Ah well. You will likely succeed either way. Good luck!"
                        jump xmasST_wagon_4

            else:
                john "I don't have any money on me."
                xmasST_rayne "What a shame. Nonetheless, I am sure you will succeed either way. Good luck!"
                jump xmasST_wagon_4
    else:
        xmasST_rayne "Thanks for the donation again! Make sure to check the very back of the train!"
        jump xmasST_wagon_4

label xmasST_johnGB:
    $ johnGB.name = "Jane"
    outfit johnGB casual
    show xmasST_bg wagon 4
    show xmasST_asset overlay1:
        xalign 0.5
    show john b_1 at centerright, faceleft
    show johnGB a_4 at centerleft, faceright
    with dissolve
    john "Hey there. Would you perhaps know of a key somebody lost around here?"
    johnGB "A key? I'm afraid not. Is that why the train isn't moving?"
    john "Yeah. By the way, you look really familiar."
    johnGB "I had the exact same thought just now. Guess we met before?"
    john "That's likely. Anyways, I need to be off."
    johnGB "Good luck finding it."
    jump xmasST_wagon_4

label xmasST_bear:
    show xmasST_bg wagon 5
    show xmasST_asset overlay1:
        xalign 0.5
    show john b_4 at centerright, faceleft
    show xmasST_asset bear at centerleft
    with dissolve
    "The bear-like creature is looking at you with an intense stare."
    "A soul-piercing stare penetrates your very body, eagerly awaiting for a command or action."
    menu:
        "What would you like to do?"
        "Leave with post-haste":
            jump xmasST_wagon_5
        "Give the bear a coin" if coin == True:
            $ coin = False
            "You give the bear a coin."
            "And..."
            "It still stands there. It licks it's lips as if they were dry."
            jump xmasST_wagon_5
        "Give the bear some tea" if tea == True:
            $ tea = False
            $ xmasST_bear_move = True
            "The bear sips the tea."
            "It lets out a silent growl of pleasure and starts moving and working again."
            "You spot a very out-of-place trapdoor that might be interesting."
            jump xmasST_wagon_5

label xmasST_bear_2:
    show xmasST_bg wagon 5
    show xmasST_asset overlay1:
        xalign 0.5
    show john b_4 at centerright, faceleft
    show xmasST_asset bear at centerleft
    with dissolve
    "The bear scoffs at your presence."
    "It loathes being in close proximity of your filthy human skin."
    "It judges by tossing it's many coins into the air, as if you were a mere peasant."
    "You feel the air tensening around you."
    "This feeling is the game turning from a point-and-click-visual-novel game, to an RPG game where you are meant to slay this bear."
    "Any moment now, a boss health meter will appear on screen."
    "But before that can happen, it decides to stop looking at you, freeing you from the grasp of it's sight and the could-have-been boss battle with the beast."
    jump xmasST_wagon_5

label xmasST_key:
    if kiyoshi_ == True:
        scene xmasST_bg wagon trapdoor
        show john b_9 at centerleft, faceright
        show kiyoshi b_10 at centerright, faceright
        show xmasST_asset key:
            xpos 0.87
            ypos 0.1
        with dissolve
        kiyoshi "It's up there?"
        show kiyoshi b_1
        kiyoshi "Child's play, I say."
        $ key = True
        show xmasST_asset key:
            center
            xpos 0.78
            ypos 1.0
        with dissolve
        "You got the key. Report back to Misha with it when you're ready."
        show kiyoshi at faceleft
        kiyoshi "There we go. I'll go back to the control center, I'll meet you there, W-girl."
        john "Yeah, thanks for the help."
        kiyoshi "Always, W-girl, always."
        jump xmasST_wagon_trapdoor
    if stick == True:
        $ key = True
        show xmasST_asset key:
            center
            xpos 0.78
            ypos 1.0
        with dissolve
        "You used the key and managed to bring it down fromt he shelves. You actually wonder how the hell you couldn't get the key in the first place, but that's an afterthought now that you have it in your hands."
        "You got the key. Report back to Misha with it when you're ready."
        jump xmasST_wagon_trapdoor
    else:
        $ kiyoshi_activated = True
        show screen item_search_wagon_trapdoor
        "You found the key, but it is too far up."
        "You need to figure out a way to get it from that height or have someone help you."
        jump xmasST_wagon_trapdoor

label xmasST_stick:
    $ stick = True
    show xmasST_asset stick inv:
        center
        xpos 0.825
        ypos 1.0
    "You borrowed a stick, which is very hard to see in the inventory, but believe the narrator on this, the stick is clearly there if you squint your eyes."
    "It is good luck to carry a hockey stick around in Canada, so maybe it is here too."
    jump xmasST_wagon_6



    screen item_search_tutorial_1:
        modal False
        imagebutton:
            ypos 0.3
            idle direct_path("xmasST_asset click izuna")
            hover direct_path("xmasST_asset click izuna")
            action [Hide("item_search_tutorial_1"), Jump("xmasST_tutorial_2")]

    screen item_search_tutorial_2:
        modal False
        imagebutton:
            xpos 0.668 ypos 0.552
            idle direct_path("xmasST_asset coin")
            hover direct_path("xmasST_asset coin hover")
            action [Hide("item_search_tutorial_2"), Jump("xmasST_tutorial_3")]

    screen item_search_wagon_1:
        modal False
        imagebutton:
            ypos 0.2
            xpos 0.4
            idle direct_path("xmasST_asset click misha")
            hover direct_path("xmasST_asset click misha")
            action [Hide("item_search_wagon_1"), Jump("xmasST_misha")]
        imagebutton:
            xpos 0.65
            ypos 0.2
            idle direct_path("xmasST_asset click kiyoshi")
            hover direct_path("xmasST_asset click kiyoshi")
            action [Hide("item_search_wagon_1"), Jump("xmasST_kiyoshi")]

    screen item_search_wagon_2:
        modal False
        imagebutton:
            ypos 0.3
            idle direct_path("xmasST_asset click izuna")
            hover direct_path("xmasST_asset click izuna")
            action [Hide("item_search_wagon_2"), Jump("xmasST_izuna")]

    screen item_search_wagon_3:
        modal False
        imagebutton:
            xpos 0.65
            ypos 0.42
            idle direct_path("xmasST_asset click natsumi")
            hover direct_path("xmasST_asset click natsumi")
            action [Hide("item_search_wagon_3"), Jump("xmasST_natsumi")]

    screen item_search_wagon_4:
        modal False
        imagebutton:
            xpos 0.65
            ypos 0.42
            idle direct_path("xmasST_asset click rayne")
            hover direct_path("xmasST_asset click rayne")
            action [Hide("item_search_wagon_4"), Jump("xmasST_rayne")]
        imagebutton:
            xpos 0.075
            ypos 0.42
            idle direct_path("xmasST_asset click johnGB")
            hover direct_path("xmasST_asset click johnGB")
            action [Hide("item_search_wagon_4"), Jump("xmasST_johnGB")]

    screen item_search_wagon_5_1:
        modal False
        imagebutton:
            xpos 0.15
            ypos 0.42
            idle direct_path("xmasST_asset click bear")
            hover direct_path("xmasST_asset click bear")
            action [Hide("item_search_wagon_5_1"), Jump("xmasST_bear")]

    screen item_search_wagon_5_2:
        modal False
        imagebutton:
            xpos 0.25
            ypos 0.75
            idle direct_path("xmasST_asset trapdoor")
            hover direct_path("xmasST_asset trapdoor hover")
            action [Hide("item_search_wagon_5_2"), Jump("xmasST_wagon_trapdoor")]
        imagebutton:
            xpos 0.65
            ypos 0.42
            idle direct_path("xmasST_asset click bear")
            hover direct_path("xmasST_asset click bear")
            action [Hide("item_search_wagon_5_2"), Jump("xmasST_bear_2")]

    screen item_search_wagon_6:
        modal False
        imagebutton:
            xpos 0.065
            ypos 0.2
            idle direct_path("xmasST_asset stick")
            hover direct_path("xmasST_asset stick hover")
            action [Hide("item_search_wagon_6"), Jump("xmasST_stick")]

    screen item_search_wagon_trapdoor:
        imagebutton:
            xpos 0.865
            ypos 0.1
            idle direct_path("xmasST_asset key")
            hover direct_path("xmasST_asset key hover")
            action [Hide("item_search_wagon_trapdoor"), Jump("xmasST_key")]

label xmasST_chapter_2_finale:
    $ gui.textbox_yalign = 1.0
    play music xmasST_bgm_we_wish_you fadein 1.5 fadeout 1
    scene black with wipeblinds_horiz
    pause 2
    scene xmasST_bg wagon 1
    show john b_1 at centerleft, faceright
    show kiyoshi b_23 at left, faceright
    show xmasST_misha a_9 at centerright, faceleft
    with wipeblinds_horiz
    xmasST_misha "You found my key then?"
    john "Yeah, here you go."

    show xmasST_misha b_0
    xmasST_misha "Very good. You are not so little girls after all. You are dependable girls then."
    xmasST_misha "I will make sure you get pocket change when we arrive."
    kiyoshi "It better be at least a 100 dollars."

    show xmasST_misha a_5
    xmasST_misha "Do not get content, tall girl."

    show kiyoshi a_8
    kiyoshi "{i}Eek!{/i} Sorry!"

    scene xmasST_bg winter 1
    show izuna a_5 at center, faceleft
    show john a_12 at centerright, faceleft
    show kiyoshi a_23 at centerleft, faceright
    with sawleft
    "We finally arrived after a very extended train-trip."
    "What awaited us wasn't exactly what I had thought at first though."
    john "So, where now? I'm freezing to death here."
    izuna "..."

    show john b_7
    john "Hello?"

    show izuna a_1 at faceright
    izuna "Oh! Right! I, uh... Am not familiar with where the trainstation is on the North Pole, so I just need to look around a bit to make sure I know where we are."
    john "...Are you sure you have everything under control?"

    show izuna a_4
    izuna "Of course, of course!"

    scene xmasST_bg winter 2
    show izuna a_5 at center, faceright
    show john b_10 at centerleft, faceright
    show kiyoshi b_12 at left, faceright
    with wiperadial_horiz
    izuna "This is... A town?"
    john "For real, do you have any idea where we are or do we have to ask a local?"

    show izuna a_2 at faceleft
    izuna "I... Guess we could ask a local..."
    john "Great. Hey! Excuse me?!"

    show yoshinori a_0 at right, faceleft with dissolve
    show izuna a_1 at faceright
    $ yoshinori.name = "Elderly Man"
    "I saw an elderly man walking past in a hurry, so we could as well ask."
    yoshinori "Yes?"
    john "Can you tell us where exactly we are in this world?"

    show yoshinori a_1
    yoshinori "Where we are? What a curious question."
    yoshinori "This is Winter's City."

    show izuna a_0
    izuna "Wait, isn't Winter's City a town in the South Pole...?"

    show john b_5
    show kiyoshi b_8
    show yoshinori a_0
    john "What?!"
    kiyoshi "South Pole?!"
    yoshinori "Why yes of course it is. Did you expect the North Pole perhaps?"

    show yoshinori a_2 at offscreenright, faceright with ease
    yoshinori "Ahahah, kids these days, I tell you!"

    show izuna a_6 at faceleft
    izuna "Uhm..."
    izuna "Oops?"

    scene black with dissolve
    pause 1
    "That moment I understood that the Polar Express goes to the North Pole, while the Bipolar Express goes to the South Pole."
    "Well, I guess everyone makes mistakes."
    "Except Izuna. She makes huge fuck-ups."

    gameover "Merry Christmas v2!"

    jump xmasST_chapter_select
