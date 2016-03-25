# Character class

class Character(object):
    def __init__(self, name, inventory):
        # We start with a custom name and inventory.
        # We use default values for other things.
        self.name = name
        self.inventory = inventory
        self.max_hp = 20
        self.hp = 20
        self.max_mp = 10
        self.mp = 10
        self.schmeckels = 25
        self.current_location = "main_plaza"
        self.current_location_name = "The Main Plaza of Lyadin"
        self.previous_location = "forest_1"
        self.previous_location_name = "The Forest Outside Lyadin"
    
    def print_inventory(self):
        # Prints the inventory of the character
        if len(self.inventory) == 0:
            print "You ain't got nothin' hunny."
        else:
            print "Let's see what we have."
            for key in self.inventory:
                print "%s: %s" % (key, self.inventory[key])
                
    def add_to_inventory(self, item, description):
        self.inventory.update(item, description)
    
    
    def print_status(self):
        # Print information about the character
        print "Your current HP is: %d/%d" % (self.hp, self.max_hp)
        print "Your current MP is: %d/%d" % (self.mp, self.max_mp)
        print "You are at %s" % self.current_location_name
        print "You came from %s" % self.previous_location_name
        print "You have %d Schmeckles to your name." % self.schmeckels
        
    def have_item(self, item):
        # Check if an item is available for use.
        # It will try to find the item name among the inventory.
        return item in [x.lower() for x in list(self.inventory)]
        