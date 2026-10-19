# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#LAST PREP WEEK PLANNING:
#Hikaru SPRITES
#INARISHIP ROUTE DEVELOPED, MAYBE TWO VERSIONS ONE WITH Hikaru AND ONE WITHOUT

define h = Character("Harper")
define i = Character("Inari")
define s = Character("Stitch")
define a = Character("Apple")
define hk = Character("Hikaru")
define npc1 = Character("Random Guy 1")
define npc2 = Character("Random Guy 2")

# what type of music do we want???
# list of backgrounds
# bg room, bg outside, bg bus, bg mall
# list of sprites needed per character
#Inari: inari_happy, inari_smug
#Harper: harper_happy, harper_spin, harper_excited
#sprites should be 1000 px tall i thinks?
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
    h "I should make sure I pack my TI-84 EVO graphing calculator"
    h "Oh and my sketchbook stuffs"
    h "DAD! I'm ready!!!!"
    h "Hurry up or I'm not gonna be early!"
    "Your father drives you, this is because you're a loser that still doesn't have a license"
    "You arrive at school 10 minutes before the doors even unlock"
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
    s "HAIIIIWJWJ HARPER!"
    h "Hi Stitchy! Are you working on your vtuber model?"
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
        "Of course, of course! I absolutely worship the ground you walk on! {i} eye roll {/i}":
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
    h "Lead the way"
    scene bg mall
    i "I want the citrus smoothie"
    npc1 "What would you like to order?"
    h "Can we get one citrus smoothie and one strawberry banana?"
    npc1 "Sure thing!"
    "A few minutes later"
    npc1 "Here you go!"
    h "For you, my mi'lady"
    i "You don't need to bow..."
    i "Sighs... just give it to me"
    h "Yeah, yeah, love you too"
    h "So what next mi'lady?"
    i "I am... Unsure"
    h "We could always go to your temple?"
    i "My temple?"
    h "Yeah! Obviously!"
    i "Do you?"
    i "Do you actually believe I'm a deity?"
    menu:
        "...Totally":
            i "Lets just go to a store or something"
            jump sadnari

        "Yeah! I mean you have a halo and everything":
            i "Halo's are not uncommon, even you have one"
            show harper pout
            h "Yeah but... but you're the goddess of foxes and stuff! You have to be a deity!"
            i "Awwww"
            i "At least someone believes me"
            h "If anybody doesn't believe you I'll beat them up!"
            show inari laugh
            i "Oh really? I suppose I should be honored"
            "The two of you walk to Inari's temple"
            i "Sorry it's a bit of a mess... I haven't been here in a while"
            h "Awwwwwwww; why not? It's cute!"
            i "Obviously it's cute! I made it myself!"
            h "I can tell! That has your handwriting!"
            "You point at a sign that says the visiting hours"
            h "It's really like it!!!"
            i "Awwww, I mean of course you like it, {i}I{/i} made it!"
            "You two sit down and talk for a while"
            i "You know I'm not really a deity, right? {i}sighs{/i}"
            "You sigh as well"
            h "Yeah, I know"
            i "Then why do you...?"
            h "Simply because it makes you happy"
            h "Is that?"
            h "Is that okay?"
            i "Yeah... I think it is"
            "She smiles at you softly"
            menu:
                "This was nice":
                    i "Yeah, it was, we should hang out some time"
                    h "Yeah, we should!"
                    i "Maybe with a little less skipping class next time"
                    
                "Inari, I love you":
                    i "You???"
                    i "Huhwjs??? Me?"
                    "She points at herself"
                    h "{i}Noooooooo{/i} I was talking to a different Inari"
                    h "Obviously, I was talking to you"
                    i "Mhm..."
                    "You both stare at each other akwardly before she speaks"
                    i "I love you too"
                    "You both just smile for a minute"
                    i "So uhhhh"
                    i "What do we do now?"
                    h "What do you want to do?"
                    i "We could go on a date?"
                    h "Where to, {i}goddess{/i}?"
                    "She stands up and grabs your hand, pulling you up"
                    "You don't question where you're going you just watch as you pass through the enterance to a building deeper onto the shrine's property"
                    h "Is this your house?"
                    "It's both simoultaneously falling apart and nice looking inside in a way that is disorienting"
                    "You hesitate for a moment, unsure of what to say next"
                    h "It's cute!"
                    i "Aww, thank you, yay!"




                


    show harper happy
    

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
label sadnari:
    h "Woah who is that?"
    show hikaru 
    "You see a boy walking around; his hair is a mess but other than that he seems put together"
    i "Him? That's Hikaru..."
    hk "Oh hey, who's this little guy?"
    "Inari clings to your arm"
    h "Why are you...?"
    i "This is Harper!"
    hk "Oh? You're being offly clingy, that's not like you Inari"
    show hikaru 
    #slight_glare
    i "I don't care what you think is like me! I can do whatever I want!"
    menu:
        "Talk to Inari":
            h "I don't like this guy"
            "Inari drags you away"
            jump inariship_route

        "Talk to Hikaru":
            h "Hi there...?"
            show hikaru 
            hk "You're awfully cute!"
            h "Me...?"
            "Inari looks annoyed"
            hk "Yeah obviously, what do you say we get out of here?"
            "You agree and slip out of Inari's grasp"
            "She wasn't holding on tightly but her touch lingered"
            hk "Awww the goddess Inari's beloved getting taken by a mere mortal"
            show inari 
            #flustered
            i "They are not my beloved!!!"
            i "I hate him! I hate you too!"
            "You feel slightly bad as you and Hikaru walk away"
            show hikaru
            hk "Sooooo, what are you into?"
            h "I uhhh I like a lot, that's kinda vague"
            "Hikaru laughs"
            hk "Cute"
            hk "But I meant more like...?" 
            "He does a really stupid hand motion"
            h "Huhwj...?!?"
            hk "{i}sighs{/i} Like this"
            "He flashes a pack of cigarettes"
            hk "Like do you do anything?"
            h "Ohhhhh, I'm a little dumb actually"
            h "Depends, are you offering?"
            "He smiles at you"
            hk "I must confess, this is mildly unexpected"
            hk "You just seem so innocent"
            "You pout"
            h "Heyyyyyyyyy, just because I'm a nerdy loser doesn't mean I don't have other interests!"
            hk "Oh really?"
            h "Yeah!!! Just two weeks ago I got tipsy and then..."
            "You slow to a quiet stop"
            hk "And then?"
            h "I did a bunch of math..."
            hk "You really are a nerd"
            h "Oh fuck you!"
            "Hikaru laughs at your reaction"
            h "{i} grumble grumble {/i} I hate you"
            hk "Do you really, I'm so sad now"
            hk "I guess we can't hang out or be friends anymore"
            show harper pout
            h "Awwww awwww! I'm sorry! I'm sorry!"
            hk "Giggles, I was just joking"
            h "Yeah yeah"
            "You two keep walking together for awhile"
            h "Where are we going?"
            hk "The library"
            h "You go to the library???"
            hk "Yeah? Why wouldn't I?"
            h "I dunno, you just don't seem the type"
            show hikaru scoff
            hk "I read plenty!"
            h "I guess we have that in common!"
            hk "I thought you were a math nerd, didn't take you as a literary"
            h "Well I am!"
            show harper pout
            h "I'm in higher levels of maths and english lit and art!!!"
            hk "That's such a niche combination, not many people take {i} those{/i}"
            h "I'm just cool like that!" 
            show hikaru eye roll
            hk "I wouldn't call that cool"
            h "Hmmph, bully!"
            hk "I never said I was cool, we're both losers here"
            h "Oh, we're here!"
            "He grabs your hand and leads you inside"
            "You two meander about, looking at various books"
            menu:
                "Look at the horror section":
                    label look_horror:
                    "You spend some time browsing the horror section."
                    h "I love horror, they don't have any of the authors I like though"
                    hk "{i} You {/i} like horror???"
                    h "Yeah! Our dad writes horror novels in the winter when he isn't working"
                    hk "Isn't working?"
                    h "He's a landscaper"
                    "He nods at you"
                    h "Oh my gods!"
                    "You then realize you yelled in a library and whisper"
                    h "Sorry, sorry..."
                    h "But look! They have the collection that's publishing the new Liard Barron short story!"
                    "Hikaru giggles at you"
                    h "Sorry, sorry"
                    hk "You don't have to apologize, you know that, right?"
                    show harper blush
                    h "Thanks..."
                    hk "Mhm mhm"
                    jump reading_done

                "Look at literary novels":
                    label look_lit:
                    "You spend some time browsing the literary novels section."
                    hk "Oh?"
                    h "Huh?"
                    hk "This is so self valueing of you"
                    show harper shock
                    h "Nu uh!"
                    h "I just like reading about losers ranting about being losers because I'm a loser"
                    hk "Usually those people think they're better than everyone"
                    show harper pout
                    h "Well sometimes they change the way I think of things."
                    "Hikaru laughs at you a little"

                    jump reading_done
                "Look at romance novels":
                    label look_romance:
                    "You spend some time browsing the romance novels section."
                    hk "Do you really like romance novels"
                    h "Well not often but sometimes they're fun!"
                    label start:
                        default d20_roll= 0
                        $ d20_roll=renpy.random.randint(1, 20)
                        if d20_roll == 15:
                            "He notices the specific novel you're glancing at"
                            hk "Pervert"
                            show harper blush
                            h "No!!!"
                            h "I only read this author because she had a y/a novel that I read once..."
                            h "It was about them playing chess and stuff..."
                        else:
                            h "Though a lot of the time they're just the same thing every time..."
                    jump reading_done
                
            label reading_done:
                menu:
                    "Look at the horror section":
                        "You spend some time browsing the horror section."
                        jump look_horror
                    "Look at literary novels":
                        jump look_lit
                    "Look at romance novels":
                        "You spend some time browsing the romance novels section."
                        jump look_romance
                    "Finish your meandering":
                        hk "Now let's go to the computers"
                        h "Huh? Why?"
                        hk "That's why I came here and brought you"
                        h "Is it???"
                        hk "Mhm, let me show you something cool"
                        "You watch as he pulls up various websites as you get mildly lost until he points out something specific"
                        hk "This is how we find cool shit"
                        "You realize he was just on facebook marketplace but with a weird color filter"
                        "There's a listing that he clicks on:"
                        "Free chess set plus random bag of miscellaneous items"
                        hk "It's less than a mile away"
                        h "Why did we not just look this up on our phones?"
                        h "Did we really have to walk all the way to the library for this?"
                        hk "Not really, but it's cooler using the computer, and actually the filters can work better on it"
                        h "Fair enough actually"
                        "You both start walking over and he pulls out a cigarette"
                        menu:
                            "Ignore it":
                                "He finds a bic lighter in his pocket and lights the cigarette."
                            "Offer to light it for him":
                                "You pull out a rainbow zippo lighter and light his cigarette for him."
                                show hikaru blush
                                hk "Oh...?"
                                "He whispers"
                                hk "Thank you..."
                                "He gives you a cigarette from the pack."
                                h "Thanks..."
                                hk "It's only right, since I'm the loser without a lighter."
                                "The two of you walk in silence as you both smoke"
                                "Eventually you get to the house to pick it the listing up."
                                h "Who's gonna knock on the door?"
                                hk "You should"
                                h "I don't wanna knock on a stranger's door! It's safer for you to!"
                                hk "Fine fine"
                                "He knocks on the door and a middle aged man opens it and hands him the items."
                                "The two of you run off, giggling as you do so. Eventually you reach a random grassy area."
                                "There is a random bottle of liqour in the bag"
                                h "Oh hell yeah!"
                                hk "Alchohol? You're excited about that?"
                                h "Obviously. Plus it's been a while since I've had a drink."
                                show hikaru anxious
                                hk "Are you sure?"
                                menu:
                                    "I guess if you don't want to...":
                                        "You two go through the rest of the bag together, finding random nicnacks and some snacks"
                                        h "Let's open up the chips, I'm a little dizzy and need some salt anyways"
                                        hk "POTS?"
                                        h "Yeah, how'd you know...???"
                                        hk "My ex girlfriend had it"
                                        h "Oh that makes enough sense"
                                        h "Wait? You have an ex?"
                                        hk "Yeah??? Why wouldn't I have had an ex?"
                                        h "Because you...?"
                                        menu:
                                            "You seem like a loser like me?":
                                                hk "Asshole!"
                                                h "I'm not wrong!"
                                                hk "Well clearly you are!"
                                                h "I mean look at you!"
                                                hk "What's that supposed to mean!!!"
                                                h "You know exactly what I mean!"
                                                hk "Whatever, I'm getting out of here!"
                                                h "Fine, go then!"
                                                jump choice_done
                                            "I... I dunno... It's just...":
                                                hk "Are you jealous?"
                                                h "What? No!"
                                                show harper blush
                                                h "Plus we just met today..."
                                                h "I couldn't be jealous of her, plus I've also never met her!"
                                                hk "You really are jealous!"
                                                "He laughs and you start laughing too"
                                                h "Just give me the chips already!"
                                                hk "Yeah, yeah!"
                                                "He rolls his eyes at you"
                                                h "Oh shit! It's late, I ought to get home now."
                                                hk "Awwwwww, wait!"
                                                "He hands you his phone, open on an add contact page"
                                                hk "Let's see each other again sometime"
                                                jump choice_done
                                                
                                        "Mhm mhm!!!":
                                            "You dig through your own backpack and find some apple juice you brought just because it's yummy"
                                            "After mixing both of you drinks you offer him one."
                                            hk "Thanks..."
                                            "You both sip at the drinks as you go through the rest of the bag and talk together."
                                            h "Wait? You have an ex?"
                                            hk "Yeah??? Why wouldn't I have had an ex?"
                                            h "Because you...?"
                                            menu:
                                                "You seem like a loser like me?":
                                                    hk "Fuck you!"
                                                    "He hits you, not hard enough to hurt badly but hard enough to stumble a bit"
                                                    h "Fuck!"
                                                    menu:
                                                        "Apologize":
                                                            h "I'm sorry!"
                                                            hk "Yeah yeah, whatever."
                                                            hk "Let's just leave, it's getting late anyways..."
                                                            jump choice_done
                                                        "Hit him back":
                                                            show hikaru grin
                                                            hk "Ow! Holy shit, I wasn't expecting you to be the type to punch back"
                                                            "He shoves you again but trips and falls, leaving you between him and the ground."
                                                            h "Fucking hell!"
                                                            "You spit some blood from your mouth because you bit yourself during the fall"
                                                            "You try to get out of his grasp but he punches you again."
                                                            h "I hate you!"
                                                            hk "Yeah, well, I hate you too!"
                                                            "One of your hands gets out of his grasp, and grabs his hair, pulling on it"
                                                            "This, unintentionally, pulls both of you closer together."
                                                            hk "Fuck..."
                                                            "One of you kisses the other, you're in such a daze you don't know which one of you even intiated it."
                                                            h "Fuck..."
                                                            hk "Holy shit..."
                                                            "You both stare at each other before he shoves away from you."
                                                            hk "Fuck you!"
                                                            hk "I'm not... I'm not gay!"
                                                            h "I think you fucking are!"
                                                            hk "No, of course not!"
                                                            hk "Fuck"
                                                            "He shoves you again"
                                                            h "What the fuck is wrong with you!"
                                                            hk "What's wrong with me? What's wrong with you!"
                                                            h "A lot??? But I don't think any of it is relevant here???"
                                                            h "You're gonna need to be more specific???"
                                                            hk "Sighs"
                                                            "He falls to the ground with a sigh"
                                                            hk "Just go away!"
                                                            "You don't go anywhere, you just sit down a few feet away from him and pour another drink"
                                                            hk "Whatever..."
                                                            "You're overheating from the fight and pull off your jacket leaving you just in the tanktop"
                                                            hk "What are you doing?!?"
                                                            hk "Don't undress in front of me!"
                                                            h "It's just my jacket, get over it, prude!"
                                                            hk "Ugh..."
                                                            "He runs his hands through his hair in frustration"
                                                            hk "Do you really have to do this?"
                                                            h "Yes? It's hot as shit"
                                                            h "Why? Is it upsetting you?"
                                                            hk "It's just weird, ok???"
                                                            show hikaru frustrated
                                                            hk "I'm not supposed to see you like this!"
                                                            h "And why not?"
                                                            hk "Because I'm a boy and you're a boy..."
                                                            hk "And it's not like it's bad to be gay but I'm not!"
                                                            h "Mhm"
                                                            "You give him a look of annoyance"
                                                            h "Are you sure you're not gay?"
                                                            hk "Uhhhhh fuck"
                                                            "You grab his hand"
                                                            show hikaru blush
                                                            "He mumbles"
                                                            hk "I guess you're a little right..."
                                                            h "Of course I am, I'm always right"
                                                            "You both sit there for a long while"
                                                            "And longer"
                                                            "And longer"
                                                            "Until he says something"
                                                            hk "So uhh, what next?"
                                                            h "We could make plans for a date"
                                                            hk "I guess we could..."
                                                            "You pull his hair again, this time less aggressively"
                                                            hk "Heyyyyyyyyyy!!!"
                                                            "You giggle which causes him to as well"
                                                            jump choice_done

                                                "I dunno, you just seem like you would prefer being single":
                                                    hk "I guess I have that vibe"
                                                    "You take another sip of your drink and pick at a snack"
                                                    "You dig through the bag and find some fire starters"
                                                    h "Oh hells yeah!"
                                                    "The two of you make out a clearing and grab nearby twigs to put in a pile"
                                                    "You pull out your lighter and extend it to him"
                                                    h "Do you want to, or should I?"
                                                    hk "All yours"
                                                    "You light a starter and throw it into the pile, causing the fire to slowly grow"
                                                    h "woah!!!"
                                                    jump choice_done

                                            #They should do fun illegal activities like blowing shit up and uhhhh fire, fire is fun and then they should sleep together


    jump choice_done

label choice_done:
    "The day comes to an end."
    #Note to self: figure out if I want to have unique endings or if they are all just different paths to the same ending.
    #Both are kinda interesting so I dunno
    # This ends the game.

    return
