define n = Character('Narrator')
define p = Character('Me')
define bg = Character('The Bodyguard') #Shaun masters
define cd = Character('The Cloaked Dagger') #Casper beauregard
define kfc = Character('Key Frame Crusader') #Marcus Smith
define gb = Character('Golden Boy') #John summers
define tb = Character("[player_name] the Best")
define uk = Character("???")

#backgrounds
image bg island = "bg island day.png"
image bg islandnight = "bg island night.png"
image bg volcanoday = "bg volcanoChamber Day.png"
image bg volcanonight = "bg volcanoChamber Night.png"
image bg volcanosunset = "bg volcanoChamber sunset.png"
image bg volcanoerupt = "bg island nightEruption.png"

image bg beachday = "bg beachfront day.png"
image bg news = "bg news.png"
image bg cavern = "bg volcanoCavern.png"
image bg personalRoom = "bgb personalRoom.png"
image bg roomNight = "bgb personalRoom night.png"
image bg personalHallway = "bg personalHallway.png"
image bg inventionRoom = "bg inventionRoom.png"
image bg kitchenDay = "bg kitchen.png"
image bg kitchenNight = "bg kitchen night.png"
<<<<<<< HEAD
<<<<<<< HEAD
=======
image bg doorsDay = "bg metalDoors days.png"
image bg doorsNight = "bg metalDoors night.png"
image bg secRoom = "bg securityRoom.png"
>>>>>>> main
=======
image bg doorsDay = "bg metalDoors days.png"
image bg doorsNight = "bg metalDoors night.png"
image bg secRoom = "bg securityRoom.png"
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978

#characters
image a_neutral = "ardbert neutral.png"
image a_talking = "ardbert neutral talking.png"
image c_neutral = "casper neutral.png"
image c_talking = "casper neutral talking.png"
image j_neutral = "john neutral.png"
image j_talking = "john neutral talking.png"
image m_neutral = "marcus neutral.png"
image m_talking = "marcus neutral talking.png"
image s_neutral = "shaun neutral.png"
image s_talking = "shaun neutral talking"

#character relationship variables
default cdRel = 1
default kfcRel = 1
default bgrel = 1
default tbRel = 1
default GBRoute = "No"
default gbRel = 0

label start:
   stop music
   play music "audio/Happy.mp3"

   # okay so add bg island.jpg or .png  to images directory
   scene bg island 

   # pre-establish the lore(TM)
   n "You can see it in the distance, at first just a little spec on the horizon but now fully coming into view-- The Island."
   p "This is where the note said I'd find the lair..."
   n "You notice the large volcano the note said Golden Boy's lair would be within."
   p "....Wow that's...really just...a whole volcano, huh?"
   n "While you wait for your boat to reach shore, you think of how your legacy will forever change if you accomplish this mission."
   n "You will no longer be a low-level pest of a villian to Sunnydayle Valley's only hero."
   n "You will finally be known for more than just stealing traffic cones, stealing from Christmas Charity Buckets, and printing off fake money."
   n "You will finally be seen for what you are-- a supervillian."
   n "The world will one day remember the name of...who will they remember the name of?"

   #player name moment
   $ player_name = renpy.input("What is your name?")
   #gets rid of extra spaces in name
   $ player_name = player_name.strip()
   #in case player enters nothing
   if player_name == "":
     n "Well the world must remember something...hmm.. how about something dark and scary... Susan"
     $ player_name="Susan"
     #checking

   n "You're now nearly there. Thankfully, the anonymous note said it would be easy to slip inside Golden Boy's lair within the volcano itself, giving you plenty of time to lay a trap and ruin his day."
   n "Your boat finally reaches shore... but something in your gut is urging you to reconsider. If you want to turn back, something tells you that now is your only chance."
   menu StayorGo:
    p "Do I leave?"

    "<Leave island>":
        jump BadEnd
    "<Continue to volcano>":
        jump Day1
    
label BadEnd:
        stop music
<<<<<<< HEAD
        play music "audio/Sad.mp3"
=======
        play music "audio/Test.wav" volume 0.25
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
        n "You stare at the volcano for a long while, weighing your options."
        p "Yeah...yeah no I think I'll pass on this one."
        "ONE WEEK LATER"
        
        scene bg news with dissolve
        p "Holy shit..."
        "The bodies of four known villians were found in the volcanic ruins of Hot-Hot-Romantic-Summer-Island-Firey-Passion Island, informally known as Jenny Island."
        "The Bodyguard, [player_name] the Best, The Key Frame Crusader, and the Cloaked Dagger were found early this morning. Local authorities have stated they are still looking for the culprit, and what this means for the city at large."
        n "Things are about to be a lot different now... but you can help but wonder, who gave you that note? What had happened if you had stayed? You suppose you will never truly know."
        ".:. Bad Ending."
        return 

label Day1:
    scene bg cavern with dissolve
    stop music
    play music "audio/Test.wav"

    n "Eventually, you make your way through the island's greenery and arrive at the entrance of the volcano."
    n "As the note suggested, the opening wasn't hard to find. There was some cover, but you are the greatest supervillian in the area, so it's not surprising you so easily detected the hidden cavernous entrance."
    n "As you enter, carefully walking forward, you see a door just up ahead in the cavern."
    p "Bingo."
    n "You begin heading toward the door when-"
    # Future bang noise (game/audio directory)? -> play sound "file ext"
    "BANG!"
    n "The cavern fills with the sounds of loud grinding noises as the cavern entrance is suddenly closed off by a large door."
    p "NO NO NO NO"
    
    menu door1:
        p "What do I do?"
        "<Head to door at the end of the cavern>":
            jump CharacterIntros
        "<Try to get the door open>":
             n "There's no use. You left all your gizmos on the boat and all your gadgets at home. This door isn't going to budge without something more than your own two hands."
             n "Certain there's no other options, you head to the door at the end of the cavern."

label CharacterIntros:
        scene bg doorsDay
        with dissolve
        p "Wouldn't be the first time I walked into a trap... but what kind of trap is this supposed to be?"
        n "Ahead, you hear what sounds like... arguing? You can't make out where they are saying but it seems to be multiple voices on the other side of the door bickering."
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        n "Determined to keep pushing forward, you make your way towards the other door. The door easily slides open as you step inside, attempting to be quiet as you continue inside."
=======
        n "Determind to keep pushing forward, you make your way towards the other door. The door easily slides open as you step inside, attempting to be quiet as you continue inside."
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f
=======
        n "Determined to keep pushing forward, you make your way towards the other door. The door easily slides open as you step inside, attempting to be quiet as you continue in."
>>>>>>> main
=======
        n "Determined to keep pushing forward, you make your way towards the other door. The door easily slides open as you step inside, attempting to be quiet as you continue in."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978

        # Future bang noise (game/audio directory)? -> play sound "file ext"
        n "BANG!"
        p "Shit."
        n "The noise of the door locking behind you echoes throughout, alerting the group of people ahead of your presence."
        
        scene bg volcanoday
        #talking to The Best
        show a_neutral
        with dissolve
        n "The first one to speak is a familiar pompous, purple-haired, and extravagantly dressed man. "
        show a_talking
        hide a_neutral
        tb "%(player_name)s!"
        show a_neutral
        hide a_talking
        p "Oh not this guy."
        n "You, unfortunately, are very familiar with %(player_name)s the Best. Your worst enemy. The most insufferable man you've ever met."
        show a_talking
        hide a_neutral
        tb "Oh for God's sake why are YOU here? No, no, why are any of us here?"
        show a_neutral
        hide a_talking
        p "I was given a note. I'm assuming you all were as well?"
        show a_talking
        hide a_neutral
        tb "No, no, I was told I alone was being told this location."
        show a_neutral
        hide a_talking
        p "Evidently fucking not."

        #talking to Cloaked Dagger
        n "A different voice speaks up, quietly, disregarding you completely."
        hide a_neutral
        show c_talking
        with dissolve
        uk "The doors have seemingly locked."
        hide c_talking
        show c_neutral
        n "The cloaked figure walks past you toward the toward, testing his correct hypothesis. You know this figure. It takes you a moment to place it, but when you do the memories rush back."
        n "You competed against them--The Cloaked Dagger-- to earn a position as a henchman for famous supervillian Charismata."
        show c_talking
        hide c_neutral
        cd "Any suggestions on how we are meant to escape now, gentlemen?"
        hide c_talking

        #talking to The Bodyguard
        show s_neutral
        with dissolve
        n "Before you have time to answer, a large and burly man speaks up. A man whose voice you could recognize in an instant."
        hide s_neutral
        show s_talking
        bg "%(player_name)s? Is that you?"
        hide s_talking
        show s_neutral
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        n "Your childhood friend. Shaun. He goes by The Bodyguard now, last you heard. You can't remember the last time you spoke to one another."
        p "The Bodyguard? What's going on here?"
=======
        n "Your childhood friend. Shaun. He goes by the Bodyguard now, last you heard. You can't remember the last time you spoke to one another."
        p "Bodyguard? What's going on here?"
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f
=======
        n "Your childhood friend. Shaun. He goes by The Bodyguard now, last you heard. You can't remember the last time you spoke to one another."
        p "The Bodyguard? What's going on here?"
