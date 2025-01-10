'''
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m' # called to return to standard terminal text color
'''

endings = 0
pirate = False
mafia = False
major_tom = False
corny = False
assasination = False
oligarchy = False
tom_crews = False
pasini = False
def start_game():
    print("You are an archaeologist, mainly focusing on Ancient Egypt. Living in Cairo for many years, doing very exciting, yet risky work. \nExploring Pyramids that have remained untouched, having to avoid boobytraps while in uncharted, ancient territory.")
    print("This has gotten you quite the international reputation, at least in the archaeology and history circles.\nBecause of this recognition, you were handed a very important opportunity.")
    print("The phone rings... disaster has struck. Sudan, which has been under a military dictatoriship since 2019 has just fallen into multi-front civil war.")
    print("Both sides are dangerous, but the Rapid Support Forces, RSF, are especially destructive. \nThey are the paramilitary that started the civil war, and will stop at nothing to takeover the country.")
    print("This conflict will be bloody and brutal, mass devastation is expected, including of the 255 Nubian Pyramids throughout the country.")
    print("Although not an expert in Nubian history, the danger of this situation and your daring past makes \nyou the UN's candidate to travel into Sudan and save as many artifacts as possible.")
    print("\nThe only question is, will you accept this request?\n")
    start = input("Yes [Y] or No [N] | ")
    if start == "Y" or start == "y":
        game()
    if start == "N" or start == "n":
        print("\nUnfortunatley, no one else accepted the opportunity either. Whatever is, well, was, inside those pyramids is know lost to history...")
    else:
        print("The person on the other end of the line was confused by your completely incoherrent response. \nRest assured, you wont be called upon again.")

def restart():
    again = input("Do you want to play again? [Y/N] ")
    if again == "Y" or again == "y":
        game()
    if again == "N" or again == "n":
        print("Unfortunate")

def choice1():
    global pirate
    global mafia
    global major_tom
    global corny
    global assasination
    global oligarchy
    global tom_crews
    global pasini

    print("\nIt is now November 9th, 2026, the RSF is advancing forward at a rapid pace, there are two pyramids that will be taken over, most likely by the 12th.")
    print("Only one of the pyramids can be explored before they are both taken over, you must choose which location.")
    choice1 = input("Meroë [A] or El-Kurru [B]? ")

    if choice1 == "A" or choice1 == "a":
        wealth()
    if choice1 == "B" or choice1 == "b":
        fame()
    else:
        print("You tried going somewhere else entirely, which was not a great idea considering you were in the desert\nLuckily, a pack of hyenas took you in as one of their own :)")
        restart()

