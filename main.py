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
    start = input("Launch the game? [Y/N] ")
    if start == "Y" or start == "y":
        game()
    if start == "N" or start == "n":
        print(":(")

def restart():
    again = input("Do you want to play again? [Y/N] ")
    if again == "Y" or again == "y":
        game()
    if again == "N" or again == "n":
        print(":(")

def choice1():
    global pirate
    global mafia
    global major_tom
    global corny
    global assasination
    global oligarchy
    global tom_crews
    global pasini
    choice1 = input("Wealth [A] or Fame [B]? ")

    if choice1 == "A" or choice1 == "a":
        wealth()
    if choice1 == "B" or choice1 == "b":
        fame()

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
    wealth = input("Purchase a mansion [A] or purchase stocks [B] ? ")
    ############## Mansion ##############
    if wealth == "A" or wealth == "a":
        print("ballin'")
        mansion = input("Where do you want to purchase the mansion, Florida [A] or Northern Canada [B]? ")    
        if mansion == "A" or mansion == "a":
            print("A crocodile bit your hand off, so you decide to become a pirate and set sail under the ship known as the 'SS Missing Digit' ")
            if pirate == False:
                endings+=1
            pirate = True
            print("Congratulations, you got the 'Pirate' ending! You now have " + str(endings) + "/8")
            restart()
        if mansion == "B" or mansion == "b":
            print("The polar bear mafia noticed your mansion and convinced you to pay them for protection, or else you might get 'iced'...")
            if mafia == False:
                endings+=1
            mafia = True
            print("Congratulations, you got the 'Mafia' ending! You now have " + str(endings) + "/8")
            restart()

    ############## Stocks ##############
    elif wealth == "B" or wealth == "b":
        print("Greedy feller")
        stock = input("Which stocks will you purchase, SpaceX [A] or corn [B]? ")    
        if stock == "A" or stock == "a":
            print("After purchasing so many stocks in SpaceX, the gave you the opportunity to go to space...what they didn't tell you is that you wouldn't come back! You were exiled to the moon, now spending most days fishing with the man in the moon.")
            if major_tom == False:
                endings+=1
            major_tom = True
            print("Congratulations, you got the 'Major Tom' ending! You now have " + str(endings) + "/8")
            restart()
        if stock == "B" or stock == "b":
            print("Despite confusing 'stocks' with 'stalks', your investment turned out quite well. After a plant disease wiped out most corn in the world, your massive stockpile become worth a fortune. You are now the 86th richest person alive.")
            if corny == False:
                endings+=1
            corny = True
            print("Congratulations, you got the 'Corny' ending! You now have " + str(endings) + "/8")
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
    fame = input("Would you like to become a politician [A] or an actor [B]? ")
############## Politician ##############
    if fame == "A" or fame == "a":
        print("The evil route, eh?")
        politician = input("Will you work for the good of the people [A] or become a corrupt authoritarian... but also much richer and powerful [B] ")
        if politician == "A" or politician == "a":
            print("You started small, grassroots, knocking on doors. Eventually you worked your way through the system, becoming the party leader and running to become PM. You were a hope to many people, and were set to win, but being nice makes you enemies in high places, Jeff Bezos shows up and personally assasinated you before you could win the election.")
            if assasination == False:
                endings+=1
            assasination = True
            print("Congratulations, you got the 'Assasination' ending! You now have " + str(endings) + "/8")
            restart()
        if politician == "B" or politician == "b":
            print("You take bribes and build many connections. The media fully supports your campaign, swaying public opinion to your favour enough to eventually become a party leader and even PM. After becoming PM, you declare martial law, instituting and oligarchic dictatorship.")
            if oligarchy == False:
                endings+=1
            oligarchy = True
            print("Congratulations, you got the 'Oligarchy' ending! You now have " + str(endings) + "/8")
            restart()

    ############## Politician ##############
    elif fame == "B" or fame == "b":
        print("Action!")
        actor = input("Will you travel to Hollywood [A] or try to teach others how to act [B]? ")
        if actor == "A" or actor == "a":
            print("You make it to Hollywood and immediatly start auditioning for everything you can. You don't get many offers, until a big director sees you and believes you have so much potential, you get to star in his new movie 'Mission Improbable'.")
            if tom_crews == False:
                endings+=1
            tom_crews = True
            print("Congratulations, you got the 'Tom Crews' ending! You now have " + str(endings) + "/8")
            restart()
        if actor == "B" or actor == "b":
            print("You star in local shows, some made for TV programs, but mainly focus on a teaching career. You manage to get a job working at All Saints Catholic High School teaching drama. While working you begin writing your own plays for school, but never get to use them before you retire. 200 years later the documents are found and you become the new Shakespeare.")
            if pasini == False:
                endings+=1
            pasini = True
            print("Congratulations, you got the 'Pasini' ending! You now have " + str(endings) + "/8")
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