>>>>>>> main
=======
        n "Your childhood friend. Shaun. He goes by The Bodyguard now, last you heard. You can't remember the last time you spoke to one another."
        p "The Bodyguard? What's going on here?"
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
        hide s_neutral
        show s_talking
        bg "I'm... not sure. "
        bg "Though... I don't think it's all that hard to put together."
        hide s_talking
        show s_neutral
        p "What do you mean?"
        hide s_neutral
        show s_talking
        bg "Look around. All five of us came here because of a note given to us. All fivr of us are villians. It's simple."
        hide s_talking

        #talking to KFC
        p "Five?"
        n "you notice now the fifth among you, a rather stunning individual with long, flowing green hair."
        show m_talking at left
        with dissolve
        kfc "Woah woah woah, hold on I'm not a 'villian'"
        hide m_talking at left
        show m_neutral at left
        with dissolve
        n "You know this man as the Key Frame Crusader. Formerly a hero who had recently taken up the mantle of villainy."
        n "He pay not be a villian but he's certainly a public nuisance."
        show s_talking at right 
        bg "You have been arrested for several counts of theft and dispersion of illegally-owned media."
        hide s_talking at right
        hide m_neutral at left
        show m_talking 
        kfc "Blah blah blah semantics. It's complicated."
        hide m_talking

        menu:
            n "Arguing begins amongst them, the same bickering you had heard before entering in the door."
            "<Is this really what's important right now guys?>":
                jump CavernDay1
            "<So, if we were lured here, what do they want?>":
                jump CavernDay1
            "<SHUT UP>":
                n "everyone looks at you expectantly, all clearly agitated"
                $ bgRel =- 1
                $ cdRel =- 1
                $ kfcRel =- 1
                $ tbRel =- 1
                jump CavernDay1

label CavernDay1:
         n "Before anyone has time to answer, a voice rings out from the PA system that of course this volcano happens to have."
         n "Unlike all of the voices and faces before, this voice is... unrecognizable. It was distorted, the words barely distinguishable amidst the static."
         uk "Congratulations, my friends."
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
         uk "As you may have guessed, you have all been brought here under what one might call false pretenses."
=======
         uk "As you may have guessed, you have all been brought here under what one might call, false pretense."
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f
=======
         uk "As you may have guessed, you have all been brought here under what one might call false pretenses."
>>>>>>> main
=======
         uk "As you may have guessed, you have all been brought here under what one might call false pretenses."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
         uk "I'm sorry to have to tell you this, but this volcano is set to explode in three days. Which means that should you not manage to escape, you'll be burnt to ash."
         n "Well that's... lovely."
         uk "But! I do have good news."
         p "Oh yay, good news."
         uk "I can hear you, you know. Like I can actively hear you being sarcastic."
         p "No?"
         uk "What do you mean no? I can literally- You know what? Nevermind."
         uk "You have three days to make a love connection with one another. If you can convince me you're being authentic, then I will free you before the volcano explodes."
         n "Everyone goes quiet. What? A love connection? Three days? Your head hurts."
         
         menu:
            "<You sick fuck>":
                uk "I'm sorry...I'm doing what I must."
                jump CavernSunset1
            "<Stay Silent>":
                jump CavernSunset1

label CavernSunset1:
    scene bg volcanosunset
    with dissolve

    n "As quickly as the voice came, it went. For a moment, all is quiet throughout the volcano."
    "BANG BANG BANG"
    show a_talking with dissolve
    tb "LET ME OUT. LET ME THE FUCK OUT OF HERE. FUCKING SHIT BITCH."
    hide a_talking
    n "Good thing he didn't overreact"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    n "You turn away from %(player_name)s the Best banging on the metal doors to the Bodyguard. The taller man only looks back to you for a moment before leaving."
=======
    n "You turn away from %(player_name)s banging on the metal doors to the Bodyguard. The taller man only looks back to you a moment before leaving."
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f
=======

    n "You turn away from %(player_name)s the Best banging on the metal doors to the Bodyguard. The taller man only looks back to you for a moment before leaving."
>>>>>>> main
=======

    n "You turn away from %(player_name)s the Best banging on the metal doors to the Bodyguard. The taller man only looks back to you for a moment before leaving."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
    n "You notice then that him, the Key Frame Crusader, and the Cloaked Dagger were all heading to rooms built into the central chamber."
    n "Whoever your host is, at least they were generous enough to give you beds."
    n "Still, even as you approach your own quarters, you don't feel capable of rest just yet."
    jump Night1Choice

label Night1Choice:
    stop music
    play music "audio/Emotional.mp3"
    scene bg volcanonight
    define visited = set()
    default visitconfirm = "No"
    menu NightChoice1:

        set visited
        n "What will you do?"

        # Scorching End 1
        "<Go Straight to Bed>" if visitconfirm == "No":
            scene bg personalRoom
            jump ScorchingEnd1

        "<Talk to [player_name] the Best>":
            $ visitconfirm = "Yes"
            jump TalktoTB

        "<Follow the Cloaked Dagger>":
            $ visitconfirm = "Yes"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        
=======
>>>>>>> main
            jump FollowCD

        "<Follow the Bodyguard>":
            $ visitconfirm = "Yes"
<<<<<<< HEAD
=======
            scene bg personalHallway
=======
            jump FollowCD
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978

        "<Follow the Bodyguard>":
            $ visitconfirm = "Yes"
            scene bg personalHallway
<<<<<<< HEAD
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f

=======
            scene bg personalHallway
>>>>>>> main
=======
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
            jump FollowBG

        "<Follow the Key Frame Crusader>":
            $ visitconfirm = "Yes"
            scene bg personalHallway
            jump FollowKFC
       
        #secret ending start
        "<Investigate the seam in the wall>" if visitconfirm == "No":
            $ visitconfirm = "Yes"
            $ GBRoute = "Yes"
            jump InvestigateSeam

        #Finish Day 1
        "<Call it a night>" if visitconfirm == "Yes":
<<<<<<< HEAD
<<<<<<< HEAD
            scene bg personalRoom
            p "...What the fuck"
            n "Your room is not quite what you expected. The dull room with a weirdly detailed rug, washed in shades of pinks, purples, and reds."
            n "It wasn't exactly what you expected in a situation where you are functionally kidnapped, but that's not necessarily bad?"
            menu DreamNight1:
                n "Who do you dream of in the night?"
                "The Cloaked Dagger":
                    "Your mind is filled with thoughts of his masked face, the swift way in which his capes move, and the way he caught your eye. Will he be the one?"
                    $ cdRel =+ 1
                "The Bodyguard":
                    "Your mind is filled with thoughts of your childhood together, memories you had thought were forgotten now coming to the surface. You truly had missed him more than you though. Will he be the one?"
                    $ bgRel =+ 1
                "The Key Frame Crusader":
                    "Your mind is filled with thoughts of his green flowing hair, the sway of his hips, and the mystery behind his motivations. Will he be the one?"
                    $ kfcRel =+ 1
                "[player_name] the Best":
                    "Your mind is filled with... well, thoughts of you? Not quite you, though. You but better. Is [player_name] the Best really that much better? More importantly, will he be the one?"
                    $ tbRel =+ 1
                "Golden Boy" if GBRoute == "Yes":
                    "Your mind is filled with the thoughts of your rival, your enemy, and maybe your last hope. Would he come to save you? Would he miss you? Why couldn't he be the one with you here?"
                    $ gbRel =+ 1
            n "You are unsure of what the morning will bring, but you suppose you'll have to be prepared whether you want to be or not."
            jump Day2

>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f
label ScorchingEnd1:
    scene bg personalRoom
    play music "audio/ScorchingEnd1.wav" volume 0.25

    p "...What the fuck"
    n "Your room is not quite what you expected. The dull room with a weirdly detailed rug, washed in shades of pinks, purples, and reds."
    n "It wasn't exactly what you expected in a situation where you are functionally kidnapped, but that's not necessarily bad?"
    n "You have trouble falling asleep, as if your body is urging you not to. Even still, you ignore it and eventually sleep takes you."
    n "The following three days were... not good for you"
    n "Having missed out on your initial chances for connection with your fellow villians, they paired off in the night without you."
    n "[player_name] the Best and The Bodyguard eventually found a romantic connection, sharing a tender moment as they realize they both share a connection to you."
    n "The Cloaked Dagger and Key Frame Crusader paired up by Day 2, at first out of necessity and convenience, but quickly discovered they did both share a surprising love connection."
    n "The two couples are permitted to leave, but you are not."

    scene bg volcanoerupt with dissolve

    n "You die alone and burning."
    n "Nobody will remember you"
    n "Golden Boy never even knew who you were."
    n "You have always been an obstacle and you were finally removed, proving your own lesser status."
    n "Did it have to be this way?"
    n "Was that the only way this could have ended?"

    ".:. SCORCHING END 1"


    return

