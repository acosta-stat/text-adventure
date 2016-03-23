# This file has classes for the rooms in the game

# Generic scene object
class Scene(object):
	def __init__(self):
		self.visited = False
		self.looked = False
		
	def basics(self, choice, character):
		if choice.lower() == "help":
			self.help()
			return ("help", "0", character, 0)
		elif choice.lower() == "status":
			character.print_status()
			
		elif choice.lower() == "look at inventory":
			character.print_inventory()
			
		elif (choice.lower() == "exit") | (choice.lower() == "quit"):
			print "Thank you for playing!"
			exit(1)	
			
		else:
			pass

	def help(self):
		print "The available commands are:"
		print "\t1. Help: Hopefully, you know what this does."
		print "\t2. Look: Look around you. You can use it to look at a specific",
		print " object or your inventory as well."
		print "\t3. Pick up: Pick something up. Pretty clear."
		print "\t4. Use: Uses an item from your inventory."
		print "\t5. Fight: Gets you into a fight. Tread carefully around here."
		print "\t6. Go to: When you are ready to move on, you can go to a new",
		print "location with this command (north, south, east, west)."
		print "\t7. Talk to: Say hi to locals!"
		print "\t8. Feel free to experiment! The worst thing that can happen is",
		print "to suffer a horrible death at the hands of an orc wizard."
		
	def enter(self, character):
		print "This scene does not exist yet!"
		print "Tell the programmer to implement it."
		print "Please go back to %s." % character.previous_location
		return ("move", character.previous_location, 0)

# The main plaza
class MainPlaza(Scene):
	title = "The Main Plaza"
	
	def enter(self, character):
		
		if not self.visited:
			print "This is the main plaza of Lyadin."
			self.visited = True
		
		while True:
			print "What is it going to be?"
			choice = raw_input('> ')
			
			choice = choice.lower().strip()
			self.basics(choice, character)
			
			if (choice == "look") | (choice.lower() == "look around"):
				print "To the north you see the road that leads to the castle."
				print "There is an inn on the western side."
				print "The southside looks like a market."
				print "The Lyadin forest is to your left."
				self.looked = True
				
			elif "fight" in choice:
				print "You start thinking about picking up a fight but then",
				print "you remember reading in the traveler's guide that the",
				print "town of Lyadin is a fight-free zone."
			
			elif ("go" in choice) & (not self.looked):
				print "You should look around you to have an idea of where",
				print "to go next."
			
			elif (choice == "go west") & (self.looked):
				print "Let's see if they have beer at the inn."
				return ("move", "the_inn",  0)
			
			elif (choice == "go east") & (self.looked):
				print "You decide to go explore the forest."
				return ("move", "forest1",  0)
			
			elif (choice == "go north") & (self.looked):
				print "Let's see if we can find a way into the castle."
				return ("move", "castle",  0)
			
			elif (choice == "go south") & (self.looked):
				print "Markets are always fun, let's go!"
				return ("move", "market",  0)
				
			else:
				print "I didn't catch that."


# The Inn
class TheInn(Scene):
	title = "The Inn"
	knowBoat = False
	isSeated = False
	
	def enter(self, character):
		if not self.visited:
			print "This looks like a lovely inn. There is an open seat at the bar."
			self.visited = True
			
		while True:
			print "What do you want to do?"
			choice = raw_input('> ')
			
			self.basics(choice, character)
			
	
# The Forest part 1
class TheForest1(Scene):
	title = "The Forest Outside Lyadin"
	pass
	
# The Forest part 2
class TheForest2(Scene):
	title = "The Road to Lake"
	pass
	
# The Cave
class TheCave(Scene):
	title = "The Tabuz Cave"
	pass

# The Lake
class TheLake(Scene):
	title = "The Bottomless Lake"
	pass

# The Lyadin Market
class TheMarket(Scene):
	title = "The World's Famous Lyadin Market"
	pass
	
# The Sewers
class TheSewers(Scene):
	title = "The Sewers"
	pass
	
	
# The Castle
class TheCastle(Scene):
	title = "Lyadin Castle"
	pass
	
class TheThroneRoom(Scene):
	title = "The Throne Room"
	pass
	
# The map class contains the scenes	
class Map(object):
	scenes = {
		'main_plaza': MainPlaza(),
		'the_inn':TheInn(),
		'forest_1':TheForest1(),
		'forest_2':TheForest2(),
		'cave':TheCave(),
		'lake':TheLake(),
		'market':TheMarket(),
		'sewers':TheSewers(),
		'castle':TheCastle()
		'throne_room':TheThroneRoom()
	}
	