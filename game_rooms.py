# This file has classes for the rooms in the game
# Each room is a Scene that interacts with the player via text commands

from random import randint

class Scene(object):
    # Generic scene object
    def __init__(self):
        # Every scene has visited and looked flags.
        self.visited = False
        self.looked = False
        
    def basics(self, choice, character):
        # Basic commands that are shared across scenes
        if choice == "help":
            self.help()
            return True
            
        elif choice == "status":
            character.print_status()
            return True
            
        elif choice == "look at inventory":
            character.print_inventory()
            return True
            
        elif (choice == "exit") | (choice == "quit"):
            print "Thank you for playing!"
            exit(1) 
            
        elif choice == 'talk':
            print "Who are you talking to?"
            return True
            
        else:
            return False
        

    def help(self):
        # Prints the basic commands
        print "The available commands are:"
        print "\t1. Help: Hopefully, you know what this does."
        print "\t2. Status: Tells you information about you."
        print "\t3. Look: Look around you. You can use it to look at a",
        print "specific object or your inventory as well."
        print "\t4. Pick up: Pick something up."
        print "\t5. Use: Uses an item from your inventory."
        print "\t6. Fight: Gets you into a fight. Tread carefully around here."
        print "\t7. Go to: When you are ready to move on, you can go to a new",
        print "location with this command (north, south, east, west)."
        print "\t8. Talk to: Say hi to locals!"
        print "\t9. Feel free to experiment! The worst thing that can happen",
        print "is to suffer a horrible death at the hands of an orc wizard."
        
    def enter(self, character):
        # If the player enters an unfinished scene, they will be sent back.
        print "This scene does not exist yet!"
        print "Tell the programmer to implement it."
        print "Please go back to %s." % character.previous_location
        return ("move", character.previous_location, 0)
        


############################ The Main Plaza ###################################
class MainPlaza(Scene):
    # The starting scene. The player must use the 'look' command before moving.
    # Hopefully this will teach the player to always look at the environment.
    title = "The Main Plaza"
    
    def enter(self, character):
        # The action on this scene is very simple. The player can move in any
        # direction and interact with one NPC.
        if not self.visited:
            print "This is the main plaza of Lyadin."
            self.visited = True
        
        while True:
            print "What is your next move?"
            choice = raw_input('> ')
            
            choice = choice.lower().strip()
            
            if (choice == 'look') | (choice.lower() == 'look around'):
                print "To the north you see the road that leads to the castle."
                print "There is an inn on the western side."
                print "The southside looks like a market."
                print "The Lyadin forest is to your left."
                print "There is a town guard at the entrance of the market."
                self.looked = True
                
            elif 'fight' in choice:
                print "You start thinking about picking up a fight but then",
                print "you remember reading in the traveler's guide that the",
                print "town of Lyadin is a fight-free zone."
            
            elif ('go' in choice) & (not self.looked):
                print "You should look around you to have an idea of where",
                print "to go next."
            
            elif (choice == 'go west') & (self.looked):
                print "Let's see if they have beer at the inn."
                return ("move", "the_inn",  0)
            
            elif (choice == 'go east') & (self.looked):
                print "You decide to go explore the forest."
                return ("move", "forest_1",  0)
            
            elif (choice == 'go north') & (self.looked):
                print "Let's see if we can find a way into the castle."
                return ("move", "castle",  0)
            
            elif (choice == 'go south') & (self.looked):
                print "Markets are always fun, let's go!"
                return ("move", "market",  0)
                
            elif ('use' in choice):
                item = choice[4:]
                if not character.have_item(item):
                    print "You don't seem to have that item in your inventory."
                elif item == 'sword':
                    if randint(0, 10) <= 3:
                        print "You start swhowing off your sword skills and accidentaly",
                        print "chop off your head."
                        return ("dead", 0, 1)
                    else:
                       print "There is no need to take out your sword here."
                else:
                    print "You can't use that here. Put it away."
            elif (choice == 'talk to guard') & self.looked:
                print "You say hi to the guard. He replies: \"Go bother someone else\". What a nice fella!" 
            elif self.basics(choice, character):
                pass
            else:
                print "I didn't catch that."


################################## The Inn ####################################
class TheInn(Scene):
    # The inn has a drinking contest that can only be won after acquiring
    # a special item at the market. There are two NPCs to talk to,
    # but first the player needs to be seated at the bar.
    # There is a special character revelead with the 'look' command.
    
    title = "The Inn"
    
    # We need some extra flags, know_boat is for later in the game
    # is_seated has to be turned on to be able to interact with the NPCs.
    know_boat = False
    is_seated = False
    
    def enter(self, character):
        if not self.visited:
            print "This looks like a lovely inn. There is an open seat at the",
            print "bar next to a guy in wearing what appears to be a Royal",
            print "Guard uniform."
            self.visited = True
            
        while True:
            if self.is_seated:
                print "The bar keeper is looking at you. Maybe you should order something?"
                
            print "What do you want to do?"
            choice = raw_input('> ')
            
            choice = choice.lower().strip()
            
            if (choice in ['go out' 'get out' 'go east' 'go back']) & self.is_seated:
                print "You get up and go back to the plaza."
                return ('move', 'main_plaza', 0)
                
            elif (choice in ['go out', 'get out', 'go east', 'go back']) & (not self.is_seated):
                print "You decide that you are done here for now,"
                return ('move', 'main_plaza', 0)
                
            elif self.basics(choice, character):
                pass
            
            elif ('sit' in choice) & not self.is_seated:
                print "You take the open seat next to the guard."
                self.is_seated = True
            
            elif ('sit' in choice) $ self.is_seated:
                print "You are already seated, champion."
                
            elif (choice in ['get up', 'stand up', 'stand']) & self.is_seated:
                print "Okay, back on your feet."
                self.is_seated = False
                
            elif (choice in ['get up', 'stand up', 'stand']) & not self.is_seated:
                print "You are not seated..."
                
            
            
            else:
                print "Sorry, the band is too loud so I didn't catch that."
            
    
############################## The Forest part 1 ##############################
class TheForest1(Scene):
    title = "The Forest Outside Lyadin"
    pass
    
    
############################## The Forest part 2 ##############################
class TheForest2(Scene):
    title = "The Road to Lake"
    pass
    
    
################################### The Cave ##################################
class TheCave(Scene):
    title = "The Tabuz Cave"
    pass

    
################################### The Lake ##################################
class TheLake(Scene):
    title = "The Bottomless Lake"
    pass

    
############################## The Lyadin Market ##############################
class TheMarket(Scene):
    title = "The World's Famous Lyadin Market"
    pass
    
    
################################ The Sewers ###################################
class TheSewers(Scene):
    title = "The Sewers"
    pass
    
    
################################ The Castle ###################################
class TheCastle(Scene):
    title = "Lyadin Castle"
    pass
    

############################### The Throne Room ###############################
class TheThroneRoom(Scene):
    title = "The Throne Room"
    pass
    
    

class Map(object):
    # The map class contains the scenes. The game engine will be able to save
    # the current state of the world.
    scenes = {
        'main_plaza':MainPlaza(),
        'the_inn':TheInn(),
        'forest_1':TheForest1(),
        'forest_2':TheForest2(),
        'cave':TheCave(),
        'lake':TheLake(),
        'market':TheMarket(),
        'sewers':TheSewers(),
        'castle':TheCastle(),
        'throne_room':TheThroneRoom()
    }
    