<<<<<<< HEAD
label InvestigateRoom:
=======
label InvestigateSeam:
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f
    "THIS ROUTE IS UNDER CONSTRUCTION"
    jump NightChoice1

label TalktoTB:
    scene bg volcanonight

    n "turning around again, you see [player_name] the Best still hammering on the wall and whailing."
    show a_neutral with dissolve
    p "Good to know he's still annoying as ever."
    n "You move closer to him and once you're only a few steps away, he turns around frantically."
    hide a_neutral 
    show a_talking with dissolve
    tb "YOU!"
    hide a_talking
    show a_neutral with dissolve
    p "Me?"
    hide a_neutral 
    show a_talking with dissolve
    tb "No I'm talking to the other [player_name] in the room with us. YES, I'm talking to you, dumbass."
    hide a_talking
    show a_neutral with dissolve
    n "Rude"
    hide a_neutral 
    show a_talking with dissolve
    tb "You are behind this all. I know it was you. You... you LURED me here. You knew I would want to find Golden Boy's lair and you LIED."
    hide a_talking
    show a_neutral with dissolve
    menu:
        "Wait, you got the same anonymous tip?":
            n "He looks confused at you for a second, but eventually he nods."
            hide a_neutral 
            show a_talking with dissolve
            tb "Yeah. It--YOU--said that I would find him here and that I would have the leg up because I was the only one who would know this."
            hide a_talking
            show a_neutral with dissolve
            p "[player_name] the Best, you know I didn't do this. I'm just as trapped here as you."
            tb "They seem skeptical, but are resigned to the fact that the choice is to either trust you or die"

        "You are going crazy, I didn't send you anything.":
            n "He looks at you skeptically, unbelieving."
            hide a_neutral 
            show a_talking with dissolve
            tb "Mhm sure. Whatever you say, creep. Get me out of here. Now."
            hide a_talking
            show a_neutral with dissolve
            p "I am not lying, I really didn't. I got an anonymous tip telling me this was Golden Boy's lair and I showed up. It said I was the only one who was being told this."
            n "His disbelief slowly melts into something closer to apathy. He may have no choice but to believe you in order to survive."

    tb "I'm going to bed"
    hide a_talking
    show a_neutral with dissolve
    menu:
        n "What do you say?"

        "You're going to die here":
            $ tbRel =- 1
            n "Woah. Intense much?"
            n "He flips you off as he leaves, returning to his own room."
            hide a_neutral
            n "Well, where to now?"
            jump NightChoice1
        "Goodnight, [player_name] the Best.":
            $ tbRel =+ 1
            n "He looks at you over his shoulder and gives a soft but confused smile."
            hide a_neutral 
            show a_talking with dissolve
            tb "Goodnight, [player_name]"
            hide a_talking
            n "Well, where to now?"
            jump NightChoice1
        "<Stay Silent>":
            hide a_neutral
            n "He leaves standing alone in the central chamber of the volcano."
            n "Well, where to now?"
            jump NightChoice1
            
label FollowCD:
<<<<<<< HEAD
    scene bg personalHallway
    n "As you and the others make your way into the hallway lined with doors, you follow closely behind the Cloaked Dagger."
    show c_neutral with dissolve
    n "Out of everyone, the cloaked figured seems to have the best head on his shoulders. They seem observant, if nothing else."

    #scene bg inventionRoom
    n "You follow him throughout the halls and through one of the doors, a large and open room full of shelves that contain various gizmos and gadgets."
    n "As you explore the space, you turn to see the Cloaked Dagger staring at you with a masked expression."
    p "Uh, can I help you?"
    hide c_neutral
    show c_talking
    cd "No, not likely. Not yet, anyway."
    hide c_talking
    show c_neutral
    p "That's so cryptic dude, what does that even mean?"
    hide c_neutral
    show c_talking
    cd "Not sure yet."
    cd "Whoever our gratious host is, they've left some things behind for us."
    cd "Whose to say we can't use some of these things to escape?"
    hide c_talking
    show c_neutral
    n "You gesture toward the sky-- toward the non-corporeal voice they had heard over the PA"
    p "The man in the sky, as it seems."
    hide c_neutral
    show c_talking
    cd "That's what they want us to think. Regardless, it's a good backup in case none of us can be convincing enough to pretend to fall in love in a few days."
    hide c_talking
    show c_neutral
    p "Pretend? What if they figure it out?"
    n "He shrugs, nonchalant as if this situation were not a cause for panic."
    hide c_neutral
    show c_talking
    cd "Guess you'll have to figure out how to be a good actor these next few days."
    hide c_talking
    show c_neutral
    menu:
        "And you are a good actor?":
            $ cdRel =+ 1
            hide c_neutral
            show c_talking
            cd "Wouldn't you like to find out?"
            hide c_talking
        "I don't want to fake it. I want to fall in love.":
            hide c_neutral
            show c_talking
            cd "How charming. Childish, but charming."
            hide c_talking
        "I don't want to fall in love at all. I'd rather die.":
            $ cdRel =- 1
            hide c_neutral
            show c_talking
            cd "You'll doom us. Or well, you'll doom yourself. I suppose that will make it easy for someone to be left behind."
            hide c_talking
            n "Oh, that's right- there's five of you. One of you is doomed to die."
            n "Unless your kidnapper is surprisngly progressive in the realms of accepting polyamory."
    show c_talking
    cd "Regardless, this equipment may help us should we wish to pursue that."
    hide c_talking
    show c_neutral
    n "As if both yours and the Cloaked Dagger's eyes were magnets, they were both drawn to the security camera in the corner of the room."
    p "You seeing what I'm seeing?"
    n "You can see the other nod in your peripheral."
    hide c_neutral
    show c_talking
    cd "Shall we reconvene at a later time and a different... location?"
    hide c_talking
    n "You return to the hallway you came from, leaving the Cloaked Dagger behind in the Invention room."
=======
    #scene bg
    "UNDER CONSTRUCTION"
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f

    jump Night1Choice

label FollowBG:
<<<<<<< HEAD
    scene bg personalHallway
    n "Sometimes it's easier to stick to what you know, especially when you know so, so little."
    show s_neutral
    n "You follow your former friend down the hallway, letting the chord of connection you share pull you in the direction he walked."
    n "He stops in front of a door, a small gold plaster on the door with the name 'The Bodyguard' written on it."
    p "Are you okay?"
    n "Hearing your voice, he turns around to give you his full attention."
    hide s_neutral
    show s_talking
    bg "Ah. [player_name]. It's..."
    hide s_talking
    show s_neutral
    p "Been a while? Yeah.  Yeah, I know."
    n "There is a somber moment shared between you, standing in the hallway of your captor."
    hide s_neutral
    show s_talking
    bg "Are you well? Other than uh, present circumstances?"
    hide s_talking
    show s_neutral
    menu:
        "I've been better":
            n "He clears his throat awkwardly."
            hide s_neutral
            show s_talking
            bg "Yeah, I get that."
        "Never been better, other than present circumstances":
            n "He gives a soft smile at that"
            hide s_neutral
            show s_talking
            bg "I'm glad."
            hide s_talking
            show s_neutral
            p "And you?"
            hide s_neutral
            show s_talking
            bg "Oh you know, living the dream."
        "I'll give you one guess":
            $ bgRel =- 1
            n "He opens his mouth to speak, but slowly closes it with a wince."
            hide s_neutral
            show s_talking
            bg "I suppose that's fair."
    n "You point at the plaque above his door."
    p "Assigned rooms, then?"
    hide s_neutral
    show s_talking
    bg "I guess so. Guess whoever it is planned for us to be spending a few nights here afterall."
    hide s_talking
    n "Well, it certainly meant... something."
    n "You talk a bit more about the circumstances at hand and your shared past, but eventually the Bodyguard takes his leave and slips inside his room."
    n "Returning to the main chamber, you can't help but wonder what the others think is going on."
=======
    #scene bg
    "UNDER CONSTRUCTION"
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f

    jump Night1Choice

label FollowKFC:
    #scene bg
    "UNDER CONSTRUCTION"

    jump Night1Choice
=======
            jump CallitaNight
>>>>>>> main

<<<<<<< HEAD
=======
            jump CallitaNight

>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
label CallitaNight:
            scene bg roomNight with dissolve
            p "...What the fuck"
            n "Your room is not quite what you expected. The dull room with a weirdly detailed rug, washed in shades of pinks, purples, and reds."
            n "It wasn't exactly what you expected in a situation where you are functionally kidnapped, but that's not necessarily bad?"
<<<<<<< HEAD
            play sound "audio/knock sound.mp3" volume 0.25
