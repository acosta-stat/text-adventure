# Character class

class Character(object):
	def __init__(self, name, inventory):
		self.name = name
		self.inventory = inventory
		self.max_hp = 20
		self.hp = 20
		self.max_mp = 10
		self.mp = 10
		self.current_location = "main_plaza"
		self.current_location_name = "The Main Plaza of Lyadin"
		self.previous_location = "forest_1"
		self.previous_location_name = "The Forest Outside Lyadin"
	
	def print_inventory(self):
		if len(self.inventory) == 0:
		 	print "You ain't got nothin' hunny."
		else:
			print "Let's see what we have."
			for key in self.inventory:
				print "%s: %s" % (key, self.inventory[key])
				
	def print_status(self):
		print "Your current HP is: %d/%d" % (self.hp, self.max_hp)
		print "Your current MP is: %d/%d" % (self.mp, self.max_mp)
		print "You are at %s" % self.current_location_name
		print "You came from %s" % self.previous_location_name
		
	def use_item(self, item):
		try:
			int(item)
			print "It was an integer!"
			return True
		except:
			print "It was not an integer!"
			return False
		finally:
			print "This is from finally. Yay!"