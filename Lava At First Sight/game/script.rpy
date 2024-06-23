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

label start:
   # okay so add bg island.jpg or .png  to images directory
   scene bg island 
   play music "audio/Test.wav" volume 0.5

   # pre-establish the lore(TM)
   n "You can see it in the distance, at first just a little spec on the horizon but now fully coming into view-- The Island."
   p "This is where the note said I'd find the liar..."
   n "You notice the large volcano the note said Golden Boy's liar would be within."
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
        "They bodies of four known villians were found in the volcanic ruins of Hot-Hot-Romantic-Summer-Isalnd-Firey-Passion Island, informally known as Jenny Island."
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
        n "Determind to keep pushing forward, you make your way toward the other door. The door easily slides open as you step inside, attempting to be quiet in your attempt to continue inside."

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
        p "Four?"
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

    menu NightChoice1:

        set visited
        n "What will you do?"

        # Scorching End 1
        "<Go Straight to Bed>":
            jump ScorchingEnd1
        "<Talk to [player_name] the Best>":
            jump TalktoTB
        "<Follow the Cloaked Dagger>":
            jump FollowCD
        "<Follow the Bodyguard>":
            jump FollowBG
        "<Follow the Key Frame Crusader>":
            jump FollowKFC
        #secret ending start
        "<Investigate the seam in the wall>":
            jump InvestigateSeam

label ScorchingEnd1:
    scene bg volcanoerupt with dissolve

label InvestigateSeam:
    "THIS ROUTE IS UNDER CONSTRUCTION"
    jump NightChoice1

label TalktoTB:
    scene bg volcanonight
    "UNDER CONSTRUCTION"

    jump Night1Choice

label FollowCD:
    #scene bg
    "UNDER CONSTRUCTION"

    jump Night1Choice

label FollowBG:
    #scene bg
    "UNDER CONSTRUCTION"

    jump Night1Choice

label FollowKFC:
    #scene bg
    "UNDER CONSTRUCTION"

    jump Night1Choice