=======
            play sound "audio/knock sound.mp3" volume 0.75
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
            "KNOCK KNOCK"
            n "The knocking noise on your door catches your attention"
            bg "[player_name], are you in there?"
            n "Recognizing the voice of your childhood friend, you peak your head out into the hallway."
            scene bg personalHallway with dissolve
            show m_neutral at Position(xpos = 0.15)
            show c_neutral at Position(xpos = 0.40)
            show s_neutral at Position(xpos = 0.65)
            show a_neutral at Position(xpos = 0.9)
            n "Facing you is all four of your fellow villians, staring at you."
            p "Is everything okay?"
            n "You see the Bodyguard point at your room, seemingly mouthing 'Talk Inside'"
            n "You shuffle into your room, quickly shutting the door once the last of you had filed in."
            hide s_neutral
            show s_talking at Position(xpos = 0.65)
            bg "Sorry, we needed to keep quiet."
            hide s_talking
            show s_neutral at Position(xpos = 0.65)
            hide c_neutral
            show c_talking at Position(xpos = 0.40)
            cd "The rooms are the only spaces without cameras. For now, we are under the assumption there is a but more privacy in here."
            hide c_talking
            show c_neutral at Position(xpos = 0.40)
            hide s_neutral
            show s_talking at Position(xpos = 0.65)
            bg "As far as we can tell anyway. I was looking around to find any clues and... well, didn't find much. Cameras. The inventions."
            bg "Whoever has us in here? I don't think they're kidding."
            hide s_talking
            show s_neutral at Position(xpos = 0.65)
            p "Why?"
            hide s_neutral
            show s_talking at Position(xpos = 0.65)
            bg "The lack of cameras in our room imples that well, our captor was prepared for a reality in which we were rather quickly fond of one another."
            hide s_talking
            show s_neutral at Position(xpos = 0.65)
            hide a_neutral
            show a_talking at Position(xpos = 0.9)
            tb "They didn't want to see us fucking, basically."
            hide a_talking
            show a_neutral at Position(xpos = 0.9)
            n "You see the Bodyguard scrunch his nose a bit at that."
            hide s_neutral
            show s_talking at Position(xpos = 0.65)
            bg "Yes. That."
            hide s_talking
            show s_neutral at Position(xpos = 0.65)
            hide a_talking
            show a_neutral at Position(xpos = 0.9)
            tb "Well suffice to say I am never going to romance [player_name], so I suppose one of you others will have to do."
            hide a_talking
            show a_neutral at Position(xpos = 0.9)
            p "Wow, fuck you too."
            hide a_neutral
            show a_talking at Position(xpos = 0.9)
            tb "You're my ultimate rival. You are the ruiner of days. The bane of my existence. Me but less better."
            tb "Or whatever, I don't care. Shut up. Why can't we just leave through the door, anyway?"
            hide a_talking
            show a_neutral at Position(xpos = 0.9)
            hide m_neutral
            show m_talking at Position(xpos = 0.15)
            kfc "The kitchen seems stalked for more than just three days, so someone probably lived here before. Even if it's fake, it does us no good to try to prove it's wrong."
            kfc "I did notice a locked door opposite of the rest of these, though. It's locked, unsurprisingly."
            hide m_talking
            show m_neutral at Position(xpos = 0.15)
            n "More discussions and theories were thrown at each other over the course of a few hours, and soon you all begin to grow tired."
            n "You still must decide how to best survive this, but you can all come to one agreement:"
            n "Whoever trapped you here must have been another villian, perhaps a newcomer, attempting to cull the competition."
            hide c_neutral
            show c_talking at Position(xpos = 0.40)
            cd "The door is impenetrable by normal means, but we seem to have an entire room of gadgets at our disposal."
            cd "[player_name] I know that is your realm of expertise, but should you choose that option, I would be more than happy to assist."
            hide c_talking
            show c_neutral at Position(xpos = 0.40)
            n "Other than a few grumbles from [player_name] the Best at the mention of your expertise, the group seems to nod along. It seems you have a free pick of the litter on who you'd like to assist you."
            hide m_neutral
            show m_talking at Position(xpos = 0.15)
            kfc "Even if the gadgets fail, we should pair up now in case we have to resort to faking our love connections."
            kfc "Like my Ma always used to say, a moment of embarrassment is nothing in comparison to potentially losing your life."
            hide m_talking
            show m_neutral at Position(xpos = 0.15)
            n "There is no way she said all that."
            n "But even then, it wasn't terrible advice."
            
            menu RouteChoice:
                 n "So, who will it be [player_name]?"
                 
                 ## START THE BEST'S ROUTE
                 "<[player_name] the Best?>":
                    $ tbRel =+ 1
                    hide c_neutral
                    hide a_neutral
                    hide s_neutral
                    hide m_neutral
                    show a_neutral
                    n "The grin that spread across the purple man's face almost made you wish you picked someone else."
                    hide a_neutral
                    show a_talking
                    tb "Well, naturally. Who else would you choose?"
                    n "Every moment of every day this man is hell bent on mimicing you, something you'll have to get used to now that you've signed him up as your partner."
                    n "If nothing else, he wants to be free of you as quickly as you want to be free of him-- something useful when looking for an escape partner."
                    hide a_talking
                    n "You notice the Bodyguard's wide shoulder's slump at finding out he wasn't chosen, but whatever emotions he had were quickly swept away."
                    n "Expressionless as always, the Cloaked Dagger gives a singular nod. You aren't sure, but you are certain the feather of his hat drooped ever so slightly."
                    n "Lastly, the Key Frame Crusader seemed like he barely registered any of the conversation anyway."
                    n "The green man was staring off ever since his comment about his mother, before shuffling after the Cloaked Dagger and the Bodyguard."
                    n "Lastly, [player_name] the Best leaves. He gives a once over, scanning you for something you could not determine, before giving a tense shadow of a smile and quickly turning on his feet to leave."
                    p "Every choice I have ever made in my life has somehow led to this exact moment."
                    n "It's as funny as it is depressing and surreal."
                    n "You dream of [player_name] the Best after slowly drifting off to sleep, your eyelids heavy and your heart even moreso at the thought of what would happen in the morning."
                    jump TheBestRouteDay2
                ## START THE CLOAKED DAGGER'S ROUTE
                 "<The Cloaked Dagger>":
                    $ cdRel =+ 1
                    jump CloakedDaggerRouteDay2
                ## START THE BODYGUARD'S ROUTE
                 "<The Bodyguard>":
                    $ bgRel =+ 1
                    hide c_neutral
                    hide a_neutral
                    hide s_neutral
                    hide m_neutral
                    show s_neutral
                    n "It is easy to tell that the Bodyguard has to hide a small smile when you turn to him. He seems to school his expression back the moment he realizes, but it was far too late at that point."
                    n "Unsurprisingly, given your history, he agrees to help you."
                    n "What is surprising is how kind he seemed to be even after all these years, something unexpected from a man of his size."
                    n "And boy was he a big man."
                    hide s_neutral
                    n "[player_name] the Best scoffs, clearly upset by his lack of being chosen and leaves the room."
                    n "Expressionless as always, the Cloaked Dagger gives a singular nod. You aren't sure, but you are certain the feather of his hat drooped ever so slightly."
                    n "Lastly, the Key Frame Crusader seemed like he barely registered any of the conversation anyway."
                    n "The green man was staring off ever since his comment about his mother, before shuffling after the Cloaked Dagger and [player_name] the Best."
                    n "The Bodyguard--Shaun-- leaves last, giving you yet another soft smile before slipping out the door and leaving you to yourself for the night."
                    p "Every choice I have ever made in my life has somehow led to this exact moment."
                    n "It's as funny as it is depressing and surreal."
                    n "You dream of Shaun after slowly drifting off to sleep, your eyelids heavy and your heart even moreso at the thought of what would happen in the morning."
                    jump BodyGuardRouteDay2
                ## START THE KEY FRAME CRUSADER'S ROUTE
                 "<Key Frame Crusader>":
                    $ kfcRel =+ 1
                    jump KFCDay2
           
label ScorchingEnd1:
    scene bg personalRoom
    stop music
    play music "audio/ScorchingEnd1.wav"

    p "...What the fuck"
    n "Your room is not quite what you expected. The dull room with a weirdly detailed rug, washed in shades of pinks, purples, and reds."
    n "It wasn't exactly what you expected in a situation where you are functionally kidnapped, but that's not necessarily bad?"
    n "You have trouble falling asleep, as if your body is urging you not to. Even still, you ignore it and eventually sleep takes you."
    n "The following three days were... not good for you"
    n "Having missed out on your initial chances for connection with your fellow villians, they paired off in the night without you."
    n "[player_name] the Best and The Bodyguard eventually found a romantic connection, sharing a tender moment as they realize they both share a connection to you."
    n "The Cloaked Dagger and Key Frame Crusader paired up by Day 2, at first out of necessity and convenience, but quickly discovered they did both share a surprising love connection."
    n "The two couples are permitted to leave, but you are not."

    scene bg volcanoerupt with dissolve

    n "You die alone and burning."
    n "Nobody will remember you"
    n "Golden Boy never even knew who you were."
    n "You have always been an obstacle and you were finally removed, proving your own lesser status."
    n "Did it have to be this way?"
    n "Was that the only way this could have ended?"

    ".:. SCORCHING END 1"


    return

label InvestigateSeam:
    "THIS ROUTE IS UNDER CONSTRUCTION"
    jump NightChoice1