def wealth():
    global endings 
    global pirate
    global mafia
    global major_tom
    global corny
    global assasination
    global oligarchy
    global tom_crews
    global pasini
    print("\nWhen you enter the pyramid it looks much different than expected - it has modern floors, ammenities, and... windows that show a skyline?")
    print("You look out the window, you aren't in Sudan anymore, you are in a New York Penthouse.")
    print("Just like last time you recieved an opportunity, you phone rings - its your economic advisor.")
    print("'Listen, I know you are set on buying yet another mansion, but I really think you should consider investing. \nI have some great deals lined up for you.'")
    wealth = input("Purchase a mansion [A] or purchase stocks [B] ? ")
    ############## Mansion ##############
    if wealth == "A" or wealth == "a":
        print("\n'Know what? I'm sick of this, if your so smart why don't you figure out how to live on an iceberg. I quit.'\n")
        mansion = input("Where do you want to purchase the mansion, Florida [A] or Northern Canada [B]? ")    
        if mansion == "A" or mansion == "a":
            print("\nYou found a massive mansion in southern Florida. It has a tennis court, home theatre, and even a lazy river.\nOne day you are relaxing on this lazy river, when you begin to fall asleep.")
            print("SNAP!\nYou wake up, with a terrible pain in your left arm, a gator has bit your hand off!")
            print("In a fit of rage you leave Florida, declaring you shall live at sea. \nYou become a modern day pirate, sailing the now legendary 'SS Missing Digit'")
            if pirate == False:
                endings+=1
            pirate = True
            print("Congratulations, you got the 'Pirate' ending! You now have " + str(endings) + "/8")
            restart()
        if mansion == "B" or mansion == "b":
            print("\nYou move to Nunavut, but the mansion you purchased is absolutely frigid. \nIn fact, a family of polar bears have moved in with you.")
            print("Instead of getting them removed, you take them in as pets. \nSlowly, more and more polar bears make there way to your home, \nand you even become known as the bear whisperer.")
            print("Using your new wealth you start the Oganization for Arctic Preservation, \nnow the worlds biggest contributer to saving the arctic.")
            if mafia == False:
                endings+=1
            mafia = True
            print("Congratulations, you got the 'Mafia' ending! You now have " + str(endings) + "/8")
            restart()
        else:
            print("You purchased a " + mansion + ", which is definitly not one of your options. The CRA decided they had enough and took all your money.")
            restart()

    ############## Stocks ##############
    elif wealth == "B" or wealth == "b":
        print("'\nI knew you would come around eventually! I have been in contact with Mr. Mosk, I really think SpaceX is your best bet")
        print("of course, its up to you though'\n")
        stock = input("Which stocks will you purchase, SpaceX [A] or corn [B]? ")    
        if stock == "A" or stock == "a":
            print("\nAfter purchasing so many stocks in SpaceX, the gave you the opportunity to go to space...what they didn't tell you is that you wouldn't come back! \nYou were exiled to a lunar base, now spending most days eating cheese and fishing with the man in the moon.")
            if major_tom == False:
                endings+=1
            major_tom = True
            print("Congratulations, you got the 'Major Tom' ending! You now have " + str(endings) + "/8")
            restart()
        if stock == "B" or stock == "b":
            print("\nDespite confusing 'stocks' with 'stalks', your investment turned out quite well. \nAfter a plant disease wiped out most corn in the world, your massive stockpile become worth a fortune. \nYou are now the 86th richest person alive.")
            if corny == False:
                endings+=1
            corny = True
            print("Congratulations, you got the 'Corny' ending! You now have " + str(endings) + "/8")
            restart()
        else:
            print("You bought stocks in " + stock + ", which failed miserably, you are now bankrupt.")
            restart()
    else:
        print("'What in the world man, that wasn't one of the options, if you want to buy" + wealth + " then go ahead, I quit.'")
        restart()

def fame():
    global endings 
    global pirate
    global mafia
    global major_tom
    global corny
    global assasination
    global oligarchy
    global tom_crews
    global pasini
    print("\nYou enter the pyramid and begin exploring. It is boiling hot, even in here, and the air is bone dry.")
    print("Eventually, you manage to get to the very centre of the pyramid.") 
    print("There is a massive stone chest, strange symbols carved into its entirety, unlike any hieroglyphs you have ever seen.")
    print("You push the lid off, expecting coins, or perhaps a body, but something unexpected is inside.")
    print("A perfectly preserved amulet in the shape of an eye, the iris made of some kind of jewel.")
    print("You reach out to grab it, but instead it seems to grab you, sucking you into a new world, with nothing \nin sight besides a man in an all white suit.")
    print("You walk up to him, the Stranger just stares. He is the first to break the silence, 'want to make a deal?'")
    print("'What kind of deal? Who ar-' Before finishing your question the Stranger interrupts.")
    print("Power, you can become powerful, leading, having verything you could ever ask for, as long as you don't interfere with the order...")
    print("Or the ability to change who you are at a moments notice. The ability to change into any person you want to be...")
    print("'What do you me-' You try to speak but are again interrupted")
    print("The Stranger asks again 'Power or Transformation'\n")
    fame = input("Power [A] or Transformation [B]? | ")
