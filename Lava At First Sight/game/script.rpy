define n = Character('Narrator')
define p = Character('Me')
define bg = Character('The Bodyguard') #Shaun masters
define cd = Character('The Cloaked Dagger') #Casper beauregard
define kfc = Character('Key Frame Crusader') #Marcus Smith
define gb = Character('Golden Boy') #John summers
define tb = Character('%(player_name)s the Best') #Ardbert D'arc
image bg island = "island.png"


label start:

   # okay so add bg island.jpg or .png  to images directory
   scene bg island 

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
        "{INSERT HOW THE VILLIANS DIED}"
        p "Holy shit..."
        n "Things are about to be a lot different now... but you can't help but wonder, who gave you that note? What had happened if you had stayed? You suppose you'll never truly know."
        ".:. Bad Ending."
        return 

label Day1:
        #add volcanointerior.jpg or .png to images directory
        #scene bg cavern
        #with dissolve
        
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
        p "Wouldn't be the first time I walked into a trap... but what kind of trap is this supposed to be?"
        n "Ahead, you hear what sounds like... arguing? You can't make out where they are saying but it seems to be multiple voices on the other side of the door bickering."
        n "Determind to keep pushing forward, you make your way toward the other door. The door easily slides open as you step inside, attempting to be quiet in your attempt to continue inside."
        
        #scene bg volcanointeriorday
        #with dissolve

        # Future bang noise (game/audio directory)? -> play sound "file ext"
        n "BANG!"
        p "Shit."
        n "The noise of the door locking behind you echoes throughout, alerting the group of people ahead of your presence."

        #show ardbert neutral
        #with dissolve
        n "The first one to speak is a familiar pompous, purple-haired, and extravagantly dressed man. "
        tb "%(player_name)s!"
        p "Oh not this guy."
        n "You, unfortunately, are very familiar with %(player_name)s the Best. Your worst enemy. The most insufferable man you've ever met."
        tb "Oh for God's sake why are YOU here? No, no, why are any of us here?"
        p "I was given a note. I'm assuming you all were as well?"
        tb "No, no, I was told I alone was being told this location."
        p "Evidently fucking not."

       
        #show casper neutral
        #with dissolve

        #show shaun neutral
        #with dissolve

        #show marcus neutral
        #with dissolve