label TalktoTB:
    scene bg volcanonight

    n "turning around again, you see [player_name] the Best still hammering on the wall and whailing."
    show a_neutral with dissolve
    p "Good to know he's still annoying as ever."
    n "You move closer to him and once you're only a few steps away, he turns around frantically."
    hide a_neutral 
    show a_talking with dissolve
    tb "YOU!"
    hide a_talking
    show a_neutral with dissolve
    p "Me?"
    hide a_neutral 
    show a_talking with dissolve
    tb "No I'm talking to the other [player_name] in the room with us. YES, I'm talking to you, dumbass."
    hide a_talking
    show a_neutral with dissolve
    n "Rude"
    hide a_neutral 
    show a_talking with dissolve
    tb "You are behind this all. I know it was you. You... you LURED me here. You knew I would want to find Golden Boy's lair and you LIED."
    hide a_talking
    show a_neutral with dissolve
    menu:
        "Wait, you got the same anonymous tip?":
            n "He looks confused at you for a second, but eventually he nods."
            hide a_neutral 
            show a_talking with dissolve
            tb "Yeah. It--YOU--said that I would find him here and that I would have the leg up because I was the only one who would know this."
            hide a_talking
            show a_neutral with dissolve
            p "[player_name] the Best, you know I didn't do this. I'm just as trapped here as you."
            tb "They seem skeptical, but are resigned to the fact that the choice is to either trust you or die"

        "You are going crazy, I didn't send you anything.":
            n "He looks at you skeptically, unbelieving."
            hide a_neutral 
            show a_talking with dissolve
            tb "Mhm sure. Whatever you say, creep. Get me out of here. Now."
            hide a_talking
            show a_neutral with dissolve
            p "I am not lying, I really didn't. I got an anonymous tip telling me this was Golden Boy's lair and I showed up. It said I was the only one who was being told this."
            n "His disbelief slowly melts into something closer to apathy. He may have no choice but to believe you in order to survive."

    tb "I'm going to bed"
    hide a_talking
    show a_neutral with dissolve
    menu:
        n "What do you say?"

        "You're going to die here":
            $ tbRel =- 1
            n "Woah. Intense much?"
            n "He flips you off as he leaves, returning to his own room."
            hide a_neutral
            n "Well, where to now?"
            jump Night1Choice
        "Goodnight, [player_name] the Best.":
            $ tbRel =+ 1
            n "He looks at you over his shoulder and gives a soft but confused smile."
            hide a_neutral 
            show a_talking with dissolve
            tb "Goodnight, [player_name]"
            hide a_talking
            n "Well, where to now?"
            jump Night1Choice
        "<Stay Silent>":
            hide a_neutral
            n "He leaves standing alone in the central chamber of the volcano."
            n "Well, where to now?"
            jump Night1Choice
            
label FollowCD:
    scene bg personalHallway with dissolve
    n "As you and the others make your way into the hallway lined with doors, you follow closely behind the Cloaked Dagger."
    show c_neutral with dissolve
    n "Out of everyone, the cloaked figured seems to have the best head on his shoulders. They seem observant, if nothing else."

    scene bg inventionRoom with dissolve
    n "You follow him throughout the halls and through one of the doors, a large and open room full of shelves that contain various gizmos and gadgets."
    n "As you explore the space, you turn to see the Cloaked Dagger staring at you with a masked expression."
    p "Uh, can I help you?"
    hide c_neutral
    show c_talking
    cd "No, not likely. Not yet, anyway."
    hide c_talking
    show c_neutral
    p "That's so cryptic dude, what does that even mean?"
    hide c_neutral
    show c_talking
    cd "Not sure yet."
    cd "Whoever our gratious host is, they've left some things behind for us."
    cd "Whose to say we can't use some of these things to escape?"
    hide c_talking
    show c_neutral
    n "You gesture toward the sky-- toward the non-corporeal voice they had heard over the PA"
    p "The man in the sky, as it seems."
    hide c_neutral
    show c_talking
    cd "That's what they want us to think. Regardless, it's a good backup in case none of us can be convincing enough to pretend to fall in love in a few days."
    hide c_talking
    show c_neutral
    p "Pretend? What if they figure it out?"
    n "He shrugs, nonchalant as if this situation were not a cause for panic."
    hide c_neutral
    show c_talking
    cd "Guess you'll have to figure out how to be a good actor these next few days."
    hide c_talking
    show c_neutral
    menu:
        "And you are a good actor?":
            $ cdRel =+ 1
            hide c_neutral
            show c_talking
            cd "Wouldn't you like to find out?"
            hide c_talking
        "I don't want to fake it. I want to fall in love.":
            hide c_neutral
            show c_talking
            cd "How charming. Childish, but charming."
            hide c_talking
        "I don't want to fall in love at all. I'd rather die.":
            $ cdRel =- 1
            hide c_neutral
            show c_talking
            cd "You'll doom us. Or well, you'll doom yourself. I suppose that will make it easy for someone to be left behind."
            hide c_talking
            n "Oh, that's right- there's five of you. One of you is doomed to die."
            n "Unless your kidnapper is surprisngly progressive in the realms of accepting polyamory."
    show c_talking
    cd "Regardless, this equipment may help us should we wish to pursue that."
    hide c_talking
    show c_neutral
    n "As if both yours and the Cloaked Dagger's eyes were magnets, they were both drawn to the security camera in the corner of the room."
    p "You seeing what I'm seeing?"
    n "You can see the other nod in your peripheral."
    hide c_neutral
    show c_talking
    cd "Shall we reconvene at a later time and a different... location?"
    hide c_talking
    n "You return to the hallway you came from, leaving the Cloaked Dagger behind in the Invention room."

    #scene bg
    "UNDER CONSTRUCTION"

    jump Night1Choice

label FollowBG:
    scene bg personalHallway
<<<<<<< HEAD
    stop music
    play music "audio/Emotional.mp3"

=======
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
    n "Sometimes it's easier to stick to what you know, especially when you know so, so little."
    show s_neutral
    n "You follow your former friend down the hallway, letting the chord of connection you share pull you in the direction he walked."
    n "He stops in front of a door, a small gold plaster on the door with the name 'The Bodyguard' written on it."
    p "Are you okay?"
    n "Hearing your voice, he turns around to give you his full attention."
    hide s_neutral
    show s_talking
    bg "Ah. [player_name]. It's..."
    hide s_talking
    show s_neutral
    p "Been a while? Yeah.  Yeah, I know."
    n "There is a somber moment shared between you, standing in the hallway of your captor."
    hide s_neutral
    show s_talking
    bg "Are you well? Other than uh, present circumstances?"
    hide s_talking
    show s_neutral
    menu:
        "I've been better":
            n "He clears his throat awkwardly."
            hide s_neutral
            show s_talking
            bg "Yeah, I get that."
        "Never been better, other than present circumstances":
            n "He gives a soft smile at that"
            hide s_neutral
            show s_talking
            bg "I'm glad."
            hide s_talking
            show s_neutral
            p "And you?"
            hide s_neutral
            show s_talking
            bg "Oh you know, living the dream."
        "I'll give you one guess":
            $ bgRel =- 1
            n "He opens his mouth to speak, but slowly closes it with a wince."
            hide s_neutral
            show s_talking
            bg "I suppose that's fair."
    n "You point at the plaque above his door."
    p "Assigned rooms, then?"
    hide s_neutral
    show s_talking
    bg "I guess so. Guess whoever it is planned for us to be spending a few nights here afterall."
    hide s_talking
    n "Well, it certainly meant... something."
    n "You talk a bit more about the circumstances at hand and your shared past, but eventually the Bodyguard takes his leave and slips inside his room."
    n "Returning to the main chamber, you can't help but wonder what the others think is going on."

    #scene bg
    "UNDER CONSTRUCTION"

<<<<<<< HEAD
=======

>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
    jump Night1Choice

label FollowKFC:
    scene bg kitchenNight with dissolve
    "UNDER CONSTRUCTION"

    jump Night1Choice

label CloakedDaggerRouteDay2:
    #test
    "ROUTE UNDERCONSTRUCTION"
    return

label BodyGuardRouteDay2:
    #test
    "ROUTE UNDER CONSTRUCTION"
    return

label KFCDay2:
    "ROUTE UNDERCONSTRUCTION"
    return

label TheBestRouteDay2:
<<<<<<< HEAD
<<<<<<< HEAD
    scene bg personalRoom with dissolve
    n "Your unconscious mind races as you dream of days before your arrival here on the island. You remember your days as a fledgeling villain, fresh off your henchmanship under Charismata."
    n "You began by committing the smallest crimes possible. Shoplifting from supermarkets, stealing plant cuttings, literally taking candy from babies, the works."
    n "You've come a long way since then. By now, though the scope of your crimes hasn't increased too much, you're finally gaining some serious notoriety and fame in Sunnydayle Valley."
    n "Unfortunately for you... That also comes with some downsides."
