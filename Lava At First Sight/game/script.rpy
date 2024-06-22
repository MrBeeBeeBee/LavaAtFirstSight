# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t1 = Character("The Cloaked Dagger")
define t2 = Character("The Bodyguard")
define t3 = Character("The Best")
define t4 = Character("Key Frame Crusader")
define t5 = Character("Golden Boy")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg genshin

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show joost blue

    t1 "I'm finally real! I'm a real boy!"

    show joost hat

    t1 "..."
    t1 "What..? I'm a character in a visual novel..?"
    t1 "I guess I always suspected it... I need some time alone..."

    "The Cloaked Dagger skulks away..."
    with dissolve

    with fade
    scene bg zeroescape

    show joost punk
    t2 "I'm also real! I'm a real boy!"

    show joost silly

    t1 "..."
    t1 "What..? I'm a character in a visual novel..?"

    show joost spike

    t2 "No! I refuse to believe this! I'll prove that I'm real one way or another, you'll see!"

    "The Bodyguard storms off..."

    # This ends the game.

    return
