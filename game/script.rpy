# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Harper")
define i = Character("Inari")
define s = Character("Stitch")
define a = Character("Apple")
define p = Character("Patches")
define npc1 = Character("Random Guy 1")
define npc2 = Character("Random Guy 2")


# list of backgrounds
# bg room, bg outside, bg bus, bg mall
# list of sprites needed per character
#Inari: inari_happy, inari_smug
#Harper: harper_happy, harper_spin, harper_excited
#spites should be 1000 px tall i thinks?
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "harper happy.png" to the images
    # directory.

    show harper happy

    # These display lines of dialogue.

    "You wake up, what should we do?"
    menu:
        "Go to school":
            jump goodkid_route

        "Skip class":
            jump delinquent_route
label goodkid_route:
    h "I should make sure I pack my TI-84 EVO"
    h "Oh and my sketchbook stuffs"
    h "DAD! I'm ready!!!!"
    h "Hurry up or I'm not gonna be early!"
    "Your father drives you, this is because you're a loser that stull doesn't have a liscence"
    "You arrive at school 10 minuetes before the doors even unlock"
    "Bzzzt, a teacher lets you in early"
    "Sitting in the hall you wait for your friend who gets there roughly when the door unlocks"
    show apple
    "You two hang out for awhile before school starts most days since you're both early"
    h "Hey Apple!"
    a "HI!!! what's up?"
    h "Nothing much, how about you?"
    a "I'm chilling, wanna head to the store?"
    h "Sure, why not!"
    "You two walk to the store"
    show bg mall
    h "What do you want?"
    a "Huh?"
    h "To pay you back, for getting me an energy drink yesterday"
    a "Ohhhhhhhh"
    "She grabs a can and hands it to you"
    a "Do you want one yourself?"
    h "..."
    h "Nah"
    a "Oh ok! I'll take that at face value I guess"
    a "No need to question things"
    "She paces around a little while giggling lightheartedly as you pay"
    show bg outside
    a "Ugh I'm so tired from work last night"
    h "Oh, that sucks, what were y'all doing?"
    "She says something about construction work that you don't fully understand"
    h "Quel dommage"
    a "Huh?"
    h "It's french! You talk in Spanish randomly all the time!"
    a "Yeah but I don't take French"
    h "And I don't take Spanish???"
    a "You used to!"
    a "You know enough to understand most of what I say anyways"
    h "Fair! Fair!"
    #this is where we start the part that is gonna be deleted in the future
    a "I'm so sad we're in different grades and have no classes together"
    h "Yeah, me too"
    "You two part ways and need to go to classes; you have art class first"
    show stitchy
    s "HAIIII HARPER!"
    h "Hi Stitchy! Are you working on your model?"
    s "no comment"
    h "Giggles. Well I need to work on my art trade during this class"
    # Add the good kid storyline here
    jump choice_done

label delinquent_route:
    show harper spin
    h "Tada! I'm evil and stuff >:3!"
    #add smirking face with like spinny pose
    show harper happy d
    "You check your phone and see messages asking for homework answers and whatnot."
    "Unfortunately for them, you forgot the assignment existed."
    "You put on headphones and start listening to music."
    #i should really lock in on music and make my own music for this 
    #add an outside background
    scene bg outside
    "Waiting on the bus..."
    #bus background
    scene bg bus
    "Theres only one seat left"
    "So you do the most rational thing and stand so that you don't have to talk"
    npc1 "How's work bro?"
    npc2 "Not bad man, not bad"
    "Ding ding ding!"
    "The bus is approaching the mall"
    scene bg outside
    show harper happy d
    h "Oh my gods! Is that Inari?"
    "You run up to them"
    show inari
    i "Oh hi Harper! What are you doing here??? Don't you have school?"
    h "Nah, I'm skipping lol"
    i "Oh! How could you?"
    #show inari smug
    h "What about you, shouldn't skipping be below someone of your starture?"
    i "I can do whatever I want!"
    i "Unlike someone, I am a divine being! Earthly rules don't apply to me!"

    menu: 
        "What should you say?"
        "Of course, of course! I absolutely worship the ground you walk on! *eye roll*":
            i "As you should!"
            h "Yeah yeah lol" 
            h "What were you even planning to do, all alone. Kinda desperate for a being such as you"
            i "I obviously predicted you would come here..."
            i "Obviously..."
            h "Oh? Well I guess I'm obligated to stay"
            jump inariship_route
        "L, I'm better than you actually":
            jump murder_route

label inariship_route:
    i "You ought to repay me"
    show harper 
    #grin
    h "Repay you how?"
    i "You can repay me with a drink"
    h "lead the way"
    scene bg mall
    i "I want the citrus smoothie"
    npc1 "What would you like to order?"
    h "Can we get one citrus smoothie and one strawberry banana?"
    npc1 "Sure thing!"
    "A few minutes later"
    npc1 "Here you go!"
    h "For you, my lord"
    i "You don't need to bow..."
    i "Sighs... just give it to me"
    h "Yeah, yeah, love you too"
    h "So what next mi'lady?"
    i "We should go to your house"
    jump choice_done
label murder_route:
    show inari 
    #disapointed
    i "Sighs, must you be like this?"
    i "{i}I even waited here specifically for you...{/i}"
    h "What was that?"
    i "Nothing!"
    "..."
    h "Anyways... Let's go to a store..."
    scene bg mall
    i "Hmmph, this skirt would be better for you than whatever that is"
    h "That is so not true! Jeans are my thing!!!"
    h "Woah who is that?"
    show patches 
    "You see a boy walking around; his hair is a mess but other than that he seems put together"
    i "Him? That's Patches..."
    p "Oh hey, who's this little guy?"
    "Inari clings to your arm"
    h "Why are you...?"
    i "This is Harper!"
    p "Oh? You're being offly clingy, that's not like you Inari"
    show patches 
    #slight_glare
    i "I don't care what you think is like me! I can do whatever I want!"
    menu:
        "Talk to Inari":
            h "I don't like this guy"
            "Inari drags you away"
            jump inariship_route

        "Talk to Patches":
            h "Hi there...?"
            show patches 
            p "You're awfully cute!"
            h "Me...?"
            "Inari looks annoyed"
            p "Yeah obviously, what do you say we get out of here?"
            "You agree and slip out of Inari's grasp"
            "She wasn't holding on tightly but her touch lingered"
            p "Awww the goddess Inari's beloved getting taken by a mere mortal"
            show inari 
            #flustered
            i "They are not my beloved!!!"
            i "I hate him! I hate you too!"
            "You feel slightly bad as you and Patches walk away"
            show patches
            p "Sooooo, what are you into?"
            h "I uhhh I like a lot, that's kinda vague"
            "Patches laughs"
            p "Cute"
            p "Wanna head to my place?"
            h "Uh, sure..."


    # Add the delinquent storyline here
    jump choice_done

label choice_done:
    "The day comes to an end."

    # This ends the game.

    return