=======
    play sound "audio/Motif SFX.mp3"
    scene bg personalRoom with fade
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
    n "BANG! BANG! BANG!"
    n "You're rudely woken up by a series of incredibly loud knocks at your door, accompanied by an unfortunately immediately recognizeable shrill voice."
    tb "GET OUT HERE THIS INSTANT [player_name]! I KNOW YOU'RE USED TO SLACKING OFF BUT WE HAVE VITAL WORK TO DO!"
    n "Regret hits you like a truck, as you already feel dread in the face of what you must do."
    n "The heavy knocks continue as you slowly get dressed and get up to open the door."
    scene bg personalHallway with dissolve
    show a_neutral
    n "As you do so, you swing it open quickly and are met with a fist just as swift, originally aimed for the door but landing square on your face. That bastard [player_name] the Best hit you!"
    menu HitReaction:
        n "How do you react?"
        "<Berate [player_name] the Best for hitting you>":
<<<<<<< HEAD
            p "What the hell, man? I just woke up! Are you seriously so impatient you'd deck me for waking up a little late? News flash, this is KIND OF a stressful situation here! Sorry if I want to sleep in a little."
=======
    play sound "audio/Motif SFX.mp3"
    stop music
    play music "Happy.mp3"
    scene bg personalRoom with fade
    n "BANG! BANG! BANG!"
    n "You're rudely woken up by a series of incredibly loud knocks at your door, accompanied by an unfortunately immediately recognizeable shrill voice."
    tb "GET OUT HERE THIS INSTANT [player_name]! I KNOW YOU'RE USED TO SLACKING OFF BUT WE HAVE VITAL WORK TO DO!"
    n "Regret hits you like a truck, as you already feel dread in the face of what you must do."
    n "The heavy knocks continue as you slowly get dressed and get up to open the door."
    scene bg personalHallway with dissolve
    show a_neutral
    n "As you do so, you swing it open quickly and are met with a fist just as swift, originally aimed for the door but landing square on your face. That bastard [player_name] the Best hit you!"
    menu HitReaction:
        n "How do you react?"
        "<Berate [player_name] the Best for hitting you>":
            p "What the hell, man? I just woke up! Sorry if I want to sleep in a little, but it's not exactly lost on me this is a STRESSFUL SITUATION."
            p "Jesus CHRIST, man."
>>>>>>> main
=======
            p "What the hell, man? I just woke up! Sorry if I want to sleep in a little, but it's not exactly lost on me this is a STRESSFUL SITUATION."
            p "Jesus CHRIST, man."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
            n "[player_name] the Best looks taken aback, like they didn't expect such a harsh reaction from you, but that doesn't last very long."
            hide a_neutral
            show a_talking
            tb "If you're so keenly aware of our predicament then you need to act like it! My life is at stake here and I certainly won't have you holding me back from saving it!"
            tb "Now, are you coming along or not?"
            hide a_talking
            show a_neutral
            n "As much as you want to speak up against the annoyance, you decide it's too early in the morning to keep barking up this tree."
            n "You begrudgingly follow [player_name] the Best as he storms off without so much as another word."
            jump TBInventionScene
        "<Flirt with [player_name] the Best>":
            $ tbRel =+ 1
            p "Listen, if you wanted to hit on me you could have just done so. No need to be so physical, handsome."
<<<<<<< HEAD
<<<<<<< HEAD
            n "[player_name] the Best is clearly taken aback by your brazen flirting, scanning your expression. Taking a moment to compose himself, he smirks at you before leaning in close and whispering to you."
            hide a_neutral
            show a_talking
            tb "You really are committed to this performance, aren't you? Not that I blame you, I'd want to be anyone but yourself too if I were you."
=======
            n "[player_name] the Best is clearly taken aback by your brazen flirting, scanning your expression. Taking a moment to compose himself, he leans in close and whispers to you."
            hide a_neutral
            show a_talking
            tb "You really are committed to this performance, aren't you? It's charming to see you try to play anyone that isn't yourself. Almost convinced me."
>>>>>>> main
=======
            n "[player_name] the Best is clearly taken aback by your brazen flirting, scanning your expression. Taking a moment to compose himself, he leans in close and whispers to you."
            hide a_neutral
            show a_talking
            tb "You really are committed to this performance, aren't you? It's charming to see you try to play anyone that isn't yourself. Almost convinced me."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
            hide a_talking
            show a_neutral
            n "[player_name] the Best takes a moment to adjust their uniform and pull at their collar. It seems that despite their words, you had at least somewhat of an effect on them."
            hide a_neutral
            show a_talking
            tb "Well, are you ready? We must begin our work at once, lest you hold me and my brilliance back and we fail to invent ourselves a way out of here."
            hide a_talking
            n "[player_name] the Best quickly skitters away, seemingly wanting to get to work as quick as possible."
            n "You follow with a smirk on your face. Maybe this won't be the worst thing in the world."
            jump TBInventionScene
        "<Pretend to be more hurt than you actually are>":
            $ tbRel =+ 2
            n "You theatrically crash to the ground, holding a hand to your face where [player_name] the Best's fist landed. Masquerading a horrible pain, you writhe on the ground dramatically."
<<<<<<< HEAD
<<<<<<< HEAD
            n "[player_name] the Best's expression shifts to one of horror, as they temporarily regard their own fist with fear of their heretofore unknown power."
            n "[player_name] the Best quickly rushes to help you, kneeling on the ground and trying to get a look at your face."
            hide a_neutral
            show a_talking
            tb "[player_name] you really ARE weak, aren't you. Despite how mighty my punches can be, I thought you were made of stronger stuff than that."
=======
            n "[player_name] the Best's expression shifts to one of horror, as they temporarily regard their own fist with fear of their unknown power."
            n "[player_name] the Best quickly rushes to help you, kneeling on the ground and trying to get a look at your face."
            hide a_neutral
            show a_talking
            tb "You really ARE weak, aren't you. Despite how mighty my punches can be, I thought you were made of stronger stuff than that."
>>>>>>> main
=======
            n "[player_name] the Best's expression shifts to one of horror, as they temporarily regard their own fist with fear of their unknown power."
            n "[player_name] the Best quickly rushes to help you, kneeling on the ground and trying to get a look at your face."
            hide a_neutral
            show a_talking
            tb "You really ARE weak, aren't you. Despite how mighty my punches can be, I thought you were made of stronger stuff than that."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
            hide a_talking
            show a_neutral
            n "[player_name] the Best reaches out a hand to help you up. Surprised, you take it, letting yourself rise via [player_name] the Best's steady hand."
            p "Huh, I didn't take you for the charitable type."
            hide a_neutral
            show a_talking
            tb "Well don't get too used to it. We've already wasted far too much time and I just wanted to make sure you weren't overwhelmed by my devastating blows."
            hide a_talking
            show a_neutral
<<<<<<< HEAD
<<<<<<< HEAD
            n "Before you can get out any sort of response, [player_name] the Best is already leading you by the hand towards the invention room."
=======
            n "Before you can get out any sort of response, [player_name] the Best is already leading you towards the invention room."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
            n "UNDER CONSTRUCTION."
            jump TBInventionScene

label TBInventionScene:
    scene bg inventionRoom with dissolve
    n "The moment the two of you set foot in the invention room, you're both blown away by the facilities within. It's not the most high-tech to begin with, but one thing catches your eye."
=======
            n "Before you can get out any sort of response, [player_name] the Best is already leading you towards the invention room."
            jump TBInventionScene

label TBInventionScene:
    stop music
    play music "audio/Happy.mp3"
    scene bg inventionRoom with dissolve

>>>>>>> main
    show a_talking
    tb "Oh my heavens, there's a crafting table!"
    hide a_talking
    show a_neutral
<<<<<<< HEAD
    p "Holy fuck it's a crafting table!"
    n "Yes, a crafting table. Inspired by the incredibly popular video game Cavernbuild, 3D printing technology had soared in recent years, culminating in the most expensive yet easiest way to make whatever your mind desired."
=======
    p "Holy fuck it's actually a crafting table."
    n "Yes, a crafting table. Inspired by the incredibly popular video game Cavernbuild. 3D printing technology had soared in recent years, culminating in the most expensive yet easiest way to make whatever your mind desired."
>>>>>>> main
    n "With the right know-how, dedicated time, and even a vague idea of what you want to make, just about anything was possible."
    n "If you both weren't so enamoured, you might even begin to wonder who could afford to have such a thing on a deserted island."
    n "Grandiose in all ways, [player_name] the Best immediately pipes up with an equally grand suggestion."
    hide a_neutral
    show a_talking
    tb "A flying machine! Yes we absolutely must! A great escape through the volcano's ceiling! A daring endeavor for a daring villain such as myself."
    hide a_talking
    show a_neutral
    n "If it weren't for the tech in front of you making that idea possible, you usually would have shut that down, but you'd be lying if you weren't interested in going big with this one."
    p "You know what? Let's go for it. It'll have to carry all five of us, but I actually think it's possible between the two of us."
    n "[player_name] the Best looks at you shocked, having fully expected you to argue the idea down."
    hide a_neutral
    show a_talking
    tb "Well then, let's get to work, shall we? Don't worry, with me leading the way, everything is sure to go smoothly."
    hide a_talking
    n "The two of you get to work immediately, drafting up schematics to generate each part you'll need for the flying machine. The excitement in the air is palpable, and for a moment, you forget your grievances with [player_name] the Best."
    n "..."
    n "At least, you were able to for a little while."
    show a_talking
    tb "You know, when you're the best, you really are the best. Oh wait, you wouldn't really know that, would you? Your inventions have always paled in comparison to mine, after all."
    n "[player_name] the Best keeps jabbering on and on about his \"accomplishments\" while you try to keep your head in any sort of productive mood. It's not working too well, and you're getting to the point where you need to say SOMETHING."
    menu SpeakUp:
        n "What do you say?"
