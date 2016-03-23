# This file contains the game engine

class Engine(object):
	def __init__(self, map, character):
		self.map = map
		self.character = character
		self.endgame = False
	
	
	def play(self, message):
		print message

		while not self.endgame:
			action = self.map.scenes[self.character.current_location].enter(self.character)
			if action[2] >= 1:
				print "You died! huehueheu"
				self.endgame = True
			else:
				if action[0] == "move":
					self.character.previous_location = self.character.current_location
					self.character.previous_location_name = self.character.current_location_name
					self.character.current_location = action[1]
					self.character.current_location_name = self.map.scenes[action[1]].title
					