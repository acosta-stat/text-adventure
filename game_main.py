import game_character as gchar
import game_rooms as grooms
import game_engine as geng

game_map = grooms.Map()
felipe = gchar.Character("Felipe", {'Sword':'Be careful, it\'s sharp.'})

start_message = """
Welcome, welcome!\nThis is a text adventure made by Felipe Acosta as a 
fun project to start programming with Python. Type 'help' to get started,
good luck and have fun!
"""
a_game = geng.Engine(game_map, felipe)
a_game.play(start_message)