<<<<<<< HEAD
        "My inventions have held their own more than a few times, you know.":
            $ tbRel =+ 2
=======
        ## neutral options
        "My inventions have held their own more than a few times, you know.":
>>>>>>> main
            hide a_talking
            show a_neutral
            n "[player_name] the Best opens his mouth to object, but you keep going."
            p "Like that one time you stole hundreds of sub sandwiches from Shrublix. I saw that and thought, \"Yeah, I can steal a few\" I fed myself for weeks!"
            p "Or that other time you convinced Belle Thorpe she had Dyslexia. Well guess who went and convinced her to talk about it on Didney Channel?"
            n "[player_name] the Best's mouth opens wider with each and every example you provide."
            p "You know what? I think that every time I see you do something interesting, I just have to take a crack at it."
            p "You always seem to spur me to do better than I did before. I know we fight a lot, but I have to say, I appreciate the calmer moments."
            n "[player_name] the Best's jaw is basically on the floor at this point, and he sputters to respond."
            hide a_neutral
            show a_talking
            tb "Oh- oh yeah? Well, I'm glad that you recognize I'm someone you're always going to have to look up to. You know, as your superior and all."
            hide a_talking
            show a_neutral
            n "[player_name] the Best turns away to hide his face, mumbling something about \"Of COURSE his inventions inspire the masses\"."
            n "You can't help but notice the obvious blushing he tries to hide. Maybe it is a LITTLE fun to tease him."
<<<<<<< HEAD

            jump TBInventionTest
=======
            jump TBInventionTest

         #me when i stroke his ego
>>>>>>> main
        "Absolutely, you've always been the better inventor between the two of us, after all.":
            $ tbRel =+ 1
            hide a_talking
            show a_neutral
            n "You don't even need to look in [player_name] the Best's direction to know he's shocked, as you hear the pen in his hand drop to the floor."
            n "You turn to see [player_name] the Best staring intently at you as if he's trying to bore into your head and figure out what you're thinking."
            p "I really do think you're incredible. I mean, stealing hundreds of sub sandwiches from Shrublix? How'd you manage that?"
            p "You literally stole Christmas! I remember you smelled like gingerbread until April. And didn't you convinve Belle Thorp she had dyslexia? Amazing work there, I couldn't even get an interview with her!"
            n "[player_name] the Best's expression becomes more incredulous with each word of praise you utter, before his eyes eventually narrow."
            hide a_neutral
            show a_talking
            tb "You know, you don't have to be such a sarcastic asshole all the time. I get we don't get along, but try to have some decorum."
            hide a_talking
            show a_neutral
            n "[player_name] the Best turns away to resume working, but you can see the corner of his mouth curl up in what seems to be a smile, with his cheeks blushing just a little."
            n "Perhaps the praise meant more to him than you realized."
            
<<<<<<< HEAD
=======
            #stfu twink
>>>>>>> main
            jump TBInventionTest
        "You've literally never invented a single thing better than my worst invention.":
            $ tbRel =- 1
            hide a_talking
            show a_neutral
            n "[player_name] the Best looks at you incredulously. A flurry of fury, confusion, and embarrassment brews within him until he unleashes what he would consider hell on you."
            hide a_neutral
            show a_talking
            tb "EXCUUUUUUUUUUUUUSE MEEEEEEEEEE?!"
            tb "Have you lost your mind completely? Have you forgotten the Shrublix debaucle where I successfully lifted several HUNDRED sub sandwiches compared to your measly twelve?"
            tb "Are we going to ignore when you dressed like the grinch while I LITERALLY stole Christmas?"
            tb "And lest we forget about the time I convinced Belle Thorp that she had Dyslexia! You couldn't even get an interview with her!"
            hide a_talking
            show a_neutral
            n "As much as these incidents are kind of right, they're not the whole truth."
<<<<<<< HEAD
<<<<<<< HEAD
            p "And every one of those cases where you \"succeeded\" backfired every time! You gained nothing! Villainy for villainy's sake alone is what those were."p
=======
            p "And every one of those cases where you \"succeeded\" backfired every time! You gained nothing! Villainy for villainy's sake alone is what those were."
>>>>>>> main
=======
            p "And every one of those cases where you \"succeeded\" backfired every time! You gained nothing! Villainy for villainy's sake alone is what those were."
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
            p "The sandwiches expired before you could eat even two!"
            p "You smelled like gingerbread well into April AND couldn't get rid of all those decorations for YEARS!"
            p "You didn't even get credit for Belle Thorp, she went on Dindey Channel and got celebrated for it!"
            p "Face it, every \"success\" you've had has crashed down on you and left you even worse off."
            n "An air of silence permeates the room, as a thick tension fills the space between you. You kind of feel bad about going so hard on him."
            hide a_neutral
            show a_talking
            n "[player_name] the Best tries to object, but comes up short. Instead, they dejectedly mumble under their breath, and the two of you continue working on the flying machine in silence."
            
            jump TBInventionTest

label TBInventionTest:
    show bg volcanosunset with fade
    n "The flying machine has been completed by the afternoon, and it's finally time to test it. You had to assemble the parts outside of the invention room for fear of it not fitting through the door, but it was ready to go."
    show a_talking
    tb "At last, the fruits of our labor are shown! Now let us prove once and for all that our minds are made of the same stuff as the greats of old!"
    hide a_talking
    show a_neutral
    p "For the sake of everyone's lives in here, I hope that's the truth bud. Let's give it a spin."
    n "As the two of you get inside the flying machine, it whirs to live, brimming with electricity."
    n "All is well during initial takeoff, and you begin rising from the ground in no time. [player_name] the Best pumps his fist in the air."
    hide a_neutral
    show a_talking
    tb "MUAHAHAHAHA! Behold! The power of a genius at work!"
    hide a_talking
    show a_neutral
    n "Maybe [player_name] the Best should have kept quiet just a BIT longer, as the engine starts smoking violently."
    n "Sharing a look between the both of you, you dive out of each side of the machine as it crashes down to the ground."
    hide a_neutral
    n "As you both pick yourselves off the ground and stare at the rubble that was your first flying machine, you think to yourself that every great invention has a million failed prototypes. You'll just have to try again."
    show a_neutral
    n "[player_name] the Best, however, doesn't have such an optimistic outlook on things. A quick glance shows you his scrunched up expression, trying and failing to fight back tears."
    hide a_neutral
    show a_talking
    tb "You... You... You must have messed something up, [player_name]! There's no other reason this could have failed!"
    hide a_talking
    show a_neutral
<<<<<<< HEAD
<<<<<<< HEAD
    menu: InventionBlame
=======
    menu InventionBlame:
>>>>>>> main
=======
    menu InventionBlame:
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
        n "What do you say in response?"
        "You're right, I must have messed up a calculation or two.":
            $ tbRel =+ 1
            n "Looking dejected, you sit on the ground and start to mope. You definitely weren't focused the whole time in there, a mistake wasn't out of the question."
            n "With things like these, you needed to be exact with everything. A slight miscalculation and the whole thing crumbles. Maybe [player_name] was right."
            p "Sorry for messing things up, I understand if you want to keep trying without me."
            n "[player_name] the Best looks at you with complete shock. You somehow keep surprising them today. He picks himself off the ground before slowly approaching you and resting a hand on your shoulder."
            n "His expression softens as he looks at you, and you get the feeling that he's going to comfort you."
            hide a_neutral
            show a_talking
            tb "Get yourself off the ground and stop moping around like a total wuss. We have work to do and I won't have you holding me back."
            hide a_talking
            show a_neutral
            n "You were wrong."
            hide a_neutral
            show a_talking
            tb "You know what, I think we just need to figure out how to work together a little bit better."
            hide a_talking
            show a_neutral
            n "Both of your stomachs begin rumbling and you share a look of mutual understanding."
            hide a_neutral
            p "The kitchen?"
            show a_talking
            tb "The kitchen."
            n "[player_name] the Best helps you off the ground as he ushers you towards the kitchen. It's time to eat."

            jump TBKitchenScene
        "Are you kidding me? This is all my fault? Take a good look at yourself, buddy.":
            jump ScorchingEnd2
        "Calm down, jeez. Everyone makes mistakes, we just need to keep trying till we get it.":
            $ tbRel =+ 2
            n "Looking dejected, you sit on the ground and start to mope. Neither of you were focused the whole time in there, a mistake wasn't out of the question."
            n "With things like these, you needed to be exact with everything. A slight miscalculation and the whole thing crumbles. You'd be able to try again, though."
            p "Sorry for messing things up, I understand if you want to keep trying without me."
            n "[player_name] the Best looks at you with complete shock. You somehow keep surprising them today. He picks himself off the ground before slowly approaching you and resting a hand on your shoulder."
            n "His expression softens as he looks at you, and it seems like he feels sympathetic towards you."
            hide a_neutral
            show a_talking
            tb "Come on, let me help you up. We might not have got it this time, but the both of us are made of stronger stuff than that. If you weren't, I'd have killed you by now due to my AMAZING strength."
            hide a_talking
            show a_neutral
            n "[player_name] the Best flexes a little, still sure of his strength from his earlier hit he landed on you."
            hide a_neutral
            show a_talking
            tb "You know what, I think we just need to figure out how to work together a little bit better."
            hide a_talking
            show a_neutral
            n "Both of your stomachs begin rumbling and you share a look of mutual understanding."
            hide a_neutral
            p "The kitchen?"
            n "[player_name] the Best nods in agreement."
            show a_talking
            tb "Let us learn to truly collaberate in the greatest warzone known to man."
            tb "The kitchen."
            n "[player_name] the Best helps you off the ground as he ushers you towards the kitchen. It's time to eat."
            
            jump TBKitchenScene

