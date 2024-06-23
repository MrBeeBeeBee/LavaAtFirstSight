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
image bg personalHallway = "bg personalHallway.png"

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

label start:
   # okay so add bg island.jpg or .png  to images directory
   scene bg island 
   # play music "audio/Test.wav" volume 0.5

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

   n "You're now nearly there. Thankfully, the anonymous note said it would be easy to slip inside Golden Boy's liar within the volcano itself, giving you plenty to lay a trap to ruin his day."
   n "Your boat finally reaches shore... but something in your gut is urging you to reconsider. If you want to turn back, something tells you that now is your only chance."
   menu StayorGo:
    p "Do I leave?"

    "<Leave island>":
        jump BadEnd
    "<Continue to volcano>":
        jump Day1
    
label BadEnd:
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
        scene bg volcanoday
        with dissolve
        p "Wouldn't be the first time I walked into a trap... but what kind of trap is this supposed to be?"
        n "Ahead, you hear what sounds like... arguing? You can't make out where they are saying but it seems to be multiple voices on the other side of the door bickering."
        n "Determind to keep pushing forward, you make your way towards the other door. The door easily slides open as you step inside, attempting to be quiet as you continue inside."

        # Future bang noise (game/audio directory)? -> play sound "file ext"
        n "BANG!"
        p "Shit."
        n "The noise of the door locking behind you echoes throughout, alerting the group of people ahead of your presence."
        
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
        n "Your childhood friend. Shaun. He goes by the Bodyguard now, last you heard. You can't remember the last time you spoke to one another."
        p "Bodyguard? What's going on here?"
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
         n "Unlike all of the voices and faces before, this voice is... unrecognizable. It was distorted beyond recognition, the words barely distinguishable amidst the static."
         uk "Congratulations, my friends."
         uk "As you may have guessed, you have all been brought here under what one might call, false pretense."
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
    n "You turn away from %(player_name)s banging on the metal doors to the Bodyguard. The taller man only looks back to you a moment before leaving."
    n "You notice then that him, the Key Frame Crusader, and the Cloaked Dagger were all heading to rooms built into the central chamber."
    n "Whoever your host is, at least they were generous enough to give you beds."
    n "Still, even as you approach your own quarters, you don't feel capable of rest just yet."
    jump Night1Choice

label Night1Choice:
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
            scene bg personalHallway

            jump FollowCD
        "<Follow the Bodyguard>":
            $ visitconfirm = "Yes"
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

    jump Night1Choice

label FollowBG:
    #scene bg
    "UNDER CONSTRUCTION"

    jump Night1Choice

label FollowKFC:
    #scene bg
    "UNDER CONSTRUCTION"

    jump Night1Choice

label Day2:
    scene bg personalroom
