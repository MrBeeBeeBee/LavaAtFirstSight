define n = Character('Narrator')
define p = Character('Me')
define sm = Character('The Bodyguard') #Shaun masters
define tb = Character('The Best') #Ardbert D'arc
define cd = Character('The Cloaked Dagger') #Casper beauregard
define kfc = Character('Key Frame Crusader') #Marcus Smith
define gb = Character('Golden Boy') #John summers



label start:

   # okay so add bg island.jpg or .png  to images directory
   # scene bg island 

   # pre-establish the lore(TM)
   n "You can see it in the distance, at first just a little spec on the horizon but now fully coming into view-- The Island."
   p "This is where the note said I'd find the liar..."
   n "You notice the large volcano the note said Golden Boy's liar would be within."
   p "....Wow that's...really just...a whole volcano, huh?"
   n "While you wait for your boat to reach shore, you think of how your legacy will forever change if you accomplish this mission."
   n "You will no longer be a low-level pest of a villian to Sunnydayle Valley's only hero."
   n "You will finally be known for more than just stealing traffic cones, stealing from Christmas Charity Buckets, and printing off fake money."
   n "You will finally be seen for what you are-- a supervillian. Golden Boy doesn't even know what's coming."
   n "The anonymous note said it would be easy to slip inside Golden Boy's liar within the volcano itself, giving you plenty to lay a trap to ruin his day."
   n "Your boat finally reaches shore... but something in your gut is urging you to reconsider. If you want to turn back, something tells you that now is your only chance."
  
   menu:
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
        #scene bg volacanointerior 
        #with dissolve
        
         n "Eventually, you make your way through the island's greenery and arrive at the entrance of the volcano."
         n "As the note suggested, the opening wasn't hard to find. There was some cover, but you are the greatest supervillian in the area, so it's not surprising you so easily detected the hidden cavernous entrance."
         n "As you enter, carefully walking forward, you see a door just up ahead in the cavern."
         p "Bingo."
         n "You begin heading toward the door when-"
         "BANG!"
         n "The cavern fills with the sounds of loud grinding noises as the cavern entrance is suddenly closed off by a large door."
         p "NO NO NO NO"

         menu:
            p "What do I do?"

            "<Head to door at the end of the cavern>"
                p "Wouldn't be the first time I walked into a trap... but what kind of trap is this supposed to be?"
                n "Ahead, you hear"
                n "Determind to keep pushing forward, you make your way toward the other door. The door easily creaks open

            "<Try to get the door open>"
                n "There's no use. "

   