############## Politician ##############
    if fame == "A" or fame == "a":
        print("\nYou sucked back out of the amulet, but not into the pyramid. You are in a campaign office?")
        print("You face is on lawn signs across Canada, you are somehow the leader of a new political party.")
        print("An analyst comes into the room and gives you a sheet of statistics and a coffee.")
        print("Apparently, you are expected to win 73 percent of the votes in the federal election. \nThe fate of Canada is in your hands...\n")
        politician = input("Will you work for the good of the people [A] or become a corrupt authoritarian... but also much richer and powerful [B] ")
        if politician == "A" or politician == "a":
            print("\nManaging to enlist the support of both the people and politicians, you advocated for change and democracy.")
            print("You were a hope to many people, and were set to win, but those weren't the conditions.")
            print("While making a speech next to the Centennial Flame, a man fires upon you, three shots connect.")
            print("You are put on the operating table, but are ultimately pronounced dead after 8 hours of surgery.")
            if assasination == False:
                endings+=1
            assasination = True
            print("\nCongratulations, you got the 'Assasination' ending! You now have " + str(endings) + "/8")
            restart()
        if politician == "B" or politician == "b":
            print("\nYou take bribes and build many connections. The media fully supports your campaign, \nswaying public opinion even more to your favour, enough to win the election essentially uncontested.") 
            print("After becoming PM, you orchestrate a terrorist disaster to stoke fear and unrest across the country, \ngiving you the ability to declare martial law.")
            print("Elections are suspended, Canada becomes de facto dictatorship under your government. \nCanada is a husk of what it once was, but you are at the helm.\n")
            if oligarchy == False:
                endings+=1
            oligarchy = True
            print("Congratulations, you got the 'Oligarchy' ending! You now have " + str(endings) + "/8")
            restart()
        else:
            print("Your leadership of the party is so bad, your 73% projection went down to 26%" + " until your party completely collapsed. \nYou had to retire in disgrace, a footnote in Canadian history.")
            restart()

    ############## Politician ##############
    elif fame == "B" or fame == "b":
        print("\nYou black out, but upon awakening you are in an office, sitting infront of a big, mahoganey desk. \nA man is sitting behind it, smoking a cigar, he hands you a contract...")
        print("'So, how does it sound? You will be the star, the biggest actor in Hollywood, not to mention the money.'")
        print("The contract is an offer of $100 million to star in a new block buster action movie.")
        print("Acting wasn't what you expected the Stranger to mean by transformation powers. \nYou aren't even sure you want to be a famous actor, you enjoyed your life out of the public eye...")
        print("'May I have some time to think about the offer', you tell the man across the desk.")
        print("'Sure, sure, of course. I will be expecting your call, I'm certain we will have a successful deal...'")
        print("24 hours pass, you have to make a decision.")
        actor = input("Accept [A] or Decline [B]? | ")
        if actor == "A" or actor == "a":
            print("\nYou make it to Hollywood and immediatly get to work. \nYou get to star in the new movie 'Mission Improbable'.")
            print("It is an incredible success, getting you more roles and catipulting you to becoming the most famous actor in Hollywood history.")
            if tom_crews == False:
                endings+=1
            tom_crews = True
            print("Congratulations, you got the 'Tom Crews' ending! You now have " + str(endings) + "/8")
            restart()
        if actor == "B" or actor == "b":
            print("\nYou star in local shows, some made for TV programs, but find a passion for teaching. \nYou manage to get a job working at All Saints Catholic High School teaching drama. While working you begin writing your own plays for school, but never get to use them before you retire. \n200 years later the documents are found and you become the new Shakespeare.")
            if pasini == False:
                endings+=1
            pasini = True
            print("Congratulations, you got the 'Pasini' ending! You now have " + str(endings) + "/8")
            restart()
        else:
            print("Instead of signing the contract, you write '" + actor + "' where your name should be.")
            restart()
    else:
        print("'no'\nSuddenly you sucked back out of the portal into the pyramid, but you can't find the exit. The paths inside are seemingly infinite and ever changing.\nYou are lost forever.")
        restart()
def game():
    global endings 
    print("Endings achieved: " + str(endings) + "/8")  
    print("Unlocked endings:")
    global pirate
    global mafia
    global major_tom
    global corny
    global assasination
    global oligarchy
    global tom_crews
    global pasini
    if pirate == True:
        print("Pirate")
    if mafia == True:
        print("Mafia")
    if major_tom == True:
        print("Major Tom")
    if corny == True:
        print("Corny")
    if assasination == True:
        print("Assasination")
    if oligarchy == True:
        print("Oligarchy")
    if tom_crews == True:
        print("Tom Crews")
    if pasini == True:
        print("Pasini")
    choice1()
    
start_game()