<<<<<<< HEAD
label TBKitchenScene:
    show bg kitchenNight
    n "KITCHEN TIME!!!!! Now kiss."
    n "UNDER CONSTRUCTION"
    return
    #test

label ScorchingEnd2:
    n "[player_name] the Best goes to yell at you, but finds himself coming up short with what to say. Without a word, he begins to sob relentlessly."
    n "The scene goes on uncomfortably long, with the sounds of [player_name] the Best's sobbing only being broken up by the cracking flames of the broken flying machine."
    n "After a while of this, [player_name] the Best wipes away his tears and looks over at you with a tired expression."
    hide a_neutral
    show a_talking
    tb "You know what? Go ahead, work on it yourself. I'll focus on doing something more productive with my time. You can get burnt to a crisp for all I care."
    hide a_talking
    n "[player_name] the Best walks away without sparing another thought towards you, marching directly towards The Bodyguard's room."
    show bg volcanonight with fade
    n "The day ends with you cleaning up your failed invention and preparing for the next day."
    show bg volcanoday with fade
    n "As the day ticks by, you find yourself alone in the invention room, frantically calculating as your workload has increased twofold."
    show bg volcanosunset with fade
    n "The others are nowhere to be seen, likely having socialized and paired up, lacking faith in your ability to complete the machine in time."
    show bg volcanonight with fade
    n "As you continue to work, you don't even notice as the PA system announces the departure of two groups."
    n "Seems like The Bodyguard and [player_name] the Best grouped up, The Bodyguard always was an expert at comforting people."
    n "Key Frame Crusader and The Cloaked Dagger also paired up. Likely a strategic move from what you've seen of the two of them."
    n "And here you are, alone. Destined to die a no-one supervillain on an island in the middle of nowhere."
    show bg volcanoerupt with fade
    n "Romance is dead, but it sure is hot in here."
    return
    #test
<<<<<<< HEAD



=======
label Day2:
    scene bg personalroom
>>>>>>> ffe96e578f82a40682a0bc4588777853ff7ed61f
=======
label ScorchingEnd2:
    scene bg volcanoerupt with dissolve
    stop music
    play music "audio/Sad.mp3"
    n "[player_name] the Best goes to yell at you, but finds himself coming up short with what to say. Without a word, he begins to sob relentlessly."
    n "The scene goes on uncomfortably long, with the sounds of [player_name] the Best's sobbing only being broken up by the cracking flames of the broken flying machine."
    n "After a while of this, [player_name] the Best wipes away his tears and looks over at you with a tired expression."
    hide a_neutral
    show a_talking
    tb "You know what? Go ahead, work on it yourself. I'll focus on doing something more productive with my time. You can get burnt to a crisp for all I care."
    hide a_talking
    n "[player_name] the Best walks away without sparing another thought towards you, marching directly towards The Bodyguard's room."
    show bg volcanonight with fade
    n "The day ends with you cleaning up your failed invention and preparing for the next day."
    show bg volcanoday with fade
    n "As the day ticks by, you find yourself alone in the invention room, frantically calculating as your workload has increased twofold."
    show bg volcanosunset with fade
    n "The others are nowhere to be seen, likely having socialized and paired up, lacking faith in your ability to complete the machine in time."
    show bg volcanonight with fade
    n "As you continue to work, you don't even notice as the PA system announces the departure of two groups."
    n "Seems like The Bodyguard and [player_name] the Best grouped up, The Bodyguard always was an expert at comforting people."
    n "Key Frame Crusader and The Cloaked Dagger also paired up. Likely a strategic move from what you've seen of the two of them."
    n "And here you are, alone. Destined to die a no-one supervillain on an island in the middle of nowhere."
    show bg volcanoerupt with fade
    n "Romance is dead, but it sure is hot in here."
    return
    #test

label TBKitchenScene:
    show bg kitchenNight with dissolve
    stop music
    play music "audio/Emotional.mp3"

    show a_neutral
    n "Well at least Key Frame Crusader was right, the kitchens were certainly stocked."
    n "You make your way into the kitchen, looking for what food there is to make."
    n "When was the last time you ate? You don't even remember anymore."
    n "Another thing you can't tell is whether it's the starving stomach or changing feelings, you don't... entirely dread being in the presence of [player_name] the Best."
    n "Glancing over to your partner-in-escape, you wonder if this could be a chance to stare woeing them."
    n "Well, you were certain the quickest way to the heart is throught he back with a sharp knife... but in this case, you could try the stomach."
    hide a_neutral

    menu MakeTBFood:
        "<Attempt to make Beef Stroganoff (You, dear player, do not know how to make Beef Stroganoff)>":
            #test
            n "...Well, if you're sure that's what you want to do."
            n "It's sure to impress him if it works!"
            n "You both work together and despite your combined efforts, the dish ends up... horrendous."
            # one day insert failed image of bad beef stroganoff here
            n "It tastes fine... if you eat fast. It doesn't add much to morale nor does it precisely woe your target but... food is food!"
            n "You share a moment where you wipe a bit of food off his face, but in an act of panic he recoils and excuses himself for the night."
            n "Well, could have been worse?"
            n "You get up and clean the mess you both made, washing the dishes and spending at least fifteen minutes staring at the needlessly fancy dishwasher until you could open it."
            uk "Hello, Mr. Summers!"
            n "You jump back at the dishwasher...speaking, to you?"
            p "Who?"
            n "The dishwasher does not reply, the message seemingly automatic. Who programs their dishwasher to say hello to them?"
            n "It appears that your captor, likely this 'Mr.Summers', is someone who does that."

            scene bg roomNight with dissolve
            n "New clue in hand, you eventually return to your room for the evening."
            jump Day3

        "<Attempt to make Pizza>":
            $ tbRel =+ 1
            p "Pizza, that should be pretty simple."
            n "Thankfully, you are relatively correct."
            n "Making the pizza alongside [player_name] the Best goes well, both of you even beginning to joke around regarding pizza toppings."
            menu Pizza:
                n "What is your favorite?"
                
                "I'm just a cheese kind of guy.":
                    n "The other man side eyes you, clearly in disgust, but says nothing else as you cook"
                "Veggies all the way!":
                    n "The other man side eyes you, clearly in disgust, but says nothing else as you cook"
                "Meat lovers is the only way to go":
                    n "The other man side eyes you, clearly in disgust, but says nothing else as you cook"
                "Hawaiin or nothing.":
                    $ tbRel =-1
                    n "The other man side eyes you, gagging slightly in utter disgust. He says nothing, but you can sense he really didn't like that."
            n "Unfortunately, just when everything begins to go well, the mood set, the smell of the pizza wafts through the entire interior chambers of the volcano."
            n "The other three villians rush in, some asking and others simply taking from the prepared pizza without a second thought."
            n "Despite the mood change, you and [player_name] the Best share one final smile before parting for the night, food in hand."
            n "Well, could have been worse?"
            n "You get up and clean the mess you both made, washing the dishes and spending at least fifteen minutes staring at the needlessly fancy dishwasher until you could open it."
            uk "Hello, Mr. Summers!"
            n "You jump back at the dishwasher...speaking, to you?"
            p "Who?"
            n "The dishwasher does not reply, the message seemingly automatic. Who programs their dishwasher to say hello to them?"
            n "It appears that your captor, likely this 'Mr.Summers', is someone who does that."
            jump Day3

        "<Attempt to make Spaghetti>":
            $ tbRel =+ 2

            jump Day3
    

label Day3:
    play sound "audio/Motif SFX.mp3"
    scene bg personalRoom with fade
    "END OF ROUTE IS UNDER CONSTRUCTION"
    return
>>>>>>> main
=======
>>>>>>> 53fe2e13bb05574eaee4f15332e329dabffbe978
